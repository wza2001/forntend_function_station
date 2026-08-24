<template>
  <div class="homework-container">
    <router-link to="/" class="back-btn">
      <el-button type="primary" circle>
        <el-icon><HomeFilled /></el-icon>
      </el-button>
    </router-link>

    <!-- Header area (optional, there's some text in top corners in the original but we can skip or add mock text) -->

    <!-- Left Panel -->
    <div class="panel left-panel">
      <!-- Section 1: Security Overview -->
      <div class="panel-section">
        <div class="section-title">
          <span class="title-icon">||</span> 安防概况
        </div>
        <div class="security-overview">
          <div class="overview-top">
            <el-icon class="overview-icon" color="#409eff" :size="40"><DataBoard /></el-icon>
            <div class="stat-item">
              <div class="stat-label">当前社区总人数</div>
              <div class="stat-value highlight">12530</div>
            </div>
            <div class="stat-item">
              <div class="stat-label">黑名单</div>
              <div class="stat-value">25</div>
            </div>
          </div>
          <div class="overview-bottom">
            <div class="stat-sub">
              <div class="sub-label bg-cyan">业主人数</div>
              <div class="sub-value">2318</div>
            </div>
            <div class="stat-sub">
              <div class="sub-label bg-purple">访客人数</div>
              <div class="sub-value">880</div>
            </div>
            <div class="stat-sub">
              <div class="sub-label bg-blue">外来人数</div>
              <div class="sub-value">174</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Section 2: Alarm Messages -->
      <div class="panel-section flex-1">
        <div class="section-title">
          <span class="title-icon">||</span> 报警讯息列表
        </div>
        <div class="alarm-list">
          <div class="alarm-item" v-for="i in 8" :key="i">
            <div class="alarm-info">
              <div class="alarm-name">监控{{i}}: 大西门云台</div>
              <div class="alarm-time">07:12:18</div>
            </div>
            <el-tag :type="i % 3 === 0 ? 'success' : (i % 3 === 1 ? 'warning' : 'info')" size="small">
              {{ i % 3 === 0 ? '已消警' : (i % 3 === 1 ? '待派遣' : '处理中') }}
            </el-tag>
          </div>
        </div>
      </div>
    </div>

    <!-- Right Panel -->
    <div class="panel right-panel">
      <!-- Section 1: Blacklist -->
      <div class="panel-section">
        <div class="section-title">
          <span class="title-icon">||</span> 黑名单数据
        </div>
        <div class="blacklist-stats">
          <el-icon color="#67c23a" :size="40"><UserFilled /></el-icon>
          <div class="stat-text">近一月出现黑名单次数</div>
          <div class="stat-value-large">754</div>
        </div>
      </div>

      <!-- Section 2: Overdue Visitors (Bar Chart) -->
      <div class="panel-section chart-section">
        <div class="section-title">
          <span class="title-icon">||</span> 超时访客数据
        </div>
        <div class="chart-subtitle">近一周访客超时楼栋分布</div>
        <div class="chart-container" ref="barChartRef"></div>
      </div>

      <!-- Section 3: Owner Care (Donut Chart) -->
      <div class="panel-section chart-section">
        <div class="section-title">
          <span class="title-icon">||</span> 业主关怀
        </div>
        <div class="chart-container" ref="pieChartRef"></div>
      </div>

      <!-- Section 4: Alarm Data (Line Chart) -->
      <div class="panel-section chart-section">
        <div class="section-title">
          <span class="title-icon">||</span> 报警数据
        </div>
        <div class="chart-subtitle flex-between">
          <span>近一月报警次数</span>
          <span>单位: 次数/天</span>
        </div>
        <div class="chart-container" ref="lineChartRef"></div>
      </div>
    </div>

    <!-- Bottom Navigation -->
    <div class="bottom-nav">
      <div class="nav-item">社区管理</div>
      <div class="nav-item">安保监控</div>
      <div class="nav-item active">CIM平台</div>
      <div class="nav-item">能源检测</div>
      <div class="nav-item">节能分析</div>
    </div>

  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, shallowRef } from 'vue'
import { HomeFilled, DataBoard, UserFilled } from '@element-plus/icons-vue'
import * as echarts from 'echarts'

const barChartRef = ref<HTMLElement | null>(null)
const pieChartRef = ref<HTMLElement | null>(null)
const lineChartRef = ref<HTMLElement | null>(null)

const barChart = shallowRef<echarts.ECharts | null>(null)
const pieChart = shallowRef<echarts.ECharts | null>(null)
const lineChart = shallowRef<echarts.ECharts | null>(null)

