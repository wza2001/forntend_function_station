---
cssClass: wide-page
title: BaseChart.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
  - "echarts: ^5.4.0"
routes: []
parent_components: ["[[education/src/views/HomeworkView.vue.guide]]"]
child_components: []
tags: [vue3, component, composition-api, echarts, dataviz]
---

# 🧩 Component: `BaseChart.vue`

> [!abstract] Component Overview / 组件概览
> A reusable wrapper component for ECharts. It handles initialization, responsive resizing, option updates, and proper destruction of the chart instance.
> ECharts 的可重用包装组件。它处理图表实例的初始化、响应式调整大小、选项更新和正确销毁。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```vue
>> <template>
>>   <div class="chart-container" ref="chartRef"></div>
>> </template>
>>
>> <script setup lang="ts">
>> import { ref, onMounted, onUnmounted, watch, shallowRef } from 'vue'
>> import * as echarts from 'echarts'
>>
>> const props = defineProps<{
>>   option: Record<string, unknown>
>> }>()
>>
>> const chartRef = ref<HTMLElement | null>(null)
>> const chartInstance = shallowRef<echarts.ECharts | null>(null)
>>
>> const initChart = () => {
>>   if (chartRef.value) {
>>     chartInstance.value = echarts.init(chartRef.value)
>>     chartInstance.value.setOption(props.option)
>>   }
>> }
>>
>> watch(() => props.option, (newOption) => {
>>   if (chartInstance.value) {
>>     chartInstance.value.setOption(newOption)
>>   }
>> }, { deep: true })
>>
>> const handleResize = () => {
>>   chartInstance.value?.resize()
>> }
>>
>> onMounted(() => {
>>   initChart()
>>   window.addEventListener('resize', handleResize)
>> })
>>
>> onUnmounted(() => {
>>   window.removeEventListener('resize', handleResize)
>>   chartInstance.value?.dispose()
>> })
>> </script>
>>
>> <style scoped>
>> .chart-container {
>>   width: 100%;
>>   flex: 1;
>>   min-height: 120px;
>> }
>> </style>
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Reactivity (核心逻辑与响应式)
>>
>> ### TypeScript Interfaces & Types / 类型定义
>> > [!info] Data Structures / 数据结构
>> `Record<string, unknown>` is used for the ECharts option to satisfy strict TypeScript rules while avoiding deep typing of every possible ECharts configuration. This is crucial for project-wide ESLint compliance without resorting to `any`.
>> （`Record<string, unknown>` 用于 ECharts 选项，以满足严格的 TypeScript 规则，同时避免深入定义所有可能的 ECharts 配置类型。这对于全项目遵守 ESLint 规则至关重要，而无需使用 `any`。）
>>
>> ### Composition API State / 响应式状态
>> - **`chartRef`**: A `ref<HTMLElement | null>` used to get a reference to the DOM element where ECharts will be mounted. (用于获取 ECharts 将要挂载的 DOM 元素的引用。)
>> - **`chartInstance`**: A `shallowRef<echarts.ECharts | null>` to store the ECharts instance.
>>
>> ## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)
>>
>> ### 📥 Props (Inputs / 输入)
>> | Prop Name | Type | Default | Required | Description |
>> | :--- | :--- | :--- | :--- | :--- |
>> | `option` | `Record<string, unknown>` | - | Yes | The ECharts configuration object. (ECharts 配置对象) |
>>
>> ### 📤 Emits (Outputs / 输出)
>> None. (无)
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> ### Initialization (`onMounted`)
>> Instantiates ECharts on the target DOM node (`chartRef.value`) and immediately sets the initial option. Also attaches the `resize` event listener to the window.
>> （在目标 DOM 节点上实例化 ECharts 并立即设置初始选项。还将 `resize` 事件监听器附加到窗口。）
>>
>> ### Destruction & Memory Management (`onUnmounted`)
>> > [!warning] Memory Leak Prevention / 防止内存泄漏
>> > **Crucial:** Removes the window `resize` listener and calls `dispose()` on the ECharts instance to prevent memory leaks when the component unmounts.
>> > （**至关重要：** 移除窗口 `resize` 监听器并在 ECharts 实例上调用 `dispose()`，以防止组件卸载时发生内存泄漏。）
>>
>> ## 🛠️ 4. Comprehensive Function & Method Catalog (函数与方法目录)
>>
>> ### `initChart`
>> - **Purpose**: Initializes the chart instance and applies the initial option.
>> - **Trigger**: Called internally during the `onMounted` lifecycle hook.
>> - **Mechanism**: Uses `echarts.init()` and stores the result in a `shallowRef`.
>>
>> ### `watch(props.option)`
>> - **Purpose**: Reacts to changes in the parent-provided configuration.
>> - **Trigger**: Deep watcher on `props.option`.
>> - **Mechanism**: Calls `setOption(newOption)` on the existing chart instance when data changes.
>>
>> ### `handleResize`
>> - **Purpose**: Adjusts the chart canvas size when the browser window is resized.
>> - **Trigger**: `window` resize event.
>> - **Mechanism**: Calls `resize()` on the ECharts instance.
>>
>> ## 🚨 5. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!warning] Vue Reactivity Traps / Vue 响应式陷阱
>> > **Warning:** The ECharts instance is stored in a `shallowRef`. If wrapped in a standard `ref` or `reactive`, Vue's Proxy would attempt to intercept thousands of internal properties, causing severe performance drops and potentially freezing the UI.
>> > （**警告：** ECharts 实例存储在 `shallowRef` 中。如果包装在标准的 `ref` 或 `reactive` 中，Vue 的 Proxy 会尝试拦截数千个内部属性，从而导致严重的性能下降并可能冻结 UI。）
