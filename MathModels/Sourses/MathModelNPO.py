from MathModels.MathModel import MathModel
from Geometry.GeometryNPO import GeometryNPO


class MathModelNPO(MathModel):
    def __init__(self):
        print("Constructor MathModelNPO")
        # geometry =
        super().__init__(GeometryNPO())

    def solve(self): # Перегружаем метод Solve, общий для всех матмоделй
        MathModel.solve(self)
        print(self.geometry.d_critical) # Например

        # GeometryNPO.GeometryNPO
        # Geometry.


x = MathModelNPO()
x.solve()