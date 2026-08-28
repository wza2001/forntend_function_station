<template>
  <div class="right-panel-content">
    <div class="panel-card flex-1">
      <div class="card-title"><span class="title-indicator"></span>Alert Monitoring</div>
      <el-table :data="tableData" style="width: 100%; background: transparent;" :row-style="{background: 'transparent', color: '#e2e8f0', borderBottom: '1px solid #334155'}" :header-cell-style="{background: 'transparent', color: '#94a3b8', borderBottom: '1px solid #334155'}">
        <el-table-column prop="time" label="Time" width="80" />
        <el-table-column prop="location" label="Location" />
        <el-table-column prop="level" label="Level" width="80">
          <template #default="{ row }">
            <span :class="['level-badge', row.level.toLowerCase()]">{{ row.level }}</span>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <div class="panel-card flex-1">
      <div class="card-title"><span class="title-indicator"></span>Daily Alert Stats</div>
      <div class="chart-container">
        <v-chart class="chart" :option="barOption" autoresize />
      </div>
    </div>

    <div class="panel-card">
      <div class="card-title"><span class="title-indicator"></span>System Status</div>
      <div class="sys-status">
        <div class="sys-item">
          <div class="sys-label"><span>CPU Usage</span> <span>65%</span></div>
          <el-progress :percentage="65" :show-text="false" color="#4299e1" :stroke-width="8" />
        </div>
        <div class="sys-item">
          <div class="sys-label"><span>Memory Usage</span> <span>80%</span></div>
          <el-progress :percentage="80" :show-text="false" color="#f6ad55" :stroke-width="8" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import VChart from 'vue-echarts'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { BarChart } from 'echarts/charts'
import { GridComponent, TooltipComponent } from 'echarts/components'

use([CanvasRenderer, BarChart, GridComponent, TooltipComponent])

const tableData = ref([
  { time: '10:24', location: 'Main St & 1st Ave', level: 'High' },
  { time: '10:15', location: 'Highway 61', level: 'Medium' },
  { time: '09:40', location: 'North Bridge', level: 'Low' },
  { time: '08:55', location: 'Airport Road', level: 'High' }
])

const barOption = ref<Record<string, unknown>>({
  tooltip: { trigger: 'axis', axisPointer: { type: 'shadow' } },
  grid: { top: 20, right: 10, bottom: 20, left: 30 },
  xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    axisLine: { lineStyle: { color: '#4a5568' } },
    axisLabel: { color: '#a0aec0', fontSize: 10 }
  },
  yAxis: {
    type: 'value',
    splitLine: { lineStyle: { color: '#2d3748' } },
    axisLabel: { color: '#a0aec0', fontSize: 10 }
  },
  series: [{
    data: [12, 19, 15, 25, 22, 30, 28],
    type: 'bar',
    barWidth: '40%',
    itemStyle: {
      color: {
        type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
        colorStops: [{ offset: 0, color: '#fc8181' }, { offset: 1, color: '#742a2a' }]
      },
      borderRadius: [4, 4, 0, 0]
    }
  }]
})
</script>

<style scoped>
.right-panel-content {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.panel-card {
  background: rgba(15, 23, 42, 0.85);
  border: 1px solid rgba(51, 65, 85, 0.6);
  border-radius: 8px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  backdrop-filter: blur(8px);
}

.flex-1 { flex: 1; min-height: 250px; }

.card-title {
  color: #e2e8f0;
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 16px;
  display: flex;
  align-items: center;
}

.title-indicator {
  width: 3px;
  height: 14px;
  background: #3b82f6;
  margin-right: 8px;
  border-radius: 2px;
}

:deep(.el-table) {
  --el-table-border-color: #334155;
  --el-table-bg-color: transparent;
  --el-table-tr-bg-color: transparent;
  --el-table-header-bg-color: transparent;
}
:deep(.el-table__inner-wrapper::before) { display: none; }
:deep(.el-table td.el-table__cell), :deep(.el-table th.el-table__cell.is-leaf) {
  border-bottom: 1px solid #334155;
}
:deep(.el-table--enable-row-hover .el-table__body tr:hover > td.el-table__cell) {
  background-color: rgba(255, 255, 255, 0.05);
}

.level-badge {
  font-size: 11px;
  padding: 2px 6px;
  border-radius: 4px;
}
.level-badge.high { background: rgba(239, 68, 68, 0.2); color: #fca5a5; }
.level-badge.medium { background: rgba(245, 158, 11, 0.2); color: #fcd34d; }
.level-badge.low { background: rgba(16, 185, 129, 0.2); color: #6ee7b7; }

.chart-container {
  flex: 1;
  width: 100%;
  position: relative;
}
.chart { width: 100%; height: 100%; }

.sys-status { display: flex; flex-direction: column; gap: 12px; }
.sys-item { display: flex; flex-direction: column; gap: 4px; }
.sys-label { display: flex; justify-content: space-between; font-size: 12px; color: #cbd5e1; }
:deep(.el-progress-bar__outer) { background-color: rgba(255,255,255,0.1); }
</style>
