<template>
  <div class="dashboard-root">
    <div class="back-button-container">
      <el-button type="info" :icon="HomeFilled" circle @click="router.push('/')" />
    </div>

    <ViewMap ref="viewMapRef" geojson-url="/abudhabi_city_buildings.geojson" />

    <div class="panel left-panel">
      <div class="card"><SpatialChart :chart-option="barOption1" /></div>
      <div class="card"><SpatialChart :chart-option="pieOption1" /></div>
      <div class="card"><SpatialChart :chart-option="lineOption1" /></div>
    </div>

    <div class="panel right-panel">
      <div class="card"><SpatialChart :chart-option="barOption2" /></div>
      <div class="card"><SpatialChart :chart-option="lineOption2" /></div>
    </div>

    <MapControls @preset-clicked="handlePresetClick" @mode-changed="handleModeChange" />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { HomeFilled } from '@element-plus/icons-vue';
import ViewMap from '@/components/ViewMap.vue';
import SpatialChart from '@/components/SpatialChart.vue';
import MapControls from '@/components/MapControls.vue';

const router = useRouter();
const viewMapRef = ref<InstanceType<typeof ViewMap> | null>(null);

const handlePresetClick = (preset: 'downtown' | 'overview') => {
  if (!viewMapRef.value) return;
  if (preset === 'downtown') {
    viewMapRef.value.flyTo({ center: [54.363, 24.496], zoom: 15, pitch: 60, bearing: -17.6, duration: 2000 });
  } else {
    viewMapRef.value.flyTo({ center: [54.36, 24.48], zoom: 12, pitch: 0, bearing: 0, duration: 2000 });
  }
};

const handleModeChange = (is3D: boolean) => {
  if (viewMapRef.value) viewMapRef.value.setViewMode(is3D);
};

const barOption1 = ref<Record<string, unknown>>({
  title: { text: 'Test 3 - Chart A', textStyle: { color: '#fff' } },
  xAxis: { type: 'category', data: ['A', 'B', 'C', 'D'] },
  yAxis: { type: 'value' },
  series: [{ data: [10, 20, 15, 30], type: 'bar', itemStyle: { color: '#3b82f6' } }]
});
const pieOption1 = ref<Record<string, unknown>>({
  title: { text: 'Test 3 - Chart B', textStyle: { color: '#fff' } },
  series: [{ type: 'pie', radius: '50%', data: [{ value: 10, name: 'X' }, { value: 20, name: 'Y' }] }]
});
const lineOption1 = ref<Record<string, unknown>>({
  title: { text: 'Test 3 - Chart C', textStyle: { color: '#fff' } },
  xAxis: { type: 'category', data: ['Mon', 'Tue', 'Wed'] },
  yAxis: { type: 'value' },
  series: [{ data: [150, 230, 224], type: 'line', itemStyle: { color: '#10b981' } }]
});
const barOption2 = ref<Record<string, unknown>>({
  title: { text: 'Test 3 - Chart D', textStyle: { color: '#fff' } },
  xAxis: { type: 'value' },
  yAxis: { type: 'category', data: ['Val1', 'Val2'] },
  series: [{ data: [100, 200], type: 'bar', itemStyle: { color: '#f59e0b' } }]
});
const lineOption2 = ref<Record<string, unknown>>({
  title: { text: 'Test 3 - Chart E', textStyle: { color: '#fff' } },
  xAxis: { type: 'category', data: ['Q1', 'Q2', 'Q3'] },
  yAxis: { type: 'value' },
  series: [{ data: [12, 34, 11], type: 'line', itemStyle: { color: '#ef4444' } }]
});
</script>

<style scoped>
.dashboard-root {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: #000;
}
.back-button-container {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 15;
}
.panel {
  position: absolute;
  top: 70px;
  width: 320px;
  z-index: 10;
  display: flex;
  flex-direction: column;
  gap: 16px;
  bottom: 20px;
  overflow-y: auto;
}
.left-panel {
  left: 20px;
}
.right-panel {
  right: 20px;
}
.card {
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}
</style>
