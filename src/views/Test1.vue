<template>
  <div class="dashboard-container">
    <router-link to="/" class="back-btn">
      <el-button type="primary" circle>
        <el-icon><HomeFilled /></el-icon>
      </el-button>
    </router-link>
    <MapBackground />
    <div class="overlay-container">
      <LeftPanel class="left-panel" />
      <RightPanel class="right-panel" />
      <BottomMenu class="bottom-menu" />
    </div>
  </div>
</template>

<script setup lang="ts">
import {HomeFilled} from "@element-plus/icons-vue";

defineOptions({ name: 'TestOneView' })
import MapBackground from '../components/Test1/MapBackground.vue'
import LeftPanel from '../components/Test1/LeftPanel.vue'
import RightPanel from '../components/Test1/RightPanel.vue'
import BottomMenu from '../components/Test1/BottomMenu.vue'
</script>

<style scoped>
.dashboard-container {
  width: 100vw;
  height: 100vh;
  position: relative;
  overflow: hidden;
  background-color: #0f172a;
  color: #fff;
  font-family: sans-serif;
}

.back-btn {
  position: absolute;
  top: 20px;
  left: 20px;
  z-index: 100;
  pointer-events: auto;
}
.overlay-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 10;
}

.left-panel {
  position: absolute;
  top: 60px;
  left: 20px;
  width: 380px;
  display: flex;
  flex-direction: column;
  gap: 20px;
  pointer-events: auto;
}

.right-panel {
  position: absolute;
  top: 60px;
  right: 20px;
  width: 380px;
  pointer-events: auto;
}

.bottom-menu {
  position: absolute;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  pointer-events: auto;
}
</style>
