Working paper link update for Taejun Kim's academic website

New working-paper destination:
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7692000

Updated files:
  docs/index.html
  docs/research.html
  templates/index.html
  templates/research.html
  build.py

Upload the CONTENTS of this ZIP to the TOP LEVEL of your existing public
GitHub repository teejuun123-dev/foreignworker on branch main.
Existing filenames are replaced in the commit; do not delete other files.
Ensure GitHub Pages still publishes from main /docs.

The working-paper title and the link button on both the homepage and
Research page now open SSRN instead of docs/files/robust-estimation-paper.pdf.
The PDF remains in your existing repository if you don't delete it; this
update simply removes the website's links to it.

For Spyder, open and run the updated build.py. The generator now uses
SSRN for the working-paper links even if the local PDF file exists.

The CV PDF embedded in the website was not modified. If your CV's
[PDF] link should point to SSRN too, modify the LaTeX CV source, rebuild
its PDF, and replace docs/files/cv.pdf as a separate update.
