import sys
import os
from pathlib import Path

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OMP_WAIT_POLICY"] = "PASSIVE"
os.environ["ORT_DISABLE_GPU"] = "1"

from PIL import Image
from rembg import remove, new_session
from io import BytesIO

OUTPUT_SIZE = (512, 512)

if len(sys.argv) < 2:
    print("[-] No file provided.")
    input("Press Enter to exit...")
    sys.exit(1)

input_path = Path(sys.argv[1])

if not input_path.is_file():
    print("[-] Invalid file path.")
    input("Press Enter to exit...")
    sys.exit(1)

print(f"[+] Processing: {input_path}")

with input_path.open("rb") as f:
    input_data = f.read()

print("[+] Removing background (CPU)...")
session = new_session(providers=["CPUExecutionProvider"])
output_data = remove(input_data, session=session)

with Image.open(BytesIO(output_data)) as img:
    image = img.convert("RGBA")

print("[+] Resizing to 512x512...")

image.thumbnail(OUTPUT_SIZE, Image.LANCZOS)

final_img = Image.new("RGBA", OUTPUT_SIZE, (0, 0, 0, 0))

x = (OUTPUT_SIZE[0] - image.width) // 2
y = (OUTPUT_SIZE[1] - image.height) // 2

final_img.paste(image, (x, y), image)

output_path = Path(__file__).resolve().parent / f"{input_path.stem}_processed.png"

print(f"[+] Saving: {output_path}")
final_img.save(output_path, "PNG")

print("[✓] Done!")

input("Press Enter to exit...")