<template>
  <div class="data-panel" :class="{ 'is-collapsed': isCollapsed }">
    <div class="panel-header" @click="toggleCollapse">
      <span>Building Data</span>
      <el-button type="text" :icon="isCollapsed ? ArrowUp : ArrowDown" circle size="small" />
    </div>

    <div class="panel-content" v-show="!isCollapsed">
      <el-table :data="tableData" style="width: 100%" height="250" :row-class-name="tableRowClassName" size="small">
        <el-table-column prop="id" label="ID" width="80" />
        <el-table-column prop="name" label="Building Name" />
        <el-table-column prop="height" label="Height (m)" width="100" />
        <el-table-column prop="type" label="Type" width="120" />
        <el-table-column prop="status" label="Status" width="100">
          <template #default="scope">
            <el-tag :type="scope.row.status === 'Active' ? 'success' : 'warning'" size="small">
              {{ scope.row.status }}
            </el-tag>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ArrowUp, ArrowDown } from '@element-plus/icons-vue'

const isCollapsed = ref(false)

const toggleCollapse = () => {
  isCollapsed.value = !isCollapsed.value
}

// Mock data
const tableData = [
  { id: 'B001', name: 'Burj Mohammed Bin Rashid', height: 381, type: 'Mixed Use', status: 'Active' },
  { id: 'B002', name: 'ADNOC Headquarters', height: 342, type: 'Office', status: 'Active' },
  { id: 'B003', name: 'The Landmark', height: 324, type: 'Mixed Use', status: 'Active' },
  { id: 'B004', name: 'Etihad Towers T2', height: 305, type: 'Residential', status: 'Active' },
  { id: 'B005', name: 'Sky Tower', height: 292, type: 'Mixed Use', status: 'Maintenance' },
  { id: 'B006', name: 'ADIA Tower', height: 268, type: 'Office', status: 'Active' },
  { id: 'B007', name: 'Nation Towers Res', height: 268, type: 'Residential', status: 'Active' },
]

const tableRowClassName = ({ row }: { row: { height: number } }) => {
  if (row.height > 300) {
    return 'highlight-row'
  }
  return ''
}
</script>

<style scoped>
.data-panel {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 800px;
  background: rgba(30, 30, 30, 0.85);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  z-index: 10;
  pointer-events: auto;
  transition: all 0.3s ease;
  overflow: hidden;
}

.data-panel.is-collapsed {
  width: 200px;
  bottom: 20px;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 16px;
  cursor: pointer;
  background: rgba(45, 45, 45, 0.9);
  color: white;
  font-weight: bold;
  user-select: none;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.panel-content {
  padding: 12px;
}

:deep(.el-table) {
  --el-table-bg-color: transparent;
  --el-table-tr-bg-color: transparent;
  --el-table-header-bg-color: rgba(255, 255, 255, 0.05);
  --el-table-header-text-color: #e2e8f0;
  --el-table-text-color: #cbd5e1;
  --el-table-border-color: rgba(255, 255, 255, 0.1);
  --el-table-row-hover-bg-color: rgba(255, 255, 255, 0.05);
}

:deep(.el-table__body-wrapper tr td.el-table-fixed-column--left),
:deep(.el-table__body-wrapper tr td.el-table-fixed-column--right) {
  background-color: transparent;
}

:deep(.highlight-row) {
  background: rgba(239, 68, 68, 0.1) !important;
}

:deep(.el-button--text) {
  color: #a1a1aa;
}
:deep(.el-button--text:hover) {
  color: white;
}
</style>
