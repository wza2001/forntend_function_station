<template>
  <div class="panel-section" :class="{ 'flex-1': flex }">
    <div class="section-title"><span class="title-icon">||</span> {{ title }}</div>
    <slot></slot>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  title: string
  flex?: boolean
}>()
</script>

<style scoped>
.panel-section {
  display: flex;
  flex-direction: column;
}

.flex-1 {
  flex: 1;
  min-height: 0;
}

.section-title {
  font-size: 16px;
  font-weight: bold;
  color: #fff;
  margin-bottom: 15px;
  display: flex;
  align-items: center;
}

.title-icon {
  color: #409eff;
  margin-right: 8px;
  font-weight: bold;
}
</style>
