# Taejun Kim — Academic Website (Python + Jinja2)

This project is populated using the November 2026 CV. The design is a minimalist academic job-market website, generated entirely from Python and HTML/CSS. GitHub Pages serves the generated HTML pages for free.

## Instructions for Spyder (Windows)

1. Extract this ZIP. Open `build.py` in Spyder (File > Open).
2. In the IPython Console, run `import jinja2`. If it fails, install it into the Python environment used by Spyder, e.g. `%pip install jinja2`, and restart the console.
3. Review the profile, papers, teaching, education, awards, presentations and references in `build.py`.
4. Press **F5** to run the file. It uses `Path(__file__)`, so you don't need to change Spyder's working directory.
5. Open `docs/index.html` in a browser to preview your homepage.
6. To publish the changes to your existing repository, upload **the contents of the new `docs/` folder** to the `docs/` folder of `https://github.com/teejuun123-dev/foreignworker` on its `main` branch. Also upload updated `build.py`, `templates/` and `static/` so the GitHub repository remains editable.
7. In GitHub `Settings > Pages`, choose `Deploy from a branch`, `main`, `/docs`, and Save. Website: `https://teejuun123-dev.github.io/foreignworker/`.

**Important:** If uploading using GitHub's browser interface, drag a folder into the upload area from Windows File Explorer. Keep `docs/index.html` inside the root `docs/` directory, not inside a second project folder. For updates, consider using GitHub Desktop because replacing multiple generated files via the browser can be tedious.

## Editing content

The start of `build.py` contains the editable `PROFILE`, `PAPERS`, `TEACHING`, `EDUCATION`, `EXPERIENCE`, `AWARDS`, `PRESENTATIONS`, `REFERENCES`, and `SKILLS` definitions.

- The headshot is optional: `static/profile.jpg` (not included).
- A privacy-safe version of the supplied CV is included as `files/cv.pdf`, with the home address and telephone number removed. Please review it before publishing. If you prefer a different PDF, replace that file.
- Full paper texts were not provided. To enable paper download links, put your PDFs in `files/` under the exact names specified in `PAPERS`: `job-market-paper.pdf`, `robust-estimation-paper.pdf`, etc., then rerun `build.py`.
- Paper abstracts and links have **not** been fabricated. Enter them yourself in `PAPERS` when available.
- Term notation (`2027-S`, `2026-F`, etc.) follows the supplied CV.

## How the build works

`build.py` uses Jinja2 to render HTML templates from `templates/` into `docs/`, copies CSS/images from `static/` into `docs/assets/`, and copies PDFs from `files/` into `docs/files/`. It creates `.nojekyll` for GitHub Pages. GitHub Pages does not run Python; upload the generated `docs/` output after each update.

## Privacy

The uploaded original CV contained a street address and phone number. These are deliberately excluded from `PROFILE` and were removed from the PDF included here to avoid publishing personal contact information accidentally. The institutional email is displayed, and the supplied referees' professional addresses are shown on the CV page.
