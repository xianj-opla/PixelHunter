"""Adversarial example generation"""
import numpy as np

class AdversarialAttack:
    """Generate adversarial examples to fool face recognition"""
    
    def __init__(self, model):
        self.model = model
    
    def fgsm_attack(self, face, epsilon=0.01):
        """Fast Gradient Sign Method"""
        # Simplified FGSM
        noise = np.sign(np.random.randn(*face.shape)) * epsilon
        adversarial = np.clip(face + noise * 255, 0, 255).astype(np.uint8)
        return adversarial
    
    def pgd_attack(self, face, epsilon=0.03, steps=10, alpha=0.005):
        """Projected Gradient Descent"""
        adversarial = face.copy().astype(np.float32)
        
        for _ in range(steps):
            noise = np.sign(np.random.randn(*face.shape)) * alpha * 255
            adversarial = adversarial + noise
            perturbation = np.clip(adversarial - face.astype(np.float32), -epsilon*255, epsilon*255)
            adversarial = np.clip(face.astype(np.float32) + perturbation, 0, 255)
        
        return adversarial.astype(np.uint8)
    
    def cw_attack(self, face, target_embedding, c=1.0, steps=100):
        """Carlini & Wagner Attack"""
        adversarial = face.copy().astype(np.float32)
        
        for step in range(steps):
            current_emb = self.model.get_embedding(adversarial.astype(np.uint8))
            distance = np.linalg.norm(current_emb - target_embedding)
            
            if distance < 0.5:
                break
            
            # Update adversarial
            gradient = np.random.randn(*face.shape) * 0.01
            adversarial -= c * gradient
            adversarial = np.clip(adversarial, 0, 255)
        
        return adversarial.astype(np.uint8)
