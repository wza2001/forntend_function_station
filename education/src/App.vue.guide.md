---
cssClass: wide-page
title: App.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
routes: []
parent_components: ["[[education/src/main.ts.guide]]"]
child_components: ["[[education/src/components/ViewMap.vue.guide]]", "[[education/src/components/spatialchart.vue.guide]]"]
tags: [vue3, component, layout, dashboard]
---

# 🧩 Component: `App.vue`

> [!abstract] Component Overview / 组件概览
> `src/App.vue` is the "Root Component" of your Vue application. It acts as a layout container or "dashboard wrapper". It defines the structure of the screen, layering a full-screen 3D map (`ViewMap`) underneath floating UI elements (charts via `spatialchart`).
> `src/App.vue` 是你 Vue 应用程序的“根组件”。它充当布局容器或“仪表板包装器”。它定义了屏幕的结构，将全屏 3D 地图 (`ViewMap`) 垫在悬浮的用户界面元素（通过 `spatialchart` 显示的图表）之下。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```vue
>> <template>
>>   <div class="dashboard-root">
>>     <!-- 1. 全屏底层地图 -->
>>     <ViewMap geojson-url="/abudhabi_city_buildings.geojson" />
>>
>>     <!-- 2. 左侧悬浮图表面板 -->
>>     <div class="first_parts">
>>       <div class="card">
>>         <spatialchart :chart-option="pieOption" />
>>       </div>
>>       <div class="card">
>>         <spatialchart :chart-option="barOption" />
>>       </div>
>>     </div>
>>
>>     <!-- 3. 其他功能区占位（如用地分析） -->
>>     <div class="land-use"></div>
>>   </div>
>> </template>
>>
>> <script setup lang="ts">
>> import { ref } from 'vue';
>> import ViewMap from '@/components/ViewMap.vue';
>> import spatialchart from '@/components/spatialchart.vue';
>>
>> const barOption = ref({
>>   title: { text: '区域建筑高度分布', textStyle: { color: '#fff', fontSize: 14 } },
>>   tooltip: { trigger: 'axis' },
>>   grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
>>   xAxis: {
>>     type: 'category',
>>     data: ['0-10m', '10-30m', '30-50m', '50-100m', '>100m'],
>>     axisLabel: { color: '#ccc' }
>>   },
>>   yAxis: { type: 'value', axisLabel: { color: '#ccc' } },
>>   series: [
>>     {
>>       data: [120, 200, 150, 80, 40],
>>       type: 'bar',
>>       itemStyle: { color: '#3b82f6', borderRadius: [4, 4, 0, 0] }
>>     }
>>   ]
>> });
>>
>> const pieOption = ref({
>>   title: { text: '空域/用地类型占比', textStyle: { color: '#fff', fontSize: 14 } },
>>   tooltip: { trigger: 'item' },
>>   legend: { bottom: '0', textStyle: { color: '#ccc' } },
>>   series: [
>>     {
>>       name: '用地类型',
>>       type: 'pie',
>>       radius: ['40%', '70%'],
>>       avoidLabelOverlap: false,
>>       itemStyle: { borderRadius: 6, borderColor: '#1e1e1e', borderWidth: 2 },
>>       label: { show: false },
>>       data: [
>>         { value: 1048, name: '住宅区' },
>>         { value: 735, name: '商业区' },
>>         { value: 580, name: '绿地与公园' },
>>         { value: 300, name: '禁飞管控区' }
>>       ]
>>     }
>>   ]
>> });
>> </script>
>>
>> <style scoped>
>> .dashboard-root {
>>   position: relative;
>>   width: 100vw;
>>   height: 100vh;
>>   overflow: hidden;
>> }
>>
>> .first_parts {
>>   position: absolute;
>>   top: 20px;
>>   left: 20px;
>>   width: 320px;
>>   z-index: 10;
>>   display: flex;
>>   flex-direction: column;
>>   gap: 16px;
>>   pointer-events: auto;
>> }
>>
>> .card {
>>   background: rgba(30, 30, 30, 0.85);
>>   backdrop-filter: blur(10px);
>>   border: 1px solid rgba(255, 255, 255, 0.1);
>>   border-radius: 8px;
>>   padding: 12px;
>>   box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
>> }
>> </style>
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Reactivity (核心逻辑与响应式)
>>
>> ### Composition API State / 响应式状态
>> - **`refs`**: `const barOption = ref({...})` and `const pieOption = ref({...})`.
>>   - **Usage**: Here, `ref` holds complex objects containing ECharts configurations. While these configs are static initially, wrapping them in `ref` is best practice in case you want to dynamically update the charts later (e.g., updating data from an API). Vue will automatically re-render the child components when these `.value` objects change.
>>
>> ## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)
>>
>> ### Passing Props to Children (向子组件传递 Props)
>>
>> - **Static Prop (静态 Prop)**: `<ViewMap geojson-url="/abudhabi_city_buildings.geojson" />` passes a plain string to the `ViewMap` component.
>> - **Dynamic Prop (v-bind) (动态 Prop)**: `<spatialchart :chart-option="pieOption" />` uses the `:` shorthand for `v-bind`. It passes the reactive `pieOption` object down to the child `spatialchart` component.
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> > [!info] Declarative Rendering
>> > As the Root Component, `App.vue` rarely interacts directly with the DOM. Instead, it declaratively defines the layout structure and delegates heavy DOM manipulation to specialized child components (like `ViewMap`).
>>
>> ## 🚨 4. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!warning] Z-Index & Layout Constraints / 层级与布局约束
>> > **Concept:** The `App.vue` establishes the absolute positioning context.
>> > **Implementation:**
>> > - `.dashboard-root` uses `position: relative` with `100vw`/`100vh` to fill the entire screen.
>> > - `.first_parts` uses `position: absolute; z-index: 10;` to float the UI *above* the WebGL canvas, which is implicitly at a lower `z-index`. Without this explicit layering, the MapLibre canvas might consume all pointer events, preventing users from interacting with the charts.