from MathModels import *
from MathModels.Sourses import *

from Geometry import *
from Geometry.Sourses import *

from Section import *
from Section.Section import Section
from Solver import *

class Solver:
    def __init__(self):
        self.sections = []
        self.number_sections = 0
        self.results = []

    def make_solution(self):
        for section in self.sections: # Для каждой секции вызывается свой решатель и результат складывается одно место
            self.results.append(section.solve())
            #TODO
        return True

    def add_section(self):
        section = Section()
        section.create_section()
        section.get_math_model()
        self.sections.append(section)



