#!/usr/bin/env python3
"""
Image Encryption Tool
SkillCraft Technology — Cybersecurity Internship
Task 02: Encrypt and decrypt images using pixel manipulation.

Operations supported:
  - XOR  : XOR each pixel with a key value (most common in real crypto)
  - ADD  : Add key to each pixel (with wraparound)
  - SWAP : Swap R and B channels of each pixel

Author: Manoj
"""

from PIL import Image
import os


def xor_encrypt(image: Image.Image, key: int) -> Image.Image:
    """XOR every pixel channel with the key. Same operation encrypts and decrypts."""
    pixels = image.load()
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)
    return image


def add_encrypt(image: Image.Image, key: int) -> Image.Image:
    """Add key to every pixel channel (mod 256) to encrypt."""
    pixels = image.load()
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)
    return image


def add_decrypt(image: Image.Image, key: int) -> Image.Image:
    """Subtract key from every pixel channel (mod 256) to decrypt."""
    pixels = image.load()
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)
    return image


def swap_channels(image: Image.Image) -> Image.Image:
    """Swap R and B channels. Same operation encrypts and decrypts."""
    pixels = image.load()
    width, height = image.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y][:3]
            pixels[x, y] = (b, g, r)
    return image


def get_key() -> int:
    """Get and validate key value from user."""
    while True:
        try:
            key = int(input("Enter key value (0-255): "))
            if 0 <= key <= 255:
                return key
            print("[!] Key must be between 0 and 255.")
        except ValueError:
            print("[!] Invalid input. Enter a number.")


def load_image(path: str) -> Image.Image:
    """Load image and convert to RGB."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    img = Image.open(path).convert("RGB")
    return img


def save_image(image: Image.Image, original_path: str, suffix: str) -> str:
    """Save processed image with a suffix added to filename."""
    base, ext = os.path.splitext(original_path)
    output_path = f"{base}_{suffix}{ext}"
    image.save(output_path)
    return output_path


def main():
    print("=" * 50)
    print("     Image Encryption Tool — SkillCraft")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  [1] Encrypt image (XOR)")
        print("  [2] Decrypt image (XOR)")
        print("  [3] Encrypt image (ADD)")
        print("  [4] Decrypt image (ADD)")
        print("  [5] Encrypt/Decrypt image (Channel Swap)")
        print("  [6] Exit")

        choice = input("\nSelect option: ").strip()

        if choice == '6':
            print("\n[*] Exiting. Goodbye.")
            break

        if choice not in ('1', '2', '3', '4', '5'):
            print("[!] Invalid option. Choose 1–6.")
            continue

        path = input("Enter image path (e.g. C:\\image.png): ").strip().strip('"')

        try:
            img = load_image(path)
        except FileNotFoundError as e:
            print(f"[!] {e}")
            continue

        if choice == '1':
            key = get_key()
            result = xor_encrypt(img, key)
            out = save_image(result, path, "xor_encrypted")
            print(f"\n[+] Encrypted image saved: {out}")

        elif choice == '2':
            key = get_key()
            result = xor_encrypt(img, key)  # XOR is its own inverse
            out = save_image(result, path, "xor_decrypted")
            print(f"\n[+] Decrypted image saved: {out}")

        elif choice == '3':
            key = get_key()
            result = add_encrypt(img, key)
            out = save_image(result, path, "add_encrypted")
            print(f"\n[+] Encrypted image saved: {out}")

        elif choice == '4':
            key = get_key()
            result = add_decrypt(img, key)
            out = save_image(result, path, "add_decrypted")
            print(f"\n[+] Decrypted image saved: {out}")

        elif choice == '5':
            result = swap_channels(img)
            out = save_image(result, path, "swap")
            print(f"\n[+] Channel-swapped image saved: {out}")


if __name__ == "__main__":
    main()
