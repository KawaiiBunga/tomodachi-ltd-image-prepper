# tomodachi-ltd-image-prepper

A basic command line tool that:

- Converts the image to .PNG format
- Removes the images background
- Resizes the result to fit within `512x512`
- Centers it on a transparent `512x512` canvas
- Saves a `*_processed.png` next to the script

The image can then be used with [LTD Toolkit](https://github.com/MadMax1960/LivingTheDreamToolkit)

For BEST results:
- Make sure there is only one main subject in the image. No logos or watermarks.
- Use clean, high contrast images for input
- Using higher resolution images will net better results than lower resolution images
- Avoid busy backgrounds/tricky details (hair, fur, foliage, crowds, chains/fences, etc)

This should work with the following image formats:
- PNG
- JPEG/JPG
- WEBP
- BMP
- TIFF/TIF
- Gif (Typically uses the first frame, animated gifs aren't saved with animation in the final output)

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



