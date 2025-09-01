# 👁️ PixelHunter

<p align="center">
  <img src="https://img.shields.io/badge/version-1.8.0-blue.svg" alt="version">
  <img src="https://img.shields.io/badge/python-3.9+-green.svg" alt="python">
  <img src="https://img.shields.io/badge/license-MIT-yellow.svg" alt="license">
  <img src="https://img.shields.io/badge/deep_learning-PyTorch-orange.svg" alt="pytorch">
</p>

> **AI-Powered Face Recognition Security Audit Framework** — Automated vulnerability assessment, anti-spoofing testing, and adversarial attack generation for face recognition systems.

<p align="center">
  <b>⚠️ For authorized security testing only ⚠️</b>
</p>

---

## 🎯 Overview

PixelHunter is a comprehensive security framework for auditing face recognition systems. It provides tools for testing anti-spoofing measures, generating adversarial examples, and assessing the overall security posture of biometric authentication systems.

## ✨ Features

- 🎭 **Anti-Spoofing Testing** — Test resistance to photo/video/3D mask attacks
- 🖼️ **Adversarial Examples** — Generate adversarial images to fool recognition
- 🔍 **Model Extraction** — Extract face recognition model parameters
- 📊 **Accuracy Assessment** — Test false acceptance/rejection rates
- 🎥 **Deepfake Detection** — Identify manipulated face images
- 🔐 **Bypass Generation** — Create bypass attempts for authentication
- 📈 **Security Scoring** — CVSS-based security assessment
- 🧪 **Benchmark Suite** — Standard benchmark datasets for testing

## 📦 Installation

```bash
git clone https://github.com/xianj-opla/PixelHunter.git
cd PixelHunter
pip install -r requirements.txt
```

## 🚀 Quick Start

```bash
# Test anti-spoofing
python pixelhunter.py antispoof --target http://api.example.com/face

# Generate adversarial examples
python pixelhunter.py adversarial --image face.jpg --model arcface

# Assess face recognition system
python pixelhunter.py assess --target http://api.example.com

# Detect deepfakes
python pixelhunter.py deepfake --input suspicious.jpg
```

## 🏗️ Architecture

```
PixelHunter/
├── core/
│   ├── detector.py        # Face detection
│   ├── recognizer.py      # Face recognition
│   ├── antispoof.py       # Anti-spoofing testing
│   └── adversarial.py     # Adversarial attacks
├── attacks/
│   ├── photo_attack.py    # Photo-based attacks
│   ├── video_attack.py    # Video-based attacks
│   ├── mask_attack.py     # 3D mask attacks
│   └── deepfake.py        # Deepfake generation
├── models/
│   ├── arcface.py         # ArcFace wrapper
│   ├── facenet.py         # FaceNet wrapper
│   └── insightface.py     # InsightFace wrapper
├── utils/
│   ├── preprocessing.py   # Image preprocessing
│   ├── visualization.py   # Result visualization
│   └── metrics.py         # Security metrics
└── benchmarks/
    ├── lfw.py             # LFW benchmark
    ├── cfp.py             # CFP benchmark
    └── agedb.py           # AgeDB benchmark
```

## 🎭 Attack Vectors

### 1. Presentation Attacks
- **Print Attack** — Photo displayed on screen
- **Replay Attack** — Video replay on device
- **3D Mask Attack** — Silicone/paper mask
- **Makeup Attack** — Cosmetic transformation

### 2. Digital Attacks
- **Adversarial Examples** — Perturbation-based bypass
- **Deepfake** — AI-generated face swap
- **Face Morphing** — Identity merging
- **Feature Collision** — Gradient-based attack

### 3. Model Attacks
- **Model Extraction** — Steal model parameters
- **Model Inversion** — Reconstruct training data
- **Membership Inference** — Determine training membership

## 📊 Supported Models

| Model | Testing | Attack | Status |
|-------|---------|--------|--------|
| ArcFace | ✅ | ✅ | Active |
| FaceNet | ✅ | ✅ | Active |
| InsightFace | ✅ | 🟡 | Active |
| DeepFace | ✅ | 🟡 | Active |
| VGGFace2 | ✅ | 🔴 | Planned |
| OpenFace | ✅ | 🔴 | Planned |

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [Usage Manual](docs/usage.md)
- [API Reference](docs/api.md)
- [Attack Techniques](docs/attacks.md)

## ⚠️ Disclaimer

For authorized security testing and research only. Unauthorized access to biometric systems is illegal.

## 📄 License

MIT License
