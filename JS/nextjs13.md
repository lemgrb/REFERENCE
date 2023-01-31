1. `npx create-next-app@latest`
2. Install tailwind using [this guide](https://beta.nextjs.org/docs/styling/tailwind-css)
3. Install @headlessui/react and 
4. pages.js per app/<folder>
	1. 1 page.js : 1 layout.js
5. Link prefetches! (in prod not in develop)
6. Layout
	1. Should accept children prop: `export default function ConferenceLayout({ children })`
	2. Required for root. Optional for the rest of pages
7. Image optimization?
8. Use `@next/font/google` (Google fonts)

## Error

You're importing a component that needs useState. It only works in a Client Component but none of its parents are marked with "use client", so they're Server Components by default.

