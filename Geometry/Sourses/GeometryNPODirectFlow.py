from Geometry.GeometryNPO import GeometryNPO


class GeometryNPODirectFlow(GeometryNPO):
    flow_pattern = GeometryNPO.SCHEMES_FLOWS.get("direct flow")
    print(flow_pattern)

    def __init__(self):
        super().__init__()

    # TODO
    # Требуется дополнить эти модели