const initCharts = () => {
  // Bar Chart
  if (barChartRef.value) {
    barChart.value = echarts.init(barChartRef.value)
    barChart.value.setOption({
      grid: { top: 10, right: 10, bottom: 20, left: 30 },
      xAxis: {
        type: 'category',
        data: ['6-27', '6-28', '6-29', '6-27', '6-27', '6-27', '6-27'],
        axisLabel: { color: '#888', fontSize: 10 }
      },
      yAxis: {
        type: 'value',
        splitLine: { lineStyle: { color: 'rgba(255,255,255,0.1)', type: 'dashed' } },
        axisLabel: { color: '#888', fontSize: 10 }
      },
      series: [
        {
          data: [150, 80, 200, 320, 400, 310, 350],
          type: 'bar',
          itemStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              { offset: 0, color: '#00f2fe' },
              { offset: 1, color: '#4facfe' }
            ])
          },
          barWidth: '60%'
        }
      ]
    })
  }

  // Pie Chart
  if (pieChartRef.value) {
    pieChart.value = echarts.init(pieChartRef.value)
    pieChart.value.setOption({
      tooltip: { trigger: 'item' },
      legend: {
        orient: 'vertical',
        right: 10,
        top: 'center',
        textStyle: { color: '#ccc', fontSize: 10 },
        itemWidth: 10,
        itemHeight: 10
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
            { value: 484, name: '老人独自出门超时', itemStyle: { color: '#ee6666' } }
          ]
        }
      ]
    })
  }

  // Line Chart
  if (lineChartRef.value) {
    lineChart.value = echarts.init(lineChartRef.value)
    lineChart.value.setOption({
      grid: { top: 10, right: 10, bottom: 20, left: 30 },
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['6-27', '6-27', '6-27', '6-27', '6-27', '6-27', '6-27', '6-27'],
        axisLabel: { color: '#888', fontSize: 10 }
      },
      yAxis: {
        type: 'value',
        splitLine: { lineStyle: { color: 'rgba(255,255,255,0.1)', type: 'dashed' } },
        axisLabel: { color: '#888', fontSize: 10 }
      },
      series: [
        {
          data: [10, 25, 45, 30, 80, 50, 40, 15],
          type: 'line',
          smooth: true,
          areaStyle: {
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
              { offset: 0, color: 'rgba(238, 102, 102, 0.8)' },
              { offset: 1, color: 'rgba(238, 102, 102, 0.1)' }
            ])
          },
          lineStyle: { color: '#ee6666' },
          itemStyle: { color: '#ee6666' }
        }
      ]
    })
  }
}

const handleResize = () => {
  barChart.value?.resize()
  pieChart.value?.resize()
  lineChart.value?.resize()
}

onMounted(() => {
  initCharts()
  window.addEventListener('resize', handleResize)
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
  barChart.value?.dispose()
  pieChart.value?.dispose()
  lineChart.value?.dispose()
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
  overflow: hidden;
  color: #fff;
  font-family: sans-serif;
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

.panel-section {
  display: flex;
  flex-direction: column;
}

.flex-1 {
  flex: 1;
  min-height: 0;
}

.section-title {
  font-size: 16px;
  font-weight: bold;
  color: #fff;
  margin-bottom: 15px;
  display: flex;
  align-items: center;
}

.title-icon {
  color: #409eff;
  margin-right: 8px;
  font-weight: bold;
}

/* Security Overview */
.security-overview {
  background: rgba(255, 255, 255, 0.05);
  padding: 15px;
  border: 1px solid rgba(64, 158, 255, 0.2);
}

.overview-top {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}

.stat-item {
  display: flex;
  flex-direction: column;
}

.stat-label {
  font-size: 12px;
  color: #ccc;
  margin-bottom: 5px;
}

.stat-value {
  font-size: 18px;
  font-weight: bold;
}

.stat-value.highlight {
  font-size: 24px;
  color: #409eff;
}

.overview-bottom {
  display: flex;
  justify-content: space-between;
}

.stat-sub {
  text-align: center;
}

.sub-label {
  font-size: 12px;
  padding: 2px 8px;
  border-radius: 2px;
  margin-bottom: 5px;
  color: #fff;
}

.bg-cyan { background: #00bcd4; }
.bg-purple { background: #9c27b0; }
.bg-blue { background: #2196f3; }

.sub-value {
  font-size: 14px;
  font-weight: bold;
}

/* Alarm List */
.alarm-list {
  flex: 1;
  overflow-y: auto;
  padding-right: 5px;
}

.alarm-list::-webkit-scrollbar {
  width: 4px;
}
.alarm-list::-webkit-scrollbar-thumb {
  background: rgba(64, 158, 255, 0.5);
  border-radius: 2px;
}

.alarm-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background: rgba(255, 255, 255, 0.05);
  margin-bottom: 8px;
  border-left: 3px solid #409eff;
}

.alarm-name {
  font-size: 13px;
  margin-bottom: 4px;
}

.alarm-time {
  font-size: 11px;
  color: #888;
}

/* Blacklist */
.blacklist-stats {
  display: flex;
  align-items: center;
  gap: 15px;
  background: rgba(255, 255, 255, 0.05);
  padding: 15px;
}

.stat-text {
  font-size: 13px;
  color: #ccc;
}

.stat-value-large {
  font-size: 28px;
  color: #00bcd4;
  font-weight: bold;
  margin-left: auto;
}

/* Charts */
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

.chart-container {
  width: 100%;
  flex: 1;
  min-height: 120px;
}

/* Bottom Nav */
.bottom-nav {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 15px;
  background: rgba(0, 20, 50, 0.6);
  padding: 10px 20px;
  border-radius: 4px;
  border: 1px solid rgba(64, 158, 255, 0.3);
  z-index: 10;
}

.nav-item {
  padding: 8px 16px;
  font-size: 14px;
  color: #ccc;
  cursor: pointer;
  border: 1px solid transparent;
  transition: all 0.3s;
}

.nav-item:hover {
  color: #fff;
  border-color: rgba(64, 158, 255, 0.5);
}

.nav-item.active {
  color: #fff;
  background: rgba(64, 158, 255, 0.2);
  border-color: #409eff;
}
</style>
