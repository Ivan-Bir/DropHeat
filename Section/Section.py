from Geometry.Sourses import *
from Geometry.Geometry import *
from MathModels.Sourses import *
from MathModels.MathModel import *

class Section:
    is_ready = False

    def __init__(self, geometry: Geometry, math_model: MathModel, context = None):
        self.geometry = geometry
        self.math_model = math_model

        print("Constructor Section")

    def create_section(self):
        # self.get_geometry()
        self.get_math_model()

        self.geometry.input_coords()
        self.geometry.input_diameters()

        if self.math_model.input_parameters():
            print("Success get input_parameters")

        self.is_ready = True
        return True


    # def get_geometry(self): # Обращается к GUI
    #     print("Need geometry to Section")

    def get_math_model(self):
        print("Need math model to Section")