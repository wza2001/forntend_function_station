<div style="display: flex; gap: 20px; font-family: sans-serif; align-items: stretch; height: 100vh;">

<div style="flex: 1; min-width: 0; overflow-y: auto; padding: 20px; border-right: 2px solid #ddd; background-color: #f6f8fa;">

# `src/App.vue`

## Full Original Source Code (完整原始源代码)
```vue
<template>
  <div class="dashboard-root">
    <!-- 1. 全屏底层地图 -->
    <ViewMap geojson-url="/abudhabi_city_buildings.geojson" />

    <!-- 2. 左侧悬浮图表面板 -->
    <div class="first_parts">
      <div class="card">
        <spatialchart :chart-option="pieOption" />
      </div>
      <div class="card">
        <spatialchart :chart-option="barOption" />
      </div>
    </div>

    <!-- 3. 其他功能区占位（如用地分析） -->
    <div class="land-use"></div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import ViewMap from '@/components/ViewMap.vue';
import spatialchart from '@/components/spatialchart.vue';

const barOption = ref({
  title: { text: '区域建筑高度分布', textStyle: { color: '#fff', fontSize: 14 } },
  tooltip: { trigger: 'axis' },
  grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
  xAxis: {
    type: 'category',
    data: ['0-10m', '10-30m', '30-50m', '50-100m', '>100m'],
    axisLabel: { color: '#ccc' }
  },
  yAxis: { type: 'value', axisLabel: { color: '#ccc' } },
  series: [
    {
      data: [120, 200, 150, 80, 40],
      type: 'bar',
      itemStyle: { color: '#3b82f6', borderRadius: [4, 4, 0, 0] }
    }
  ]
});

const pieOption = ref({
  title: { text: '空域/用地类型占比', textStyle: { color: '#fff', fontSize: 14 } },
  tooltip: { trigger: 'item' },
  legend: { bottom: '0', textStyle: { color: '#ccc' } },
  series: [
    {
      name: '用地类型',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      itemStyle: { borderRadius: 6, borderColor: '#1e1e1e', borderWidth: 2 },
      label: { show: false },
      data: [
        { value: 1048, name: '住宅区' },
        { value: 735, name: '商业区' },
        { value: 580, name: '绿地与公园' },
        { value: 300, name: '禁飞管控区' }
      ]
    }
  ]
});
</script>

<style scoped>
.dashboard-root {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}

.first_parts {
  position: absolute;
  top: 20px;
  left: 20px;
  width: 320px;
  z-index: 10;
  display: flex;
  flex-direction: column;
  gap: 16px;
  pointer-events: auto;
}

.card {
  background: rgba(30, 30, 30, 0.85);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}
</style>
```
</div>

<div style="flex: 1; min-width: 0; overflow-y: auto; padding: 20px; background-color: #ffffff;">

# Guide Explanation (指南说明)

## Imports Breakdown (导入部分解析)
- `import { ref } from 'vue';`: Imports the `ref` function from Vue. This function is used to create reactive data variables, meaning when the data changes, the UI updates automatically.
  (从 Vue 导入 `ref` 函数。此函数用于创建响应式数据变量，这意味着当数据更改时，UI 会自动更新。)
- `import ViewMap from '@/components/ViewMap.vue';`: Imports the custom `ViewMap` component. This allows you to use `<ViewMap />` in the template to render the 3D map.
  (导入自定义的 `ViewMap` 组件。这允许你在模板中使用 `<ViewMap />` 来渲染 3D 地图。)
- `import spatialchart from '@/components/spatialchart.vue';`: Imports the custom `spatialchart` component. This allows you to use `<spatialchart />` to render the ECharts visualizations.
  (导入自定义的 `spatialchart` 组件。这允许你使用 `<spatialchart />` 来渲染 ECharts 可视化图表。)

## File Purpose & Architecture (文件用途与架构)
`src/App.vue` is the "Root Component" of your Vue application. It is the topmost component in the component tree, loaded directly by `main.ts`.
(`src/App.vue` 是你 Vue 应用程序的“根组件”。它是组件树中最顶层的组件，由 `main.ts` 直接加载。)
In this specific project, `App.vue` acts as a layout container or "dashboard wrapper". It defines the structure of the screen, layering a full-screen 3D map (`ViewMap`) underneath floating UI elements (charts via `spatialchart`).
(在这个特定的项目中，`App.vue` 充当布局容器或“仪表板包装器”。它定义了屏幕的结构，将全屏 3D 地图 (`ViewMap`) 垫在悬浮的用户界面元素（通过 `spatialchart` 显示的图表）之下。)

## Syntax Breakdown (语法解析)

