> [!multi-column]
>
>> [!note] `src/components/spatialchart.vue`
>> ## Full Original Source Code (完整原始源代码)
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
>> [!info] Guide Explanation (指南说明)
>> ## Imports Breakdown (导入部分解析)
>> - `import { use } from 'echarts/core';`: Imports the `use` function which is required to register specific ECharts components and charts. This is the core of the tree-shaking process.
>>   (导入 `use` 函数，该函数用于注册特定的 ECharts 组件和图表。这是摇树优化 (tree-shaking) 过程的核心。)
>> - `import { CanvasRenderer } from 'echarts/renderers';`: Imports the rendering engine. ECharts can render using Canvas or SVG; this project explicitly chooses Canvas for better performance with large datasets.
>>   (导入渲染引擎。ECharts 可以使用 Canvas 或 SVG 进行渲染；此项目明确选择了 Canvas，以便在处理大数据集时获得更好的性能。)
>> - `import { PieChart, BarChart } from 'echarts/charts';`: Imports only the logic for Pie and Bar charts, avoiding the need to load code for unused chart types like lines or scatter plots.
>>   (仅导入饼图和柱状图的逻辑，避免加载诸如折线图或散点图等未使用图表类型的代码。)
>> - `import { TitleComponent, TooltipComponent, LegendComponent, GridComponent } from 'echarts/components';`: Imports UI components for the chart, such as the title, hover tooltips, data legends, and the layout grid.
>>   (导入图表的 UI 组件，如标题、悬停提示框、数据图例和布局网格。)
>> - `import VChart from 'vue-echarts';`: Imports the official Vue component wrapper for ECharts, which simplifies passing props and listening to resize events.
>>   (导入 ECharts 的官方 Vue 组件包装器，它简化了传递 props 和监听调整大小事件的过程。)
>>
>> ## File Purpose & Architecture (文件用途与架构)
>> This file is a reusable, wrapper Vue Component designed to render ECharts data visualizations.
>> (此文件是一个可重用的包装型 Vue 组件，旨在渲染 ECharts 数据可视化图表。)
>> Architecturally, it abstracts away the complex import and setup processes required by ECharts. Instead of writing ECharts initialization logic in every single view, you import this component and simply pass it the configuration data.
>> (在架构上，它抽象掉了 ECharts 所需的复杂导入和设置过程。你无需在每一个视图中编写 ECharts 的初始化逻辑，只需导入这个组件并简单地将配置数据传递给它即可。)
>>
>> ## Component Nesting & Hierarchy (组件嵌套与层级)
>> - **Parent (父组件)**: Can be used by any component, currently used by `App.vue`.
>>   (可以被任何组件使用，目前由 `App.vue` 使用。)
>> - **Child (子组件)**: Utilizes `<v-chart>` (from the `vue-echarts` library) as its core child component.
>>   (利用 `<v-chart>`（来自 `vue-echarts` 库）作为其核心子组件。)
>> - **Communication (通信)**: It receives instructions exclusively via the `chartOption` prop from its parent.
>>   (它完全通过来自其父组件的 `chartOption` prop 接收指令。)
>>
>> ## Syntax Breakdown (语法解析)
>>
>> ### 1. ECharts Tree-Shaking Imports (Flexible/ECharts Syntax) (ECharts 摇树优化导入：灵活/ECharts 语法)
>> ```typescript
>> import { use } from 'echarts/core';
>> import { CanvasRenderer } from 'echarts/renderers';
>> import { PieChart, BarChart } from 'echarts/charts';
>> import { TitleComponent, TooltipComponent, LegendComponent, GridComponent } from 'echarts/components';
>> import VChart from 'vue-echarts';
>>
>> use([ CanvasRenderer, PieChart, BarChart, TitleComponent, TooltipComponent, LegendComponent, GridComponent ]);
>> ```
>> - **Purpose (用途)**: ECharts is a massive library. If you imported the entire library (`import * as echarts from 'echarts'`), your final application bundle would be huge and slow to load.
>>   (ECharts 是一个庞大的库。如果你导入整个库（`import * as echarts from 'echarts'`），你最终的应用程序打包文件将会非常大且加载缓慢。)
>> - **Mechanism (机制)**: The `echarts/core` module allows you to import *only* the specific charts (Pie, Bar) and components (Title, Tooltip) you actually need. The `use([])` function registers these specific modules with the core ECharts engine. This technique is called "Tree-shaking."
>>   (`echarts/core` 模块允许你*仅*导入你实际需要的特定图表（饼图、柱状图）和组件（标题、提示框）。`use([])` 函数将这些特定的模块注册到核心 ECharts 引擎中。这种技术被称为“摇树优化 (Tree-shaking)”。)
>>
>> ### 2. Defining Props (Fixed Boilerplate) (定义 Props：固定样板代码)
>> ```typescript
>> defineProps<{
>>   chartOption: Record<string, any>;
>> }>();
>> ```
>> - **Purpose (用途)**: This component requires the parent to provide a `chartOption` object.
>>   (此组件要求父组件提供一个 `chartOption` 对象。)
>> - **TypeScript `Record<string, any>`**: This is a TypeScript utility type. It essentially means "an object where the keys are strings, and the values can be absolutely anything (`any`)."
>>   (这是一个 TypeScript 实用工具类型。它本质上意味着“一个键是字符串，且值可以是绝对任何东西（`any`）的对象”。)
>>   - *Note (注意)*: While `any` defeats some purposes of TypeScript, ECharts configuration objects are notoriously complex and deeply nested. Using `Record<string, any>` is a common pragmatic shortcut, though importing explicit `EChartsOption` types is better for strictness.
>>     (虽然 `any` 违背了 TypeScript 的某些初衷，但 ECharts 的配置对象以极其复杂和深度嵌套而闻名。使用 `Record<string, any>` 是一种常见的务实捷径，尽管导入明确的 `EChartsOption` 类型在严格性上会更好。)
>>
>> ### 3. Template Usage (Vue Syntax) (模板用法：Vue 语法)
>> ```html
>> <v-chart class="chart" :option="chartOption" autoresize />
>> ```
>> - `<v-chart>`: This is the component provided by the `vue-echarts` wrapper library.
>>   (这是由 `vue-echarts` 包装库提供的组件。)
>> - `:option="chartOption"`: Binds the prop passed from the parent directly to the underlying ECharts instance.
>>   (将从父组件传递过来的 prop 直接绑定到底层的 ECharts 实例。)
>> - `autoresize`: A specific prop provided by `vue-echarts` that automatically listens to window resize events and redraws the canvas so the chart doesn't distort.
>>   (由 `vue-echarts` 提供的一个特定 prop，它会自动监听窗口大小调整事件并重绘图布，这样图表就不会变形。)
>>
>> ## Styling (Scoped) (样式：作用域)
>> ```css
>> .wrapper_chart { width: 100%; height: 320px; }
>> .chart { width: 100%; height: 100%; }
>> ```
>> - **Constraint Handling (约束处理)**: ECharts canvases absolutely require their parent containers to have a defined height and width. If the container is `0x0`, the chart will simply not render. This wrapper ensures a default height of `320px`, while filling `100%` of whatever width the parent gives it.
>>   (ECharts 画布绝对需要其父容器具有定义好的高度和宽度。如果容器是 `0x0`，图表将根本不会渲染。这个包装器确保了默认高度为 `320px`，同时填满父组件给定的任何宽度的 `100%`。)
>>
>> ## Class/Interface Usage (类/接口使用)
>> This component leverages functional imports and composition rather than object-oriented classes. The TypeScript type `Record<string, any>` acts as a structural interface defining the shape of the expected props.
>> (此组件利用了函数式导入和组合，而不是面向对象的类。TypeScript 类型 `Record<string, any>` 充当了一个结构化接口，定义了预期 props 的形状。)