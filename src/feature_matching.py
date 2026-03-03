import cv2
import numpy as np


def load_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        raise ValueError("Error loading images. Check file paths.")

    return img1, img2


def detect_and_compute(img):
    orb = cv2.ORB_create(
        nfeatures=2000,
        scaleFactor=1.2,
        nlevels=8
    )

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    keypoints, descriptors = orb.detectAndCompute(gray, None)

    return keypoints, descriptors


def match_features(desc1, desc2):
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(desc1, desc2)

    matches = sorted(matches, key=lambda x: x.distance)

    return matches


def filter_matches(matches, ratio=0.75):
    return matches


def get_matched_keypoints(kp1, kp2, matches):
    pts1 = np.float32([kp1[m.queryIdx].pt for m in matches])
    pts2 = np.float32([kp2[m.trainIdx].pt for m in matches])

    return pts1, pts2