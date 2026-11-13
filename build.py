"""Generate Taejun Kim's academic website using Python and Jinja2.

In Spyder: open this file and press F5.
On the command line: python build.py
Publish the generated docs/ directory with GitHub Pages.

Update the dictionaries below whenever your details change. The builder
only displays paper downloads when the files exist in files/.
"""

from datetime import date
from pathlib import Path
from shutil import copy2, copytree, rmtree

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "docs"

# -----------------------------------------------------------------------------
# ACADEMIC PROFILE (adapted from the November 2026 CV)
# -----------------------------------------------------------------------------
PROFILE = {
    "name": "Taejun Kim",
    "role": "PhD Student in Economics",
    "university": "University of Nottingham",
    "department": "School of Economics",
    "email": "lextk13@nottingham.ac.uk",
    "location": "Nottingham, United Kingdom",
    "interests": [
        "Time-Series Econometrics",
        "Explosive Processes and Co-Explosivity",
        "Structural Breaks and Bubble Dating",
    ],
    "bio": (
        "I am a PhD student in Economics at the University of Nottingham. "
        "My research focuses on univariate time-series econometric theory, "
        "with applications to explosive processes, financial bubbles, "
        "and the estimation of structural change points."
    ),
    "github": "https://github.com/teejuun123-dev",
    "linkedin": "",  # Add a real LinkedIn URL only if you have one.
    "scholar": "",   # Add a real Google Scholar URL only if you have one.
}

# The CV supplies these titles and author lists but no abstracts or public PDF URLs.
# To activate a PDF button, place the file at the exact relative path shown.
PAPERS = [
    {
        "title": "Recursive Subsample Testing for Co-Explosivity Breakdowns",
        "authors": "Taejun Kim",
        "year": "2026",
        "category": "Job Market Paper",
        "abstract": "",  # Paste your approved abstract here, if desired.
        "pdf": "files/job-market-paper.pdf",
        "slides": "files/job-market-slides.pdf",
        "featured": True,
    },
    {
        "title": (
            "Robust Estimation of Bubble Regime Change Points in the "
            "Presence of Level Shifts and Time-Varying Volatility"
        ),
        "authors": "David Harvey, Stephen Leybourne, and Taejun Kim",
        "year": "2026",
        "category": "Working Paper",
        "abstract": "",
        "pdf": "files/robust-estimation-paper.pdf",
        "slides": "",
        "featured": False,
    },
    {
        "title": "Uncertainty and Cooperation: Evidence from Colonial India",
        "authors": "Mattia Bertazzini, Maanik Nath, and Taejun Kim",
        "year": "",  # Year not specified in the CV.
        "category": "Work in Progress",
        "abstract": "",
        "pdf": "",
        "slides": "",
        "featured": False,
    },
]

# Term strings are retained exactly as in your CV (S = spring; F = autumn).
TEACHING = [
    {"code": "ECON2006", "course": "Applied Econometrics 2", "role": "Tutorial", "institution": "University of Nottingham", "term": "2027-S"},
    {"code": "ECON1069", "course": "Mathematical Economics", "role": "Tutorial", "institution": "University of Nottingham", "term": "2026-F"},
    {"code": "ECON1044", "course": "Mathematical Economics and Econometrics", "role": "Tutorial", "institution": "University of Nottingham", "term": "2026-S"},
    {"code": "ECON2005", "course": "Applied Econometrics 1", "role": "Tutorial", "institution": "University of Nottingham", "term": "2025-F"},
    {"code": "ECON2006", "course": "Applied Econometrics 2", "role": "Tutorial", "institution": "University of Nottingham", "term": "2025-S"},
    {"code": "ECON2050", "course": "Econometric Theory 2", "role": "Tutorial", "institution": "University of Nottingham", "term": "2025-S"},
    {"code": "ECON2005", "course": "Applied Econometrics 1", "role": "Computer Lab", "institution": "University of Nottingham", "term": "2024-F"},
    {"code": "ECON2006", "course": "Applied Econometrics 2", "role": "Computer Lab", "institution": "University of Nottingham", "term": "2024-S"},
    {"code": "ECON2005", "course": "Applied Econometrics 1", "role": "Tutorial", "institution": "University of Nottingham", "term": "2023-F"},
]

