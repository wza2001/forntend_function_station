---
cssClass: wide-page
title: Vue 3 Component Name
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
  - "maplibre-gl: ^3.6.2" # Example third-party dependency
routes: []
parent_components: []
child_components: []
tags: [vue3, component, composition-api]
---

# 🧩 Component: `{{Component Name}}`

> [!abstract] Component Overview / 组件概览
> Provide a brief description of what this component does, its primary responsibility, and where it fits into the overall application architecture.
> 简要描述此组件的功能、主要职责及其在整体应用架构中的位置。

---

## 🏗️ 1. Core Logic & Reactivity (核心逻辑与响应式)

### TypeScript Interfaces & Types / 类型定义
> [!info] Data Structures / 数据结构
> Define the core data models used in this component to ensure type safety.
> 定义此组件中使用的核心数据模型，以确保类型安全。

```typescript
// Example:
interface UserData {
  id: number;
  name: string;
}
```

### Composition API State / 响应式状态
> Document the usage of `ref`, `reactive`, `computed`, and `watch`. Group them logically.
> 记录 `ref`、`reactive`、`computed` 和 `watch` 的使用情况。按逻辑进行分组。

- **`refs` / `reactives`**: (e.g., `const isLoading = ref(false);` - Tracks loading state)
- **`computed`**: (e.g., `const formattedData = computed(...)` - Derives display data)
- **`watch` / `watchEffect`**: (e.g., `watch(() => props.id, fetchData)` - Reacts to prop changes)

---

## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)

### 📥 Props (Inputs / 输入)
> List the properties this component receives from its parent. Include type, default value, and purpose.
> 列出此组件从其父组件接收的属性。包括类型、默认值和用途。

| Prop Name | Type | Default | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| `data` | `Array<UserData>` | `[]` | Yes | The primary dataset to render. (要渲染的主要数据集) |
| `config` | `Record<string, unknown>` | `{}` | No | Configuration options. (配置选项) |

### 📤 Emits (Outputs / 输出)
> List the custom events this component triggers to communicate back to its parent.
> 列出此组件触发的自定义事件，以与父组件进行通信。

| Event Name | Payload Type | Description |
| :--- | :--- | :--- |
| `update:data` | `UserData` | Fired when a user item is modified. (修改用户项时触发) |
| `render-complete` | `void` | Fired when the 3D/Map canvas finishes loading. (3D/地图画布加载完成时触发) |

---

## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)

> [!important] Heavy Library Integration Strategy / 重型库集成策略
> Document how this component interacts with the actual DOM, especially when mounting third-party libraries (MapLibre, Three.js, ECharts).
> 记录此组件如何与实际 DOM 交互，特别是在挂载第三方库（MapLibre、Three.js、ECharts）时。

### Initialization (`onMounted`)
> Explain the setup process. How is the target DOM element acquired? How is the external library instantiated?
> 解释初始化过程。如何获取目标 DOM 元素？外部库是如何实例化的？

```typescript
// Example: MapLibre Integration
import { onMounted, ref, shallowRef } from 'vue';
import maplibregl from 'maplibre-gl';

const mapContainer = ref<HTMLElement | null>(null);
// Use shallowRef for heavy objects like map instances to prevent Vue from deeply tracking them, which causes severe performance drops.
// 使用 shallowRef 存储像地图实例这样的重型对象，防止 Vue 对其进行深度追踪，从而导致严重的性能下降。
const mapInstance = shallowRef<maplibregl.Map | null>(null);

onMounted(() => {
    if (!mapContainer.value) return;
    mapInstance.value = new maplibregl.Map({
        container: mapContainer.value,
        style: 'https://demotiles.maplibre.org/style.json',
        // ...
    });
});
```

### Destruction & Memory Management (`onUnmounted` / `onBeforeUnmount`)
> [!warning] Memory Leak Prevention / 防止内存泄漏
> **Crucial:** Detail the cleanup steps required when the component is destroyed. Failure to do this with WebGL canvases will crash the browser over time.
> **至关重要：** 详细说明组件销毁时所需的清理步骤。如果不清理 WebGL 画布，随着时间的推移会导致浏览器崩溃。

```typescript
// Example Cleanup
import { onUnmounted } from 'vue';

onUnmounted(() => {
    if (mapInstance.value) {
        mapInstance.value.remove(); // Native library cleanup method
        mapInstance.value = null;   // Release memory reference
    }
    // Also remove any manually attached event listeners (e.g., window.addEventListener)
    // 还要移除任何手动附加的事件监听器
});
```

---

## 🚨 4. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)

> Use the callouts below to track specific issues encountered during development and how they were resolved.
> 使用下面的标注块来记录开发过程中遇到的具体问题以及解决方法。

> [!bug] Known Bug / Bug Log (已知问题 / Bug 日志)
> **Issue:** (e.g., The map canvas resizes incorrectly when the sidebar toggles).
> **Root Cause:** Vue reactive state update triggers a re-render before the CSS transition finishes.
> **Solution:** Use `ResizeObserver` on the map container instead of relying solely on Vue state.

> [!warning] Vue Reactivity Traps / Vue 响应式陷阱
> **Warning:** Never wrap a `MapLibre` or `ECharts` instance in a standard `ref` or `reactive`. Vue's Proxy will attempt to intercept thousands of internal properties, freezing the UI.
> **Fix:** ALWAYS use `shallowRef` for instances of heavy third-party classes.

> [!check] Performance Optimizations / 性能优化记录
> - Implemented `v-once` or `v-memo` on static list renders.
> - Debounced the map's `moveend` event before dispatching to the Pinia store.
