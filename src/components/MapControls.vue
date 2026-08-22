<template>
  <div class="map-controls">
    <el-card class="controls-card" :body-style="{ padding: '12px' }">
      <div class="control-group">
        <span class="group-title">Camera Presets</span>
        <el-button-group>
          <el-button type="primary" size="small" @click="emit('preset-clicked', 'downtown')">Downtown</el-button>
          <el-button type="primary" size="small" @click="emit('preset-clicked', 'overview')">Overview</el-button>
        </el-button-group>
      </div>

      <el-divider class="divider" />

      <div class="control-group">
        <span class="group-title">View Mode</span>
        <el-switch
          v-model="is3D"
          active-text="3D"
          inactive-text="2D"
          inline-prompt
          style="--el-switch-on-color: #3b82f6; --el-switch-off-color: #64748b"
          @change="handleModeChange"
        />
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const is3D = ref(true)

const emit = defineEmits<{
  (e: 'preset-clicked', preset: 'downtown' | 'overview'): void
  (e: 'mode-changed', is3D: boolean): void
}>()

const handleModeChange = (val: string | number | boolean) => {
  emit('mode-changed', val as boolean)
}
</script>

<style scoped>
.map-controls {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 10;
  pointer-events: auto;
}

.controls-card {
  background: rgba(30, 30, 30, 0.85);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
}

/* Override element-plus styles for dark theme card */
:deep(.el-card) {
  --el-card-bg-color: rgba(30, 30, 30, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.control-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.group-title {
  font-size: 12px;
  color: #a1a1aa;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.divider {
  margin: 12px 0;
  border-color: rgba(255, 255, 255, 0.1);
}
</style>
