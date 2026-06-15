import streamlit as st
import cv2
from src.change_detection import detect_changes

st.set_page_config(
    page_title="GeoVision AI",
    layout="wide"
)

# Header
st.title("🌍 GeoVision AI")
st.subheader("Satellite Disaster Change Detection")

# File Uploaders
before = st.file_uploader(
    "Upload BEFORE Image",
    type=["jpg", "png", "jpeg"]
)

after = st.file_uploader(
    "Upload AFTER Image",
    type=["jpg", "png", "jpeg"]
)

# Run Detection
if before and after:

    with open("before.jpg", "wb") as f:
        f.write(before.read())

    with open("after.jpg", "wb") as f:
        f.write(after.read())

    result, mask, heatmap, percent, score = detect_changes(
        "before.jpg",
        "after.jpg"
    )

    # Severity Classification
    if percent < 10:
        severity = "Low"

    elif percent < 30:
        severity = "Moderate"

    else:
        severity = "Severe"

    # Severity Banner
    if severity == "Low":
        st.success("🟢 Low Impact Region")

    elif severity == "Moderate":
        st.warning("🟡 Moderate Damage Detected")

    else:
        st.error("🔴 Severe Damage Detected")

    # Results
    st.subheader("📊 Analysis Results")

    img1, img2, img3 = st.columns(3)

    with img1:
        st.image(
            result,
            caption="Detected Changes",
            use_container_width=True
        )

    with img2:
        st.image(
            mask,
            caption="Change Mask",
            use_container_width=True
        )

    with img3:
        st.image(
            heatmap,
            caption="Damage Heatmap",
            use_container_width=True
        )

    # Summary Box
    st.info(
        f"""
        Similarity Score: {score:.4f}

        Estimated Changed Area: {percent:.2f}%

        Severity Level: {severity}
        """
    )

# Footer
st.markdown("---")
st.caption(
    "GeoVision AI • Satellite Disaster Assessment using SSIM and Computer Vision"
)