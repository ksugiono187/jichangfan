import os, glob, re
blog_dir = r'src\content\blog'
tags = set()
for f in glob.glob(os.path.join(blog_dir, '*.md'))[:50]:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.search(r'tags:\s*\[(.*?)\]', content)
        if match:
            t_list = [t.strip().strip('\'"') for t in match.group(1).split(',')]
            tags.update(t_list)
print('Found tags:', tags)
