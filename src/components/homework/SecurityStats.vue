<template>
  <div class="security-overview">
    <div class="overview-bottom">
      <div class="stat-sub">
        <img src="/img/title.png" class="overview-icon" alt="">
        <div class="sub-label bg-cyan">业主人数</div>
        <div class="sub-value">{{ ownerCount }}</div>
      </div>
      <div class="stat-sub">
        <div class="stat-label">当前社区总人数</div>
        <div class="stat-value highlight">{{ totalPeople }}</div>
        <div class="sub-label bg-purple">访客人数</div>
        <div class="sub-value">{{ visitorCount }}</div>
      </div>
      <div class="stat-sub">
        <div class="stat-item">
        <div class="stat-label">黑名单</div>
        <div class="stat-value">{{ blacklistCount }}</div>
        </div>
        <div class="sub-label bg-blue">外来人数</div>
        <div class="sub-value">{{ outsiderCount }}</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">


defineProps<{
  totalPeople: number
  blacklistCount: number
  ownerCount: number
  visitorCount: number
  outsiderCount: number
}>()
</script>

<style scoped>
.security-overview {
  background: rgba(255, 255, 255, 0.05);
  padding: 15px;
  border: 1px solid rgba(64, 158, 255, 0.2);
}

.overview-top {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}

.overview-icon{
  width: 46px;
  height: 46px;
  object-fit: contain;
  margin-right: 8px;
}

.stat-item {
  display: flex;
  flex-direction: column;
}

.stat-label {
  font-size: 12px;
  margin-bottom: 5px;
}

.stat-value {
  font-size: 18px;
  font-weight: bold;
}

.stat-value.highlight {
  font-size: 24px;
  color: #409eff;
}

.overview-bottom {
  display: flex;
  justify-content: space-between;
}

.stat-sub {
  text-align: center;
}

.sub-label {
  font-size: 12px;
  padding: 2px 8px;
  border-radius: 2px;
  margin-bottom: 5px;
  color: #fff;
}

.bg-cyan { background: #00bcd4; }
.bg-purple { background: #9c27b0; }
.bg-blue { background: #2196f3; }

.sub-value {
  font-size: 14px;
  font-weight: bold;
}
</style>
