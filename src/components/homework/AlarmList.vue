<template>
<div class="alarm-item" v-for="(alarm, index) in alarms" :key="index">
  <div class="alarm-info">
    <div class="alarm-name">
      <span class="name-text">{{ alarm.name }}</span>
      <el-tag
        class="tag_style"
        :color="getStatusType[alarm.status]?.color"
        style="color: #ffffff;"
        size="small"
      >
        {{ getStatusType[alarm.status]?.label }}
      </el-tag>
    </div>
    <div class="alarm-time">{{ alarm.time }}</div>
  </div>
</div>
</template>

<script setup lang="ts">
export type AlarmStatus = 'resolved' | 'pending' | 'processing'

export interface AlarmMessage {
  name: string
  time: string
  status: AlarmStatus
}

defineProps<{
  alarms: AlarmMessage[]
}>()

const getStatusType: Record<AlarmStatus, { label: string; type: 'success' | 'warning' | 'info'; color: string }> = {
  resolved:   { label: '已消警', type: 'success', color: '#3F51B5'},
  pending:    { label: '待派遣', type: 'warning', color: '#673AB7' },
  processing: { label: '处理中', type: 'info',    color: '#409EFF' }
}
</script>

<style scoped>
.alarm-list {
  flex: 1;
  overflow-y: auto;
  padding-right: 5px;
}

.alarm-list::-webkit-scrollbar {
  width: 4px;
}
.alarm-list::-webkit-scrollbar-thumb {
  background: rgba(64, 158, 255, 0.5);
  border-radius: 2px;
}
.alarm-item {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background: rgba(255, 255, 255, 0.05);
  margin-bottom: 8px;
  border-left: 6px solid #409eff;
}
.alarm-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 50%;
  background: #0B0E1180;
  z-index: -1;
}

.alarm-name {
  color: #D9DEE2;
  justify-content: space-between;
  display: flex;
  align-items: center;
  width:170%;
  margin-bottom: 20px;
}

.alarm-time {
  font-size: 11px;
  color: #D9DEE2;
}

.tag_style {
  border: none;                     /* 去除 Element Plus 默认灰色边框 */
  border-radius: 2px;               /* 微圆角科技感硬朗切角 */
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.5px;
  padding: 0 8px;
  height: 22px;
  line-height: 22px;
  display: inline-flex;
  align-items: baseline;
  justify-content: center;
  user-select: none;
  margin-left: auto;
  flex-shrink: 0;
}
</style>
