---
cssClass: wide-page
title: ViewMap.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
  - "maplibre-gl: ^3.6.2"
routes: []
parent_components: ["[[education/src/views/MapDashboardView.vue.guide]]"]
child_components: []
tags: [vue3, component, maplibre, 3d-rendering, composition-api]
---

# 🧩 Component: `ViewMap.vue`

> [!abstract] Component Overview / 组件概览
> This file is a Vue Component dedicated to rendering a 3D Map using MapLibre GL JS. Architecturally, it isolates all map-related logic from the rest of the application. It receives data instructions (via props) from its parent and manages a complex third-party library (`MapLibre`) within its own lifecycle. It also exposes API methods via `defineExpose` allowing parents to safely command the map instance.
> 此文件是一个专门用于使用 MapLibre GL JS 渲染 3D 地图的 Vue 组件。在架构上，它将所有与地图相关的逻辑与应用程序的其余部分隔离开来。它接收来自其父组件的数据指令（通过 props），并在其自身的生命周期内管理一个复杂的第三方库 (`MapLibre`)。它还通过 `defineExpose` 暴露 API 方法，允许父组件安全地控制地图实例。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```vue
>> <template>
>>   <div ref="mapContainer" class="map-view-container"></div>
>> </template>
>>
>> <script setup lang="ts">
>> // Fixed Boilerplate Imports
>> import { ref, onMounted, onUnmounted } from 'vue';
>> import { Map } from 'maplibre-gl';
>> import * as maplibregl from 'maplibre-gl';
>> import 'maplibre-gl/dist/maplibre-gl.css';
>>
>> // Flexible/Common Syntax
>> const props = withDefaults(
>>   defineProps<{
>>     geojsonUrl?: string;
>>   }>(),
>>   {
>>     geojsonUrl: '/abudhabi_city_buildings.geojson'
>>   }
>> );
>>
>> const mapContainer = ref<HTMLElement | null>(null);
>> let mapInstance: Map | null = null;
>>
>> onMounted(() => {
>>   if (!mapContainer.value) return;
>>
>>   try {
>>     mapInstance = new Map({
>>       container: mapContainer.value,
>>       style: 'https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json',
>>       center: [54.363, 24.496],
>>       zoom: 14.5,
>>       pitch: 60,
>>       bearing: -17.6,
>>       maxPitch: 85,
>>       antialias: true
>>     } as unknown as maplibregl.MapOptions);
>>     (window as unknown as { map: maplibregl.Map }).map = mapInstance;
>>
>>     mapInstance.scrollZoom.setWheelZoomRate(1 / 450);
>>
>>     mapInstance.on('load', () => {
>>       if (!mapInstance) return;
>>
>>       mapInstance.addSource('buildings-source', {
>>         type: 'geojson',
>>         data: props.geojsonUrl
>>       });
>>
>>       mapInstance.addLayer({
>>         id: 'buildings-3d',
>>         type: 'fill-extrusion',
>>         source: 'buildings-source',
>>         paint: {
>>           'fill-extrusion-color': [
>>             'interpolate',
>>             ['linear'],
>>             ['coalesce', ['get', 'height'], 25],
>>             0,   '#1e3a8a',
>>             30,  '#2563eb',
>>             60,  '#06b6d4',
>>             100, '#38bdf8',
>>             180, '#f59e0b',
>>             250, '#ef4444'
>>           ],
>>           'fill-extrusion-opacity': 0.85
>>         }
>>       });
>>     });
>>
>>     mapInstance.on('error', (e) => {
>>       console.warn('MapLibre 底图事件警告:', e);
>>     });
>>   } catch (err) {
>>       console.error('地图初始化失败:', err);
>>   }
>> });
>>
>> const flyTo = (options: maplibregl.FlyToOptions) => {
>>   if (mapInstance) {
>>     mapInstance.flyTo(options);
>>   }
>> };
>>
>> const setViewMode = (is3D: boolean) => {
>>   if (!mapInstance) return;
>>   if (is3D) {
>>     mapInstance.easeTo({ pitch: 60, bearing: -17.6, duration: 1000 });
>>   } else {
>>     mapInstance.easeTo({ pitch: 0, bearing: 0, duration: 1000 });
>>   }
>> };
>>
>> defineExpose({
>>   flyTo,
>>   setViewMode
>> });
>>
>> onUnmounted(() => {
>>   mapInstance?.remove();
>> });
>> </script>
>>
>> <style scoped>
>> .map-view-container {
>>   position: absolute;
>>   top: 0;
>>   left: 0;
>>   width: 100vw;
>>   height: 100vh;
>>   z-index: 0;
>> }
>> </style>
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Reactivity (核心逻辑与响应式)
>>
>> ### Template Reference (`ref`)
>> - `mapContainer`: A reactive reference to the DOM element (`<div ref="mapContainer">`). MapLibre requires a raw HTML element to attach its WebGL canvas.
>>
>> ### Non-Reactive State (`let mapInstance`)
>> - Notice that `mapInstance` is declared as a standard `let` variable, **not** a `ref` or `reactive`. This is a critical architectural decision. MapLibre Map objects are massive, deeply nested structures with their own internal state management. Wrapping them in Vue's Proxy reactivity would cause severe performance issues (UI freezing).
>> - (注意 `mapInstance` 被声明为一个标准的 `let` 变量，**而不是** `ref` 或 `reactive`。这是一个关键的架构决定。MapLibre 地图对象是庞大的、深度嵌套的结构，拥有自己的内部状态管理。用 Vue 的 Proxy 响应式包裹它们会导致严重的性能问题。)
>>
>> ## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)
>>
>> ### 📥 Props
>> - **`geojsonUrl`**: URL pointing to the GeoJSON data file to load on the map.
>>
>> ### 📤 Component API (`defineExpose`)
>> - Instead of emitting events, this component acts as an API provider. Using `defineExpose`, it explicitly reveals internal functions (`flyTo`, `setViewMode`) to its parent component. This allows the parent (`MapDashboardView`) to control the map programmatically without needing direct access to the `mapInstance` itself, maintaining encapsulation.
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> ### Initialization (`onMounted`)
>> - The MapLibre instance is created only *after* the DOM is mounted, ensuring `mapContainer.value` exists.
>> - **`mapInstance.on('load', ...)`**: Map operations (like adding sources and layers) are asynchronous and must wait for the base map style to finish loading.
>>
>> ### Memory Management (`onUnmounted`)
>> > [!warning] WebGL Context Leaks
>> > **CRITICAL:** `mapInstance?.remove()` must be called when the component is destroyed. WebGL contexts are limited in browsers. Failing to destroy the map instance will quickly crash the browser if the user navigates back and forth to this page.
>>
>> ## 🛠️ 4. Syntax Breakdown & Function Details (语法解析与函数详情)
>>
>> ### Paint Expression Syntax (`fill-extrusion-color`)
>> - The component uses MapLibre's data-driven styling expressions.
>> - `['interpolate', ['linear'], ['coalesce', ['get', 'height'], 25], ...]`
>>   - **`get`**: Retrieves the `height` property from the GeoJSON feature.
>>   - **`coalesce`**: Provides a fallback value (25) if the height property is missing or null, preventing rendering errors.
>>   - **`interpolate`**: Smoothly blends colors based on the numerical height value.
>>
>> > [!bug] MapLibre Expression Pitfall
>> > In MapLibre paint expressions, use `['case', ['has', 'property'], ...]` instead of `coalesce` combined with `to-number` to correctly handle missing data in some edge cases, as `to-number` on a missing property evaluates to 0 and breaks fallback logic. (Though coalesce is used here directly, be wary of type coercion in expressions).
