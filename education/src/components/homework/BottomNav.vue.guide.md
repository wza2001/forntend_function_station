---
cssClass: wide-page
title: BottomNav.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
routes: []
parent_components: ["[[education/src/views/HomeworkView.vue.guide]]"]
child_components: []
tags: [vue3, component, composition-api, navigation, layout]
---

# 🧩 Component: `BottomNav.vue`

> [!abstract] Component Overview / 组件概览
> A horizontal bottom navigation bar used to toggle views or modes within a dashboard. Implements a common two-way binding pattern using v-model syntax conventions.
> 一个水平底部导航栏，用于在仪表板中切换视图或模式。实现了使用 v-model 语法约定的常见双向绑定模式。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```vue
>> <template>
>>   <div class="bottom-nav">
>>     <div
>>       v-for="(item, index) in items"
>>       :key="index"
>>       class="nav-item"
>>       :class="{ active: activeIndex === index }"
>>       @click="$emit('update:activeIndex', index)"
>>     >
>>       {{ item }}
>>     </div>
>>   </div>
>> </template>
>>
>> <script setup lang="ts">
>> defineProps<{
>>   items: string[]
>>   activeIndex: number
>> }>()
>>
>> defineEmits<{
>>   (e: 'update:activeIndex', index: number): void
>> }>()
>> </script>
>>
>> <style scoped>
>> .bottom-nav {
>>   position: absolute;
>>   bottom: 20px;
>>   left: 50%;
>>   transform: translateX(-50%);
>>   display: flex;
>>   gap: 15px;
>>   background: rgba(0, 20, 50, 0.6);
>>   padding: 10px 20px;
>>   border-radius: 4px;
>>   border: 1px solid rgba(64, 158, 255, 0.3);
>>   z-index: 10;
>> }
>>
>> .nav-item {
>>   padding: 8px 16px;
>>   font-size: 14px;
>>   color: #ccc;
>>   cursor: pointer;
>>   border: 1px solid transparent;
>>   transition: all 0.3s;
>> }
>>
>> .nav-item:hover {
>>   color: #fff;
>>   border-color: rgba(64, 158, 255, 0.5);
>> }
>>
>> .nav-item.active {
>>   color: #fff;
>>   background: rgba(64, 158, 255, 0.2);
>>   border-color: #409eff;
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
>> None defined explicitly; relies on inline primitive types for props.
>> （未明确定义；依赖于 props 的内联基本类型。）
>>
>> ## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)
>>
>> ### 📥 Props (Inputs / 输入)
>> | Prop Name | Type | Default | Required | Description |
>> | :--- | :--- | :--- | :--- | :--- |
>> | `items` | `string[]` | - | Yes | The text labels for the navigation tabs. (导航选项卡的文本标签) |
>> | `activeIndex` | `number` | - | Yes | The currently selected tab index. Used for styling the active tab. (当前选定的选项卡索引。用于设置活动选项卡的样式。) |
>>
>> ### 📤 Emits (Outputs / 输出)
>> | Event Name | Payload Type | Description |
>> | :--- | :--- | :--- |
>> | `update:activeIndex` | `number` | Emitted when a tab is clicked. This naming convention allows the parent component to use `v-model:activeIndex` for easy two-way binding. (当单击选项卡时发出。这种命名约定允许父组件使用 `v-model:activeIndex` 进行简单的双向绑定。) |
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> Pure presentational component. Relies entirely on CSS for hover/active state transitions. (纯展示组件。完全依赖 CSS 进行悬停/活动状态转换。)
>>
>> ## 🛠️ 4. Comprehensive Function & Method Catalog (函数与方法目录)
>>
>> ### `@click="$emit('update:activeIndex', index)"`
>> - **Purpose**: Notifies the parent component that a specific tab was selected.
>> - **Trigger**: User clicks a navigation item.
>> - **Mechanism**: Uses Vue's inline `$emit` method directly within the template.
>>
>> ## 🚨 5. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!check] Clean Architecture
>> > By using `v-model` naming conventions (`update:activeIndex`), the parent component's template stays cleaner, hiding the boilerplate event listening code.
>> > （通过使用 `v-model` 命名约定（`update:activeIndex`），父组件的模板保持整洁，隐藏了繁琐的事件监听代码。）
