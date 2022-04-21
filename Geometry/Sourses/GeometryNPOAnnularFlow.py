from Geometry.GeometryNPO import GeometryNPO


class GeometryNPOAnnularFlow(GeometryNPO):
    flow_pattern = GeometryNPO.SCHEMES_FLOWS.get("annular flow")
    print(flow_pattern)

    def __init__(self):
        super().__init__()

    # TODO
    # Требуется дополнить эти модели