
import cv2
import sys
from ORB_SLAM3.CameraModels.KannalaBrandt8 import KannalaBrandt8
from ORB_SLAM3.CameraModels.Pinhole import Pinhole

def readParameterFloat(fSettings, name, required=False):
    node = fSettings.getNode(name)
    if node.empty():
        if required:
            sys.stderr.write(f"{name} required parameter does not exist, aborting...\n")
            sys.exit(-1)
        else:
            sys.stderr.write(f"{name} optional parameter does not exist...")
            return 0.0, False
    elif not node.isReal():
        sys.stderr.write(f"{name} parameter must be a real number, aborting...")
        exit(-1)
    else:
        return node.real(), True

def readParameterInt(fSettings, name, required=False):
    node = fSettings.getNode(name)
    if node.empty():
        if required:
            sys.stderr.write(f"{name} required parameter does not exist, aborting...\n")
            sys.exit(-1)
        else:
            sys.stderr.write(f"{name} optional parameter does not exist...")
            return 0, False
    elif not node.isInt():
        sys.stderr.write(f"{name} parameter must be a real number, aborting...")
        exit(-1)
    else:
        return node.int(), True

class Settings:
    def __init__(self, path_to_settings) -> None:
        """ params to be stored """
        fsettings = cv2.FileStorage(path_to_settings, cv2.FILE_STORAGE_READ)

        
        self.readCamera(fsettings)
        print(f"\t-Loaded camera")

        self.readImageInfo(fsettings)
        print(f"\t-Loaded image info")

        self.readORB(fsettings)
        print(f"\t-Loaded ORB settings")
        # self.readViewer(fsettings)
        # print(f"\t-Loaded viewer settings")
        # self.readLoadAndSave(fsettings)
        # print(f"\t-Loaded Atlas settings")
        # self.readOtherParameters(fsettings)
        # print(f"\t-Loaded misc parameters")
        
        print(f"----------------------------------")

    def readCamera(self, fsettings):
        # camera: cameraModel, width, height, fx, fy, cx, cy, k1, k2, p1, p2, k3
        cameraModel = fsettings.getNode("Camera.type").string()
        self.vPinHoleDistorsion1_ = []
        self.bNeedToUndistort_ = False
        self.calibration1_ = None
        self.originalCalib1_ = None

        if cameraModel == "PinHole":
            self.cameraType_ = cameraModel
            fx, found = readParameterFloat(fsettings, "Camera1.fx")
            fy, found = readParameterFloat(fsettings, "Camera1.fy")
            cx, found = readParameterFloat(fsettings, "Camera1.cx")
            cy, found = readParameterFloat(fsettings, "Camera1.cy")
            vCalibration = (fx, fy, cx, cy)
            self.calibration1_ = Pinhole(vCalibration)
            self.originalCalib1_ = Pinhole(vCalibration)
            k1, found = readParameterFloat(fsettings, "Camera1.k1")
            if found:
                k2, found = readParameterFloat(fsettings, "Camera1.k2")
                p1, found = readParameterFloat(fsettings, "Camera1.p1")
                p2, found = readParameterFloat(fsettings, "Camera1.p2")
                k3, found = readParameterFloat(fsettings, "Camera1.k3")
                if found:
                    self.vPinHoleDistorsion1_ = [k1, k2, p1, p2, k3]
                else:
                    self.vPinHoleDistorsion1_ = [k1, k2, p1, p2]
            if len(self.vPinHoleDistorsion1_) == 0:
                self.bNeedToUndistort_ = True

        elif cameraModel == "KannalaBrandt8":
            self.cameraType_ = cameraModel
            # TODO: Judge if not found
            fx, found = readParameterFloat(fsettings, "Camera.fx")
            fy, found = readParameterFloat(fsettings, "Camera.fy")
            cx, found = readParameterFloat(fsettings, "Camera.cx")
            cy, found = readParameterFloat(fsettings, "Camera.cy")
            k0, found = readParameterFloat(fsettings, "Camera.k0")
            k1, found = readParameterFloat(fsettings, "Camera.k1")
            k2, found = readParameterFloat(fsettings, "Camera.k2")
            k3, found = readParameterFloat(fsettings, "Camera.k3")
            vCalibration = [fx, fy, cx, cy, k0, k1, k2, k3]
            self.calibration1_ = KannalaBrandt8(vCalibration)
            self.originalCalib1_ = KannalaBrandt8(vCalibration)

        else:
            sys.stderr.write(f"Camera model {cameraModel} not supported, aborting...\n")
            sys.exit(-1)

    def readImageInfo(self, fsettings):
        # image: width, height, fps, bRGB
        # self.imageWidth_ = fsettings['Camera.width']
        # self.imageWidth_, found = readParameterInt(fsettings, "Camera.width")
        # self.imageHeight_ = fsettings.getNode("Camera.height").int()
        # self.imageFPS_ = fsettings.getNode("Camera.fps").real()
        # self.imageRGB_ = fsettings.getNode("Camera.RGB").bool()
        pass
    
    def readORB(self, fsettings):

        nFeatures_, found = readParameterInt(fsettings, "ORBextractor.nFeatures")
        scaleFactor_, found = readParameterFloat(fsettings, "ORBextractor.scaleFactor")
        nLevels_, found = readParameterInt(fsettings, "ORBextractor.nLevels")
        initThFAST_, found = readParameterInt(fsettings, "ORBextractor.iniThFAST")
        minThFAST_, found = readParameterInt(fsettings, "ORBextractor.minThFAST")

    def readViewer(self, fsettings):
        pass

    def readLoadAndSave(self, fsettings):
        pass

    def readOtherParameters(self, fsettings):
        pass

    def nFeatures(self):
        return self.nFeatures_
    def nLevels(self):
        return self.nLevels_
    def initThFAST(self):
        return self.initThFAST_
    def minThFAST(self):
        return self.minThFAST_
    def scaleFactor(self):
        return self.scaleFactor_