
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
        self.mpMapDrawer = MapDrawer(self.mpMap, self.settings)
        self.mpTracker = Tracking(self.settings, self.mpMap, self.mpKeyFrameDatabase, self.mpFrameDrawer, self.mpMapDrawer, esensor)

        pass

    def TrackMonocular(self, im, timestamp):
        # TODO: check sensor mode

        # TODO: check mode change(activate/deactivate localization)

        # TODO: check reset

        Tcw = self.mpTracker.TrackMonocular(im, timestamp)

        # update tracking_state, mappoints and frame

        return Tcw

    