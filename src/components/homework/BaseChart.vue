<template>
  <div class="chart-container" ref="chartRef"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, shallowRef } from 'vue'
import * as echarts from 'echarts'

const props = defineProps<{
  option: Record<string, unknown>
}>()

const chartRef = ref<HTMLElement | null>(null)
const chartInstance = shallowRef<echarts.ECharts | null>(null)
const resizeObserver = ref<ResizeObserver | null>(null)

const initChart = () => {
  if (chartRef.value) {
    chartInstance.value = echarts.init(chartRef.value)
    chartInstance.value.setOption(props.option)
  }
}

watch(() => props.option, (newOption) => {
  if (chartInstance.value) {
    chartInstance.value.setOption(newOption)
  }
}, { deep: true })

onMounted(() => {
  initChart()

  if (chartRef.value) {
    resizeObserver.value = new ResizeObserver(() => {
      if (chartInstance.value) {
        chartInstance.value.resize()
      }
    })
    resizeObserver.value.observe(chartRef.value)
  }
})

onUnmounted(() => {
  if (resizeObserver.value) {
    resizeObserver.value.disconnect()
  }
  chartInstance.value?.dispose()
})
</script>

<style scoped>
.chart-container {
  width: 100%;
  flex: 1;
  min-height: 120px;
}
</style>
