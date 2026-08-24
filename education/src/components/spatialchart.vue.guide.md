---
cssClass: wide-page
title: SpatialChart.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
  - "echarts: ^5.5.0"
  - "vue-echarts: ^6.7.0"
routes: []
parent_components: ["[[education/src/App.vue.guide]]"]
child_components: []
tags: [vue3, component, echarts, visualization]
---

# 🧩 Component: `SpatialChart.vue`

> [!abstract] Component Overview / 组件概览
> This file is a reusable, wrapper Vue Component designed to render ECharts data visualizations. Architecturally, it abstracts away the complex import and setup processes required by ECharts. Instead of writing ECharts initialization logic in every single view, you import this component and simply pass it the configuration data.
> 此文件是一个可重用的包装型 Vue 组件，旨在渲染 ECharts 数据可视化图表。在架构上，它抽象掉了 ECharts 所需的复杂导入和设置过程。你无需在每一个视图中编写 ECharts 的初始化逻辑，只需导入这个组件并简单地将配置数据传递给它即可。

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
>> defineProps<{
>>   chartOption: Record<string, any>;
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
>> ### ECharts Tree-Shaking Imports
>> - `import { use } from 'echarts/core';`: Imports the `use` function which is required to register specific ECharts components and charts. This is the core of the tree-shaking process.
>> - `import { CanvasRenderer } from 'echarts/renderers';`: Imports the rendering engine. ECharts can render using Canvas or SVG; this project explicitly chooses Canvas for better performance with large datasets.
>> - `import { PieChart, BarChart } from 'echarts/charts';`: Imports only the logic for Pie and Bar charts, avoiding the need to load code for unused chart types like lines or scatter plots.
>> - `import VChart from 'vue-echarts';`: Imports the official Vue component wrapper for ECharts, which simplifies passing props and listening to resize events.
>>
>> ## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)
>>
>> ### 📥 Props (Inputs / 输入)
>> | Prop Name | Type | Required | Description |
>> | :--- | :--- | :--- | :--- |
>> | `chartOption` | `Record<string, any>` | Yes | The configuration object defining the ECharts visualization. (定义 ECharts 可视化的配置对象。) |
>>
>> *TypeScript `Record<string, any>` Note*: While `any` defeats some purposes of TypeScript, ECharts configuration objects are notoriously complex and deeply nested. Using `Record<string, any>` is a common pragmatic shortcut.
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> ### Initialization & DOM
>> - `<v-chart>`: This is the component provided by the `vue-echarts` wrapper library.
>> - `:option="chartOption"`: Binds the prop passed from the parent directly to the underlying ECharts instance.
>> - `autoresize`: A specific prop provided by `vue-echarts` that automatically listens to window resize events and redraws the canvas so the chart doesn't distort.
>>
>> ## 🚨 4. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!warning] CSS Container Constraints / CSS 容器约束
>> > **Issue:** ECharts canvases absolutely require their parent containers to have a defined height and width. If the container is `0x0`, the chart will simply not render.
>> > **Fix:** This wrapper ensures a default height of `320px`, while filling `100%` of whatever width the parent gives it.
