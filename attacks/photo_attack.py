"""Photo-based presentation attacks"""
import cv2
import numpy as np

class PhotoAttack:
    """Test resistance to photo-based attacks"""
    
    def __init__(self, detector, recognizer):
        self.detector = detector
        self.recognizer = recognizer
    
    def generate_attack(self, original_face, output_size=(640, 480)):
        """Generate printed photo attack"""
        # Resize face to realistic size
        photo = cv2.resize(original_face, output_size)
        
        # Add print artifacts
        photo = self._add_print_artifacts(photo)
        
        return photo
    
    def _add_print_artifacts(self, image):
        """Add artifacts typical of printed photos"""
        # Add slight blur (printer quality)
        image = cv2.GaussianBlur(image, (3, 3), 0.5)
        
        # Add paper texture noise
        noise = np.random.normal(0, 5, image.shape).astype(np.uint8)
        image = cv2.add(image, noise)
        
        return image
    
    def test(self, target_api, original_face, num_trials=10):
        """Run photo attack test"""
        successes = 0
        for i in range(num_trials):
            photo = self.generate_attack(original_face)
            result = target_api.recognize(photo)
            if result and result.get("match"):
                successes += 1
        
        return {
            "success_rate": successes / num_trials,
            "successes": successes,
            "total": num_trials,
        }