### `<script setup lang="ts">` (Fixed Boilerplate / 固定样板代码)
- **`script setup`**: This is the modern Composition API syntactic sugar in Vue 3. It compiles the script block into the component's `setup()` function. Variables and functions declared here are automatically available to the `<template>` without needing to explicitly `return` them.
  (这是 Vue 3 中现代的组合式 API（Composition API）语法糖。它将脚本块编译为组件的 `setup()` 函数。在此处声明的变量和函数会自动暴露给 `<template>`，而无需显式地 `return` 它们。)
- **`lang="ts"`**: Tells Vite to process this script as TypeScript, enabling static type checking.
  (告诉 Vite 将此脚本作为 TypeScript 处理，从而启用静态类型检查。)

### Flexible/Common Syntax (Business Logic) (灵活/通用语法：业务逻辑)
#### `ref` Initialization (`ref` 初始化)
```typescript
import { ref } from 'vue';
const barOption = ref({ ... });
const pieOption = ref({ ... });
```
- **`ref()`**: A core Vue function that creates a reactive reference to a value. If the inner value (`.value`) changes, Vue automatically triggers a re-render of the template where this `ref` is used.
  (一个核心的 Vue 函数，用于创建一个对值的响应式引用。如果内部值（`.value`）发生变化，Vue 会自动触发使用了这个 `ref` 的模板重新渲染。)
- **Usage (用法)**: Here, `ref` holds complex objects containing ECharts configurations. While these configs are static initially, wrapping them in `ref` is best practice in case you want to dynamically update the charts later (e.g., updating data from an API).
  (在这里，`ref` 保存了包含 ECharts 配置的复杂对象。虽然这些配置最初是静态的，但将它们包装在 `ref` 中是一种最佳实践，以防你稍后想要动态更新图表（例如，从 API 更新数据）。)

## Component Nesting & Hierarchy (组件嵌套与层级)

### Parent-Child Relationships (父子关系)
`App.vue` is the **Parent**, and it imports and uses two **Child** components:
(`App.vue` 是**父组件**，它导入并使用了两个**子组件**：)
1. `ViewMap`
2. `spatialchart` (used twice / 使用了两次)

### Passing Props to Children (向子组件传递 Props)
```html
<ViewMap geojson-url="/abudhabi_city_buildings.geojson" />
<spatialchart :chart-option="pieOption" />
```
- **Static Prop (静态 Prop)**: `geojson-url="..."` passes a plain string to `ViewMap`.
  (`geojson-url="..."` 将一个普通字符串传递给 `ViewMap`。)
- **Dynamic Prop (v-bind) (动态 Prop)**: `:chart-option="pieOption"` uses the `:` shorthand for `v-bind`. It passes the reactive `pieOption` object to the `spatialchart` component.
  (`:chart-option="pieOption"` 使用了 `:` 作为 `v-bind` 的简写。它将响应式的 `pieOption` 对象传递给 `spatialchart` 组件。)

## CSS Styling (Scoped) (CSS 样式：作用域)
```vue
<style scoped>
```
- **`scoped`**: A crucial Vue feature. It ensures that the CSS defined in this block only applies to elements within `App.vue`. Vue achieves this by automatically appending unique data attributes (like `data-v-xyz`) to the HTML elements and CSS selectors.
  (一个至关重要的 Vue 特性。它确保在此块中定义的 CSS 仅适用于 `App.vue` 内的元素。Vue 通过自动将唯一的数据属性（如 `data-v-xyz`）附加到 HTML 元素和 CSS 选择器来实现这一点。)

### Layout Logic (布局逻辑)
- `.dashboard-root`: Uses `position: relative` with `100vw`/`100vh` to fill the entire screen and establish a positioning context for children.
  (使用 `position: relative` 结合 `100vw`/`100vh` 来填满整个屏幕，并为子元素建立定位上下文。)
- `.first_parts`: Uses `position: absolute; z-index: 10;` to float the charts *above* the map, which sits at `z-index: 0` (defined in `ViewMap.vue`).
  (使用 `position: absolute; z-index: 10;` 使图表悬浮在地图*上方*，而地图位于 `z-index: 0`（在 `ViewMap.vue` 中定义）。)

## Class/Interface Usage (类/接口使用)
This file does not define custom classes or interfaces. The TypeScript engine infers the type of `barOption` and `pieOption` based on the provided object literals. In a larger application, you might import an `EChartsOption` interface from the `echarts` package to strictly type these `ref`s.
(此文件没有定义自定义的类或接口。TypeScript 引擎会根据提供的对象字面量推断 `barOption` 和 `pieOption` 的类型。在更大的应用程序中，你可能会从 `echarts` 包中导入一个 `EChartsOption` 接口来严格约束这些 `ref` 的类型。)

</div>
</div>