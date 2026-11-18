<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:f59e0b&height=170&section=header&text=WebP%20Workbench&fontColor=ffffff&fontSize=38&animation=fadeIn" width="100%" alt="WebP Workbench banner"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2800&pause=900&color=f59e0b&center=true&vCenter=true&width=650&lines=WebP%20Workbench%3BBatch%20image%20conversion%20with%20predictable%20local%20output.%3BLocal-first%20tools%20for%20focused%20work." alt="Typing introduction"/>
<p>Batch image conversion with predictable local output.</p>
<p><img src="https://img.shields.io/github/license/CyberLoop-dev/webp-workbench?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/webp-workbench?style=for-the-badge" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/webp-workbench?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/webp-workbench?style=for-the-badge" alt="Last commit"/></p>
<img src="assets/icon.svg" width="112" alt="WebP Workbench icon"/>
</div>

## ✨ Overview
WebP Workbench converts image files on your computer into WebP, PNG, or JPEG. It applies EXIF orientation, can resize by maximum width, and writes converted files into a separate output directory.

## 🚀 Features
- ✨ Convert a single image or a directory of images
- ✨ Choose WebP, PNG, or JPEG output
- ✨ Set quality for lossy formats and a maximum width
- ✨ Correct EXIF orientation before saving
- ✨ Keep original files untouched

## 🎬 Demo
Try `python main.py photos/ --output-dir converted --format webp --quality 82 --recursive`.

## ⚡ Quick Start
```bash
python -m pip install -r requirements.txt
python main.py photos/ --output-dir converted --format webp --quality 82 --recursive
```

## 🧰 Tech Stack
Python 3.10+ and Pillow for image decoding, orientation, resizing, and encoding.

## 🗂️ Folder Structure
```text
.
├── main.py
├── requirements.txt
└── tests/test_main.py
├── assets/icon.svg
├── .gitignore
└── LICENSE
```

## 🧭 Roadmap
- [ ] Add maximum-height resizing
- [ ] Add a contact-sheet summary
- [ ] Add per-file conversion timing

## 🤝 Contributing
Issues and focused pull requests are welcome. Explain the problem, keep changes small, and update tests when behavior changes.

## 📄 License
Released under the [MIT License](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:f59e0b&height=100&section=footer" width="100%" alt="Animated wave footer"/></div>
