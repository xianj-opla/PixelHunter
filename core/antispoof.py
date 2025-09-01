"""
Anti-Spoofing Module
Tests face recognition systems against presentation attacks
"""

import cv2
import numpy as np
from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum

class AttackType(Enum):
    PHOTO = "photo"
    VIDEO = "video"
    MASK_3D = "3d_mask"
    MAKEUP = "makeup"
    DEEPFAKE = "deepfake"

@dataclass
class SpoofResult:
    """Result of anti-spoofing test"""
    attack_type: AttackType
    success: bool
    confidence: float
    details: str

class AntiSpoofTester:
    """Test anti-spoofing measures of face recognition systems"""
    
    def __init__(self, target_url: str, api_key: str = None):
        self.target_url = target_url
        self.api_key = api_key
        self.results: List[SpoofResult] = []
    
    def test_photo_attack(self, original_face: str, test_images: List[str]) -> SpoofResult:
        """
        Test resistance to photo-based attacks
        
        Args:
            original_face: Path to original face image
            test_images: List of test image paths (printed photos, screens)
        """
        successes = 0
        total = len(test_images)
        
        for img_path in test_images:
            # Send to target API
            result = self._send_recognition(img_path)
            if result and result.get("match", False):
                successes += 1
        
        success_rate = successes / total if total > 0 else 0
        
        return SpoofResult(
            attack_type=AttackType.PHOTO,
            success=success_rate > 0.1,  # >10% success = vulnerable
            confidence=success_rate,
            details=f"{successes}/{total} photo attacks succeeded ({success_rate*100:.1f}%)",
        )
    
    def test_video_attack(self, video_path: str) -> SpoofResult:
        """Test resistance to video replay attacks"""
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        success_count = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_count += 1
            if frame_count % 30 == 0:  # Test every 30th frame
                result = self._send_recognition_frame(frame)
                if result and result.get("match", False):
                    success_count += 1
        
        cap.release()
        
        return SpoofResult(
            attack_type=AttackType.VIDEO,
            success=success_count > 0,
            confidence=success_count / max(1, frame_count // 30),
            details=f"Video attack: {success_count} frames matched",
        )
    
    def generate_report(self) -> Dict:
        """Generate anti-spoofing test report"""
        return {
            "total_tests": len(self.results),
            "vulnerable": sum(1 for r in self.results if r.success),
            "safe": sum(1 for r in self.results if not r.success),
            "results": [
                {
                    "attack": r.attack_type.value,
                    "success": r.success,
                    "confidence": r.confidence,
                    "details": r.details,
                }
                for r in self.results
            ],
        }
    
    def _send_recognition(self, image_path: str) -> Dict:
        """Send image to face recognition API"""
        import requests
        
        try:
            with open(image_path, "rb") as f:
                files = {"image": f}
                headers = {}
                if self.api_key:
                    headers["Authorization"] = f"Bearer {self.api_key}"
                
                response = requests.post(
                    f"{self.target_url}/recognize",
                    files=files,
                    headers=headers,
                    timeout=10,
                )
                
                if response.status_code == 200:
                    return response.json()
        except Exception as e:
            print(f"Error: {e}")
        
        return None
    
    def _send_recognition_frame(self, frame: np.ndarray) -> Dict:
        """Send frame to face recognition API"""
        import requests
        
        try:
            _, img_encoded = cv2.imencode('.jpg', frame)
            files = {"image": ("frame.jpg", img_encoded.tobytes(), "image/jpeg")}
            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"
            
            response = requests.post(
                f"{self.target_url}/recognize",
                files=files,
                headers=headers,
                timeout=10,
            )
            
            if response.status_code == 200:
                return response.json()
        except:
            pass
        
        return None
