import os
import cv2
from feature_matching import load_images, detect_and_compute, match_features, get_matched_keypoints


from pose_estimation import estimate_pose, extract_planar_motion
from feature_matching import get_matched_keypoints


from visualization import draw_inlier_matches, draw_motion_arrow, overlay_text


def run_pipeline(img1_path, img2_path, pair_name):
    print(f"\n ---Computation for Pair: {pair_name}---\n")
    img1, img2 = load_images(img1_path, img2_path)

    kp1, desc1 = detect_and_compute(img1)
    kp2, desc2 = detect_and_compute(img2)

    matches = match_features(desc1, desc2)

    pts1, pts2 = get_matched_keypoints(kp1, kp2, matches)

    R, t, mask = estimate_pose(pts1, pts2, img1.shape)
    
    dx, dy, dtheta = extract_planar_motion(R, t)

    print(f"ΔX: {dx:.4f}")
    print(f"ΔY: {dy:.4f}")
    print(f"Δθ (degrees): {dtheta:.2f}")

    corr_x = -dx
    corr_y = -dy
    corr_theta = -dtheta

    print("\n--- Suggested Correction ---")
    print(f"Move X: {corr_x:.4f}")
    print(f"Move Y: {corr_y:.4f}")
    print(f"Rotate θ: {corr_theta:.2f}")

    # Visualization
    match_img = draw_inlier_matches(img1, img2, kp1, kp2, matches, mask.ravel())
    motion_img = draw_motion_arrow(img1.copy(), dx, dy)
    motion_img = overlay_text(motion_img, dx, dy, dtheta)

    cv2.imwrite(f"results/{pair_name}_matches.jpg", match_img)
    cv2.imwrite(f"results/{pair_name}_motion.jpg", motion_img)

    return dx, dy, dtheta


if __name__ == "__main__":
    # img1_path = "data/Pair1/Desk_1(a).jpg"
    # img2_path = "data/Pair1/Desk_1(b).jpg"
    # pair_name = "Pair1"

    # img1_path = "data/Pair2/Chair_1.jpg"
    # img2_path = "data/Pair2/Chair_2.jpg"
    # pair_name = "Pair2"

    # img1_path = "data/Pair3/Desk_2(a).jpg"
    # img2_path = "data/Pair3/Desk_2(b).jpg"
    # pair_name = "Pair3"

    # img1_path = "data/Pair4/Desk_3(a).jpg"
    # img2_path = "data/Pair4/Desk_3(b).jpg"
    # pair_name = "Pair4"

    img1_path = "data/Pair5/Desk_4(a).jpg"
    img2_path = "data/Pair5/Desk_4(b).jpg"
    pair_name = "Pair5"

    run_pipeline(img1_path, img2_path, pair_name)