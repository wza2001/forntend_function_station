<template>
  <div ref="mapContainer" class="map-view-container"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { Map } from 'maplibre-gl'
import * as maplibregl from 'maplibre-gl'
import 'maplibre-gl/dist/maplibre-gl.css'

const props = withDefaults(
  defineProps<{
    geojsonUrl?: string
  }>(),
  {
    geojsonUrl: '/abudhabi_city_buildings.geojson',
  },
)

const mapContainer = ref<HTMLElement | null>(null)
let mapInstance: Map | null = null

onMounted(() => {
  if (!mapContainer.value) return

  try {
    mapInstance = new Map({
      container: mapContainer.value,
      style: 'https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json',
      center: [54.363, 24.496],
      zoom: 14.5, // 推荐拉近到 14.5~15（13.5 略远，建筑细节不易看清）
      pitch: 60, // 初始倾斜 55°~65°，3D 立体感更强
      bearing: -17.6,
      maxPitch: 85, // 解锁大角度俯仰限制
      antialias: true, // 开启抗锯齿，提升 3D 白模边缘质感
    } as unknown as maplibregl.MapOptions)
    ;(window as unknown as { map: maplibregl.Map }).map = mapInstance

    // 调整滚轮缩放阻尼（使缩放更平滑稳定）
    mapInstance.scrollZoom.setWheelZoomRate(1 / 450)

    mapInstance.on('load', () => {
      if (!mapInstance) return

      // 1. 加载 GeoJSON 建筑数据源
      mapInstance.addSource('buildings-source', {
        type: 'geojson',
        data: props.geojsonUrl,
      })

      // 2. 渲染 3D 建筑白模拉伸图层
      mapInstance.addLayer({
        id: 'buildings-3d',
        type: 'fill-extrusion',
        source: 'buildings-source',
        paint: {
          // 2. 基于高度动态渐变颜色
          'fill-extrusion-color': [
            'interpolate',
            ['linear'], // 线性插值
            ['coalesce', ['get', 'height'], 25], // 渐变依据的属性（高度）
            0,
            '#1e3a8a', // 0m - 15m: 深海军蓝（低矮裙楼、平房）
            30,
            '#2563eb', // 30m: 科技蓝（多层住宅）
            60,
            '#06b6d4', // 60m: 青绿色/青色（中高层）
            100,
            '#38bdf8', // 100m: 亮天蓝（高层办公楼）
            180,
            '#f59e0b', // 180m+: 琥珀金/亮橙（地标/超高层建筑）
            250,
            '#ef4444', // 250m+: 警示红（极高建筑/空域危险源）
          ],

          'fill-extrusion-opacity': 0.85,
        },
      })
    })

    mapInstance.on('error', (e) => {
      console.warn('MapLibre 底图事件警告:', e)
    })
  } catch (err) {
    console.error('地图初始化失败:', err)
  }
})

// Expose methods for parent components
const flyTo = (options: maplibregl.FlyToOptions) => {
  if (mapInstance) {
    mapInstance.flyTo(options)
  }
}

const setViewMode = (is3D: boolean) => {
  if (!mapInstance) return

  if (is3D) {
    mapInstance.easeTo({
      pitch: 60,
      bearing: -17.6,
      duration: 1000,
    })
  } else {
    mapInstance.easeTo({
      pitch: 0,
      bearing: 0,
      duration: 1000,
    })
  }
}

defineExpose({
  flyTo,
  setViewMode,
})

onUnmounted(() => {
  mapInstance?.remove()
})
</script>

<style scoped>
.map-view-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 0;
}
</style>

// [Sync Test] MapLibre pipeline verified.
