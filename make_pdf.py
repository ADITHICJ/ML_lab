from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, PageBreak,
    Image, Preformatted
)
from reportlab.lib.styles import getSampleStyleSheet
import os

pdf = SimpleDocTemplate("ML_LAB_Programs.pdf")
styles = getSampleStyleSheet()

content = []

for folder, _, files in os.walk("."):

    for file in sorted(files):

        if file.endswith(".py") and file != "make_pdf.py":

            path = os.path.join(folder, file)

            content.append(
                Paragraph(f"<b>{path}</b>", styles["Heading2"])
            )

            with open(path, "r", encoding="utf-8") as f:
                code = f.read()

            # Preserve indentation and line breaks
            content.append(
                Preformatted(code, styles["Code"])
            )

            # Add images from same folder
            for img in sorted(files):
                if img.endswith(".png"):
                    img_path = os.path.join(folder, img)
                    content.append(Image(img_path, width=350, height=250))

            content.append(PageBreak())

pdf.build(content)

print("PDF created successfully!")