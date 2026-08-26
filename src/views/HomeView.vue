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

    <div class="homework-legend">
      <h2>Homework</h2>
      <div class="test-links">
        <el-button class="test-btn" @click="router.push('/test1')">
          <img src="/img/dl.png" alt="Test 1 Icon" class="btn-icon" />
          <span>Test 1</span>
        </el-button>
        <el-button class="test-btn" @click="router.push('/test2')">
          <img src="/img/fy.png" alt="Test 2 Icon" class="btn-icon" />
          <span>Test 2</span>
        </el-button>
        <el-button class="test-btn" @click="router.push('/test3')">
          <img src="/img/gl.png" alt="Test 3 Icon" class="btn-icon" />
          <span>Test 3</span>
        </el-button>
        <el-button class="test-btn" @click="router.push('/test4')">
          <img src="/img/jk.png" alt="Test 4 Icon" class="btn-icon" />
          <span>Test 4</span>
        </el-button>
      </div>
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
  margin-bottom: 3rem;
}

.homework-legend {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: rgba(30, 41, 59, 0.8);
  padding: 2rem;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

h2 {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  color: #38bdf8;
}

.test-links {
  display: flex;
  gap: 1.5rem;
}

.test-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 100px;
  padding: 10px;
  background: #1e293b;
  border: 1px solid #475569;
  color: white;
}

.test-btn:hover {
  background: #334155;
  border-color: #38bdf8;
  color: #38bdf8;
}

.btn-icon {
  width: 40px;
  height: 40px;
  margin-bottom: 8px;
  object-fit: contain;
}
</style>
