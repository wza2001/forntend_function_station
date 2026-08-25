---
cssClass: wide-page
title: HomeworkView.vue
type: Component
version: 1.1.0
dependencies:
  - "vue: ^3.3.0"
  - "element-plus: ^2.3.8"
  - "echarts: ^5.4.0"
routes: ["/homework"]
parent_components: ["[[education/src/router/index.ts.guide]]"]
child_components: [
  "[[education/src/components/homework/PanelSection.vue.guide]]",
  "[[education/src/components/homework/SecurityStats.vue.guide]]",
  "[[education/src/components/homework/AlarmList.vue.guide]]",
  "[[education/src/components/homework/BlacklistCard.vue.guide]]",
  "[[education/src/components/homework/BottomNav.vue.guide]]",
  "[[education/src/components/homework/BaseChart.vue.guide]]"
]
tags: [vue3, component, view, dashboard, container]
---

# 🧩 Component: `HomeworkView.vue`

> [!abstract] Component Overview / 组件概览
> `HomeworkView.vue` is the main container view for the homework dashboard. It has been refactored to orchestrate several child components, passing data down as props. It acts as the single source of truth for the dashboard's state.
> `HomeworkView.vue` 是作业仪表板的主要容器视图。它已被重构以协调多个子组件，并将数据作为 props 向下传递。它充当仪表板状态的单一事实来源。

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
>>       <!-- Section 1: Security Overview -->
>>       <PanelSection title="安防概况">
>>         <SecurityStats
>>           :total-people="overviewStats.totalPeople"
>>           :blacklist-count="overviewStats.blacklistCount"
>>           :owner-count="overviewStats.ownerCount"
>>           :visitor-count="overviewStats.visitorCount"
>>           :outsider-count="overviewStats.outsiderCount"
>>         />
>>       </PanelSection>
>>
>>       <!-- Section 2: Alarm Messages -->
>>       <PanelSection title="报警讯息列表" flex>
>>         <AlarmList :alarms="alarmData" />
>>       </PanelSection>
>>     </div>
>>
>>     <!-- Right Panel -->
>>     <div class="panel right-panel">
>>       <!-- Section 1: Blacklist -->
>>       <PanelSection title="黑名单数据">
>>         <BlacklistCard :count="754" />
>>       </PanelSection>
>>
>>       <!-- Section 2: Overdue Visitors (Bar Chart) -->
>>       <PanelSection title="超时访客数据" class="chart-section">
>>         <div class="chart-subtitle">近一周访客超时楼栋分布</div>
>>         <BaseChart :option="barChartOption" />
>>       </PanelSection>
>>
>>       <!-- Section 3: Owner Care (Donut Chart) -->
>>       <PanelSection title="业主关怀" class="chart-section">
>>         <BaseChart :option="pieChartOption" />
>>       </PanelSection>
>>
>>       <!-- Section 4: Alarm Data (Line Chart) -->
>>       <PanelSection title="报警数据" class="chart-section">
>>         <div class="chart-subtitle flex-between">
>>           <span>近一月报警次数</span>
>>           <span>单位: 次数/天</span>
>>         </div>
>>         <BaseChart :option="lineChartOption" />
>>       </PanelSection>
>>     </div>
>>
>>     <!-- Bottom Navigation -->
>>     <BottomNav
>>       :items="navItems"
>>       v-model:activeIndex="activeNavIndex"
>>     />
>>
>>   </div>
>> </template>
>>
>> <script setup lang="ts">
>> import { ref, reactive } from 'vue'
>> import { HomeFilled } from '@element-plus/icons-vue'
>> import * as echarts from 'echarts'
>>
>> import PanelSection from '@/components/homework/PanelSection.vue'
>> import SecurityStats from '@/components/homework/SecurityStats.vue'
>> import AlarmList, { type AlarmStatus } from '@/components/homework/AlarmList.vue'
>> import BlacklistCard from '@/components/homework/BlacklistCard.vue'
>> import BottomNav from '@/components/homework/BottomNav.vue'
>> import BaseChart from '@/components/homework/BaseChart.vue'
>>
>> // --- Data ---
>> const overviewStats = reactive({
>>   totalPeople: 12530,
>>   blacklistCount: 25,
>>   ownerCount: 2318,
>>   visitorCount: 880,
>>   outsiderCount: 174
>> })
>>
>> const alarmData = ref([
>>   { name: '监控1: 大西门云台', time: '07:12:18', status: 'resolved' as AlarmStatus },
>>   { name: '监控2: 大西门云台', time: '07:12:18', status: 'pending' as AlarmStatus },
>>   { name: '监控3: 大西门云台', time: '07:12:18', status: 'processing' as AlarmStatus },
>>   { name: '监控4: 大西门云台', time: '07:12:18', status: 'resolved' as AlarmStatus },
>>   { name: '监控5: 大西门云台', time: '07:12:18', status: 'pending' as AlarmStatus },
>>   { name: '监控6: 大西门云台', time: '07:12:18', status: 'processing' as AlarmStatus },
>>   { name: '监控7: 大西门云台', time: '07:12:18', status: 'resolved' as AlarmStatus },
>>   { name: '监控8: 大西门云台', time: '07:12:18', status: 'pending' as AlarmStatus }
>> ])
>>
>> const navItems = ['社区管理', '安保监控', 'CIM平台', '能源检测', '节能分析']
>> const activeNavIndex = ref(2) // Default to 'CIM平台'
>>
>> // --- Chart Options ---
>> const barChartOption = ref<Record<string, unknown>>({
>>   grid: { top: 10, right: 10, bottom: 20, left: 30 },
>>   xAxis: {
>>     type: 'category',
>>     data: ['6-27', '6-28', '6-29', '6-27', '6-27', '6-27', '6-27'],
>>     axisLabel: { color: '#888', fontSize: 10 }
>>   },
>>   yAxis: {
>>     type: 'value',
>>     splitLine: { lineStyle: { color: 'rgba(255,255,255,0.1)', type: 'dashed' } },
>>     axisLabel: { color: '#888', fontSize: 10 }
>>   },
>>   series: [
>>     {
>>       data: [150, 80, 200, 320, 400, 310, 350],
>>       type: 'bar',
>>       itemStyle: {
>>         color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
>>           { offset: 0, color: '#00f2fe' },
>>           { offset: 1, color: '#4facfe' }
>>         ])
>>       },
>>       barWidth: '60%'
>>     }
>>   ]
>> })
>>
>> const pieChartOption = ref<Record<string, unknown>>({
>>   tooltip: { trigger: 'item' },
>>   legend: {
>>     orient: 'vertical',
>>     right: 10,
>>     top: 'center',
>>     textStyle: { color: '#ccc', fontSize: 10 },
>>     itemWidth: 10,
>>     itemHeight: 10
>>   },
>>   series: [
>>     {
>>       name: '业主关怀',
>>       type: 'pie',
>>       radius: ['50%', '80%'],
>>       center: ['30%', '50%'],
>>       avoidLabelOverlap: false,
>>       label: { show: false },
>>       labelLine: { show: false },
>>       data: [
>>         { value: 1048, name: '长期空置', itemStyle: { color: '#5470c6' } },
>>         { value: 735, name: '长期未外出', itemStyle: { color: '#91cc75' } },
>>         { value: 580, name: '小孩独自出门超时', itemStyle: { color: '#fac858' } },
>>         { value: 484, name: '老人独自出门超时', itemStyle: { color: '#ee6666' } }
>>       ]
>>     }
>>   ]
>> })
>>
>> const lineChartOption = ref<Record<string, unknown>>({
>>   grid: { top: 10, right: 10, bottom: 20, left: 30 },
>>   xAxis: {
>>     type: 'category',
>>     boundaryGap: false,
>>     data: ['6-27', '6-27', '6-27', '6-27', '6-27', '6-27', '6-27', '6-27'],
>>     axisLabel: { color: '#888', fontSize: 10 }
>>   },
>>   yAxis: {
>>     type: 'value',
>>     splitLine: { lineStyle: { color: 'rgba(255,255,255,0.1)', type: 'dashed' } },
>>     axisLabel: { color: '#888', fontSize: 10 }
>>   },
>>   series: [
>>     {
>>       data: [10, 25, 45, 30, 80, 50, 40, 15],
>>       type: 'line',
>>       smooth: true,
>>       areaStyle: {
>>         color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
>>           { offset: 0, color: 'rgba(238, 102, 102, 0.8)' },
>>           { offset: 1, color: 'rgba(238, 102, 102, 0.1)' }
>>         ])
>>       },
>>       lineStyle: { color: '#ee6666' },
>>       itemStyle: { color: '#ee6666' }
>>     }
>>   ]
>> })
>> </script>
>>
>> <style scoped>
>> .homework-container {
>>   width: 100vw;
>>   height: 100vh;
>>   position: relative;
>>   background-image: url('/main.jpg');
>>   background-size: cover;
>>   background-position: center;
>>   background-repeat: no-repeat;
>>   position: relative;
>> }
>>
>> .back-btn {
>>   position: absolute;
>>   top: 20px;
>>   left: 20px;
>>   z-index: 100;
>> }
>>
>> .panel {
>>   position: absolute;
>>   top: 0;
>>   bottom: 0;
>>   width: 380px;
>>   background: linear-gradient(to right, rgba(0, 10, 30, 0.9), rgba(0, 10, 30, 0.4));
>>   padding: 60px 20px 20px;
>>   display: flex;
>>   flex-direction: column;
>>   gap: 20px;
>>   z-index: 10;
>> }
>>
>> .left-panel {
>>   left: 0;
>> }
>>
>> .right-panel {
>>   right: 0;
>>   background: linear-gradient(to left, rgba(0, 10, 30, 0.9), rgba(0, 10, 30, 0.4));
>> }
>>
>> .chart-section {
>>   flex: 1;
>>   min-height: 140px;
>> }
>>
>> .chart-subtitle {
>>   font-size: 11px;
>>   color: #888;
>>   margin-bottom: 5px;
>> }
>>
>> .flex-between {
>>   display: flex;
>>   justify-content: space-between;
>> }
>> </style>
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Reactivity (核心逻辑与响应式)
>>
>> ### Composition API State / 响应式状态
>> - **`overviewStats` (`reactive`)**: Holds the core numerical statistics for the top-left panel. Grouped into a single reactive object for clean prop passing.
>> - **`alarmData` (`ref`)**: An array of alarm objects passed to `AlarmList`.
>> - **`navItems`**, **`activeNavIndex`**: State for the bottom navigation bar. `activeNavIndex` is reactive so the UI can update when a tab is clicked.
>> - **Chart Options (`ref<Record<string, unknown>>`)**: `barChartOption`, `pieChartOption`, and `lineChartOption` store the complex configuration objects required by ECharts.
>>
>> ## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)
>>
>> - **Props Passed Down**: This view acts as a "Smart Component" (Container), fetching/holding data and passing it down to "Dumb Components" (Presentational) like `SecurityStats`, `AlarmList`, and `BaseChart`.
>> - **Two-Way Binding**: It uses `v-model:activeIndex="activeNavIndex"` on `<BottomNav>` to seamlessly handle tab switching events emitted by the child.
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> - Relies on child components (like `BaseChart`) to handle heavy DOM lifting (e.g., ECharts instantiation). This view remains focused on layout and data management.
>>
>> ## 🛠️ 4. UI Architecture & Layout (UI架构与布局)
>>
>> - Utilizes CSS absolute positioning and flexbox to create fixed left and right sidebars (`.panel`) overlaying a background image (`/main.jpg`).
>>
>> ## 🚨 5. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!check] Refactoring Success
>> > The component was successfully refactored from a massive, static HTML file into a clean composition of reusable child components. This significantly improves maintainability and prepares the dashboard for real-time data integration.
>> > （该组件已成功从一个庞大的静态 HTML 文件重构为由可重用子组件组成的干净结构。这显着提高了可维护性，并为仪表板实时数据集成做好了准备。）
