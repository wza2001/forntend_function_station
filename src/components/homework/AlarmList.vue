<template>
  <div class="alarm-list">
    <div class="alarm-item" v-for="(alarm, index) in alarms" :key="index">
      <div class="alarm-info">
        <div class="alarm-name">{{ alarm.name }}</div>
        <div class="alarm-time">{{ alarm.time }}</div>
      </div>
      <el-tag :type="getStatusType(alarm.status)" size="small">
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
    case 'pending': return 'warning'
    case 'processing': return 'info'
    default: return 'info'
  }
}

const getStatusLabel = (status: AlarmStatus) => {
  switch (status) {
    case 'resolved': return '已消警'
    case 'pending': return '待派遣'
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
  background: rgba(64, 158, 255, 0.5);
  border-radius: 2px;
}

.alarm-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background: rgba(255, 255, 255, 0.05);
  margin-bottom: 8px;
  border-left: 3px solid #409eff;
}

.alarm-name {
  font-size: 13px;
  margin-bottom: 4px;
}

.alarm-time {
  font-size: 11px;
  color: #888;
}
</style>
