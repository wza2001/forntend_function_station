---
cssClass: wide-page
title: DataPanel.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
  - "element-plus: ^2.3.8"
routes: []
parent_components: ["[[education/src/views/MapDashboardView.vue.guide]]"]
child_components: []
tags: [vue3, component, element-plus, composition-api, data-table]
---

# 🧩 Component: `DataPanel.vue`

> [!abstract] Component Overview / 组件概览
> `DataPanel.vue` is a UI overlay component responsible for displaying tabular data (like building information) on top of the map. It features a collapsible panel design and leverages Element Plus for the table rendering.
> `DataPanel.vue` 是一个 UI 叠加层组件，负责在地图上方显示表格数据（如建筑信息）。它具有可折叠面板设计，并利用 Element Plus 进行表格渲染。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```vue
>> <template>
>>   <div class="data-panel" :class="{ 'is-collapsed': isCollapsed }">
>>     <div class="panel-header" @click="toggleCollapse">
>>       <span>Building Data</span>
>>       <el-button type="text" :icon="isCollapsed ? ArrowUp : ArrowDown" circle size="small" />
>>     </div>
>>
>>     <div class="panel-content" v-show="!isCollapsed">
>>       <el-table :data="tableData" style="width: 100%" height="250" :row-class-name="tableRowClassName" size="small">
>>         <el-table-column prop="id" label="ID" width="80" />
>>         <el-table-column prop="name" label="Building Name" />
>>         <el-table-column prop="height" label="Height (m)" width="100" />
>>         <el-table-column prop="type" label="Type" width="120" />
>>         <el-table-column prop="status" label="Status" width="100">
>>           <template #default="scope">
>>             <el-tag :type="scope.row.status === 'Active' ? 'success' : 'warning'" size="small">
>>               {{ scope.row.status }}
>>             </el-tag>
>>           </template>
>>         </el-table-column>
>>       </el-table>
>>     </div>
>>   </div>
>> </template>
>>
>> <script setup lang="ts">
>> // Fixed Boilerplate Imports
>> import { ref } from 'vue'
>> import { ArrowUp, ArrowDown } from '@element-plus/icons-vue'
>>
>> // Flexible/Common Syntax
>> const isCollapsed = ref(false)
>>
>> const toggleCollapse = () => {
>>   isCollapsed.value = !isCollapsed.value
>> }
>>
>> // Mock data
>> const tableData = [
>>   { id: 'B001', name: 'Burj Mohammed Bin Rashid', height: 381, type: 'Mixed Use', status: 'Active' },
>>   // ... [truncated for brevity]
>> ]
>>
>> const tableRowClassName = ({ row }: { row: { height: number } }) => {
>>   if (row.height > 300) {
>>     return 'highlight-row'
>>   }
>>   return ''
>> }
>> </script>
>>
>> <style scoped>
>> /* [Styles truncated for brevity] */
>> </style>
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Reactivity (核心逻辑与响应式)
>>
>> ### Composition API State / 响应式状态
>> - **`isCollapsed` (ref<boolean>)**: Controls the visual state of the panel (expanded vs. collapsed). By binding this to a dynamic class `:class="{ 'is-collapsed': isCollapsed }"`, the component smoothly transitions its width.
>>   (控制面板的视觉状态（展开与折叠）。通过将其绑定到动态类，组件可以平滑地过渡其宽度。)
>>
>> ## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)
>>
>> - **Props**: None currently. The component uses hardcoded mock data. In a production environment, `tableData` should ideally be passed as a prop from the parent (`MapDashboardView`) or fetched from a Pinia store.
>> - **Emits**: None. The collapse state is strictly local UI state, not affecting the parent.
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> ### Template Specifics / 模板细节
>> - **`v-show="!isCollapsed"`**: Unlike `v-if`, `v-show` simply toggles the `display: none` CSS property. This is highly performant for UI elements that toggle frequently, as it avoids destroying and recreating the heavy `el-table` DOM nodes.
>>   (与 `v-if` 不同，`v-show` 只是切换 `display: none` CSS 属性。这对于频繁切换的 UI 元素来说性能很高，因为它避免了销毁和重新创建沉重的 `el-table` DOM 节点。)
>>
>> ## 🛠️ 4. Comprehensive Function & Method Catalog (函数与方法目录)
>>
>> ### `toggleCollapse`
>> - **Purpose**: Inverts the boolean value of `isCollapsed`.
>> - **Trigger**: User clicks on the `.panel-header` div.
>> - **Mechanism**: Basic Vue reactivity mutation (`isCollapsed.value = !isCollapsed.value`).
>>
>> ### `tableRowClassName`
>> - **Purpose**: Dynamically assigns a CSS class to specific rows in the Element Plus table based on data.
>> - **Trigger**: Invoked internally by `el-table` during render for every row.
>> - **Signature**: `({ row }: { row: { height: number } }) => string`
>> - **Mechanism**: Checks if the building height exceeds 300m, returning `'highlight-row'` to trigger a specific CSS styling.
>>
>> ## 🚨 5. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!warning] Element Plus Table Performance
>> > Large datasets in `el-table` can cause significant UI lag. Always ensure pagination or virtual scrolling is implemented if the `tableData` array grows beyond a few hundred rows.
