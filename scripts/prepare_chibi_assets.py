from pathlib import Path
from PIL import Image
from rembg import remove

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "chibi" / "master-sheet.png"
OUT = ROOT / "assets" / "chibi" / "expressions"

# Crop regions are based on the current 1214x1295 character-sheet draft.
# Coordinates are scaled automatically if the source image is resized.
REFERENCE_SIZE = (1214, 1295)
CROPS = {
    "normal": (438, 185, 665, 420),
    "senang": (675, 185, 910, 420),
    "analisis": (915, 185, 1140, 420),
    "marah": (445, 480, 670, 700),
    "kaget": (680, 480, 910, 700),
    "kecewa": (915, 480, 1140, 700),
}

def main():
    if not SOURCE.exists():
        raise SystemExit(
            "Master sheet belum ditemukan. Upload character sheet sebagai "
            "assets/chibi/master-sheet.png lalu jalankan workflow lagi."
        )

    OUT.mkdir(parents=True, exist_ok=True)
    with Image.open(SOURCE) as src:
        src = src.convert("RGB")
        sx = src.width / REFERENCE_SIZE[0]
        sy = src.height / REFERENCE_SIZE[1]

        for name, (x1, y1, x2, y2) in CROPS.items():
            box = (round(x1*sx), round(y1*sy), round(x2*sx), round(y2*sy))
            crop = src.crop(box)
            # Remove the white card/background so each expression can be
            # composited over the channel's dark navy layout.
            result = remove(crop)
            if result.mode != "RGBA":
                result = result.convert("RGBA")
            result.save(OUT / f"chibi-{name}.png", optimize=True)
            print(f"Created {OUT / f'chibi-{name}.png'}")

if __name__ == "__main__":
    main()
