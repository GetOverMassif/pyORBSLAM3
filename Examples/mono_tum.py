import argparse

import sys, os
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import os.path as osp
import cv2

sys.path.append(PROJECT_PATH)
from ORB_SLAM3.System import System

def LoadImages(strFile):
    with open(strFile, 'r') as f:
        vstrImageFilenames = []
        vTimestamps = []
        for line in f.readlines():
            if line[0] == '#':
                continue
            line = line.split()
            vstrImageFilenames.append(line[1])
            vTimestamps.append(float(line[0]))
    return vstrImageFilenames, vTimestamps

if __name__=="__main__":
    argparser = argparse.ArgumentParser(description= "Usage: \
        python mono_tum.py \
            -c path_to_settings \
            -s path_to_sequence"
    )
    default_path_to_settings = "/home/lj/Documents/pyORBSLAM3/configs/TUM1.yaml"
    default_path_to_sequence = "/media/lj/TOSHIBA/dataset/TUM/2-Handheld_SLAM/rgbd_dataset_freiburg1_desk"
    # default_path_to_settings = "/home/nio/文档/pyORBSLAM3/configs/TUM1.yaml"
    # default_path_to_sequence = "/mnt/dataDisk/BUAA/TUM/RGB-D/Handheld_SLAM/rgbd_dataset_freiburg1_desk"
    # argparser.add_argument('-v', '--path_to_vocabulary', type=str, help='Path to vocabulary file', required=True)
    argparser.add_argument('-c', '--path_to_settings', type=str, help='Path to settings file', default=default_path_to_settings)
    argparser.add_argument('-s', '--path_to_sequence', type=str, help='Path to sequence folder', default=default_path_to_sequence)

    args = argparser.parse_args()

    strFile = osp.join(args.path_to_sequence, "rgb.txt")
    vstrImageFilenames, vTimestamps = LoadImages(strFile)

    nImages = len(vstrImageFilenames)

    SLAM = System(args.path_to_settings)

    for ni in range(nImages):
        im = cv2.imread(osp.join(args.path_to_sequence, vstrImageFilenames[ni]), cv2.IMREAD_UNCHANGED)
        tframe = vTimestamps[ni]

        if im is None:
            print(f"Failed to load image at {vstrImageFilenames[ni]}")
            sys.exit(0)
        
        SLAM.TrackMonocular(im, tframe)
    
    cv2.destroyAllWindows()


    