
from ORB_SLAM3.Settings import Settings
from ORB_SLAM3.KeyFrameDatabase import KeyFrameDatabase
from ORB_SLAM3.Map import Map
from ORB_SLAM3.FrameDrawer import FrameDrawer
from ORB_SLAM3.MapDrawer import MapDrawer
from ORB_SLAM3.Tracking import Tracking

class System:
    def __init__(self, path_to_settings, esensor=0) -> None:
        self.settings = Settings(path_to_settings)

        self.mpKeyFrameDatabase = KeyFrameDatabase()
        self.mpMap = Map()
        self.mpFrameDrawer = FrameDrawer()
        self.mpMapDrawer = MapDrawer(self.mpMap)
        self.mpTracker = Tracking(self.settings, self.mpMap, self.mpKeyFrameDatabase, self.mpFrameDrawer, self.mpMapDrawer, esensor)

        pass

    