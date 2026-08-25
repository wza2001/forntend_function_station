---
cssClass: wide-page
title: BlacklistCard.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
routes: []
parent_components: ["[[education/src/views/HomeworkView.vue.guide]]"]
child_components: []
tags: [vue3, component, composition-api, element-plus, card, static-ui]
---

# 🧩 Component: `BlacklistCard.vue`

> [!abstract] Component Overview / 组件概览
> A simple statistical card component displaying the count of blacklist occurrences, utilizing Element Plus icons.
> 一个简单的统计卡片组件，显示黑名单出现的次数，并使用 Element Plus 图标。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```vue
>> <template>
>>   <div class="blacklist-stats">
>>     <el-icon color="#67c23a" :size="40"><UserFilled /></el-icon>
>>     <div class="stat-text">近一月出现黑名单次数</div>
>>     <div class="stat-value-large">{{ count }}</div>
>>   </div>
>> </template>
>>
>> <script setup lang="ts">
>> import { UserFilled } from '@element-plus/icons-vue'
>>
>> defineProps<{
>>   count: number
>> }>()
>> </script>
>>
>> <style scoped>
>> .blacklist-stats {
>>   display: flex;
>>   align-items: center;
>>   gap: 15px;
>>   background: rgba(255, 255, 255, 0.05);
>>   padding: 15px;
>> }
>>
>> .stat-text {
>>   font-size: 13px;
>>   color: #ccc;
>> }
>>
>> .stat-value-large {
>>   font-size: 28px;
>>   color: #00bcd4;
>>   font-weight: bold;
>>   margin-left: auto;
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
>> | `count` | `number` | - | Yes | The number of blacklist occurrences to display. (要显示的黑名单出现次数) |
>>
>> ### 📤 Emits (Outputs / 输出)
>> None. (无)
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> Pure presentational component. (纯展示组件。)
>>
>> ## 🛠️ 4. Comprehensive Function & Method Catalog (函数与方法目录)
>>
>> No custom methods defined. Rendering is entirely declarative based on passed props.
>> （未定义自定义方法。渲染完全基于传入的 props 以声明方式进行。）
>>
>> ## 🚨 5. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!check] Performance Optimizations
>> > Extremely lightweight component. (极其轻量级的组件。)
