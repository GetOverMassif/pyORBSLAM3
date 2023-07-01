from ORB_SLAM3.CameraModels.GeometricCamera import GeometricCamera

class Pinhole(GeometricCamera):
    def __init__(self, _vParameters) -> None:
        super().__init__(_vParameters)
        self.mnId = self.nNextId
        self.nNextId = self.nNextId + 1
        self.mnType = self.CAM_PINHOLE
    