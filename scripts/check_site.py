"""Check static structure and local links; no third-party dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.tags, self.dates = set(), [], [], []
        self.lang = None
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append(tag)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'html': self.lang = a.get('lang')
        if tag == 'time': self.dates.append(a.get('datetime',''))
        for key in ('href','src'):
            if key in a: self.links.append(a[key])

files = [ROOT/'index.html', *sorted((ROOT/'guides').glob('*.html'))]
pages = {f: Page(f.read_text()) for f in files}
errors = []
for f, page in pages.items():
    label = str(f.relative_to(ROOT))
    def require(condition, msg):
        if not condition: errors.append(f'{label}: {msg}')
    require(page.lang == 'zh-Hant', 'missing zh-Hant language')
    require(page.tags.count('h1') == 1, 'must have one h1')
    require('main' in page.ids, 'missing main anchor')
    require('TODO' not in f.read_text(), 'unfilled placeholder')
    if f.parent.name == 'guides':
        require({'quick-answer','steps','english','sources','related'} <= page.ids,'missing guide section')
        require(any(re.fullmatch(r'\d{4}-\d{2}-\d{2}', d) for d in page.dates),'missing review date')
        require(any(urlsplit(u).hostname == 'www.metro.taipei' for u in page.links),'missing official source')
    for link in page.links:
        require(bool(link.strip()),'empty link')
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc: continue
        require(not parsed.path.startswith('/'), f'root-relative path: {link}')
        target = (f.parent/unquote(parsed.path)).resolve() if parsed.path else f
        require(target.is_file(), f'missing file: {link}')
        if parsed.fragment and target.is_file() and target.suffix == '.html':
            target_page = pages.get(target) or Page(target.read_text())
            require(unquote(parsed.fragment) in target_page.ids, f'missing anchor: {link}')
for f in files[1:]:
    relative = f.relative_to(ROOT).as_posix()
    if relative not in pages[ROOT/'index.html'].links: errors.append(f'{relative}: missing homepage link')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(files)} pages; structure, source presence, dates, local files and anchors checked.')
