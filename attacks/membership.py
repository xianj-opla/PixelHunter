"""Membership inference attack"""
import numpy as np

class MembershipInference:
    """Determine if a face was in training set"""
    
    def __init__(self, model, threshold=0.8):
        self.model = model
        self.threshold = threshold
    
    def infer(self, face, known_members=None):
        """Infer if face was in training data"""
        embedding = self.model.get_embedding(face)
        
        # Check confidence score
        # Members typically have higher confidence
        confidence = np.max(np.abs(embedding))
        
        is_member = confidence > self.threshold
        
        return {
            "is_member": is_member,
            "confidence": float(confidence),
            "threshold": self.threshold,
        }
    
    def batch_infer(self, faces):
        """Infer membership for multiple faces"""
        results = []
        for face in faces:
            results.append(self.infer(face))
        return results
