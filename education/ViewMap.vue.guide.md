# Guide: `src/components/ViewMap.vue`

## File Purpose & Architecture (文件用途与架构)
This file is a Vue Component dedicated to rendering a 3D Map using MapLibre GL JS.
(此文件是一个专门用于使用 MapLibre GL JS 渲染 3D 地图的 Vue 组件。)
Architecturally, it isolates all map-related logic from the rest of the application. It receives data instructions (via props) from its parent (`App.vue`) and manages a complex third-party library (`MapLibre`) within its own lifecycle.
(在架构上，它将所有与地图相关的逻辑与应用程序的其余部分隔离开来。它接收来自其父组件 (`App.vue`) 的数据指令（通过 props），并在其自身的生命周期内管理一个复杂的第三方库 (`MapLibre`)。)

## Component Nesting & Hierarchy (组件嵌套与层级)
- **Parent (父组件)**: `App.vue`. The parent dictates *where* the map goes and *what* data it should load (via the `geojsonUrl` prop).
  (`App.vue`。父组件决定了地图放置在*哪里*，以及它应该加载*什么*数据（通过 `geojsonUrl` prop）。)
- **Child (子组件)**: None. This is a leaf component.
  (无。这是一个叶子组件（最底层的组件）。)

## Syntax Breakdown (语法解析)

### 1. Props Definition (Fixed/TypeScript Syntax) (Props 定义：固定/TypeScript 语法)
```typescript
const props = withDefaults(
  defineProps<{
    geojsonUrl?: string;
  }>(),
  {
    geojsonUrl: '/abudhabi_city_buildings.geojson'
  }
);
```
- **`defineProps`**: A compiler macro in `<script setup>` used to declare what props the component accepts. Here it uses TypeScript type arguments (`<{ geojsonUrl?: string; }>`) to enforce that `geojsonUrl` is a string and is optional (`?`).
  (`<script setup>` 中的一个编译器宏，用于声明组件接收哪些 props。这里它使用 TypeScript 类型参数 (`<{ geojsonUrl?: string; }>`) 来强制规定 `geojsonUrl` 是一个字符串并且是可选的 (`?`)。)
- **`withDefaults`**: A helper function to provide default values for optional props. If the parent doesn't provide a URL, it defaults to the local Abu Dhabi file.
  (一个辅助函数，用于为可选的 props 提供默认值。如果父组件没有提供 URL，它将默认使用本地的阿布扎比文件。)

### 2. DOM Referencing (DOM 引用)
```html
<div ref="mapContainer" class="map-view-container"></div>
```
```typescript
const mapContainer = ref<HTMLElement | null>(null);
```
- **Template Ref (`ref="mapContainer"`) (模板引用)**: Vue's way of directly interacting with a DOM element. The `mapContainer` variable in the script is bound to this `<div>`.
  (Vue 直接与 DOM 元素交互的方式。脚本中的 `mapContainer` 变量绑定到了这个 `<div>` 上。)
- MapLibre needs a raw HTML element to attach the map canvas to. We cannot pass it just a Vue component.
  (MapLibre 需要一个原生的 HTML 元素来挂载地图画布。我们不能只传递给它一个 Vue 组件。)

### 3. State Management (状态管理)
```typescript
let mapInstance: Map | null = null;
```
- Notice this is a standard `let` variable, **not** a `ref`.
  (注意，这是一个标准的 `let` 变量，**不是**一个 `ref`。)
- **Why? (为什么？)** MapLibre's `Map` object is highly complex and manages its own internal state. Making it a reactive Vue `ref` would cause Vue to deeply track thousands of internal map properties, causing severe performance issues. It is a best practice to keep heavy third-party instances out of Vue's reactivity system.
  (MapLibre 的 `Map` 对象非常复杂，并且管理着它自己的内部状态。如果将其设为响应式的 Vue `ref`，会导致 Vue 深度追踪成千上万个内部地图属性，从而引起严重的性能问题。将沉重的第三方实例排除在 Vue 的响应式系统之外是一种最佳实践。)

## Lifecycle Hooks & Functions (生命周期钩子与函数)

### `onMounted` (Fixed Boilerplate / 固定样板代码)
- **Purpose (用途)**: A Vue lifecycle hook that runs *after* the component has been inserted into the DOM.
  (一个 Vue 生命周期钩子，在组件被插入到 DOM *之后*运行。)
- **Trigger (触发时机)**: Called automatically by Vue during component creation.
  (在组件创建期间由 Vue 自动调用。)
- **Action (操作)**: It initializes the MapLibre `Map` instance. It *must* happen here because MapLibre requires the `mapContainer` `<div>` to actually exist in the browser DOM before it can render.
  (它初始化 MapLibre 的 `Map` 实例。这*必须*在这里发生，因为 MapLibre 要求在它可以渲染之前，`mapContainer` 的 `<div>` 必须实际存在于浏览器的 DOM 中。)

#### Inside `onMounted` (Flexible/MapLibre Logic) (在 `onMounted` 内部：灵活/MapLibre 逻辑):
1. **Instantiation (实例化)**: `new Map({...})` sets up the visual parameters (center, zoom, pitch).
   (`new Map({...})` 设置了视觉参数（中心点、缩放级别、倾斜度）。)
2. **Event Listeners (事件监听器)**: `mapInstance.on('load', ...)` waits for the base map style to finish downloading before adding custom data.
   (`mapInstance.on('load', ...)` 等待底图样式下载完成，然后再添加自定义数据。)
3. **Adding Data (添加数据)**:
   - `addSource`: Registers the GeoJSON data URL.
     (注册 GeoJSON 数据 URL。)
   - `addLayer`: Tells the map *how* to draw the data. Uses `fill-extrusion` to draw 3D buildings based on the `height` property in the GeoJSON.
     (告诉地图*如何*绘制数据。使用 `fill-extrusion` 基于 GeoJSON 中的 `height` 属性绘制 3D 建筑。)

### `onUnmounted` (Fixed Boilerplate / 固定样板代码)
- **Purpose (用途)**: Runs right before the component is destroyed (removed from the DOM).
  (在组件被销毁（从 DOM 中移除）之前运行。)
- **Trigger (触发时机)**: Called automatically by Vue (e.g., if you navigated to a different page using Vue Router).
  (由 Vue 自动调用（例如，如果你使用 Vue Router 导航到了不同的页面）。)
- **Action (操作)**: `mapInstance?.remove();` destroys the WebGL context and frees up memory. This is crucial for preventing memory leaks in Single Page Applications (SPAs).
  (`mapInstance?.remove();` 销毁 WebGL 上下文并释放内存。这对于防止单页应用程序 (SPA) 中的内存泄漏至关重要。)

## Class/Interface Usage (类/接口使用)
- **`Map` (from 'maplibre-gl')**: An imported Class. `new Map(...)` creates a specific instance of the map engine.
  (一个导入的类。`new Map(...)` 创建地图引擎的特定实例。)
- **TypeScript Generics (`ref<HTMLElement | null>`) (TypeScript 泛型)**: Explicitly tells TypeScript that `mapContainer` will eventually hold an HTML element, but starts as `null` (before `onMounted` runs).
  (显式地告诉 TypeScript，`mapContainer` 最终将持有一个 HTML 元素，但在开始时为 `null`（在 `onMounted` 运行之前）。)