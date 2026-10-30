from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

out_dir = Path(r"C:\Users\Asus\.gemini\antigravity\scratch\AI-Assistant-for-data-Analyst\screenshots")
out_dir.mkdir(parents=True, exist_ok=True)

try:
    font_bold = ImageFont.truetype("arialbd.ttf", 22)
    font_reg = ImageFont.truetype("arial.ttf", 18)
    font_sm = ImageFont.truetype("arial.ttf", 15)
except Exception:
    font_bold = ImageFont.load_default()
    font_reg = ImageFont.load_default()
    font_sm = ImageFont.load_default()

# ----------------- Diagram 1: Level 0 DFD -----------------
img1 = Image.new("RGB", (1200, 260), "#ffffff")
d1 = ImageDraw.Draw(img1)

def draw_box(draw, xy, text_lines, bg="#e0f2fe", border="#0284c7"):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=bg, outline=border, width=2)
    total_h = len(text_lines) * 22
    start_y = y0 + (y1 - y0 - total_h) / 2
    for i, line in enumerate(text_lines):
        bbox = draw.textbbox((0, 0), line, font=font_reg)
        w = bbox[2] - bbox[0]
        draw.text((x0 + (x1 - x0 - w) / 2, start_y + i * 24), line, fill="#0f172a", font=font_reg)

def draw_arrow(draw, start, end, label=""):
    x0, y0 = start
    x1, y1 = end
    draw.line([(x0, y0), (x1, y1)], fill="#64748b", width=2)
    draw.polygon([(x1, y1), (x1 - 8, y1 - 5), (x1 - 8, y1 + 5)], fill="#64748b")
    if label:
        bbox = draw.textbbox((0, 0), label, font=font_sm)
        w = bbox[2] - bbox[0]
        draw.text(((x0 + x1 - w) / 2, y0 - 22), label, fill="#475569", font=font_sm)

# Level 0 boxes
draw_box(d1, (40, 70, 230, 170), ["User", "(CSV/Excel/JSON + Qs)"], bg="#dbeafe", border="#2563eb")
draw_box(d1, (360, 50, 680, 190), ["AI Data Analyst Assistant", "Streamlit UI + Code Runner"], bg="#f1f5f9", border="#0284c7")
draw_box(d1, (800, 30, 1030, 110), ["Groq Cloud", "(Llama-3.3-70b-versatile)"], bg="#fef3c7", border="#d97706")
draw_box(d1, (800, 130, 1030, 210), ["Analytics & Plots", "(Pandas, Seaborn, Matplotlib)"], bg="#ecfdf5", border="#059669")
draw_box(d1, (1070, 70, 1180, 170), ["Insights +", "Seaborn Visuals +", "Clean Data"], bg="#dcfce7", border="#16a34a")

# Arrows
draw_arrow(d1, (230, 120), (360, 120), "Upload / Query")
draw_arrow(d1, (680, 80), (800, 80), "Prompt LLM")
draw_arrow(d1, (680, 160), (800, 160), "Exec Code")
draw_arrow(d1, (1030, 80), (1070, 105), "")
draw_arrow(d1, (1030, 160), (1070, 135), "")

img1.save(out_dir / "diagram_level0.png")

# ----------------- Diagram 2: System Block Diagram -----------------
img2 = Image.new("RGB", (1200, 480), "#ffffff")
d2 = ImageDraw.Draw(img2)

d2.text((40, 20), "Data Ingestion & Cleaning Pipeline", fill="#0369a1", font=font_bold)
p1_boxes = [
    ("1. Upload", "CSV/XLSX/JSON"),
    ("2. Parser", "Pandas Readers"),
    ("3. Overview", "Rows, Cols, Nulls"),
    ("4. De-duplicate", "Drop Duplicates"),
    ("5. Impute", "Fill Missing (0)")
]
w_box = 190
h_box = 80
y_p1 = 60

for i, (t1, t2) in enumerate(p1_boxes):
    x_box = 40 + i * 230
    draw_box(d2, (x_box, y_p1, x_box + w_box, y_p1 + h_box), [t1, t2], bg="#e0f2fe", border="#0284c7")
    if i < len(p1_boxes) - 1:
        draw_arrow(d2, (x_box + w_box, y_p1 + h_box/2), (x_box + 230, y_p1 + h_box/2))

d2.text((40, 180), "Natural Language Querying & Visual Analytics Pipeline", fill="#0369a1", font=font_bold)
p2_boxes = [
    ("1. User Query", "Natural Language"),
    ("2. Groq LLM", "Llama-3.3-70b"),
    ("3. Code Generator", "Python/Pandas/Seaborn"),
    ("4. Code Exec", "Sandboxed Local Run"),
    ("5. Visualization", "Matplotlib / Seaborn")
]
y_p2 = 220
for i, (t1, t2) in enumerate(p2_boxes):
    x_box = 40 + i * 230
    draw_box(d2, (x_box, y_p2, x_box + w_box, y_p2 + h_box), [t1, t2], bg="#fef3c7" if i==1 else "#f1f5f9", border="#d97706" if i==1 else "#475569")
    if i < len(p2_boxes) - 1:
        draw_arrow(d2, (x_box + w_box, y_p2 + h_box/2), (x_box + 230, y_p2 + h_box/2))

# Result Box at bottom
draw_box(d2, (270, 360, 930, 440), ["6. Streamlit User Interface: Metric Overview Cards + Interactive Chat + Real-Time Plots"], bg="#dcfce7", border="#16a34a")
draw_arrow(d2, (960, 300), (800, 360), "Render Plot")
draw_arrow(d2, (270, 300), (400, 360), "Display Summary")

img2.save(out_dir / "diagram_block.png")
print("AI-Assistant-for-data-Analyst diagrams generated!")

