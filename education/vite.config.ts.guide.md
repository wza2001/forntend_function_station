# Guide: `vite.config.ts`

## File Purpose & Architecture
`vite.config.ts` is the master configuration file for Vite, the build tool and development server used in this project.
While Vue handles *how* your components behave, Vite handles *how* your files are compiled, served during development, and bundled for production. This file is not run in the browser; it is executed by Node.js when you run commands like `npm run dev` or `npm run build`.

## Syntax Breakdown

### Config Initialization (Fixed Boilerplate)
```typescript
import { defineConfig } from 'vite'
export default defineConfig({ ... })
```
- **`defineConfig`**: A helper function provided by Vite. While you could technically just `export default { ... }`, wrapping it in `defineConfig` provides intelligent TypeScript auto-completion (IntelliSense) in your code editor for all available Vite configuration options.

### Plugins Configuration
```typescript
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

plugins: [
  vue(),
  vueDevTools(),
],
```
- **`vue()`**: The official Vite plugin for Vue. Vite natively only understands JavaScript, TypeScript, and CSS. This plugin tells Vite how to parse `.vue` Single File Components (SFCs), extracting the `<template>`, `<script>`, and `<style>` blocks and compiling them into standard JS/CSS.
- **`vueDevTools()`**: Enables the Vue DevTools extension directly in the browser during development, allowing you to inspect component state, props, and Pinia stores.

### Resolve Aliases (Flexible/Common Syntax)
```typescript
resolve: {
  alias: {
    '@': fileURLToPath(new URL('./src', import.meta.url))
  },
},
```
- **Purpose**: Creates an absolute path shortcut.
- **Effect**: Instead of writing ugly, fragile relative paths like `import ViewMap from '../../components/ViewMap.vue'`, you can use the `@` symbol to always point to the `src` directory: `import ViewMap from '@/components/ViewMap.vue'`.

### Dependency Optimization (Specific Fix)
```typescript
optimizeDeps: {
  exclude: ['@vue/test-utils', 'maplibre-gl']
}
```
- **Purpose**: Vite attempts to pre-bundle external dependencies (node_modules) for performance. However, some complex libraries or testing utilities can break during this process.
- **`exclude`**: This explicitly tells Vite *not* to pre-bundle `maplibre-gl` and `@vue/test-utils`, bypassing issues where Vite might incorrectly process MapLibre's internal WebGL workers or WebAssembly dependencies.

## Hierarchy & Scope
- **Scope**: Global to the entire project build process.
- **Hierarchy**: It sits at the very root of the project, defining the environment in which all Vue code is processed.

## Class/Interface Usage
There are no custom classes here. However, `defineConfig` leverages complex TypeScript interfaces under the hood (specifically `UserConfig`) to enforce that the object you pass to it contains valid Vite configuration keys.