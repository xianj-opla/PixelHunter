"""Model extraction attack"""
import numpy as np
import requests

class ModelExtractor:
    """Extract face recognition model via API queries"""
    
    def __init__(self, target_api):
        self.api = target_api
        self.queries = 0
        self.responses = []
    
    def extract(self, num_queries=1000):
        """Extract model by querying with random inputs"""
        for i in range(num_queries):
            # Generate random face-like input
            random_face = np.random.randint(0, 255, (112, 112, 3), dtype=np.uint8)
            
            # Query API
            result = self.api.recognize(random_face)
            self.responses.append(result)
            self.queries += 1
        
        return self._analyze_responses()
    
    def _analyze_responses(self):
        """Analyze API responses to extract model information"""
        embedding_dims = set()
        for resp in self.responses:
            if resp and "embedding" in resp:
                embedding_dims.add(len(resp["embedding"]))
        
        return {
            "queries": self.queries,
            "embedding_dims": list(embedding_dims),
            "success": len(embedding_dims) > 0,
        }
