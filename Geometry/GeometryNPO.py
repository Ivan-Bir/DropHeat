
from Geometry.Geometry import Geometry

from cmath import pi
from math import cos, sin, floor, sqrt


class GeometryNPO(Geometry):
    SCHEMES_FLOWS = {
            "direct flow": 1,
            "reverse flow": -1,
            "annular flow": 0
    }

    def __init__(self):
        super().__init__()

        self.sigma_wall = 0.0
        self.sigma_p = 0.0
        self.sigma_wall_outer = 0.0
        self.height_wall = 0.0
        self.betta_p = 0.0  # град
        self.t_N_min = 0.0
        self.t_N_max = 0.0

        self.d_05_h = []
        self.number_rib_cr = 0.0
        self.t_N_crit = 0.0
        self.d_k = []
        self.number_rib = []

        self.t = []
        self.t_N = []
        self.f = []
        self.d_gas = []

    def get_ribbing_inputs(self): # Считывание из GUI параметров оребрения
        # TODO
        return None

    def make_ribbing(self):
        self.d_05_h = [0] * self.number_sections
        for i in range(self.number_sections):
            self.d_05_h[i] = self.d_sections[i] * (1 + (2 * self.sigma_wall + self.height_wall) / self.d_sections[i])

        self.number_rib_cr = pi * min(self.d_05_h) * cos(self.betta_p * pi / 180) / self.t_N_min
        self.number_rib_cr = floor(self.number_rib_cr)
        while self.number_rib_cr % 4 != 0:
            self.number_rib_cr -= 1

        self.t_N_crit = pi * min(self.d_05_h) * cos(self.betta_p) / self.number_rib_cr

        self.d_k = [0] * 5
        k = [1, 2, 4, 8, 16]
        for i in range(5):
            self.d_k[i] = self.t_N_max * k[i] * self.number_rib_cr\
                          / (pi * cos(self.betta_p * pi / 180)) - (2 * self.sigma_wall + self.height_wall)

        self.number_rib = [0] * self.number_sections
        multiplier = 1
        for i in range(self.number_sections):
            if self.d_05_h[i] < self.d_k[2]:
                multiplier = k[2]
            if self.d_05_h[i] < self.d_k[1]:
                multiplier = k[1]
            if self.d_05_h[i] < self.d_k[0]:
                multiplier = k[0]
            self.number_rib[i] = self.number_rib_cr * multiplier

        self.t = [0] * self.number_sections
        self.t_N = [0] * self.number_sections
        self.f = [0] * self.number_sections
        self.d_gas = [0] * self.number_sections
        for i in range(self.number_sections):
            self.t[i] = pi * self.d_05_h[i] / self.number_rib[i]
            self.t_N[i] = self.t[i] * cos(self.betta_p * pi / 180)
            self.f[i] = self.t_N[i] * self.height_wall * (1 - self.sigma_p / self.t_N[i]) * self.number_rib[i]
            self.d_gas[i] = 2 * self.height_wall * (self.t_N[i] - self.sigma_p) \
                            / (self.t_N[i] - self.sigma_p + self.height_wall)
