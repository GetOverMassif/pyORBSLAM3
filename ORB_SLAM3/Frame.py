

class Frame:
    def __init__(self, imLeft, timestamp) -> None:
        # params to be copy: 
        #   mpcpi, mpORBvocabulary,mpORBextractorLeft ,mpORBextractorRight,
        #   mTimeStamp, mK, mK_, mDistCoef, mbf, mThDepth,
        #   mImuCalib, mpImuPreintegrated, mpPrevFrame,mpImuPreintegratedFrame, 
        #   mpReferenceKF, mbImuPreintegrated, mpCamera, mpCamera2,
        #   mbHasPose, mbHasVelocity


        self.mpFeatureExtractor = None
        
        # copy the image

        # Frame ID

        # Scale Level Info: 
        #   levels, factor, logFactor, 
        #   mvScaleFactors, mvInvScaleFactors, mvLevelSigma2, mvInvLevelSigma2

        # Feature Extraction


        pass

    def ExtractORB(self, im):
        self.numKeyPoints, self.mvKeys, self.mDescriptors \
            = self.mpFeatureExtractor(im, None)