"""
Face Detection Module
Supports MTCNN, RetinaFace, and YOLO-Face
"""

import cv2
import numpy as np
from typing import List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class FaceDetection:
    """Represents a detected face"""
    bbox: Tuple[int, int, int, int]  # x1, y1, x2, y2
    confidence: float
    landmarks: Optional[np.ndarray] = None
    embedding: Optional[np.ndarray] = None

class FaceDetector:
    """Multi-backend face detector"""
    
    def __init__(self, backend: str = "mtcnn", confidence_threshold: float = 0.9):
        self.backend = backend
        self.threshold = confidence_threshold
        self.model = self._load_model()
    
    def _load_model(self):
        """Load detection model"""
        if self.backend == "mtcnn":
            from facenet_pytorch import MTCNN
            return MTCNN(keep_all=True, thresholds=[self.threshold, self.threshold, self.threshold])
        elif self.backend == "retinaface":
            return self._load_retinaface()
        else:
            raise ValueError(f"Unknown backend: {self.backend}")
    
    def detect(self, image: np.ndarray) -> List[FaceDetection]:
        """
        Detect faces in image
        
        Args:
            image: Input image (BGR format)
        
        Returns:
            List of FaceDetection objects
        """
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes, probs, landmarks = self.model.detect(rgb, landmarks=True)
        
        detections = []
        for i, (box, prob) in enumerate(zip(boxes, probs)):
            if prob >= self.threshold:
                det = FaceDetection(
                    bbox=tuple(map(int, box)),
                    confidence=float(prob),
                    landmarks=landmarks[i] if landmarks is not None else None,
                )
                detections.append(det)
        
        return detections
    
    def extract_face(self, image: np.ndarray, detection: FaceDetection, size: Tuple[int, int] = (112, 112)) -> np.ndarray:
        """Extract and align face from detection"""
        x1, y1, x2, y2 = detection.bbox
        face = image[y1:y2, x1:x2]
        face = cv2.resize(face, size)
        return face
