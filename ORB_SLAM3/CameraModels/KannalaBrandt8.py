from ORB_SLAM3.CameraModels.GeometricCamera import GeometricCamera

class KannalaBrandt8(GeometricCamera):
    def __init__(self, _vParameters) -> None:
        super().__init__(_vParameters)