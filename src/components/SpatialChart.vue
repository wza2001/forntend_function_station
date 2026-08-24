<template>
  <div class="wrapper_chart">
    <v-chart class="chart" :option="chartOption" autoresize />
  </div>
</template>

<script setup lang="ts">
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { PieChart, BarChart } from 'echarts/charts';
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
} from 'echarts/components';
import VChart from 'vue-echarts';

use([
  CanvasRenderer,
  PieChart,
  BarChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
]);

defineProps<{
  chartOption: Record<string, unknown>;
}>();
</script>

<style scoped>
.wrapper_chart {
  width: 100%;
  height: 320px;
}
.chart {
  width: 100%;
  height: 100%;
}
</style>
