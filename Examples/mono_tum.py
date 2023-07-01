import argparse

import sys, os
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(PROJECT_PATH)
from ORB_SLAM3.System import System

if __name__=="__main__":
    argparser = argparse.ArgumentParser(description= "Usage: \
        python mono_tum.py \
            -c path_to_settings \
            -s path_to_sequence"
    )
    default_path_to_settings = "/home/lj/Documents/pyORBSLAM3/configs/TUM1.yaml"
    default_path_to_sequence = "/media/lj/TOSHIBA/dataset/TUM/2-Handheld_SLAM/rgbd_dataset_freiburg1_desk/rgb"
    # argparser.add_argument('-v', '--path_to_vocabulary', type=str, help='Path to vocabulary file', required=True)
    argparser.add_argument('-c', '--path_to_settings', type=str, help='Path to settings file', default=default_path_to_settings)
    argparser.add_argument('-s', '--path_to_sequence', type=str, help='Path to sequence folder', default=default_path_to_sequence)

    args = argparser.parse_args()

    SLAM = System(args.path_to_settings)
    