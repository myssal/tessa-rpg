from pathlib import Path
from PIL import Image

folder = Path(
    r"F:\FullSetC\Game\Active\PGR\PGR_Assets\assets\product\texture\image\uifubenmaintab"
)

dimension_map = {}

for file in folder.glob("*.webp"):
    try:
        with Image.open(file) as image:
            dimension = f"{image.width}x{image.height}"

        dimension_map.setdefault(dimension, []).append(file.name)

    except Exception as e:
        print(f"failed to read {file.name}: {e}")

output_file = folder / "dim.txt"

with output_file.open("w", encoding="utf-8") as f:
    f.write("Dimension:\n\n")

    for dimension in sorted(dimension_map):
        f.write(f"- {dimension}\n")

    f.write("\nData:\n\n")

    for dimension in sorted(dimension_map):
        f.write(f"- {dimension}:\n")

        for filename in sorted(dimension_map[dimension]):
            f.write(f"  - {filename}\n")

        f.write("\n")

print(f"saved: {output_file}")