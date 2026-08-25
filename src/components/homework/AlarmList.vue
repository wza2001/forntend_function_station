<template>
  <div class="alarm-list">
    <div class="alarm-item" v-for="(alarm, index) in alarms" :key="index">
      <div class="alarm-info">
        <div class="alarm-name">{{ alarm.name }}</div>
        <div class="alarm-time">{{ alarm.time }}</div>
      </div>
      <el-tag :type="getStatusType(alarm.status)" size="small" effect="dark" class="cyber-tag">
        {{ getStatusLabel(alarm.status) }}
      </el-tag>
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

const getStatusType = (status: AlarmStatus) => {
  switch (status) {
    case 'resolved': return 'success'
    case 'pending': return 'danger'
    case 'processing': return 'warning'
    default: return 'info'
  }
}

const getStatusLabel = (status: AlarmStatus) => {
  switch (status) {
    case 'resolved': return '已消警'
    case 'pending': return '未处理'
    case 'processing': return '处理中'
    default: return '未知'
  }
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
  background: rgba(0, 246, 255, 0.5);
  border-radius: 2px;
}

.alarm-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background: rgba(0, 40, 60, 0.5);
  margin-bottom: 8px;
  border-left: 3px solid #00f6ff;
  transition: all 0.3s;
  cursor: default;
}

.alarm-item:hover {
  background: rgba(0, 80, 120, 0.6);
  box-shadow: 0 0 10px rgba(0, 246, 255, 0.3);
}

.alarm-name {
  font-size: 13px;
  margin-bottom: 4px;
  color: #fff;
}

.alarm-time {
  font-size: 11px;
  color: #88c0d0;
}

.cyber-tag {
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 0;
}
</style>
