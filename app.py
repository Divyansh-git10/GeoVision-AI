import cv2
from src.change_detection import detect_changes

result, mask, percent = detect_changes(
    "data/before/image1.jpg",
    "data/after/image1.jpg"
)

print(f"Changed Area: {percent:.2f}%")

cv2.imwrite("result.jpg", result)
cv2.imwrite("mask.jpg", mask)

print("Results saved successfully")
if percent < 10:
    severity = "Low"

elif percent < 30:
    severity = "Moderate"

else:
    severity = "Severe"

print(f"Severity: {severity}")