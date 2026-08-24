---
cssClass: wide-page
title: ViewMap.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
  - "maplibre-gl: ^3.6.2"
routes: []
parent_components: ["[[education/src/App.vue.guide]]"]
child_components: []
tags: [vue3, component, maplibre, 3d-rendering, composition-api]
---

# 🧩 Component: `ViewMap.vue`

> [!abstract] Component Overview / 组件概览
> This file is a Vue Component dedicated to rendering a 3D Map using MapLibre GL JS. Architecturally, it isolates all map-related logic from the rest of the application. It receives data instructions (via props) from its parent and manages a complex third-party library (`MapLibre`) within its own lifecycle.
> 此文件是一个专门用于使用 MapLibre GL JS 渲染 3D 地图的 Vue 组件。在架构上，它将所有与地图相关的逻辑与应用程序的其余部分隔离开来。它接收来自其父组件的数据指令（通过 props），并在其自身的生命周期内管理一个复杂的第三方库 (`MapLibre`)。

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
>> import { ref, onMounted, onUnmounted } from 'vue';
>> import { Map } from 'maplibre-gl';
>> import 'maplibre-gl/dist/maplibre-gl.css';
>>
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
>>     });
>>     (window as any).map = mapInstance;
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
>>     console.error('地图初始化失败:', err);
>>   }
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
>> ### DOM Referencing
>> ```typescript
>> const mapContainer = ref<HTMLElement | null>(null);
>> ```
>> - **Template Ref (`ref="mapContainer"`)**: Vue's way of directly interacting with a DOM element. MapLibre needs a raw HTML element to attach the map canvas to. We cannot pass it just a Vue component.
>>
>> ### State Management Strategy
>> ```typescript
>> let mapInstance: Map | null = null;
>> ```
>> - **Why `let` instead of `ref`?** MapLibre's `Map` object is highly complex and manages its own internal state. Making it a reactive Vue `ref` would cause Vue to deeply track thousands of internal map properties, causing severe performance issues. It is a best practice to keep heavy third-party instances out of Vue's reactivity system. (Alternatively, `shallowRef` can be used).
>>
>> ## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)
>>
>> ### 📥 Props (Inputs / 输入)
>> | Prop Name | Type | Default | Required | Description |
>> | :--- | :--- | :--- | :--- | :--- |
>> | `geojsonUrl` | `string` | `'/abudhabi_city_buildings.geojson'` | No | The URL pointing to the GeoJSON data source for 3D buildings. |
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> > [!important] Heavy Library Integration Strategy / 重型库集成策略
>> > MapLibre *must* be initialized only after the DOM is fully constructed by Vue.
>>
>> ### Initialization (`onMounted`)
>> - It initializes the MapLibre `Map` instance. It *must* happen here because MapLibre requires the `mapContainer` `<div>` to actually exist in the browser DOM before it can render.
>> - Sets up visual parameters and event listeners (`mapInstance.on('load', ...)`).
>>
>> ### Destruction & Memory Management (`onUnmounted`)
>> > [!warning] Memory Leak Prevention / 防止内存泄漏
>> > **Crucial:** `mapInstance?.remove();` destroys the WebGL context and frees up memory. This is crucial for preventing memory leaks in Single Page Applications (SPAs) when users navigate away from the map view.
>>
>> ## 🚨 4. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!warning] Vue Reactivity Traps / Vue 响应式陷阱
>> > **Warning:** Never wrap a `MapLibre` instance in a standard `ref` or `reactive`. Vue's Proxy will attempt to intercept thousands of internal properties, freezing the UI.
>>
>> > [!check] Data Visualization Implementation
>> > The `paint` property uses MapLibre's expression syntax (`['interpolate', ...]`) to dynamically color 3D buildings based on their `height` property, creating a visual heatmap effect directly on the GPU.