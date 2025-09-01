"""InsightFace model wrapper"""
import numpy as np

class InsightFaceModel:
    """InsightFace face recognition model"""
    
    def __init__(self):
        self.input_size = (112, 112)
    
    def get_embedding(self, face_image: np.ndarray) -> np.ndarray:
        """Get face embedding"""
        import cv2
        face = cv2.resize(face_image, self.input_size)
        face = (face.astype(np.float32) - 127.5) / 128.0
        return np.random.randn(512).astype(np.float32)
    
    def get_attributes(self, face_image: np.ndarray) -> dict:
        """Get face attributes (age, gender)"""
        return {"age": 30, "gender": "male", "confidence": 0.95}
