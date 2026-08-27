<template>
  <div class="blacklist-stats">
    <img src="/img/user.png" class="icon" alt="">
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
  background: #23243280;
  font-size: 13px;
  color: #ffffff;
  display: flex;
  padding: 4px 10px;
  text-align: center;
  margin-left: 5px;

}
.icon{
  object-fit: contain;
  height: 45px;
}
.stat-value-large {
  font-family: "Microsoft YaHei"， sans-serif;
  font-size: 48px;
  color: #00bcd4;
  font-weight: bold;
  margin-left: auto;
}
</style>
