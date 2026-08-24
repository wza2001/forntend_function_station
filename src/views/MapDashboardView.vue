<template>
  <div class="dashboard-root">
    <!-- 0. 返回主页按钮 -->
    <div class="back-button-container">
      <el-button type="info" :icon="HomeFilled" circle @click="router.push('/')" />
    </div>

    <!-- 1. 全屏底层地图 -->
    <ViewMap ref="viewMapRef" geojson-url="/abudhabi_city_buildings.geojson" />

    <!-- 2. 左侧悬浮图表面板 -->
    <div class="first_parts">
      <div class="card">
        <SpatialChart :chart-option="pieOption" />
      </div>
      <div class="card">
        <SpatialChart :chart-option="barOption" />
      </div>
    </div>

    <!-- 3. 地图控制面板 -->
    <MapControls @preset-clicked="handlePresetClick" @mode-changed="handleModeChange" />

    <!-- 4. 数据面板 -->
    <DataPanel />

    <!-- 5. 其他功能区占位（如用地分析） -->
    <div class="land-use"></div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { HomeFilled } from '@element-plus/icons-vue';
import ViewMap from '@/components/ViewMap.vue';
import SpatialChart from '@/components/SpatialChart.vue';
import MapControls from '@/components/MapControls.vue';
import DataPanel from '@/components/DataPanel.vue';

const router = useRouter();

const viewMapRef = ref<InstanceType<typeof ViewMap> | null>(null);

const handlePresetClick = (preset: 'downtown' | 'overview') => {
  if (!viewMapRef.value) return;

  if (preset === 'downtown') {
    viewMapRef.value.flyTo({
      center: [54.363, 24.496],
      zoom: 15,
      pitch: 60,
      bearing: -17.6,
      duration: 2000
    });
  } else if (preset === 'overview') {
    viewMapRef.value.flyTo({
      center: [54.36, 24.48],
      zoom: 12,
      pitch: 0,
      bearing: 0,
      duration: 2000
    });
  }
};

const handleModeChange = (is3D: boolean) => {
  if (viewMapRef.value) {
    viewMapRef.value.setViewMode(is3D);
  }
};

const barOption = ref<Record<string, unknown>>({
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

const pieOption = ref<Record<string, unknown>>({
  title: { text: '空域/用地类型占比', textStyle: { color: '#fff', fontSize: 14 } },
  tooltip: { trigger: 'item' },
  legend: { bottom: 0, textStyle: { color: '#ccc' } },
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
.dashboard-root {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}

.back-button-container {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 15;
  pointer-events: auto;
}

.first_parts {
  position: absolute;
  top: 70px;
  left: 20px;
  width: 320px;
  z-index: 10;
  display: flex;
  flex-direction: column;
  gap: 16px;
  pointer-events: auto;
}

.card {
  background: rgba(30, 30, 30, 0.85);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}
</style>
