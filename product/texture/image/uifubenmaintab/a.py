from pathlib import Path
from PIL import Image

folder = Path(
    r"F:\FullSetC\Game\Active\PGR\PGR_Assets\assets\product\texture\image\uifubenmaintab"
)

resize_map = {
    (128, 64): (338, 228),
    (256, 128): (350, 130),
    (512, 512): (735, 398),
    (256, 256): (400, 256),
}

for file in folder.glob("*.webp"):
    try:
        with Image.open(file) as image:
            original_size = image.size

            if original_size not in resize_map:
                continue

            new_size = resize_map[original_size]

            resized = image.resize(new_size, Image.Resampling.LANCZOS)
            resized.save(file, format="WEBP")

            print(f"{file.name}: {original_size} -> {new_size}")

    except Exception as e:
        print(f"failed to process {file.name}: {e}")