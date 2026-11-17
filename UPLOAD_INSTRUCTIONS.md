# Job Market Paper — Google Drive PDF link update

This update adds a **PDF (Google Drive)** link to:
- Job Market page: `docs/jobmarket.html`
- Homepage: `docs/index.html`
- Research page: `docs/research.html`
- CV webpage: `docs/cv.html`

The GitHub code link remains unchanged. The working-paper SSRN and sBIC links and the Google Drive CV links are preserved.

## Upload to GitHub
Open https://github.com/teejuun123-dev/foreignworker and ensure branch `main`.
Upload the contents of this package at the **repository root**, retaining the `docs/` and `templates/` folders; replace existing files when GitHub asks. Commit the changes. Do not upload the enclosing `JMP_Google_Drive_PDF_Update` directory.

For future rebuilds in Spyder, replace `build.py` and the four files in `templates/` as well. `build.py` now stores `paper_url` for the Job Market Paper so the PDF link is not gated on a local PDF.

## URL and access
Paper: https://drive.google.com/file/d/1rCjl1uoClClzIveW8x3iBroIBQDiQ9-v/view?usp=drive_link
Code: https://github.com/teejuun123-dev/recursive-coexplosivity-breakdowns

Set the Google Drive file permission to **Anyone with the link → Viewer** so visitors can open it.

These are prepared upload files, not changes made directly in GitHub. The separate CV PDF stored on Google Drive is not modified. To add a PDF link inside that PDF itself, edit its LaTeX source and re-export it.
