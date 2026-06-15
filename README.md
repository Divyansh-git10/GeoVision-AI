# 🌍 GeoVision AI

GeoVision AI is a satellite disaster change detection system built using OpenCV, SSIM, and Streamlit.

The application compares before-disaster and after-disaster satellite imagery, identifies affected regions, estimates the percentage of changed area, generates damage heatmaps, and classifies disaster severity.

## Features

* Satellite image comparison
* Structural Similarity Index (SSIM) analysis
* Change detection and localization
* Damage heatmap generation
* Severity classification (Low, Moderate, Severe)
* Interactive Streamlit dashboard

## Tech Stack

* Python
* OpenCV
* NumPy
* scikit-image
* Streamlit

## Project Workflow

1. Upload BEFORE satellite image
2. Upload AFTER satellite image
3. Compute SSIM similarity score
4. Generate change mask
5. Detect affected regions
6. Estimate changed area percentage
7. Generate damage heatmap
8. Classify disaster severity

## Results

The system provides:

* Similarity Score
* Changed Area Percentage
* Severity Level
* Detected Change Regions
* Binary Change Mask
* Damage Heatmap

## Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app_streamlit.py
```

## Future Improvements

* Deep Learning-based segmentation
* Multi-temporal satellite analysis
* Cloud deployment
* Real-time disaster monitoring

## Author

Divyansh Gautam
