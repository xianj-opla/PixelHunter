"""Model inversion attack"""
import numpy as np

class ModelInverter:
    """Reconstruct face images from embeddings"""
    
    def __init__(self, model):
        self.model = model
    
    def invert(self, target_embedding, iterations=1000, lr=0.01):
        """Reconstruct face from embedding"""
        # Initialize random image
        reconstructed = np.random.randint(0, 255, (112, 112, 3), dtype=np.uint8)
        
        for i in range(iterations):
            # Get embedding of current reconstruction
            current_emb = self.model.get_embedding(reconstructed)
            
            # Calculate gradient (simplified)
            gradient = target_embedding - current_emb
            
            # Update image
            update = (gradient.reshape(-1, 1) * np.random.randn(3)).reshape(reconstructed.shape)
            reconstructed = np.clip(reconstructed.astype(np.float32) + lr * update, 0, 255).astype(np.uint8)
            
            # Check convergence
            distance = np.linalg.norm(current_emb - target_embedding)
            if distance < 0.1:
                break
        
        return reconstructed
