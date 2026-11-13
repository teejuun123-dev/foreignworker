"""Build a static economics job-market website using Python and Jinja2.

Run:
    pip install -r requirements.txt
    python build.py

Publish the generated docs/ folder with GitHub Pages.
"""

from datetime import date
from pathlib import Path
from shutil import copy2, copytree, rmtree

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "docs"

# -------------------------------------------------------------------------
# EDIT YOUR DETAILS HERE
# -------------------------------------------------------------------------
PROFILE = {
    "name": "Your Name",
    "role": "PhD Candidate in Economics",
    "university": "Your University",
    "department": "Department of Economics",
    "email": "your.email@university.edu",
    "interests": ["Macroeconomics", "Monetary Economics", "Financial Economics"],
    "bio": (
        "I am a PhD candidate in Economics at Your University. "
        "My research studies how monetary policy and financial markets "
        "affect economic outcomes. I am on the 2026–2027 academic job market."
    ),
    "location": "Your City, Country",
    "github": "",   # e.g. https://github.com/yourusername
    "linkedin": "", # e.g. https://www.linkedin.com/in/yourusername/
    "scholar": "",  # e.g. your Google Scholar profile URL
}

PAPERS = [
    {
        "title": "Your Job Market Paper Title",
        "authors": "Your Name",
        "year": "2026",
        "category": "Job Market Paper",
        "abstract": (
            "What economic question are you studying? Summarise your identification "
            "strategy or model, your main finding, and its policy significance "
            "in approximately 100–150 words."
        ),
        "pdf": "files/job-market-paper.pdf",
        "slides": "files/job-market-slides.pdf",
        "featured": True,
    },
    {
        "title": "Your Second Working Paper",
        "authors": "Your Name and Coauthor Name",
        "year": "2026",
        "category": "Working Paper",
        "abstract": "Add a concise description of the paper and its contribution.",
        "pdf": "files/working-paper-2.pdf",
        "slides": "",
        "featured": False,
    },
    {
        "title": "Your Research-in-Progress Project",
        "authors": "Your Name",
        "year": "2026",
        "category": "Work in Progress",
        "abstract": "Describe the research question and current stage of the project.",
        "pdf": "",
        "slides": "",
        "featured": False,
    },
]

TEACHING = [
    {"course": "Intermediate Macroeconomics", "role": "Teaching Assistant", "institution": "Your University", "term": "2025–2026"},
    {"course": "Introduction to Econometrics", "role": "Teaching Assistant", "institution": "Your University", "term": "2024–2025"},
]

# -------------------------------------------------------------------------
# SITE BUILD: you usually do not need to edit anything below this line.
# -------------------------------------------------------------------------
PAGES = {
    "index.html": ("index.html", "Home", "home"),
    "jobmarket.html": ("jobmarket.html", "Job Market", "jobmarket"),
    "research.html": ("research.html", "Research", "research"),
    "teaching.html": ("teaching.html", "Teaching", "teaching"),
    "cv.html": ("cv.html", "CV", "cv"),
}


def build() -> None:
    if OUTPUT.exists():
        rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)

    # Copy CSS, optional headshot, and any PDF documents.
    copytree(ROOT / "static", OUTPUT / "assets")
    (OUTPUT / "files").mkdir()
    for pdf in (ROOT / "files").glob("*.pdf"):
        copy2(pdf, OUTPUT / "files" / pdf.name)
    (OUTPUT / ".nojekyll").touch()

    # Hide PDF/slide buttons until the corresponding files exist.
    papers = []
    for paper in PAPERS:
        item = dict(paper)
        for field in ("pdf", "slides"):
            item[f"{field}_available"] = bool(
                item[field] and (OUTPUT / item[field]).is_file()
            )
        papers.append(item)
    featured_paper = next((p for p in papers if p["featured"]), None)
    photo_available = (OUTPUT / "assets" / "profile.jpg").is_file()
    cv_available = (OUTPUT / "files" / "cv.pdf").is_file()

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    for filename, (template, title, active_page) in PAGES.items():
        html = env.get_template(template).render(
            profile=PROFILE,
            papers=papers,
            featured_paper=featured_paper,
            teaching=TEACHING,
            photo_available=photo_available,
            cv_available=cv_available,
            page_title=title,
            active_page=active_page,
            current_year=date.today().year,
        )
        (OUTPUT / filename).write_text(html, encoding="utf-8")
        print(f"Generated docs/{filename}")

    print("\nDone! Preview with: python -m http.server 8000 -d docs")
    print("Open: http://localhost:8000")


if __name__ == "__main__":
    build()
