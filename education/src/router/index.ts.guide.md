---
cssClass: wide-page
title: router/index.ts
type: Configuration
version: 1.0.0
dependencies:
  - "vue-router: ^4.2.0"
routes: ["/", "/about"]
parent_components: ["[[education/src/main.ts.guide]]"]
child_components: ["[[education/src/views/HomeView.vue.guide]]", "[[education/src/views/AboutView.vue.guide]]"]
tags: [vue3, vue-router, routing, performance]
---

# 🧩 Configuration: `router/index.ts`

> [!abstract] File Overview / 文件概览
> This file configures Vue Router, the official routing library for Vue. It maps URL paths to specific Vue components, enabling Single Page Application (SPA) navigation without page reloads.
> 此文件配置了 Vue Router，即 Vue 的官方路由库。它将 URL 路径映射到特定的 Vue 组件，从而实现无需重新加载页面的单页应用程序 (SPA) 导航。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```typescript
>> import { createRouter, createWebHistory } from 'vue-router'
>> import HomeView from '../views/HomeView.vue'
>>
>> const router = createRouter({
>>   history: createWebHistory(import.meta.env.BASE_URL),
>>   routes: [
>>     {
>>       path: '/',
>>       name: 'home',
>>       component: HomeView,
>>     },
>>     {
>>       path: '/about',
>>       name: 'about',
>>       // route level code-splitting
>>       // this generates a separate chunk (About.[hash].js) for this route
>>       // which is lazy-loaded when the route is visited.
>>       component: () => import('../views/AboutView.vue'),
>>     },
>>   ],
>> })
>>
>> export default router
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Architecture (核心逻辑与架构)
>>
>> ### Router Instance Creation
>> - `createRouter({...})`: Initializes the router instance.
>> - `history: createWebHistory(...)`: Configures the router to use HTML5 History API. This creates clean URLs (e.g., `yourapp.com/about`) without the hash (`#`) symbol. `import.meta.env.BASE_URL` allows Vite to dynamically inject the base deployment path.
>>
>> ## 🔄 2. Route Definitions (路由定义)
>>
>> ### Static Routing (Eager Loading)
>> - **`/` (Home)**: Uses standard `import HomeView from ...`. This means the code for `HomeView` is bundled into the main initial JavaScript file loaded by the user. It's instantly available, but increases the initial load time.
>>
>> ### Dynamic Routing (Lazy Loading)
>> - **`/about`**: Uses a dynamic import `() => import('../views/AboutView.vue')`.
>> - **Why?** This is a performance optimization known as "route-level code-splitting". Vite/Rollup will separate the `AboutView` code into a distinct `.js` chunk. The browser only downloads this chunk if/when the user actually clicks the link to go to the About page, significantly speeding up the initial load of the application.
>>
>> ## 🚨 4. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!check] Performance Best Practice
>> > Always use dynamic imports (`() => import(...)`) for routes that are not immediately visible when the application loads. Reserve standard static imports only for the primary landing page or critical layout components.
