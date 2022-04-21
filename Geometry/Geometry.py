from cmath import pi


class Geometry:
    def __init__(self):
        self.x_coord = []
        self.number_sections = 0
        self.number_segments = 0
        self.d_sections = []

        # self.x_coord = self.input_coords()
        # self.d_sections = self.input_diameters()

        self.number_sections = 0
        self.number_segments = 0

        self.d_critical = 0.0
        self.calculate_geometry_parameters()

        self.d_relative = [0.0]
        self.area_sections = [0.0]
        self.area_relative = [0.0]
        self.area_critical = 0.0

        self.delta_x_coord = [0.0]
        self.delta_area = [0.0]

    def input_coords(self): # Тут нужно получить данные для расстояний из Экселя/файла/GUI
        # TODO
        self.number_sections = len(self.x_coord)
        self.number_segments = self.number_sections - 1

        self.d_critical = min(self.d_sections)
        print("success get coords from GUI")
        return True # В случае, если все данные были корректно введены

    def input_diameters(self): # Тут нужно получить данные сечений из Экселя/файла/GUI
        # TODO
        print("success get diams from GUI")
        return True  # В случае, если все данные были корректно введены

    def calculate_geometry_parameters(self): # Считает основные геометрические параметры
        self.d_relative = [0.0] * self.number_sections
        self.area_sections = [0.0] * self.number_sections
        self.area_relative = [0.0] * self.number_sections
        self.area_critical = pi * self.d_critical * self.d_critical / 4
        for i in range(self.number_sections):
            self.d_relative[i] = self.d_sections[i] / self.d_critical
            self.area_sections[i] = pi * self.d_sections[i] * self.d_sections[i] / 4
            self.area_relative[i] = self.area_sections[i] / self.area_critical

        self.delta_x_coord = [0.0] * self.number_segments
        self.delta_area = [0.0] * self.number_segments
        for i in range(self.number_segments):
            self.delta_x_coord[i] = self.x_coord[i + 1] - self.x_coord[i]
            self.delta_area[i] = pi * (self.d_sections[i + 1] + self.d_sections[i]) * self.delta_x_coord[i] / 2

    def print_geometry(self):
        print("Coordination's, mm: ", self.x_coord)
        print("Diameters, mm: ", self.d_sections)
        # Дополнить печать остальными полями(Чисто для дебага)

