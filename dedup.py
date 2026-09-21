import os, glob, re

blog_dir = r'src\content\blog'
files = glob.glob(os.path.join(blog_dir, '*.md'))

seen_intents = set()
deleted_count = 0

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    title_match = re.search(r'title:\s*["\']?(.*?)["\']?$', content, re.MULTILINE)
    if not title_match:
        continue
    
    title = title_match.group(1)
    
    core_title = re.sub(r'\s*\(.*?\)\s*|\s*\[.*?\]\s*|\s*-.*|\s*\|.*', '', title).strip()
    
    if core_title in seen_intents:
        os.remove(f)
        deleted_count += 1
    else:
        seen_intents.add(core_title)

print(f'Deleted {deleted_count} perfectly duplicate intent articles. Kept {len(seen_intents)} unique articles.')
