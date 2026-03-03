import cv2
import numpy as np


def get_camera_matrix(img_shape):
    h, w = img_shape[:2]

    focal_length = w
    cx = w / 2
    cy = h / 2

    K = np.array([
        [focal_length, 0, cx],
        [0, focal_length, cy],
        [0, 0, 1]
    ])

    return K

def estimate_pose(pts1, pts2, img_shape):
    K = get_camera_matrix(img_shape)

    E, mask = cv2.findEssentialMat(
        pts1,
        pts2,
        K,
        method=cv2.RANSAC,
        prob=0.999,
        threshold=1.0
    )

    pts1_inliers = pts1[mask.ravel() == 1]
    pts2_inliers = pts2[mask.ravel() == 1]

    _, R, t, _ = cv2.recoverPose(E, pts1_inliers, pts2_inliers, K)

    return R, t, mask


def extract_planar_motion(R, t):
    # delta_x = t[0][0]
    # delta_y = t[1][0]

    delta_x = -t[0][0]
    delta_y = -t[1][0]

    yaw = np.arctan2(R[1, 0], R[0, 0])
    yaw_deg = np.degrees(yaw)

    return delta_x, delta_y, yaw_deg