# Guide: `src/router/index.ts`

## File Purpose & Architecture
This file configures **Vue Router**, the official routing library for Vue.
In a Single Page Application (SPA) like this one, the browser does not actually load new HTML pages when you navigate. Instead, Vue Router intercepts URL changes and dynamically swaps out Vue components inside a `<router-view>` element. This file defines the "map" that tells Vue which URL paths correspond to which components.

## Syntax Breakdown

### 1. Router Initialization (Fixed Boilerplate)
```typescript
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [ ... ]
})

export default router
```
- **`createRouter`**: Factory function to instantiate the router object. This object is what is eventually passed to `app.use(router)` in `main.ts`.
- **`history: createWebHistory(...)`**: Defines how the router manages the browser's URL history. `createWebHistory` uses the modern HTML5 History API, which gives you clean URLs (e.g., `yoursite.com/about`) without the ugly hash symbol (e.g., `yoursite.com/#/about`).
- **`import.meta.env.BASE_URL`**: A Vite-specific environment variable. It ensures routing works correctly even if your app is hosted in a sub-folder (like `yoursite.com/my-vue-app/`).

### 2. Defining Routes (Flexible/Common Syntax)
The `routes` array holds objects defining path-to-component mappings.

#### Synchronous Route (Eager Loading)
```typescript
{
  path: '/',
  name: 'home',
  component: HomeView,
}
```
- **`path`**: The URL path.
- **`name`**: A unique identifier for the route. It's best practice to navigate using names (e.g., `<router-link :to="{ name: 'home' }">`) rather than hardcoded paths, as paths might change.
- **`component: HomeView`**: Because `HomeView` is imported at the top of the file, it is included in the initial JavaScript bundle. When the user visits `/`, this component renders immediately.

#### Asynchronous Route (Lazy Loading / Code Splitting)
```typescript
{
  path: '/about',
  name: 'about',
  component: () => import('../views/AboutView.vue'),
}
```
- **`component: () => import(...)`**: This is a crucial performance optimization. Instead of importing `AboutView` at the top of the file, it uses dynamic import syntax.
- **Effect**: Vite and Rollup (the bundler) will split `AboutView.vue` into a separate JavaScript file (a "chunk"). The browser will *only* download this chunk if and when the user actually navigates to the `/about` route, keeping the initial load time of the app fast.

## Component Nesting & Hierarchy
- The Router sits above standard components. It acts as an orchestrator, deciding which "View" component (like `HomeView` or `AboutView`) should act as the parent component for that specific URL.

## Class/Interface Usage
The objects inside the `routes` array conform to the `RouteRecordRaw` interface defined by Vue Router, which strictly enforces that you must provide a `path` and a `component` (or `redirect`).