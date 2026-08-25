---
cssClass: wide-page
title: AlarmList.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
routes: []
parent_components: ["[[education/src/views/HomeworkView.vue.guide]]"]
child_components: []
tags: [vue3, component, composition-api, element-plus, list]
---

# 🧩 Component: `AlarmList.vue`

> [!abstract] Component Overview / 组件概览
> Renders a list of alarm messages with different status indicators using Element Plus tags.
> 使用 Element Plus 标签渲染带有不同状态指示器的警报消息列表。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```vue
>> <template>
>>   <div class="alarm-list">
>>     <div class="alarm-item" v-for="(alarm, index) in alarms" :key="index">
>>       <div class="alarm-info">
>>         <div class="alarm-name">{{ alarm.name }}</div>
>>         <div class="alarm-time">{{ alarm.time }}</div>
>>       </div>
>>       <el-tag :type="getStatusType(alarm.status)" size="small">
>>         {{ getStatusLabel(alarm.status) }}
>>       </el-tag>
>>     </div>
>>   </div>
>> </template>
>>
>> <script setup lang="ts">
>> export type AlarmStatus = 'resolved' | 'pending' | 'processing'
>>
>> export interface AlarmMessage {
>>   name: string
>>   time: string
>>   status: AlarmStatus
>> }
>>
>> defineProps<{
>>   alarms: AlarmMessage[]
>> }>()
>>
>> const getStatusType = (status: AlarmStatus) => {
>>   switch (status) {
>>     case 'resolved': return 'success'
>>     case 'pending': return 'warning'
>>     case 'processing': return 'info'
>>     default: return 'info'
>>   }
>> }
>>
>> const getStatusLabel = (status: AlarmStatus) => {
>>   switch (status) {
>>     case 'resolved': return '已消警'
>>     case 'pending': return '待派遣'
>>     case 'processing': return '处理中'
>>     default: return '未知'
>>   }
>> }
>> </script>
>>
>> <style scoped>
>> .alarm-list {
>>   flex: 1;
>>   overflow-y: auto;
>>   padding-right: 5px;
>> }
>>
>> .alarm-list::-webkit-scrollbar {
>>   width: 4px;
>> }
>> .alarm-list::-webkit-scrollbar-thumb {
>>   background: rgba(64, 158, 255, 0.5);
>>   border-radius: 2px;
>> }
>>
>> .alarm-item {
>>   display: flex;
>>   justify-content: space-between;
>>   align-items: center;
>>   padding: 10px;
>>   background: rgba(255, 255, 255, 0.05);
>>   margin-bottom: 8px;
>>   border-left: 3px solid #409eff;
>> }
>>
>> .alarm-name {
>>   font-size: 13px;
>>   margin-bottom: 4px;
>> }
>>
>> .alarm-time {
>>   font-size: 11px;
>>   color: #888;
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
>> `AlarmStatus` and `AlarmMessage` interfaces are exported, allowing parent components to strictly type the data they pass in.
>> （导出了 `AlarmStatus` 和 `AlarmMessage` 接口，允许父组件对其传入的数据进行严格的类型检查。）
>>
>> ## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)
>>
>> ### 📥 Props (Inputs / 输入)
>> | Prop Name | Type | Default | Required | Description |
>> | :--- | :--- | :--- | :--- | :--- |
>> | `alarms` | `AlarmMessage[]` | - | Yes | Array of alarm objects to display. (要显示的警报对象数组) |
>>
>> ### 📤 Emits (Outputs / 输出)
>> None. (无)
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> Pure presentational component. No complex DOM manipulations or heavy library integrations.
>> （纯展示组件。没有复杂的 DOM 操作或重型库集成。）
>>
>> ## 🛠️ 4. Comprehensive Function & Method Catalog (函数与方法目录)
>>
>> ### `getStatusType`
>> - **Purpose**: Maps the alarm status to an Element Plus tag type (success, warning, info).
>> - **Trigger**: Template interpolation during render.
>> - **Mechanism**: Simple `switch` statement based on `AlarmStatus`.
>>
>> ### `getStatusLabel`
>> - **Purpose**: Translates the internal status string to a display-friendly label.
>> - **Trigger**: Template interpolation during render.
>> - **Mechanism**: Simple `switch` statement.
>>
>> ## 🚨 5. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!check] Performance Optimizations
>> > For extremely long lists, consider implementing virtual scrolling. However, for a typical dashboard sidebar, standard `v-for` is sufficient.
>> > （对于极长的列表，可以考虑实现虚拟滚动。然而，对于典型的仪表板侧边栏，标准的 `v-for` 已经足够了。）
