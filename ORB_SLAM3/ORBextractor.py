import cv2

class ORBextractor:
    def __init__(self) -> None:
        self.orb = cv2.ORB_create()
        pass

    def __call__(self, im, mask=None):
        img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        kp, des = self.orb.detectAndCompute(img, mask)
        return len(kp), kp, des