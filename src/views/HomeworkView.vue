<template>
  <div class="homework-container">
    <div class="header">
      <el-button type="info" :icon="HomeFilled" circle @click="router.push('/')" />
      <h1>Homework Page</h1>
    </div>
    <p>This is an empty structure for the homework assignment.</p>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { HomeFilled } from '@element-plus/icons-vue'

const router = useRouter()
// Homework logic will go here
</script>

<style scoped>
.homework-container {
  padding: 2rem;
  color: white;
}

.header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.header h1 {
  margin: 0;
}
</style>
