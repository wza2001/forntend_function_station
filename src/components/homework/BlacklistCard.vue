<template>
  <div class="blacklist-card">
    <div class="blacklist-header">
      <img src="/img/user.png" class="blacklist-icon" alt="" />
      <div class="blacklist-info">
        <div class="info-row">
          <span class="label">姓名：</span>
          <span class="value">{{ name }}</span>
        </div>
        <div class="info-row">
          <span class="label">身份证：</span>
          <span class="value">{{ idNumber }}</span>
        </div>
      </div>
    </div>
    <div class="blacklist-similarity">
      <div class="similarity-text">相似度</div>
      <div class="similarity-value">{{ similarity }}%</div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  name: string
  idNumber: string
  similarity: number
}>()
</script>

<style scoped>
.blacklist-card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(255, 0, 0, 0.05);
  border: 1px solid rgba(255, 0, 0, 0.3);
  padding: 15px;
  box-shadow: inset 0 0 15px rgba(255, 0, 0, 0.1);
}

.blacklist-header {
  display: flex;
  align-items: center;
  gap: 15px;
}

.blacklist-icon {
  width: 50px;
  height: 50px;
  object-fit: contain;
  filter: hue-rotate(150deg) saturate(2);
}

.info-row {
  margin-bottom: 5px;
  font-size: 14px;
}

.label {
  color: #ccc;
}

.value {
  color: #ff4d4f;
  font-weight: bold;
}

.blacklist-similarity {
  text-align: right;
}

.similarity-text {
  font-size: 12px;
  color: #ccc;
  margin-bottom: 5px;
}

.similarity-value {
  font-size: 24px;
  color: #ff4d4f;
  font-weight: bold;
  text-shadow: 0 0 10px rgba(255, 77, 79, 0.5);
}
</style>