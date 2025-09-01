"""Security scoring system"""
from typing import List, Dict

class SecurityScorer:
    """Calculate security score for face recognition systems"""
    
    WEIGHTS = {
        "antispoof": 0.30,
        "adversarial": 0.25,
        "deepfake": 0.20,
        "model_security": 0.15,
        "access_control": 0.10,
    }
    
    def calculate_score(self, test_results: Dict) -> Dict:
        """Calculate overall security score"""
        scores = {}
        
        for category, weight in self.WEIGHTS.items():
            if category in test_results:
                scores[category] = test_results[category] * weight
        
        total = sum(scores.values())
        
        return {
            "total_score": total,
            "max_score": 100,
            "grade": self._get_grade(total),
            "breakdown": scores,
            "recommendations": self._get_recommendations(scores),
        }
    
    def _get_grade(self, score):
        if score >= 90: return "A"
        if score >= 80: return "B"
        if score >= 70: return "C"
        if score >= 60: return "D"
        return "F"
    
    def _get_recommendations(self, scores):
        recs = []
        if scores.get("antispoof", 0) < 0.2:
            recs.append("Improve anti-spoofing measures")
        if scores.get("adversarial", 0) < 0.15:
            recs.append("Add adversarial training")
        if scores.get("deepfake", 0) < 0.1:
            recs.append("Implement deepfake detection")
        return recs
