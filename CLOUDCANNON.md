# Text-only CloudCannon editing for a plain-HTML page

Goal: non-technical editors change **texts only** on a hand-written static HTML page (e.g. `polet-na-lyzhah.html`) in CloudCannon's Visual Editor. CloudCannon commits the edits back to git. No site generator, no build step, no data files: the committed HTML is the deployed page.

1. **Markup.** Add CloudCannon *Source Editable Regions* to every individual text element (headings, paragraphs, short labels; whole `<ul>` where editors should add/remove items):
   `data-editable="source" data-path="/<file>.html" data-key="<unique-id>"`.
   Only insert attributes into existing opening tags. Don't add or reflow lines, don't touch text or `&nbsp;`. Skip nav, buttons, SVG, forms, meta tags. Verify: stripping the attributes gives back the original file byte-for-byte, and keys are unique.

2. **JS conflicts.** Anything that reacts to clicks on text areas (e.g. a lightbox on cards) should do nothing inside the editor: `if (window.CloudCannonAPI) return;`.

3. **`cloudcannon.config.yml`.** Add a collection on the repo root whose `glob` lists only the editable pages, with add/rename/delete disabled. Under `_editables.text` and `_editables.block`, set every formatting tool to `false` except `undo`/`redo`. Re-check this after any configuration done in the CloudCannon UI, because it rewrites the file and turns formatting back on. Don't restrict `_enabled_editors`.

4. **Git.** CloudCannon works on its own branch (e.g. `content-edits`); publishing = merging it into `main`. Never force-push that branch; use reverts.

5. **CloudCannon.** Sign up, add the site from GitHub on that branch. CloudCannon wrongly detects Astro: change the SSG to **Static**. One successful build is required, otherwise the page shows "no supported editor". The Data Editor is unavailable by design: pages have no front matter.

6. **Test, then invite.** Edit a few texts and check CloudCannon's commit: only text changed, links and `<br>` intact, and see what happened to `&nbsp;`. Then invite people with the **Editors** role (not Technical Editors, who can edit raw HTML).

Not done yet: the deploy GitHub Action (upload to the server on push to `main`), and the other pages.
