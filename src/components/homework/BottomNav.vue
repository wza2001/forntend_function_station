<template>
  <div class="bottom-nav">
    <div
      v-for="(item, index) in navItems"
      :key="index"
      class="nav-item"
      :class="{ active: activeIndex === index }"
      @click="$emit('update:activeIndex', index)"
    >
      <img :src="item.icon" alt="" class="nav-icon" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

defineProps<{
  items: string[]
  activeIndex: number
}>()

defineEmits<{
  (e: 'update:activeIndex', index: number): void
}>()

const navItems = computed(() => [
  { label: '一中', icon: '/img/yz.png' },
  { label: '独立', icon: '/img/dl.png' },
  { label: '概览', icon: '/img/gl.png' }
])
</script>

<style scoped>
.bottom-nav {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  z-index: 10;
  padding: 5px;
}

.nav-item {
  cursor: pointer;
  transition: all 0.3s;
  opacity: 0.7;
}

.nav-item:hover, .nav-item.active {
  opacity: 1;
  transform: scale(1.05);
  filter: drop-shadow(0 0 8px rgba(0, 246, 255, 0.8));
}

.nav-icon {
  width: auto;
  height: 40px;
  display: block;
}
</style>
