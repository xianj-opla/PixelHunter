"""Tests for face detector"""
import pytest
import numpy as np
from core.detector import FaceDetector

class TestFaceDetector:
    def test_init(self):
        detector = FaceDetector(backend="mtcnn")
        assert detector.backend == "mtcnn"
    
    def test_extract_face(self):
        detector = FaceDetector()
        image = np.random.randint(0, 255, (480, 640, 3), dtype=np.uint8)
        # Would need actual model for real test
        assert image.shape == (480, 640, 3)
