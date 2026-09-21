import { z, defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';

const blogCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    updatedDate: z.date().optional(),
    category: z.string(),
    tags: z.array(z.string()),
    topics: z.array(z.string()).optional(),
    draft: z.boolean().default(false),
    featured: z.boolean().default(false),
    author: z.string().default('机场翻'),
    image: z.string().optional(),
  }),
});

const brandsCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: './src/content/brands' }),
  schema: z.object({
    name: z.string(),
    description: z.string(),
    category: z.string(),
    tags: z.array(z.string()),
    featured: z.boolean().default(false),
    updatedDate: z.date().optional(),
    sortOrder: z.number().optional(),
    price: z.string().optional(),
    nodes: z.string().optional(),
    streaming: z.string().optional(),
  }),
});

const topicsCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: './src/content/topics' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    featured: z.boolean().default(false),
    updatedDate: z.date().optional(),
  }),
});

const airportCollection = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: './src/content/airport' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number().optional(),
    topics: z.array(z.string()).optional(),
  }),
});

export const collections = {
  'blog': blogCollection,
  'brands': brandsCollection,
  'topics': topicsCollection,
  'airport': airportCollection,
};
