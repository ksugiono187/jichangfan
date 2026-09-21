import os, glob, random, re

blog_dir = r'src\content\blog'
files = glob.glob(os.path.join(blog_dir, '*.md'))

desc_templates = [
    "深入解析 {brand} 在 {keyword} 方面的真实表现，提供客观的数据分析与选购参考。",
    "想知道 {brand} {keyword} 到底怎么样？本文通过实测数据为您全面揭秘。",
    "关于 {keyword} 的常见疑问解答。我们将以 {brand} 为例，教您如何正确配置与使用。",
    "为您整理了 {brand} {keyword} 的最新教程与评测，帮助新手快速避坑。",
    "全网独家评测：{brand} 的 {keyword} 体验究竟如何？结合晚高峰实测给您最真实的结论。",
    "本文针对 {brand} {keyword} 进行了深度横向对比，带您了解其背后的技术原理与性价比。",
    "还在为 {brand} {keyword} 发愁？这篇保姆级攻略为您提供一步到位的解决方案。",
    "一文看懂 {brand} {keyword}。不仅有图文教程，还有进阶的技巧分享，适合各阶段用户阅读。",
    "{brand} 官方推荐的 {keyword} 指南，结合网友真实反馈，为您提供详尽的图文解析。",
    "针对近期用户关心的 {keyword} 问题，我们对 {brand} 进行了长达一周的监控，得出以下结论。"
]

suffix_variations = [
    "",
    "",
    " (2026实测)",
    " - 最新教程",
    " [防坑指南]",
    "（附图文详解）",
    " - 新手必看",
    "",
    " | 深度测评",
    " (全网首发)"
]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract frontmatter
    match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        continue
    
    frontmatter = match.group(1)
    
    # Extract current title to find brand and keyword
    title_match = re.search(r'title:\s*["\']?(.*?)["\']?$', frontmatter, re.MULTILINE)
    if not title_match:
        continue
    
    old_title = title_match.group(1)
    # Remove (2026最新版)
    clean_title = old_title.replace('(2026最新版)', '').strip()
    
    # Try to extract brand and keyword (format was usually "Brand Keyword")
    parts = clean_title.split(' ', 1)
    if len(parts) == 2:
        brand = parts[0]
        keyword = parts[1]
    else:
        brand = "该机场"
        keyword = clean_title
        
    # Generate new title
    new_title = clean_title + random.choice(suffix_variations)
    
    # Generate new description
    new_desc = random.choice(desc_templates).format(brand=brand, keyword=keyword)
    
    # Replace in frontmatter
    new_frontmatter = re.sub(r'^title:.*$', f'title: "{new_title}"', frontmatter, flags=re.MULTILINE)
    new_frontmatter = re.sub(r'^description:.*$', f'description: "{new_desc}"', new_frontmatter, flags=re.MULTILINE)
    
    new_content = content.replace(frontmatter, new_frontmatter)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)

print(f"Processed {len(files)} files and eliminated SEO template spam.")
