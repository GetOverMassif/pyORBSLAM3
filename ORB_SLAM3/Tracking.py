
class Tracking:
    def __init__(self, settings, mpMap, mpKeyFrameDatabase, mpFrameDrawer, mpMapDrawer, esensor) -> None:
        # Load camera parameters from settings file
        self.newParameterLoader(settings)
        self.initID = 0
        self.lastID = 0
        self.mbInitWith3KFs = False
        self.mnNumDataset = 0

        # print all cam info
        pass

    def newParameterLoader(self, settings):
        # camera

        # image: K, min/max Frame

        # ORB

        # imu

        pass
    