import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def detect_changes(before_path, after_path):

    # Load Images
    before = cv2.imread(before_path)
    after = cv2.imread(after_path)

    if before is None or after is None:
        raise ValueError(
            "Could not read one or both images. Please provide valid image files (e.g. PNG/JPG)."
        )

    # Resize for consistency
    before = cv2.resize(before, (800, 800))
    after = cv2.resize(after, (800, 800))

    # Convert to grayscale
    before_gray = cv2.cvtColor(
        before,
        cv2.COLOR_BGR2GRAY
    )

    after_gray = cv2.cvtColor(
        after,
        cv2.COLOR_BGR2GRAY
    )

    # SSIM Comparison
    score, diff = ssim(
        before_gray,
        after_gray,
        full=True
    )

    diff = (diff * 255).astype("uint8")

    # Thresholding
    _, thresh = cv2.threshold(
        diff,
        120,
        255,
        cv2.THRESH_BINARY_INV
    )

    # Morphological Cleanup
    kernel = np.ones((7, 7), np.uint8)

    thresh = cv2.morphologyEx(
        thresh,
        cv2.MORPH_OPEN,
        kernel
    )

    thresh = cv2.morphologyEx(
        thresh,
        cv2.MORPH_CLOSE,
        kernel
    )

    # Find Contours
    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = after.copy()

    changed_area = 0

    # Draw Bounding Boxes
    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 15000:

            changed_area += area

            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(
                result,
                (x, y),
                (x + w, y + h),
                (0, 0, 255),
                2
            )

    # Create Heatmap
    heatmap = cv2.applyColorMap(
        cv2.GaussianBlur(
            thresh,
            (15, 15),
            0
        ),
        cv2.COLORMAP_JET
    )

    # Calculate Changed Area %
    total_area = result.shape[0] * result.shape[1]

    change_percent = (
        changed_area / total_area
    ) * 100

    return (
        result,
        thresh,
        heatmap,
        change_percent,
        score
    )