import os, glob

blog_dir = r'src\content\blog'
titles = []
descriptions = []

for f in glob.glob(os.path.join(blog_dir, '*.md')):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        lines = content.split('\n')
        for line in lines:
            if line.startswith('title:'):
                titles.append(line.replace('title:', '').strip().strip('\"\''))
            if line.startswith('description:'):
                descriptions.append(line.replace('description:', '').strip().strip('\"\''))

from collections import Counter
print("Most common titles:")
for title, count in Counter(titles).most_common(10):
    print(f"{count}: {title}")

print("\nMost common descriptions:")
for desc, count in Counter(descriptions).most_common(5):
    print(f"{count}: {desc}")
