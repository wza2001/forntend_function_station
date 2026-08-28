<template>
  <div class="left-panel-content">
    <div class="panel-card">
      <div class="card-title"><span class="title-indicator"></span>Traffic Status</div>
      <div class="status-grid">
        <div class="status-item">
          <div class="status-label">Total Vehicles</div>
          <div class="status-value text-blue">1,234</div>
        </div>
        <div class="status-item">
          <div class="status-label">Active</div>
          <div class="status-value text-green">1,020</div>
        </div>
        <div class="status-item">
          <div class="status-label">Maintenance</div>
          <div class="status-value text-yellow">150</div>
        </div>
        <div class="status-item">
          <div class="status-label">Offline</div>
          <div class="status-value text-red">64</div>
        </div>
      </div>
    </div>

    <div class="panel-card flex-1">
      <div class="card-title"><span class="title-indicator"></span>Vehicle Activity Trend</div>
      <div class="chart-container">
        <v-chart class="chart" :option="lineOption" autoresize />
      </div>
    </div>

    <div class="panel-card flex-1">
      <div class="card-title"><span class="title-indicator"></span>Vehicle Types</div>
      <div class="chart-container">
        <v-chart class="chart" :option="pieOption" autoresize />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import VChart from 'vue-echarts'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { LineChart, PieChart } from 'echarts/charts'
import { GridComponent, TooltipComponent, TitleComponent, LegendComponent } from 'echarts/components'

use([CanvasRenderer, LineChart, PieChart, GridComponent, TooltipComponent, TitleComponent, LegendComponent])

const lineOption = ref<Record<string, unknown>>({
  tooltip: { trigger: 'axis' },
  grid: { top: 20, right: 10, bottom: 20, left: 30 },
  xAxis: {
    type: 'category',
    data: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
    axisLine: { lineStyle: { color: '#4a5568' } },
    axisLabel: { color: '#a0aec0', fontSize: 10 }
  },
  yAxis: {
    type: 'value',
    splitLine: { lineStyle: { color: '#2d3748' } },
    axisLabel: { color: '#a0aec0', fontSize: 10 }
  },
  series: [{
    data: [120, 70, 300, 440, 320, 210],
    type: 'line',
    smooth: true,
    symbol: 'circle',
    symbolSize: 6,
    itemStyle: { color: '#4299e1' },
    areaStyle: {
      color: {
        type: 'linear', x: 0, y: 0, x2: 0, y2: 1,
        colorStops: [{ offset: 0, color: 'rgba(66, 153, 225, 0.5)' }, { offset: 1, color: 'rgba(66, 153, 225, 0)' }]
      }
    }
  }]
})

const pieOption = ref<Record<string, unknown>>({
  tooltip: { trigger: 'item' },
  series: [{
    type: 'pie',
    radius: ['40%', '70%'],
    avoidLabelOverlap: false,
    label: { show: false },
    data: [
      { value: 1048, name: 'Type A', itemStyle: { color: '#4299e1' } },
      { value: 735, name: 'Type B', itemStyle: { color: '#48bb78' } },
      { value: 580, name: 'Type C', itemStyle: { color: '#ecc94b' } },
      { value: 484, name: 'Type D', itemStyle: { color: '#f56565' } }
    ]
  }]
})
</script>

<style scoped>
.left-panel-content {
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

.status-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.status-item {
  background: rgba(30, 41, 59, 0.6);
  border-radius: 6px;
  padding: 12px;
  text-align: center;
}

.status-label {
  color: #94a3b8;
  font-size: 12px;
  margin-bottom: 4px;
}

.status-value {
  font-size: 18px;
  font-weight: bold;
}

.text-blue { color: #60a5fa; }
.text-green { color: #4ade80; }
.text-yellow { color: #facc15; }
.text-red { color: #f87171; }

.chart-container {
  flex: 1;
  width: 100%;
  position: relative;
}

.chart {
  width: 100%;
  height: 100%;
}
</style>
