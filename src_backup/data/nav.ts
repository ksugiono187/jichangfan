export const NAV_LINKS = [
  { text: '首页', href: '/' },
  { text: '博客', href: '/blog/' },
  { text: '专题', href: '/topics/' },
  { text: '品牌库', href: '/brands/' },
  { text: '对比', href: '/compare/' },
  { text: '关于', href: '/about/' },
];
export const FOOTER_LINKS = [
  { title: '本站导航', links: NAV_LINKS },
  { title: '热门专题', links: [
    { text: '新手入门指南', href: '/topics/beginner' },
    { text: '进阶使用技巧', href: '/topics/advanced' }
  ]},
  { title: '更多说明', links: [
    { text: '免责声明', href: '/about#disclaimer' },
    { text: '联系我们', href: '/about#contact' }
  ]}
];
