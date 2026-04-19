# tomodachi-ltd-image-prepper
# tomodachi-image-prepper

A basic command line tool that:

- Removes the images background
- Resizes the result to fit within `512x512`
- Centers it on a transparent `512x512` canvas
- Saves a `*_processed.png` next to the script

## Requirements

- Python 3.12+ (Recommended)
- Dependencies in `requirements.txt`:
  - `Pillow`
  - `rembg`
  - `onnxruntime`

Install:

```bash
pip install -r requirements.txt
```

## Usage

### Option 1 (Windows) (Easy): Drag & drop

Drag an image onto `drop_image_here.bat`. Make sure that image is in the same folder as the .bat and .py files or it will not work.

### Option 2: Run the script manually

```bash
python process_image.py "path/to/image.png"
```

Output:

- A new file named `<original_name>_processed.png` will be created in the project folder.



