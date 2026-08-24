<template>
  <div class="bottom-nav">
    <div
      v-for="(item, index) in items"
      :key="index"
      class="nav-item"
      :class="{ active: activeIndex === index }"
      @click="$emit('update:activeIndex', index)"
    >
      {{ item }}
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  items: string[]
  activeIndex: number
}>()

defineEmits<{
  (e: 'update:activeIndex', index: number): void
}>()
</script>

<style scoped>
.bottom-nav {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 15px;
  background: rgba(0, 20, 50, 0.6);
  padding: 10px 20px;
  border-radius: 4px;
  border: 1px solid rgba(64, 158, 255, 0.3);
  z-index: 10;
}

.nav-item {
  padding: 8px 16px;
  font-size: 14px;
  color: #ccc;
  cursor: pointer;
  border: 1px solid transparent;
  transition: all 0.3s;
}

.nav-item:hover {
  color: #fff;
  border-color: rgba(64, 158, 255, 0.5);
}

.nav-item.active {
  color: #fff;
  background: rgba(64, 158, 255, 0.2);
  border-color: #409eff;
}
</style>
