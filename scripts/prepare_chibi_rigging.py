from pathlib import Path
import xml.etree.ElementTree as ET
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "chibi" / "master-sheet.svg"
OUT = ROOT / "assets" / "chibi" / "rigging"

SVG = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG)
ET.register_namespace("xlink", XLINK)

PARTS = {
    # viewBox leaves a little transparent padding around each pivotable part.
    "head": {"viewBox": "-100 -155 200 220", "x": 0, "y": 0, "width": 400, "height": 440},
    "body": {"viewBox": "-105 -35 210 355", "x": 0, "y": 0, "width": 420, "height": 710},
}

def main():
    if not SOURCE.exists():
        raise SystemExit(f"Master SVG not found: {SOURCE}")

    root = ET.parse(SOURCE).getroot()
    defs = root.find(f"{{{SVG}}}defs")
    if defs is None:
        raise SystemExit("Master SVG has no defs block.")

    OUT.mkdir(parents=True, exist_ok=True)
    for part, spec in PARTS.items():
        svg = ET.Element(f"{{{SVG}}}svg", {
            "version": "1.1",
            "width": str(spec["width"]),
            "height": str(spec["height"]),
            "viewBox": spec["viewBox"],
        })
        svg.append(ET.fromstring(ET.tostring(defs, encoding="unicode")))
        use = ET.SubElement(svg, f"{{{SVG}}}use", {
            "href": f"#{part}",
            f"{{{XLINK}}}href": f"#{part}",
        })
        # SVG <use> inherits the original component geometry; transparent
        # canvas and viewBox preserve a stable local coordinate system.
        svg_bytes = ET.tostring(svg, encoding="utf-8", xml_declaration=True)
        svg_path = OUT / f"{part}-base.svg"
        png_path = OUT / f"{part}-base.png"
        svg_path.write_bytes(svg_bytes)
        cairosvg.svg2png(bytestring=svg_bytes, write_to=str(png_path))
        print(f"Created {svg_path.relative_to(ROOT)}")
        print(f"Created {png_path.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
