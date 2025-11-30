# build.py

from jinja2 import Environment, FileSystemLoader
from data import data
import os
import shutil

# Where templates live
TEMPLATES_DIR = "templates"
STATIC_DIR = "static"
OUTPUT_DIR = "."  # root of the project

def build_site():
    # Set up Jinja environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

    # Load the main template
    template = env.get_template("index.html")

    # Render with our data
    html = template.render(**data)

    # Write the generated HTML to index.html in the root
    output_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    # Copy logo.png from static/ to root (where Cloudflare expects it)
    src_logo = os.path.join(STATIC_DIR, "logo.png")
    dst_logo = os.path.join(OUTPUT_DIR, "logo.png")

    if os.path.exists(src_logo):
        shutil.copy2(src_logo, dst_logo)
        print(f"Copied logo from {src_logo} to {dst_logo}")
    else:
        print("WARNING: static/logo.png not found. Put your logo there.")

    print(f"Built {output_path}")

if __name__ == "__main__":
    build_site()

