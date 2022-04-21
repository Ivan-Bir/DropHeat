from MathModels.MathModel import MathModel
from Geometry.Sourses.GeometryTZP import GeometryTZP


class MathModelTZP(MathModel):
    def __init__(self):
        print("Constructor MathModelTZP")
        super().__init__(GeometryTZP())

    def solve(self): # Перегружаем метод Solve, общий для всех матмоделй
        MathModel.solve(self)
        print(self.geometry.area_relative) # Например
        print("Overloading solve in TZP")


x = MathModelTZP()
x.solve()