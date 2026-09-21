export const NAV_LINKS = [
  { text: '首页', href: '/' },
  { text: '博客', href: '/blog/' },
  { text: '专题', href: '/airport/' },
  { text: '品牌库', href: '/brands/' },
  { text: '优惠券', href: '/coupons/' },
  { text: '对比', href: '/compare/' },
  { text: '关于', href: '/about/' },
];
export const FOOTER_LINKS = [
  { title: '本站导航', links: NAV_LINKS },
  { title: '热门专题', links: [
    { text: '什么是机场？', href: '/airport/what-is-airport' },
    { text: 'Clash 配置指南', href: '/airport/clash' }
  ]},
  { title: '更多说明', links: [
    { text: '免责声明', href: '/disclaimer' },
    { text: '联系我们', href: '/contact' }
  ]}
];
