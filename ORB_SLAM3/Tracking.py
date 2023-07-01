import cv2
import numpy as np

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

    def TrackMonocular(self, im, timestamp):
        Tcw = np.eye(4)
        cv2.imshow("im", im)
        cv2.waitKey(1)
        
        # convert to grayscale
        mImGray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # if not initialized or no image yet, mCurrentFrame created by InitFeatureExtractor
        # else mCurrentFrame created by FeatureExtractor

        self.Track()

        # 1. Create Frame
        # 2. Track Frame
        # 3. Update Map
        # 4. Update Drawer
        # 5. Update Last Frame


        # return mCurrentFrame.mTcw.clone()
        return Tcw
    
    def track(self):
        # No image -> not initialized

        # last_state

        # if not initialized, MonocularInitialization(), update FrameDrawer
        # else: check: https://github.com/raulmur/ORB_SLAM2/blob/master/src/Tracking.cc#L238

        pass

    def MonocularInitialization(self):
        pass