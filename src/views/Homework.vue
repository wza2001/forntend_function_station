<script setup lang="ts">
import ViewMap from "@/components/ViewMap.vue";
import SpatialChart from "@/components/SpatialChart.vue";
</script>
<template>
    <div class="Page Root">

      <div class="first_parts">
        <div class="card">
          <SpatialChart :chart-option="pieOption" />
        </div>
        <div class="card">
          <SpatialChart :chart-option="barOption" />
      </div>
    </div>
</template>
