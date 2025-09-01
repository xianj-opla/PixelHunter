"""Image preprocessing utilities"""
import cv2
import numpy as np

def align_face(image, landmarks, target_size=(112, 112)):
    """Align face using landmarks"""
    src = np.array(landmarks, dtype=np.float32)
    dst = np.array([[30.2946, 51.6963], [65.5318, 51.5014], [48.0252, 71.7366]], dtype=np.float32)
    
    M = cv2.estimateAffinePartial2D(src, dst)[0]
    aligned = cv2.warpAffine(image, M, target_size)
    return aligned

def normalize(image, mean=127.5, std=128.0):
    """Normalize image for model input"""
    return (image.astype(np.float32) - mean) / std

def augment(image):
    """Apply data augmentation"""
    if np.random.random() > 0.5:
        image = cv2.flip(image, 1)
    if np.random.random() > 0.5:
        brightness = np.random.uniform(0.8, 1.2)
        image = np.clip(image * brightness, 0, 255).astype(np.uint8)
    return image
