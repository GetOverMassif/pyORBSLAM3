class GeometricCamera:
    CAM_PINHOLE = 0
    CAM_FISHEYE = 1
    # TODO: To solve the problem of static variable nNextId
    nNextId: int = 0
    def __init__(self, _vParameters) -> None:
        self.mvParameters = _vParameters
        self.mnType = self.CAM_PINHOLE