<template>
  <div class="homework-container">
    <router-link to="/" class="back-btn">
      <el-button type="primary" circle>
        <el-icon><HomeFilled /></el-icon>
      </el-button>
    </router-link>

    <!-- Left Panel -->
    <div class="panel left-panel">
      <!-- Section 1: Security Overview -->
      <PanelSection title="安防概况">
        <SecurityStats
          :total-people="overviewStats.totalPeople"
          :blacklist-count="overviewStats.blacklistCount"
          :owner-count="overviewStats.ownerCount"
          :visitor-count="overviewStats.visitorCount"
          :outsider-count="overviewStats.outsiderCount"
        />
      </PanelSection>

      <!-- Section 2: Alarm Messages -->
      <PanelSection title="报警讯息列表" flex>
        <AlarmList :alarms="alarmData" />
      </PanelSection>
    </div>

    <!-- Right Panel -->
    <div class="panel right-panel">
      <!-- Section 1: Blacklist -->
      <PanelSection title="黑名单数据">
        <BlacklistCard :count="754" />
      </PanelSection>

      <!-- Section 2: Overdue Visitors (Bar Chart) -->
      <PanelSection title="超时访客数据" class="chart-section">
        <div class="chart-subtitle">近一周访客超时楼栋分布</div>
        <BaseChart :option="barChartOption" />
      </PanelSection>

      <!-- Section 3: Owner Care (Donut Chart) -->
      <PanelSection title="业主关怀" class="chart-section">
        <BaseChart :option="pieChartOption" />
      </PanelSection>

      <!-- Section 4: Alarm Data (Line Chart) -->
      <PanelSection title="报警数据" class="chart-section">
        <div class="chart-subtitle flex-between">
          <span>近一月报警次数</span>
          <span>单位: 次数/天</span>
        </div>
        <BaseChart :option="lineChartOption" />
      </PanelSection>
    </div>

    <!-- Bottom Navigation -->
    <BottomNav :items="navItems" v-model:activeIndex="activeNavIndex" />
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import { HomeFilled } from '@element-plus/icons-vue'
import * as echarts from 'echarts'

import PanelSection from '@/components/homework/PanelSection.vue'
import SecurityStats from '@/components/homework/SecurityStats.vue'
import AlarmList, { type AlarmStatus } from '@/components/homework/AlarmList.vue'
import BlacklistCard from '@/components/homework/BlacklistCard.vue'
import BottomNav from '@/components/homework/BottomNav.vue'
import BaseChart from '@/components/homework/BaseChart.vue'

// --- Data ---
const overviewStats = reactive({
  totalPeople: 12530,
  blacklistCount: 25,
  ownerCount: 2318,
  visitorCount: 880,
  outsiderCount: 174,
})

const alarmData = ref([
  { name: '监控1: 大西门云台', time: '07:12:18', status: 'resolved' as AlarmStatus },
  { name: '监控2: 大西门云台', time: '07:12:18', status: 'pending' as AlarmStatus },
  { name: '监控3: 大西门云台', time: '07:12:18', status: 'processing' as AlarmStatus },
  { name: '监控4: 大西门云台', time: '07:12:18', status: 'resolved' as AlarmStatus },
  { name: '监控5: 大西门云台', time: '07:12:18', status: 'pending' as AlarmStatus },
  { name: '监控6: 大西门云台', time: '07:12:18', status: 'processing' as AlarmStatus },
  { name: '监控7: 大西门云台', time: '07:12:18', status: 'resolved' as AlarmStatus },
  { name: '监控8: 大西门云台', time: '07:12:18', status: 'pending' as AlarmStatus },
])

const navItems = ['社区管理', '安保监控', 'CIM平台', '能源检测', '节能分析']
const activeNavIndex = ref(2) // Default to 'CIM平台'

// --- Chart Options ---
const barChartOption = ref<Record<string, unknown>>({
  grid: { top: 10, right: 10, bottom: 20, left: 30 },
  xAxis: {
    type: 'category',
    data: ['6-27', '6-28', '6-29', '6-27', '6-27', '6-27', '6-27'],
    axisLabel: { color: '#888', fontSize: 10 },
  },
  yAxis: {
    type: 'value',
    splitLine: { lineStyle: { color: 'rgba(255,255,255,0.1)', type: 'dashed' } },
    axisLabel: { color: '#888', fontSize: 10 },
  },
  series: [
    {
      data: [150, 80, 200, 320, 400, 310, 350],
      type: 'bar',
      itemStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: '#00f2fe' },
          { offset: 1, color: '#4facfe' },
        ]),
      },
      barWidth: '60%',
    },
  ],
})

const pieChartOption = ref<Record<string, unknown>>({
  tooltip: { trigger: 'item' },
  legend: {
    orient: 'vertical',
    right: 10,
    top: 'center',
    textStyle: { color: '#ccc', fontSize: 10 },
    itemWidth: 10,
    itemHeight: 10,
  },
  series: [
    {
      name: '业主关怀',
      type: 'pie',
      radius: ['50%', '80%'],
      center: ['30%', '50%'],
      avoidLabelOverlap: false,
      label: { show: false },
      labelLine: { show: false },
      data: [
        { value: 1048, name: '长期空置', itemStyle: { color: '#5470c6' } },
        { value: 735, name: '长期未外出', itemStyle: { color: '#91cc75' } },
        { value: 580, name: '小孩独自出门超时', itemStyle: { color: '#fac858' } },
        { value: 484, name: '老人独自出门超时', itemStyle: { color: '#ee6666' } },
      ],
    },
  ],
})

const lineChartOption = ref<Record<string, unknown>>({
  grid: { top: 10, right: 10, bottom: 20, left: 30 },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: ['6-27', '6-27', '6-27', '6-27', '6-27', '6-27', '6-27', '6-27'],
    axisLabel: { color: '#888', fontSize: 10 },
  },
  yAxis: {
    type: 'value',
    splitLine: { lineStyle: { color: 'rgba(255,255,255,0.1)', type: 'dashed' } },
    axisLabel: { color: '#888', fontSize: 10 },
  },
  series: [
    {
      data: [10, 25, 45, 30, 80, 50, 40, 15],
      type: 'line',
      smooth: true,
      areaStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: 'rgba(238, 102, 102, 0.8)' },
          { offset: 1, color: 'rgba(238, 102, 102, 0.1)' },
        ]),
      },
      lineStyle: { color: '#ee6666' },
      itemStyle: { color: '#ee6666' },
    },
  ],
})
</script>

<style scoped>
.homework-container {
  width: 100vw;
  height: 100vh;
  position: relative;
  background-image: url('/main.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
}

.back-btn {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 100;
}

.panel {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 380px;
  background: linear-gradient(to right, rgba(0, 10, 30, 0.9), rgba(0, 10, 30, 0.4));
  padding: 60px 20px 20px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  z-index: 10;
}

.left-panel {
  left: 0;
}

.right-panel {
  right: 0;
  background: linear-gradient(to left, rgba(0, 10, 30, 0.9), rgba(0, 10, 30, 0.4));
}

.chart-section {
  flex: 1;
  min-height: 140px;
}

.chart-subtitle {
  font-size: 11px;
  color: #888;
  margin-bottom: 5px;
}

.flex-between {
  display: flex;
  justify-content: space-between;
}
</style>
