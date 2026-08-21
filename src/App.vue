<template>
  <div class="first_parts">
    <div class="card">
      <spatialchart :chart-option="pieOption" />
    </div>
    <div class="card">
      <spatialchart :chart-option="barOption" />
    </div>
  </div>
  <div class="LandUse">


  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import spatialchart from './components/spatialchart.vue';

const barOption = ref({
  title: { text: '区域建筑高度分布', textStyle: { color: '#fff', fontSize: 14 } },
  tooltip: { trigger: 'axis' },
  grid: { left: '3%', right: '4%', bottom: '3%', containLabel: true },
  xAxis: {
    type: 'category',
    data: ['0-10m', '10-30m', '30-50m', '50-100m', '>100m'],
    axisLabel: { color: '#ccc' }
  },
  yAxis: { type: 'value', axisLabel: { color: '#ccc' } },
  series: [
    {
      data: [120, 200, 150, 80, 40],
      type: 'bar',
      itemStyle: { color: '#3b82f6', borderRadius: [4, 4, 0, 0] }
    }
  ]
});

const pieOption = ref({
  title: { text: '空域/用地类型占比', textStyle: { color: '#fff', fontSize: 14 } },
  tooltip: { trigger: 'item' },
  legend: { bottom: '0', textStyle: { color: '#ccc' } },
  series: [
    {
      name: '用地类型',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      itemStyle: { borderRadius: 6, borderColor: '#1e1e1e', borderWidth: 2 },
      label: { show: false },
      data: [
        { value: 1048, name: '住宅区' },
        { value: 735, name: '商业区' },
        { value: 580, name: '绿地与公园' },
        { value: 300, name: '禁飞管控区' }
      ]
    }
  ]
});
</script>

<style scoped>
.first_parts {
  position: absolute;  /* 绝对定位，脱离文档流浮在底层上 */
  top: 20px;           /* 距离顶部 20px */
  left: 20px;          /* 距离左侧 20px（若放右侧改成 right: 20px） */
  width: 320px;        /* 固定面板宽度 */
  z-index: 10;         /* 确保层级高于背景地图 */

  display: flex;
  flex-direction: column; /* 垂直从上到下排列 */
  gap: 16px;
}
.card {
  background: rgba(30, 30, 30, 0.85);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 12px;
}
</style>
