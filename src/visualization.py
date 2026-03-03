import cv2
import numpy as np


def draw_inlier_matches(img1, img2, kp1, kp2, matches, mask):
    inlier_matches = [m for i, m in enumerate(matches) if mask[i]]

    matched_img = cv2.drawMatches(
        img1, kp1,
        img2, kp2,
        inlier_matches,
        None,
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )

    return matched_img


def draw_motion_arrow(img, dx, dy):
    h, w = img.shape[:2]
    center = (int(w / 2), int(h / 2))

    scale = 100
    end_point = (
        int(center[0] + dx * scale),
        int(center[1] - dy * scale)
    )

    cv2.arrowedLine(img, center, end_point, (0, 0, 255), 4)

    return img


def overlay_text(img, dx, dy, dtheta):
    text1 = f"Delta X: {dx:.3f}"
    text2 = f"Delta Y: {dy:.3f}"
    text3 = f"Delta Theta: {dtheta:.2f} deg"

    cv2.putText(img, text1, (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(img, text2, (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(img, text3, (30, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    return img