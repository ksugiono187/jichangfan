// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://jichangfan.wiki',
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/go/')
    })
  ],
  vite: {
    plugins: [tailwindcss()]
  }
});