# 🖼️ Image Encryption Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Pillow](https://img.shields.io/badge/Pillow-12.x-green?style=flat-square)
![Track](https://img.shields.io/badge/Track-Cyber%20Security-red?style=flat-square)
![Task](https://img.shields.io/badge/Task-02-orange?style=flat-square)
![Internship](https://img.shields.io/badge/SkillCraft-Technology-blueviolet?style=flat-square)

> **SkillCraft Technology — Cybersecurity Internship | Task 02**  
> A command-line tool to encrypt and decrypt images using pixel manipulation techniques.

---

## 📌 How It Works

Every image is a grid of pixels. Each pixel stores three values — **Red, Green, Blue** — each a number from 0 to 255.

This tool scrambles those numbers using three different operations:

| Operation | How It Works | Decrypt Method |
|---|---|---|
| **XOR** | `pixel XOR key` | XOR again with same key (self-inverse) |
| **ADD** | `(pixel + key) mod 256` | Subtract key `(pixel - key) mod 256` |
| **Channel Swap** | Swap R and B values | Apply again (self-inverse) |

---

## ✨ Features

- **XOR Encryption/Decryption** — closest to real-world pixel cryptography
- **ADD Encryption/Decryption** — shift all pixel values by a key
- **Channel Swap** — swap Red and Blue channels, visually obvious colour shift
- Works on any `.png` or `.jpg` image
- Saves encrypted/decrypted output as a new file (original untouched)
- Supports images with or without alpha channel

---

## 🚀 How to Run

**Install dependency:**
```bash
pip install pillow
```

**Run:**
```bash
python image_encryption.py
```

### Sample Output

```
==================================================
     Image Encryption Tool — SkillCraft
==================================================

Options:
  [1] Encrypt image (XOR)
  [2] Decrypt image (XOR)
  [3] Encrypt image (ADD)
  [4] Decrypt image (ADD)
  [5] Encrypt/Decrypt image (Channel Swap)
  [6] Exit

Select option: 1
Enter image path: ./photo.png
Enter key value (0-255): 42
[+] Encrypted image saved: ./photo_xor_encrypted.png
```

---

## 🧠 Real-World Context

| Concept | Real-World Application |
|---|---|
| XOR pixel manipulation | Foundation of AES block cipher internals |
| Channel manipulation | Digital watermarking, steganography |
| Pixel-level data hiding | Threat actors hide malware in image files |
| Medical image encryption | DICOM file security in radiology systems |

> **Steganography** — hiding secret data inside images by tweaking pixel values — is an active threat vector used by real malware. Recognising pixel-level anomalies is a core **DFIR** skill.

---

## 📁 File Structure

```
SCT_CS_2/
└── image_encryption.py
└── README.md
```

---

## 👤 Author

**Manoj**  
Cybersecurity Intern — SkillCraft Technology  
GitHub: [@pro-coder12353](https://github.com/pro-coder12353)
