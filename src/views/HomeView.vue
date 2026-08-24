<template>
  <div class="home-container">
    <h1>Project Portal</h1>
    <div class="nav-links">
      <el-button type="primary" size="large" @click="router.push('/map')">
        Go to Map Dashboard
      </el-button>
      <el-button type="success" size="large" @click="router.push('/homework')">
        Go to Homework Page
      </el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #0f172a;
  color: white;
}

h1 {
  font-size: 3rem;
  margin-bottom: 2rem;
}

.nav-links {
  display: flex;
  gap: 1rem;
}
</style>
