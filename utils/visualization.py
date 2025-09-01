"""Visualization utilities"""
import cv2
import numpy as np

def draw_detections(image, detections, color=(0, 255, 0)):
    """Draw bounding boxes on image"""
    for det in detections:
        x1, y1, x2, y2 = det.bbox
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        cv2.putText(image, f"{det.confidence:.2f}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    return image

def create_comparison(original, adversarial, label_orig, label_adv):
    """Create side-by-side comparison"""
    h, w = original.shape[:2]
    canvas = np.zeros((h, w*2+20, 3), dtype=np.uint8)
    canvas[:, :w] = original
    canvas[:, w+20:] = adversarial
    
    cv2.putText(canvas, label_orig, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.putText(canvas, label_adv, (w+30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    
    return canvas
