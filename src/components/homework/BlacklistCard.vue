<template>
  <div class="blacklist-stats">
    <el-icon color="#67c23a" :size="40"><UserFilled /></el-icon>
    <div class="stat-text">近一月出现黑名单次数</div>
    <div class="stat-value-large">{{ count }}</div>
  </div>
</template>

<script setup lang="ts">
import { UserFilled } from '@element-plus/icons-vue'

defineProps<{
  count: number
}>()
</script>

<style scoped>
.blacklist-stats {
  display: flex;
  align-items: center;
  gap: 15px;
  background: rgba(255, 255, 255, 0.05);
  padding: 15px;
}

.stat-text {
  font-size: 13px;
  color: #ccc;
}

.stat-value-large {
  font-size: 28px;
  color: #00bcd4;
  font-weight: bold;
  margin-left: auto;
}
</style>
