from pathlib import Path
import copy
import xml.etree.ElementTree as ET

import cairosvg

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "chibi" / "master-sheet.svg"
OUT = ROOT / "assets" / "chibi" / "expressions"

NS = {"svg": "http://www.w3.org/2000/svg"}
ET.register_namespace("", NS["svg"])

# Crop windows are centered on the six character poses in master-sheet.svg.
# Each export has a transparent background and excludes the caption below it.
POSES = {
    "normal": (265, 315),
    "senang": (800, 315),
    "analisis": (1335, 315),
    "marah": (265, 675),
    "kaget": (800, 675),
    "kecewa": (1335, 675),
}
CROP_W = 320
CROP_H = 490
TOP_OFFSET = 175

def local_name(tag):
    return tag.rsplit("}", 1)[-1]

def main():
    if not SOURCE.exists():
        raise SystemExit(f"Master SVG tidak ditemukan: {SOURCE}")

    tree = ET.parse(SOURCE)
    root = tree.getroot()
    defs = root.find("svg:defs", NS)
    if defs is None:
        raise SystemExit("Elemen <defs> tidak ditemukan di master SVG.")

    groups = {
        child.attrib.get("transform", ""): child
        for child in list(root)
        if local_name(child.tag) == "g"
    }

    OUT.mkdir(parents=True, exist_ok=True)
    for name, (cx, cy) in POSES.items():
        transform = f"translate({cx} {cy})"
        if transform not in groups:
            raise SystemExit(f"Pose {name} tidak ditemukan: {transform}")

        pose = copy.deepcopy(groups[transform])
        # Captions belong to the master reference sheet, not the character asset.
        for node in list(pose.iter()):
            if local_name(node.tag) == "text":
                parent = next((p for p in pose.iter() if node in list(p)), None)
                if parent is not None:
                    parent.remove(node)

        x0 = cx - CROP_W // 2
        y0 = cy - TOP_OFFSET
        svg = ET.Element(
            f"{{{NS['svg']}}}svg",
            {
                "width": str(CROP_W * 2),
                "height": str(CROP_H * 2),
                "viewBox": f"{x0} {y0} {CROP_W} {CROP_H}",
                "version": "1.1",
            },
        )
        svg.append(copy.deepcopy(defs))
        svg.append(pose)

        svg_path = OUT / f"chibi-{name}.svg"
        png_path = OUT / f"chibi-{name}.png"
        svg_bytes = ET.tostring(svg, encoding="utf-8", xml_declaration=True)
        svg_path.write_bytes(svg_bytes)
        cairosvg.svg2png(bytestring=svg_bytes, write_to=str(png_path), scale=2)
        print(f"Created {svg_path}")
        print(f"Created {png_path}")

if __name__ == "__main__":
    main()