EDUCATION = [
    {"degree": "PhD in Economics", "university": "University of Nottingham", "period": "2023–present", "detail": "Univariate time-series econometric theory"},
    {"degree": "MRes in Economics", "university": "University of Nottingham", "period": "2022–2023", "detail": "Distinction"},
    {"degree": "MSc in Economics and Econometrics", "university": "University of Nottingham", "period": "2021–2022", "detail": "Distinction"},
    {"degree": "BSc in Finance and Economics", "university": "University of Bradford", "period": "2018–2020", "detail": "First Class"},
    {"degree": "BA in Global Dual Degree (Liberal Arts)", "university": "Busan University of Foreign Studies", "period": "2014–2020", "detail": "GPA: 4.05/4.5"},
]

EXPERIENCE = [
    {"title": "Graduate Teaching Assistant", "organisation": "University of Nottingham", "period": "2023–present"},
    {"title": "Research Assistant", "organisation": "University of Nottingham", "period": "2024–2026"},
    {"title": "Sergeant", "organisation": "Republic of Korea Army", "period": "2015–2017"},
]

AWARDS = [
    {"name": "School of Economics Scholarship", "provider": "University of Nottingham · Tuition fee waiver and annual stipend", "period": "2022–2027"},
    {"name": "Teaching Excellence Award", "provider": "School of Economics, University of Nottingham", "period": "2025–2026"},
    {"name": "Teaching Excellence Award", "provider": "School of Economics, University of Nottingham", "period": "2024–2025"},
    {"name": "Second Best Presenter, Annual PhD Conference", "provider": "School of Economics, University of Nottingham", "period": "2025"},
    {"name": "Regional Excellence Award – East Asia", "provider": "University of Nottingham · £4,000", "period": "2021"},
    {"name": "Exchange Student Awards", "provider": "Busan University of Foreign Studies · $15,016", "period": "2018–2019"},
    {"name": "Exchange Student Awards", "provider": "University of Bradford · £10,000", "period": "2018–2019"},
]

PRESENTATIONS = [
    {"event": "Nottingham PhD Conference", "date": "May 2026", "title": "Recursive Testing for Co-Explosivity Breakdowns"},
    {"event": "Nottingham PhD Conference", "date": "May 2025", "title": "Robust Estimation of Bubble Regime Change Points in the Presence of Level Shifts"},
    {"event": "Nottingham PhD Conference", "date": "May 2024", "title": "Crash Regime Change Point Dating Under Time-Varying Volatility"},
    {"event": "MRes Dissertation Conference", "date": "October 2023", "title": "Dating Start and End Periods of Historical Crashes and Applications to Real-Time Bubble and Crash Detection"},
]

REFERENCES = [
    {"name": "Prof. Steve Leybourne", "title": "Professor of Econometrics", "organisation": "University of Nottingham", "email": "steve.leybourne@nottingham.ac.uk"},
    {"name": "Prof. David Harvey", "title": "Professor of Econometrics", "organisation": "University of Nottingham", "email": "dave.harvey@nottingham.ac.uk"},
    {"name": "Dr. Mattia Bertazzini", "title": "Assistant Professor of Economics", "organisation": "University of Nottingham", "email": "Mattia.Bertazzini@nottingham.ac.uk"},
]

SKILLS = ["GAUSS", "MATLAB", "Python", "Stata"]

# -----------------------------------------------------------------------------
# SITE GENERATION: no changes necessary below this section.
# -----------------------------------------------------------------------------
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

    copytree(ROOT / "static", OUTPUT / "assets")
    (OUTPUT / "files").mkdir()
    for pdf in (ROOT / "files").glob("*.pdf"):
        copy2(pdf, OUTPUT / "files" / pdf.name)
    (OUTPUT / ".nojekyll").touch()

    papers = []
    for paper in PAPERS:
        entry = dict(paper)
        for field in ("pdf", "slides"):
            entry[f"{field}_available"] = bool(
                entry[field] and (OUTPUT / entry[field]).is_file()
            )
        papers.append(entry)

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
            education=EDUCATION,
            experience=EXPERIENCE,
            awards=AWARDS,
            presentations=PRESENTATIONS,
            references=REFERENCES,
            skills=SKILLS,
            photo_available=photo_available,
            cv_available=cv_available,
            page_title=title,
            active_page=active_page,
            current_year=date.today().year,
        )
        (OUTPUT / filename).write_text(html, encoding="utf-8")
        print(f"Generated docs/{filename}")

    print("\nWebsite generated successfully.")
    print(f"Open this file in your browser: {OUTPUT / 'index.html'}")
    print("Optional local server: python -m http.server 8000 -d docs")


if __name__ == "__main__":
    build()
