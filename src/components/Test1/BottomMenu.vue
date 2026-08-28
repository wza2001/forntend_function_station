<template>
  <div class="menu-container">
    <div class="menu-items">
      <div class="menu-item active">
        <el-icon><DataLine /></el-icon>
        <span>Dashboard</span>
      </div>
      <div class="menu-item">
        <el-icon><VideoCamera /></el-icon>
        <span>Video</span>
      </div>
      <div class="menu-item">
        <el-icon><Document /></el-icon>
        <span>Reports</span>
      </div>
      <div class="menu-item">
        <el-icon><Setting /></el-icon>
        <span>Settings</span>
      </div>
    </div>
    <div class="expand-btn">
      <el-icon><ArrowDown /></el-icon>
      <el-icon class="ml-2"><Aim /></el-icon>
    </div>
  </div>
</template>

<script setup lang="ts">
import { DataLine, VideoCamera, Document, Setting, ArrowDown, Aim } from '@element-plus/icons-vue'
</script>

<style scoped>
.menu-container {
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(51, 65, 85, 0.6);
  border-radius: 24px;
  padding: 6px 16px;
  display: flex;
  align-items: center;
  backdrop-filter: blur(8px);
  position: relative;
}

.menu-items {
  display: flex;
  gap: 8px;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 20px;
  border-radius: 20px;
  color: #94a3b8;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.menu-item:hover {
  color: #e2e8f0;
  background: rgba(255, 255, 255, 0.05);
}

.menu-item.active {
  background: #3b82f6;
  color: white;
}

.expand-btn {
  position: absolute;
  bottom: -20px;
  left: 50%;
  transform: translateX(-50%);
  background: white;
  border-radius: 12px;
  padding: 2px 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #1e293b;
  cursor: pointer;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  font-size: 12px;
}
.ml-2 { margin-left: 8px; }
</style>
