<template>
  <div class="panel-section" :class="{ 'flex-1': flex }">
    <div class="section-title">
      <img src="/img/titleImg.png" class="title-icon" alt="" />
      <span>{{ title }}</span>
    </div>
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
  position: relative;
}

.flex-1 {
  flex: 1;
  min-height: 0;
}

.section-title {
  font-size: 16px;
  font-weight: bold;
  color: #00f6ff;
  margin-bottom: 15px;
  display: flex;
  align-items: center;
  text-shadow: 0 0 5px rgba(0, 246, 255, 0.5);
}

.title-icon {
  object-fit: contain;
  height: 16px;
  margin-right: 8px;
}
</style>
