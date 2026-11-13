# Economics Job Market Website — Python + Jinja2

A simple academic website inspired by the general structure of academic job-market candidate websites. It is an independently written template, not a copy of another person's site.

## 1. Install requirements

You need Python 3.9+.

```bash
python -m pip install -r requirements.txt
```

## 2. Personalise

Edit **only the top section of `build.py`** first:

- `PROFILE`: name, university, research interests, biography, email, social profiles.
- `PAPERS`: titles, abstracts, authors, and PDF filenames.
- `TEACHING`: courses, teaching roles, and terms.

Optionally add a photograph to `static/profile.jpg`. Without a photo, the site will show a monogram placeholder.

Put your actual PDFs in `files/` using filenames referenced in `build.py`. A missing PDF does not create a broken download link. You can place your CV at `files/cv.pdf`.

## 3. Build and preview

```bash
python build.py
python -m http.server 8000 -d docs
```

Open http://localhost:8000 in your browser. To stop the server, press Ctrl+C.

Every time you change content or styling, run `python build.py` again and refresh the browser.

## 4. Publish on GitHub Pages

1. Create a **public** repository named `YOURUSERNAME.github.io` (replace YOURUSERNAME with your GitHub username).
2. Upload or commit the **entire project**, including the generated `docs/` folder. (Do not upload your private files.)
3. In GitHub, navigate to **Settings → Pages**.
4. Choose **Deploy from a branch**, select branch `main`, folder `/docs`, and click **Save**.
5. Visit `https://YOURUSERNAME.github.io` once GitHub Pages has deployed it.

If you already use a project repository named `econ-site`, the URL will instead be `https://YOURUSERNAME.github.io/econ-site/` and relative links will continue to work.

Important: GitHub Pages serves the HTML/CSS in `docs/`; it does not execute `build.py` on its server. Re-run `python build.py` and commit the updated `docs/` whenever you make changes. The empty file `docs/.nojekyll` ensures GitHub serves the generated files without Jekyll processing.

## Structure

```text
build.py                # Change your content here
requirements.txt
templates/              # Jinja2 HTML templates
  base.html
  index.html
  jobmarket.html
  research.html
  teaching.html
  cv.html
static/styles.css       # Custom design
static/profile.jpg      # Optional: you add this
files/                  # Optional: you add PDFs
docs/                   # Generated static website; publish this folder
```

## Customising appearance

Edit `static/styles.css` to change typography, colours, and spacing.
For example, adjust `--burgundy: #6c292f;` for the navigation bar and links.

This site intentionally contains placeholders. Replace all placeholder information with your own before publication.
