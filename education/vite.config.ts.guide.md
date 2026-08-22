---
cssClass: wide-page
---

> [!two-column]
> > [!code] Source Code
> > ```typescript
> > import { fileURLToPath, URL } from 'node:url'
> > import { defineConfig } from 'vite'
> > import vue from '@vitejs/plugin-vue'
> > import vueDevTools from 'vite-plugin-vue-devtools'
> >
> > // https://vite.dev/config/
> > export default defineConfig({
> >   plugins: [
> >     vue(),
> >     vueDevTools(),
> >   ],
> >   resolve: {
> >     alias: {
> >       '@': fileURLToPath(new URL('./src', import.meta.url))
> >     },
> >   },
> >   // 添加下面这块配置，防止 Vite 开发服务器去扫描测试用例包
> >   optimizeDeps: {
> >     exclude: ['@vue/test-utils', 'maplibre-gl']
> >   }
> > })
> > ```
>
> > [!note] Architectural Breakdown
> >
> > ## File Relationships (文件关系)
> > Standalone configuration file. Maps to the root of the project.
> >
> > ## Imports Breakdown (导入部分解析)
> > - `import { fileURLToPath, URL } from 'node:url'`: Imports built-in Node.js utilities to safely resolve file paths across different operating systems (Windows/Mac/Linux).
> >   (导入内置的 Node.js 实用工具，以在不同的操作系统（Windows/Mac/Linux）上安全地解析文件路径。)
> > - `import { defineConfig } from 'vite'`: Imports the configuration helper function to enable TypeScript intellisense for Vite settings.
> >   (导入配置辅助函数，以启用 Vite 设置的 TypeScript 智能感知/代码补全。)
> > - `import vue from '@vitejs/plugin-vue'`: Imports the official plugin required to parse and compile Vue SFCs (Single File Components).
> >   (导入解析和编译 Vue SFC（单文件组件）所需的官方插件。)
> > - `import vueDevTools from 'vite-plugin-vue-devtools'`: Imports the plugin that injects the Vue DevTools directly into the browser during local development.
> >   (导入在本地开发期间将 Vue DevTools 直接注入浏览器的插件。)
> >
> > ## File Purpose & Architecture (文件用途与架构)
> > `vite.config.ts` is the master configuration file for Vite, the build tool and development server used in this project.
> > (`vite.config.ts` 是本项目中使用的构建工具和开发服务器 Vite 的主配置文件。)
> > While Vue handles *how* your components behave, Vite handles *how* your files are compiled, served during development, and bundled for production. This file is not run in the browser; it is executed by Node.js when you run commands like `npm run dev` or `npm run build`.
> > (虽然 Vue 处理你的组件*如何*表现，但 Vite 处理你的文件*如何*被编译、在开发期间提供服务，以及为生产环境进行打包。此文件不在浏览器中运行；当您运行诸如 `npm run dev` 或 `npm run build` 的命令时，它由 Node.js 执行。)
> >
> > ## Syntax Breakdown (语法解析)
> >
> > ### Config Initialization (Fixed Boilerplate) (配置初始化：固定样板代码)
> > ```typescript
> > import { defineConfig } from 'vite'
> > export default defineConfig({ ... })
> > ```
> > - **`defineConfig`**: A helper function provided by Vite. While you could technically just `export default { ... }`, wrapping it in `defineConfig` provides intelligent TypeScript auto-completion (IntelliSense) in your code editor for all available Vite configuration options.
> >   (Vite 提供的一个辅助函数。虽然在技术上你只需 `export default { ... }` 即可，但将其包裹在 `defineConfig` 中可以在代码编辑器里为所有可用的 Vite 配置选项提供智能的 TypeScript 自动补全（IntelliSense）。)
> >
> > ### Plugins Configuration (插件配置)
> > ```typescript
> > import vue from '@vitejs/plugin-vue'
> > import vueDevTools from 'vite-plugin-vue-devtools'
> >
> > plugins: [
> >   vue(),
> >   vueDevTools(),
> > ],
> > ```
> > - **`vue()`**: The official Vite plugin for Vue. Vite natively only understands JavaScript, TypeScript, and CSS. This plugin tells Vite how to parse `.vue` Single File Components (SFCs), extracting the `<template>`, `<script>`, and `<style>` blocks and compiling them into standard JS/CSS.
> >   (Vue 官方的 Vite 插件。Vite 原生只理解 JavaScript、TypeScript 和 CSS。这个插件告诉 Vite 如何解析 `.vue` 单文件组件 (SFC)，提取 `<template>`、`<script>` 和 `<style>` 块，并将它们编译成标准的 JS/CSS。)
> > - **`vueDevTools()`**: Enables the Vue DevTools extension directly in the browser during development, allowing you to inspect component state, props, and Pinia stores.
> >   (在开发期间直接在浏览器中启用 Vue DevTools 扩展，允许你检查组件状态、props 和 Pinia 存储。)
> >
> > ### Resolve Aliases (Flexible/Common Syntax) (解析别名：灵活/通用语法)
> > ```typescript
> > resolve: {
> >   alias: {
> >     '@': fileURLToPath(new URL('./src', import.meta.url))
> >   },
> > },
> > ```
> > - **Purpose (用途)**: Creates an absolute path shortcut.
> >   (创建一个绝对路径的快捷方式。)
> > - **Effect (效果)**: Instead of writing ugly, fragile relative paths like `import ViewMap from '../../components/ViewMap.vue'`, you can use the `@` symbol to always point to the `src` directory: `import ViewMap from '@/components/ViewMap.vue'`.
> >   (与其编写像 `import ViewMap from '../../components/ViewMap.vue'` 这样丑陋且脆弱的相对路径，你可以使用 `@` 符号，使其始终指向 `src` 目录：`import ViewMap from '@/components/ViewMap.vue'`。)
> >
> > ### Dependency Optimization (Specific Fix) (依赖优化：特定修复)
> > ```typescript
> > optimizeDeps: {
> >   exclude: ['@vue/test-utils', 'maplibre-gl']
> > }
> > ```
> > - **Purpose (用途)**: Vite attempts to pre-bundle external dependencies (node_modules) for performance. However, some complex libraries or testing utilities can break during this process.
> >   (Vite 会尝试预打包外部依赖项 (node_modules) 以提高性能。然而，一些复杂的库或测试实用程序在此过程中可能会损坏。)
> > - **`exclude`**: This explicitly tells Vite *not* to pre-bundle `maplibre-gl` and `@vue/test-utils`, bypassing issues where Vite might incorrectly process MapLibre's internal WebGL workers or WebAssembly dependencies.
> >   (这明确告诉 Vite *不要*预打包 `maplibre-gl` 和 `@vue/test-utils`，从而绕过 Vite 可能错误处理 MapLibre 内部的 WebGL workers 或 WebAssembly 依赖项的问题。)
> >
> > ## Hierarchy & Scope (层级与作用域)
> > - **Scope (作用域)**: Global to the entire project build process.
> >   (全局作用于整个项目的构建过程。)
> > - **Hierarchy (层级)**: It sits at the very root of the project, defining the environment in which all Vue code is processed.
> >   (它位于项目的最根部，定义了处理所有 Vue 代码的环境。)
> >
> > ## Class/Interface Usage (类/接口使用)
> > There are no custom classes here. However, `defineConfig` leverages complex TypeScript interfaces under the hood (specifically `UserConfig`) to enforce that the object you pass to it contains valid Vite configuration keys.
> > (这里没有自定义的类。但是，`defineConfig` 在底层利用了复杂的 TypeScript 接口（特别是 `UserConfig`）来强制约束你传递给它的对象必须包含有效的 Vite 配置键。)
