<template>
  <div class="homework-container">
    <header class="header">
      <div class="header-title">
        <img src="/img/titleImg.png" alt="icon" class="header-icon" />
        <span>XXX数据监控</span>
      </div>
    </header>
    <div class="main-content">
      <div class="left-panel">
        <PanelSection title="安全总览">
          <SecurityStats :stats="overviewStats" />
        </PanelSection>
        <PanelSection title="今日报警" flex>
          <AlarmList :alarms="alarmData" />
        </PanelSection>
      </div>
      <div class="right-panel">
        <PanelSection title="黑名单卡片">
          <BlacklistCard name="张三" idNumber="1234567890" :similarity="98" />
        </PanelSection>
        <PanelSection title="超时访客数据" class="chart-section">
          <BaseChart :option="barChartOption" />
        </PanelSection>
        <PanelSection title="业主关怀" class="chart-section">
          <BaseChart :option="pieChartOption" />
        </PanelSection>
        <PanelSection title="安全趋势" class="chart-section">
          <BaseChart :option="lineChartOption" />
        </PanelSection>
      </div>
    </div>

    <BottomNav :items="navItems" v-model:activeIndex="activeNavIndex" />
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
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
  outsiderCount: 174
})

const alarmData = ref([
  { name: '监控1: 大西门云台', time: '07:12:18', status: 'resolved' as AlarmStatus },
  { name: '监控2: 大西门云台', time: '07:12:18', status: 'pending' as AlarmStatus },
  { name: '监控3: 大西门云台', time: '07:12:18', status: 'processing' as AlarmStatus },
  { name: '监控4: 大西门云台', time: '07:12:18', status: 'resolved' as AlarmStatus },
  { name: '监控5: 大西门云台', time: '07:12:18', status: 'pending' as AlarmStatus },
  { name: '监控6: 大西门云台', time: '07:12:18', status: 'processing' as AlarmStatus },
  { name: '监控7: 大西门云台', time: '07:12:18', status: 'resolved' as AlarmStatus },
  { name: '监控8: 大西门云台', time: '07:12:18', status: 'pending' as AlarmStatus }
])

const navItems = ['社区管理', '安保监控', 'CIM平台', '能源检测', '节能分析']
const activeNavIndex = ref(2) // Default to 'CIM平台'

// --- Chart Options ---
const barChartOption = ref<Record<string, unknown>>({
  grid: { top: 20, right: 10, bottom: 20, left: 30 },
  tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
  xAxis: {
    type: 'category',
    data: ['6-27', '6-28', '6-29', '6-30', '7-01', '7-02', '7-03'],
    axisLabel: { color: '#00f6ff', fontSize: 10 },
    axisLine: { lineStyle: { color: 'rgba(0, 246, 255, 0.3)' } }
  },
  yAxis: {
    type: 'value',
    splitLine: { lineStyle: { color: 'rgba(0, 246, 255, 0.1)', type: 'dashed' } },
    axisLabel: { color: '#00f6ff', fontSize: 10 }
  },
  series: [
    {
      data: [150, 80, 200, 320, 400, 310, 350],
      type: 'bar',
      itemStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: '#00f6ff' },
          { offset: 1, color: 'rgba(0, 246, 255, 0.1)' }
        ]),
        borderRadius: [2, 2, 0, 0]
      },
      barWidth: '40%'
    }
  ]
})

const pieChartOption = ref<Record<string, unknown>>({
  tooltip: { trigger: 'item' },
  legend: {
    orient: 'vertical',
    right: 10,
    top: 'center',
    textStyle: { color: '#00f6ff', fontSize: 12 },
    itemWidth: 10,
    itemHeight: 10,
    icon: 'circle'
  },
  series: [
    {
      name: '人员类型',
      type: 'pie',
      radius: ['40%', '70%'],
      center: ['35%', '50%'],
      avoidLabelOverlap: false,
      itemStyle: {
        borderColor: '#001428',
        borderWidth: 2
      },
      label: { show: false },
      labelLine: { show: false },
      data: [
        { value: 1048, name: '长期空置', itemStyle: { color: '#00f6ff' } },
        { value: 735, name: '长期未外出', itemStyle: { color: '#ffeb3b' } },
        { value: 580, name: '小孩独自出门', itemStyle: { color: '#4caf50' } },
        { value: 484, name: '老人独自出门', itemStyle: { color: '#ff4d4f' } }
      ]
    }
  ]
})

const lineChartOption = ref<Record<string, unknown>>({
  grid: { top: 20, right: 10, bottom: 20, left: 30 },
  tooltip: { trigger: 'axis' },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: ['6-27', '6-28', '6-29', '6-30', '7-01', '7-02', '7-03', '7-04'],
    axisLabel: { color: '#00f6ff', fontSize: 10 },
    axisLine: { lineStyle: { color: 'rgba(0, 246, 255, 0.3)' } }
  },
  yAxis: {
    type: 'value',
    splitLine: { lineStyle: { color: 'rgba(0, 246, 255, 0.1)', type: 'dashed' } },
    axisLabel: { color: '#00f6ff', fontSize: 10 }
  },
  series: [
    {
      data: [10, 25, 45, 30, 80, 50, 40, 15],
      type: 'line',
      smooth: true,
      areaStyle: {
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          { offset: 0, color: 'rgba(0, 246, 255, 0.5)' },
          { offset: 1, color: 'rgba(0, 246, 255, 0)' }
        ])
      },
      lineStyle: { color: '#00f6ff', width: 2 },
      itemStyle: { color: '#00f6ff', borderWidth: 2, borderColor: '#fff' }
    }
  ]
})
</script>

<style scoped>
.homework-container {
  width: 100vw;
  height: 100vh;
  background-image: url('/main.jpg');
  background-size: cover;
  background-position: center;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  color: #fff;
}

.header {
  height: 80px;
  background-image: url('/img/title.png');
  background-size: 100% 100%;
  background-repeat: no-repeat;
  background-position: center top;
  display: flex;
  justify-content: center;
  align-items: flex-start;
  position: relative;
  z-index: 10;
}

.header-title {
  display: flex;
  align-items: center;
  margin-top: 15px;
  font-size: 24px;
  font-weight: bold;
  color: #00f6ff;
  letter-spacing: 2px;
  text-shadow: 0 0 10px rgba(0, 246, 255, 0.5);
}

.header-icon {
  width: 28px;
  height: 28px;
  margin-right: 10px;
}

.main-content {
  flex: 1;
  display: flex;
  justify-content: space-between;
  padding: 20px;
  padding-top: 10px;
  pointer-events: none;
}

.left-panel, .right-panel {
  width: 420px;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 15px;
  pointer-events: auto;
  background: rgba(0, 11, 26, 0.6);
  border: 1px solid rgba(0, 246, 255, 0.2);
  box-shadow: inset 0 0 20px rgba(0, 246, 255, 0.1);
  padding: 15px;
  box-sizing: border-box;
}

.chart-section {
  flex: 1;
  min-height: 120px;
}
</style>
