<template>
  <div class="map-container" ref="mapContainer"></div>
</template>

<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue';
import * as maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

const mapContainer = ref<HTMLElement | null>(null);
let map: maplibregl.Map | null = null;

onMounted(() => {
  if (!mapContainer.value) return;

  map = new maplibregl.Map({
    container: mapContainer.value,
    style: 'https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json',
    center: [54.37, 24.47], // Abu Dhabi city center
    zoom: 15,
    pitch: 60, // Set initial pitch for 3D effect
    maxPitch: 85, // Allow high pitch for 3D
  });

  // Adjust scrollZoom damping
  map.scrollZoom.setWheelZoomRate(1 / 150); // slow down wheel zoom rate
  map.scrollZoom.setZoomRate(1 / 150); // slow down zoom rate

  map.on('load', () => {
    if (!map) return;

    // Add 3D buildings layer
    map.addSource('abudhabi_buildings', {
      type: 'geojson',
      data: '/abudhabi_city_buildings.geojson'
    });

    map.addLayer({
      'id': '3d-buildings',
      'source': 'abudhabi_buildings',
      'type': 'fill-extrusion',
      'paint': {
        'fill-extrusion-color': '#aaa',

        // Robust height calculation handling string, number, and missing values
        'fill-extrusion-height': [
          'case',
          ['has', 'height'], ['to-number', ['get', 'height']],
          ['has', 'elevation'], ['to-number', ['get', 'elevation']],
          ['has', 'building:levels'], ['*', ['to-number', ['get', 'building:levels']], 3], // fallback 3m per level
          10 // default fallback height
        ],

        // Optional: add opacity for a better look
        'fill-extrusion-opacity': 0.8
      }
    });
  });
});

onUnmounted(() => {
  if (map) {
    map.remove();
  }
});
</script>

<style scoped>
.map-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 0; /* Background layer */
}
</style>
