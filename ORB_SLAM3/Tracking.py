import cv2
import numpy as np
from enum import Enum
from ORB_SLAM3.Frame import Frame
from ORB_SLAM3.ORBextractor import ORBextractor

class eTrackingState(Enum):
    SYSTEM_NOT_READY=-1
    NO_IMAGES_YET=0
    NOT_INITIALIZED=1
    OK=2
    RECENTLY_LOST=3
    LOST=4
    OK_KLT=5

class Tracking:
    def __init__(self, settings, mpMap, mpKeyFrameDatabase, mpFrameDrawer, mpMapDrawer, esensor) -> None:
        # Load camera parameters from settings file
        self.newParameterLoader(settings)
        self.initID = 0
        self.lastID = 0
        self.mbInitWith3KFs = False
        self.mnNumDataset = 0

        self.mState = eTrackingState.NO_IMAGES_YET

        # print all cam info
        pass

    def newParameterLoader(self, settings):
        # camera

        # image: K, min/max Frame

        # ORB
        # mpIniORBextractor.nfeatures = 5 * mpORBextractorRight.nfeatures

        # int nFeatures = settings
        # int nLevels = 
        # int fIniThFAST
        # int fMinThFAST
        # int fScaleFactor

        # self.mpInitExtractor = ORBextractor(nFeatures, fScaleFactor, nLevels, fIniThFAST, fMinThFAST)
        # self.mpTrackExtractor = ORBextractor(5*nFeatures, fScaleFactor, nLevels, fThFAST, fMinThFAST)
        # # imu

        pass

    def TrackMonocular(self, im, timestamp):
        Tcw = np.eye(4)
        cv2.imshow("im", im)
        cv2.waitKey(1)
        
        # Step 1: convert to gray
        self.mImGray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        # Step 2: create Frame

        # if not initialized or no image yet, mCurrentFrame created by InitFeatureExtractor
        # else mCurrentFrame created by FeatureExtractor

        # TODO: 可能还要考虑该帧ID与初始ID之间的差值
        if self.mState == eTrackingState.NOT_INITIALIZED or self.mState == eTrackingState.NO_IMAGES_YET:
            self.mCurrentFrame = Frame(self.mImGray, timestamp)
        else:
            self.mCurrentFrame = Frame()

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