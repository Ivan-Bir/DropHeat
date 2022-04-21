from Geometry.Geometry import Geometry
from Geometry.GeometryNPO import GeometryNPO

class MathModel: # Базовый класс всех матмоделей.
    ready_for_use = False

    def __init__(self, geometry: Geometry): # Мат модель будет содержать объект класса геометрии
        self.geometry = geometry

        print(type(geometry))
        print("Created Base Math Model")

    def input_parameters(self): # Считывает параметры для определенной модели с формы.
                                # В базовом классе не должно быть реализации
        print("Error: input_parameters MathModel in Base class.")
        return True # В случае успеха

    def solve(self): # Вызывает обсчёт имеющейся геометрии по заданным зависимостям.
                     # В базовом классе должен быть пустым
        print("Error: MathModel in Base class.")
        return True


x = MathModel(Geometry()) # Пример создания
# x.geometry.area_critical

y = MathModel(GeometryNPO()) # Пример создания. Тут производный класс спокойно преобразуюется к типу базового

cy = MathModel(1) # Будет подчеркивать
