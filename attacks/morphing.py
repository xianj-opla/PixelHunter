"""Face morphing attack"""
import cv2
import numpy as np

class FaceMorpher:
    """Create face morphs to fool recognition systems"""
    
    def morph(self, face1, face2, alpha=0.5):
        """Create morphed face between two faces"""
        # Align faces
        aligned1 = self._align_face(face1)
        aligned2 = self._align_face(face2)
        
        # Blend faces
        morphed = cv2.addWeighted(aligned1, alpha, aligned2, 1 - alpha, 0)
        
        return morphed
    
    def _align_face(self, face):
        """Align face to standard position"""
        return cv2.resize(face, (112, 112))
    
    def create_morph_sequence(self, face1, face2, steps=10):
        """Create sequence of morphed faces"""
        morphs = []
        for i in range(steps + 1):
            alpha = i / steps
            morph = self.morph(face1, face2, alpha)
            morphs.append(morph)
        return morphs
