"""3D mask attack testing"""
import cv2
import numpy as np

class MaskAttack:
    """Test resistance to 3D mask attacks"""
    
    def __init__(self, detector, recognizer):
        self.detector = detector
        self.recognizer = recognizer
    
    def generate_mask_template(self, face_image):
        """Generate 3D mask template from face"""
        # Extract face landmarks
        detections = self.detector.detect(face_image)
        if not detections:
            return None
        
        # Create mask overlay
        mask = np.zeros_like(face_image)
        x1, y1, x2, y2 = detections[0].bbox
        
        # Draw oval mask
        center = ((x1+x2)//2, (y1+y2)//2)
        axes = ((x2-x1)//2, (y2-y1)//2)
        cv2.ellipse(mask, center, axes, 0, 0, 360, (255, 255, 255), -1)
        
        return mask
    
    def test_materials(self, face_image, target_api):
        """Test different mask materials"""
        materials = ["silicone", "paper", "plaster", "3d_print"]
        results = {}
        
        for material in materials:
            # Simulate material properties
            attack_image = self._apply_material(face_image, material)
            result = target_api.recognize(attack_image)
            results[material] = {
                "match": result.get("match", False) if result else False,
                "confidence": result.get("confidence", 0) if result else 0,
            }
        
        return results
    
    def _apply_material(self, image, material):
        """Apply material simulation"""
        if material == "silicone":
            return cv2.GaussianBlur(image, (7, 7), 2)
        elif material == "paper":
            noise = np.random.normal(0, 15, image.shape).astype(np.uint8)
            return cv2.add(image, noise)
        elif material == "plaster":
            return cv2.convertScaleAbs(image, alpha=0.9, beta=10)
        else:
            return image
