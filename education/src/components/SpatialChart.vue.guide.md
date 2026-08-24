---
cssClass: wide-page
title: SpatialChart.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
  - "echarts: ^5.4.3"
  - "vue-echarts: ^6.6.1"
routes: []
parent_components: ["[[education/src/views/MapDashboardView.vue.guide]]"]
child_components: []
tags: [vue3, component, echarts, data-visualization]
---

# 🧩 Component: `SpatialChart.vue`

> [!abstract] Component Overview / 组件概览
> `SpatialChart.vue` acts as a wrapper for ECharts, providing a clean, reactive Vue interface for rendering charts. It handles the complex tree-shaking setup required by ECharts Core to ensure minimal bundle sizes, abstracting this complexity away from the rest of the application.
> `SpatialChart.vue` 充当 ECharts 的包装器，提供了一个干净、响应式的 Vue 接口来渲染图表。它处理了 ECharts Core 所需的复杂摇树优化设置，以确保最小的包大小，从而将这种复杂性从应用程序的其余部分中抽象出来。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```vue
>> <template>
>>   <div class="wrapper_chart">
>>     <v-chart class="chart" :option="chartOption" autoresize />
>>   </div>
>> </template>
>>
>> <script setup lang="ts">
>> // Fixed Boilerplate Imports - ECharts Tree Shaking
>> import { use } from 'echarts/core';
>> import { CanvasRenderer } from 'echarts/renderers';
>> import { PieChart, BarChart } from 'echarts/charts';
>> import {
>>   TitleComponent,
>>   TooltipComponent,
>>   LegendComponent,
>>   GridComponent
>> } from 'echarts/components';
>> import VChart from 'vue-echarts';
>>
>> // Register ECharts components
>> use([
>>   CanvasRenderer,
>>   PieChart,
>>   BarChart,
>>   TitleComponent,
>>   TooltipComponent,
>>   LegendComponent,
>>   GridComponent
>> ]);
>>
>> // Flexible/Common Syntax
>> defineProps<{
>>   chartOption: Record<string, unknown>;
>> }>();
>> </script>
>>
>> <style scoped>
>> .wrapper_chart {
>>   width: 100%;
>>   height: 320px;
>> }
>> .chart {
>>   width: 100%;
>>   height: 100%;
>> }
>> </style>
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Reactivity (核心逻辑与响应式)
>>
>> ### ECharts Tree Shaking Setup
>> - Instead of importing the massive monolithic `echarts` library, this component imports only the specific modules needed (CanvasRenderer, PieChart, BarChart, etc.) from `echarts/core`.
>> - The `use()` function registers these modules. This drastically reduces the final JavaScript bundle size sent to the browser.
>> - (它没有导入庞大的整体 `echarts` 库，而是仅从 `echarts/core` 导入所需的特定模块。`use()` 函数注册这些模块。这极大地减少了发送到浏览器的最终 JavaScript 包大小。)
>>
>> ## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)
>>
>> ### 📥 Props (Inputs / 输入)
>>
>> | Prop Name | Type | Required | Description |
>> | :--- | :--- | :--- | :--- |
>> | `chartOption` | `Record<string, unknown>` | Yes | The configuration object that dictates the chart's appearance and data, conforming to ECharts Option specifications. |
>>
>> > [!info] TypeScript Record Type Strategy
>> > Why use `Record<string, unknown>` instead of the specific `EChartsOption` type? When configuring ECharts with Vue 3 and TypeScript, the complex nested generic types of `EChartsOption` can sometimes cause deep type mismatch errors when passed as props or made reactive. Using `Record<string, unknown>` satisfies TypeScript and strict ESLint rules (like `@typescript-eslint/no-explicit-any`) while allowing the flexibility needed for dynamic chart configurations.
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> - The `<v-chart>` component from `vue-echarts` handles the lifecycle integration internally, automatically calling ECharts `init()` on mount and `dispose()` on unmount, preventing memory leaks.
>> - **`autoresize` prop**: A crucial attribute on `<v-chart>` that attaches a `ResizeObserver` to the container, ensuring the canvas redraws smoothly if the parent element's dimensions change.
>>
>> ## 🚨 4. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!warning] ECharts Reactivity Trap
>> > **Never** attempt to make an ECharts instance itself reactive using `ref` or `reactive`. Vue's Proxy system will attempt to recursively track the thousands of properties within the ECharts engine, causing catastrophic performance degradation and browser freezes. `vue-echarts` handles this safely internally.
