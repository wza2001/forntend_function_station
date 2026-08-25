<template>
  <div class="security-overview">
    <div class="overview-top">
      <div class="stat-item total-item">
        <img src="/img/user.png" class="overview-icon" alt="" />
        <div class="total-info">
          <div class="stat-label">当前社区总人数</div>
          <div class="stat-value highlight">{{ stats.totalPeople }}</div>
        </div>
      </div>
      <div class="stat-item blacklist-item">
        <div class="stat-label">黑名单</div>
        <div class="stat-value error-text">{{ stats.blacklistCount }}</div>
      </div>
    </div>

    <div class="overview-bottom">
      <div class="stat-sub">
        <div class="sub-label bg-cyan">业主人数</div>
        <div class="sub-value">{{ stats.ownerCount }}</div>
      </div>
      <div class="stat-sub">
        <div class="sub-label bg-purple">访客人数</div>
        <div class="sub-value">{{ stats.visitorCount }}</div>
      </div>
      <div class="stat-sub">
        <div class="sub-label bg-blue">外来人数</div>
        <div class="sub-value">{{ stats.outsiderCount }}</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  stats: {
    totalPeople: number;
    blacklistCount: number;
    ownerCount: number;
    visitorCount: number;
    outsiderCount: number;
  }
}>()
</script>

<style scoped>
.security-overview {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.overview-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.total-item {
  display: flex;
  align-items: center;
  gap: 15px;
}

.overview-icon {
  width: 50px;
  height: 50px;
  object-fit: contain;
}

.total-info {
  display: flex;
  flex-direction: column;
}

.stat-label {
  font-size: 14px;
  color: #ccc;
  margin-bottom: 5px;
}

.stat-value {
  font-size: 20px;
  font-weight: bold;
}

.stat-value.highlight {
  font-size: 28px;
  color: #00f6ff;
  text-shadow: 0 0 10px rgba(0, 246, 255, 0.5);
}

.blacklist-item {
  text-align: right;
}

.error-text {
  color: #ff4d4f;
  font-size: 24px;
  text-shadow: 0 0 10px rgba(255, 77, 79, 0.5);
}

.overview-bottom {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.stat-sub {
  text-align: center;
  flex: 1;
}

.sub-label {
  font-size: 14px;
  padding: 4px 12px;
  border-radius: 4px;
  margin-bottom: 8px;
  color: #fff;
  display: inline-block;
}

.bg-cyan { background: linear-gradient(90deg, rgba(0,246,255,0.8), rgba(0,246,255,0.2)); }
.bg-purple { background: linear-gradient(90deg, rgba(156,39,176,0.8), rgba(156,39,176,0.2)); }
.bg-blue { background: linear-gradient(90deg, rgba(33,150,243,0.8), rgba(33,150,243,0.2)); }

.sub-value {
  font-size: 18px;
  font-weight: bold;
  color: #fff;
}
</style>