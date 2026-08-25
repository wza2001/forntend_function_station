---
cssClass: wide-page
title: SecurityStats.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
routes: []
parent_components: ["[[education/src/views/HomeworkView.vue.guide]]"]
child_components: []
tags: [vue3, component, composition-api, element-plus, statistics]
---

# 🧩 Component: `SecurityStats.vue`

> [!abstract] Component Overview / 组件概览
> A complex data display component showing an overview of security statistics (total people, blacklist, owners, visitors).
> 一个复杂的数据展示组件，显示安全统计概览（总人数、黑名单、业主、访客）。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```vue
>> <template>
>>   <div class="security-overview">
>>     <div class="overview-top">
>>       <el-icon class="overview-icon" color="#409eff" :size="40"><DataBoard /></el-icon>
>>       <div class="stat-item">
>>         <div class="stat-label">当前社区总人数</div>
>>         <div class="stat-value highlight">{{ totalPeople }}</div>
>>       </div>
>>       <div class="stat-item">
>>         <div class="stat-label">黑名单</div>
>>         <div class="stat-value">{{ blacklistCount }}</div>
>>       </div>
>>     </div>
>>     <div class="overview-bottom">
>>       <div class="stat-sub">
>>         <div class="sub-label bg-cyan">业主人数</div>
>>         <div class="sub-value">{{ ownerCount }}</div>
>>       </div>
>>       <div class="stat-sub">
>>         <div class="sub-label bg-purple">访客人数</div>
>>         <div class="sub-value">{{ visitorCount }}</div>
>>       </div>
>>       <div class="stat-sub">
>>         <div class="sub-label bg-blue">外来人数</div>
>>         <div class="sub-value">{{ outsiderCount }}</div>
>>       </div>
>>     </div>
>>   </div>
>> </template>
>>
>> <script setup lang="ts">
>> import { DataBoard } from '@element-plus/icons-vue'
>>
>> defineProps<{
>>   totalPeople: number
>>   blacklistCount: number
>>   ownerCount: number
>>   visitorCount: number
>>   outsiderCount: number
>> }>()
>> </script>
>>
>> <style scoped>
>> .security-overview {
>>   background: rgba(255, 255, 255, 0.05);
>>   padding: 15px;
>>   border: 1px solid rgba(64, 158, 255, 0.2);
>> }
>>
>> .overview-top {
>>   display: flex;
>>   align-items: center;
>>   gap: 20px;
>>   margin-bottom: 20px;
>> }
>>
>> .stat-item {
>>   display: flex;
>>   flex-direction: column;
>> }
>>
>> .stat-label {
>>   font-size: 12px;
>>   color: #ccc;
>>   margin-bottom: 5px;
>> }
>>
>> .stat-value {
>>   font-size: 18px;
>>   font-weight: bold;
>> }
>>
>> .stat-value.highlight {
>>   font-size: 24px;
>>   color: #409eff;
>> }
>>
>> .overview-bottom {
>>   display: flex;
>>   justify-content: space-between;
>> }
>>
>> .stat-sub {
>>   text-align: center;
>> }
>>
>> .sub-label {
>>   font-size: 12px;
>>   padding: 2px 8px;
>>   border-radius: 2px;
>>   margin-bottom: 5px;
>>   color: #fff;
>> }
>>
>> .bg-cyan { background: #00bcd4; }
>> .bg-purple { background: #9c27b0; }
>> .bg-blue { background: #2196f3; }
>>
>> .sub-value {
>>   font-size: 14px;
>>   font-weight: bold;
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
>> | `totalPeople` | `number` | - | Yes | Total population count. (总人口数) |
>> | `blacklistCount` | `number` | - | Yes | Number of blacklisted individuals. (黑名单人数) |
>> | `ownerCount` | `number` | - | Yes | Number of property owners. (业主数量) |
>> | `visitorCount` | `number` | - | Yes | Number of visitors. (访客数量) |
>> | `outsiderCount` | `number` | - | Yes | Number of outsiders. (外来人员数量) |
>>
>> ### 📤 Emits (Outputs / 输出)
>> None. (无)
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> Pure presentational component formatting numerical data. (用于格式化数字数据的纯展示组件。)
>>
>> ## 🛠️ 4. Comprehensive Function & Method Catalog (函数与方法目录)
>>
>> No custom methods defined. Data is injected directly into the template.
>> （未定义自定义方法。数据直接注入到模板中。）
>>
>> ## 🚨 5. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!check] Layout Consistency
>> > Relies on CSS Grid/Flexbox to maintain consistent alignment of numerical data regardless of string length.
>> > （依赖 CSS Grid/Flexbox 保持数字数据的一致对齐，而不受字符串长度影响。）
