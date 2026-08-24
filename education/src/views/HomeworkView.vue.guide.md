---
cssClass: wide-page
title: HomeworkView.vue
type: Component
version: 1.1.0
dependencies:
  - "vue: ^3.3.0"
  - "element-plus: ^2.3.8"
  - "echarts: ^5.4.3"
routes: ["/homework"]
parent_components: ["[[education/src/router/index.ts.guide]]"]
child_components: ["[[education/src/components/homework/PanelSection.vue.guide]]", "[[education/src/components/homework/SecurityStats.vue.guide]]", "[[education/src/components/homework/AlarmList.vue.guide]]", "[[education/src/components/homework/BlacklistCard.vue.guide]]", "[[education/src/components/homework/BottomNav.vue.guide]]", "[[education/src/components/homework/BaseChart.vue.guide]]"]
tags: [vue3, component, view, dashboard, echarts, refactoring]
---

# 🧩 Component: `HomeworkView.vue`

> [!abstract] Component Overview / 组件概览
> `HomeworkView.vue` is a complex dashboard view designed to present security and operational statistics. Previously a monolithic static HTML block, it has now been refactored into a "Smart Container" that coordinates multiple specialized child components (like `PanelSection`, `SecurityStats`, and `BaseChart`). It holds the reactive data and ECharts configurations, passing them down as props.
> `HomeworkView.vue` 是一个复杂的仪表板视图，旨在展示安全和运营统计数据。它以前是一个单体静态 HTML 块，现在已经被重构为一个“智能容器”，负责协调多个专门的子组件（如 `PanelSection`、`SecurityStats` 和 `BaseChart`）。它持有响应式数据和 ECharts 配置，并作为 props 向下传递。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```vue
>> <template>
>>   <div class="homework-container">
>>     <router-link to="/" class="back-btn">
>>       <el-button type="primary" circle>
>>         <el-icon><HomeFilled /></el-icon>
>>       </el-button>
>>     </router-link>
>>
>>     <!-- Left Panel -->
>>     <div class="panel left-panel">
>>       <PanelSection title="安防概况">
>>         <SecurityStats :total-people="overviewStats.totalPeople" ... />
>>       </PanelSection>
>>
>>       <PanelSection title="报警讯息列表" flex>
>>         <AlarmList :alarms="alarmData" />
>>       </PanelSection>
>>     </div>
>>
>>     <!-- Right Panel -->
>>     <div class="panel right-panel">
>>       <PanelSection title="黑名单数据">
>>         <BlacklistCard :count="754" />
>>       </PanelSection>
>>
>>       <PanelSection title="超时访客数据" class="chart-section">
>>         <div class="chart-subtitle">近一周访客超时楼栋分布</div>
>>         <BaseChart :option="barChartOption" />
>>       </PanelSection>
>>
>>       <!-- [Additional sections truncated for brevity] -->
>>     </div>
>>
>>     <BottomNav :items="navItems" v-model:activeIndex="activeNavIndex" />
>>   </div>
>> </template>
>>
>> <script setup lang="ts">
>> // Fixed Boilerplate Imports
>> import { ref, reactive } from 'vue'
>> import { HomeFilled } from '@element-plus/icons-vue'
>> import * as echarts from 'echarts'
>>
>> // Flexible/Common Syntax - Child Components
>> import PanelSection from '@/components/homework/PanelSection.vue'
>> import SecurityStats from '@/components/homework/SecurityStats.vue'
>> import AlarmList, { type AlarmStatus } from '@/components/homework/AlarmList.vue'
>> import BlacklistCard from '@/components/homework/BlacklistCard.vue'
>> import BottomNav from '@/components/homework/BottomNav.vue'
>> import BaseChart from '@/components/homework/BaseChart.vue'
>>
>> // --- Data (Reactive State) ---
>> const overviewStats = reactive({
>>   totalPeople: 12530,
>>   blacklistCount: 25,
>>   // ...
>> })
>>
>> const alarmData = ref([
>>   { name: '监控1: 大西门云台', time: '07:12:18', status: 'resolved' as AlarmStatus },
>>   // ...
>> ])
>>
>> const activeNavIndex = ref(2)
>>
>> // --- Chart Options (ECharts Configurations) ---
>> const barChartOption = ref<Record<string, unknown>>({
>>   // ECharts generic configuration object
>>   // ...
>> })
>> // ... [pieChartOption and lineChartOption similarly defined]
>> </script>
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Reactivity (核心逻辑与响应式)
>>
>> ### Refactored State Management
>> - **`reactive` vs `ref`**: The component correctly uses `reactive` for grouping related primitive fields into a single object (`overviewStats`), and `ref` for arrays (`alarmData`) or single primitives (`activeNavIndex`).
>> - **Centralized Configuration**: The complex ECharts configuration objects (`barChartOption`, `pieChartOption`) are stored here in the parent. This allows the parent to easily update chart data later by modifying these reactive objects, while the actual DOM rendering is handled transparently by `<BaseChart>`.
>>
>> ## 🔄 2. State Flow: Component Orchestration (状态流转：组件编排)
>>
>> This view is a prime example of Vue's recommended **Component-Based Architecture**:
>> - Instead of a massive 300-line HTML template, the layout is now composed of semantic tags like `<PanelSection>` and `<SecurityStats>`.
>> - **Props passing**: Data like `overviewStats.totalPeople` is passed down to children.
>> - **`v-model` usage**: The `<BottomNav>` component uses `v-model:activeIndex`. This is a Vue 3 shorthand that passes the `activeNavIndex` down as a prop AND automatically listens for an `update:activeIndex` event from the child to mutate the parent's state.
>> - (由于不再是庞大的 HTML 模板，现在的布局由语义化标签组成。通过 props 向下传递数据，并使用 `v-model` 实现与子组件的双向绑定同步。)
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> - **Abstracted Chart Lifecycles**: In previous iterations, `HomeworkView` might have handled `echarts.init()` and `window.addEventListener('resize')` manually. By migrating to `<BaseChart>`, this complex canvas lifecycle and memory management (disposing on unmount) is delegated to the child, keeping the parent clean and focused on data.
>>
>> ## 🚨 4. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!check] Refactoring Success
>> > **Improvement:** The codebase has successfully resolved the "Large Template Maintainability" code smell identified in version 1.0.0. By extracting UI elements into `src/components/homework/`, the parent view is now much more scannable, and individual widgets can be optimized or reused independently.
