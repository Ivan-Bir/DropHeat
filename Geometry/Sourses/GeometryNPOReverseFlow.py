from Geometry.GeometryNPO import GeometryNPO


class GeometryNPOReverseFlow(GeometryNPO):
    flow_pattern = GeometryNPO.SCHEMES_FLOWS.get("reverse flow")
    print(flow_pattern)

    def __init__(self):
        super().__init__()

    # TODO
    # Требуется дополнить эти модели


