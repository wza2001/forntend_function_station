# Guide: `src/router/index.ts`

## Full Original Source Code (完整原始源代码)
```typescript
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

export default router
```

## Imports Breakdown (导入部分解析)
- `import { createRouter, createWebHistory } from 'vue-router'`: Imports the factory functions needed to build the router instance and configure the HTML5 history mode (clean URLs).
  (导入构建路由器实例并配置 HTML5 历史模式（干净的 URL）所需的工厂函数。)
- `import HomeView from '../views/HomeView.vue'`: Imports the HomeView component eagerly. Because it is imported at the top level, its code is bundled into the initial download when the app starts.
  (预先导入 HomeView 组件。因为它是在顶层导入的，所以它的代码在应用程序启动时会被打包到初始下载中。)

## File Purpose & Architecture (文件用途与架构)
This file configures **Vue Router**, the official routing library for Vue.
(此文件配置了 **Vue Router**，即 Vue 的官方路由库。)
In a Single Page Application (SPA) like this one, the browser does not actually load new HTML pages when you navigate. Instead, Vue Router intercepts URL changes and dynamically swaps out Vue components inside a `<router-view>` element. This file defines the "map" that tells Vue which URL paths correspond to which components.
(在像这样的单页应用程序 (SPA) 中，当你导航时，浏览器实际上并不会加载新的 HTML 页面。相反，Vue Router 会拦截 URL 的更改，并在 `<router-view>` 元素内动态地换出 Vue 组件。此文件定义了一张“地图”，告诉 Vue 哪些 URL 路径对应于哪些组件。)

## Syntax Breakdown (语法解析)

### 1. Router Initialization (Fixed Boilerplate) (路由器初始化：固定样板代码)
```typescript
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [ ... ]
})

export default router
```
- **`createRouter`**: Factory function to instantiate the router object. This object is what is eventually passed to `app.use(router)` in `main.ts`.
  (用于实例化路由器对象的工厂函数。这个对象最终将被传递给 `main.ts` 中的 `app.use(router)`。)
- **`history: createWebHistory(...)`**: Defines how the router manages the browser's URL history. `createWebHistory` uses the modern HTML5 History API, which gives you clean URLs (e.g., `yoursite.com/about`) without the ugly hash symbol (e.g., `yoursite.com/#/about`).
  (定义路由器如何管理浏览器的 URL 历史记录。`createWebHistory` 使用现代的 HTML5 History API，它能为你提供干净的 URL（例如，`yoursite.com/about`），而没有难看的哈希符号（例如，`yoursite.com/#/about`）。)
- **`import.meta.env.BASE_URL`**: A Vite-specific environment variable. It ensures routing works correctly even if your app is hosted in a sub-folder (like `yoursite.com/my-vue-app/`).
  (一个 Vite 特定的环境变量。它能确保即使你的应用程序托管在子文件夹中（如 `yoursite.com/my-vue-app/`），路由也能正常工作。)

### 2. Defining Routes (Flexible/Common Syntax) (定义路由：灵活/通用语法)
The `routes` array holds objects defining path-to-component mappings.
(`routes` 数组包含了定义路径到组件映射关系的对象。)

#### Synchronous Route (Eager Loading) (同步路由：预先加载)
```typescript
{
  path: '/',
  name: 'home',
  component: HomeView,
}
```
- **`path`**: The URL path.
  (URL 路径。)
- **`name`**: A unique identifier for the route. It's best practice to navigate using names (e.g., `<router-link :to="{ name: 'home' }">`) rather than hardcoded paths, as paths might change.
  (路由的唯一标识符。最佳实践是使用名称进行导航（例如，`<router-link :to="{ name: 'home' }">`），而不是硬编码路径，因为路径可能会改变。)
- **`component: HomeView`**: Because `HomeView` is imported at the top of the file, it is included in the initial JavaScript bundle. When the user visits `/`, this component renders immediately.
  (因为 `HomeView` 是在文件顶部导入的，所以它被包含在初始的 JavaScript 打包文件中。当用户访问 `/` 时，此组件会立即渲染。)

#### Asynchronous Route (Lazy Loading / Code Splitting) (异步路由：懒加载/代码分割)
```typescript
{
  path: '/about',
  name: 'about',
  component: () => import('../views/AboutView.vue'),
}
```
- **`component: () => import(...)`**: This is a crucial performance optimization. Instead of importing `AboutView` at the top of the file, it uses dynamic import syntax.
  (这是一个至关重要的性能优化。它没有在文件顶部导入 `AboutView`，而是使用了动态导入语法。)
- **Effect (效果)**: Vite and Rollup (the bundler) will split `AboutView.vue` into a separate JavaScript file (a "chunk"). The browser will *only* download this chunk if and when the user actually navigates to the `/about` route, keeping the initial load time of the app fast.
  (Vite 和 Rollup（打包工具）会将 `AboutView.vue` 分割成一个单独的 JavaScript 文件（一个“代码块/chunk”）。*只有*当用户实际导航到 `/about` 路由时，浏览器才会下载这个代码块，从而保持应用程序的初始加载速度很快。)

## Component Nesting & Hierarchy (组件嵌套与层级)
- The Router sits above standard components. It acts as an orchestrator, deciding which "View" component (like `HomeView` or `AboutView`) should act as the parent component for that specific URL.
  (路由器位于标准组件之上。它扮演着协调者的角色，决定哪个“视图”组件（如 `HomeView` 或 `AboutView`）应该充当该特定 URL 的父组件。)

## Class/Interface Usage (类/接口使用)
The objects inside the `routes` array conform to the `RouteRecordRaw` interface defined by Vue Router, which strictly enforces that you must provide a `path` and a `component` (or `redirect`).
(`routes` 数组中的对象符合 Vue Router 定义的 `RouteRecordRaw` 接口，该接口严格强制要求你必须提供一个 `path` 和一个 `component`（或 `redirect` 重定向）。)