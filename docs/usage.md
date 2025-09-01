# Usage Guide

## Quick Start

### Anti-Spoofing Test
```bash
python pixelhunter.py antispoof --target http://api.example.com/face
```

### Generate Adversarial Examples
```bash
python pixelhunter.py adversarial --image face.jpg --model arcface
```

### Deepfake Detection
```bash
python pixelhunter.py deepfake --input suspicious.jpg
```

### Full Assessment
```bash
python pixelhunter.py assess --target http://api.example.com
```

## API Usage

```python
from core.detector import FaceDetector
from core.antispoof import AntiSpoofTester

detector = FaceDetector()
faces = detector.detect(image)

tester = AntiSpoofTester("http://api.example.com")
result = tester.test_photo_attack("face.jpg", ["photo1.jpg", "photo2.jpg"])
```
