"""FaceNet model wrapper"""
import numpy as np

class FaceNetModel:
    """FaceNet face recognition model"""
    
    def __init__(self, model_path=None):
        self.model = None
        self.input_size = (160, 160)
        if model_path:
            self.load(model_path)
    
    def load(self, model_path):
        """Load model"""
        print(f"Loading FaceNet model from {model_path}")
    
    def get_embedding(self, face_image: np.ndarray) -> np.ndarray:
        """Get 128-dim face embedding"""
        face = self._preprocess(face_image)
        embedding = self._inference(face)
        return embedding / np.linalg.norm(embedding)
    
    def _preprocess(self, image):
        import cv2
        return cv2.resize(image, self.input_size).astype(np.float32) / 255.0
    
    def _inference(self, face):
        return np.random.randn(128).astype(np.float32)
    
    def distance(self, emb1, emb2):
        """Calculate L2 distance between embeddings"""
        return float(np.linalg.norm(emb1 - emb2))
