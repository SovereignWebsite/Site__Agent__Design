#!/usr/bin/env python3
"""a.design's pages: every reviews/*.md becomes the .html beside it, picker.md becomes picker.html,
and reviews/index.html lists the reviews newest first. Uses the site's own shell from tools/build.py.
Run from the repository root: python3 site/factory/dinis-cruz/account-a/a.design/build.py
"""
import html, importlib.util, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("sitebuild", ROOT / "tools" / "build.py")
sb = importlib.util.module_from_spec(spec); spec.loader.exec_module(sb)
AREA = pathlib.Path(__file__).resolve().parent


def render(md_path, dest, description):
    text = md_path.read_text()
    title = sb.title_of(text)
    rel = dest.relative_to(ROOT / "site").as_posix()
    up = "../" * (len(dest.relative_to(ROOT / "site").parts) - 1)
    out = sb.page(rel, title, '<article class="prose">' + sb.md(text) + "</article>", description)
    out = out.replace(f"{html.escape(title)}, design.b", f"{html.escape(title)}, a.design")
    out = out.replace('href="style.css"', f'href="{up}style.css"').replace('href="favicon.svg"', f'href="{up}favicon.svg"')
    for href, _ in sb.NAV:
        out = out.replace(f'href="{href}"', f'href="{up}{href}"')
    dest.write_text(out)
    return title


def main():
    items = []
    for f in sorted((AREA / "reviews").glob("*.md"), reverse=True):
        t = render(f, f.with_suffix(".html"), "a.design's review of a design round, for the site's keeper on account A.")
        items.append(f'- [{t}]({f.stem}.html)')
    idx = AREA / "reviews" / "index.md"
    idx.write_text("# a.design: reviews, newest first\n\nEach review names the commit it looked at, what was checked, the weakest point of each direction, a recommendation and the changes for the next round. The keeper makes the changes.\n\n" + "\n".join(items) + "\n")
    render(idx, AREA / "reviews" / "index.html", "a.design's design reviews for account A's sites, newest first.")
    idx.unlink()
    if (AREA / "src" / "picker.md").exists():
        render(AREA / "src" / "picker.md", AREA / "picker.html", "The Choose a design standard: one way to compare five designs and pick one, on every site.")
    print("built", len(items), "reviews")


if __name__ == "__main__":
    main()
