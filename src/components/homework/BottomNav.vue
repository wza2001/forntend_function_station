<template>
  <div class="bottom-nav-bar">
    <div
      v-for="(name, index) in items"
      :key="index"
      class="nav-btn-wrapper"
      :class="[`nav-pos-${index}`, { active: activeIndex === index }]"
      @click="$emit('update:activeIndex', index)"
    >
      <div class="nav-btn-inner">
        <span class="btn-text">{{ name }}</span>
      </div>
      <!-- 选中时底部发光青条 -->
      <!-- <div v-if="activeIndex === index" class="active-bottom-line"></div>
    -->
    </div>
  </div>
</template>

<script setup lang="ts">
withDefaults(
  defineProps<{
    items?: string[]
    activeIndex?: number
  }>(),
  {
    items: () => ['社区管理', '安保监控', 'CIM平台', '能源检测', '节能分析'],
    activeIndex: 2
  }
)

defineEmits<{
  (e: 'update:activeIndex', index: number): void
}>()
</script>

<style scoped>
.bottom-nav-bar {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: flex-end;
  gap: 10px;
  z-index: 100;
  user-select: none;
}

/* 按钮外层：科技蓝发光外轮廓 (1.5px 描边) */
.nav-btn-wrapper {
  position: relative;
  cursor: pointer;
  border: 2.5px solid #4B5CCD; /* 默认纯紫色线条轮廓 */
  border-radius: 4px;          /* 拐角曲面圆角 */
  background: transparent;     /* 完全透明无底色 */
  box-shadow: none;            /* 彻底移除发散/阴影 */
  transition: all 0.25s ease;
}

/* 按钮内层：透明深灰底色 */
.nav-btn-inner {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 38px;
  padding: 0 24px;
  background: rgba(85, 85, 85, 0.6);
  transition: all 0.3s ease;
}

/* ----------------- 全面对调后的倾斜顶点 (上下、左右反转) ----------------- */

/* Index 0 (最外左侧): 顶左 0, 顶右 100%, 底右 +16px, 底左 +28px (\\ 形状) */
.nav-pos-0,
/* Index 0 (最左): 大角度左斜 + 圆角 */
.nav-pos-0 {
  transform: skewX(20deg);
}
.nav-pos-0 .btn-text {
  transform: skewX(-20deg); /* 文字反向回正，保持正常阅读 */
}

/* Index 1 (次左): 小角度左斜 + 圆角 */
.nav-pos-1 {
  transform: skewX(10deg);
}
.nav-pos-1 .btn-text {
  transform: skewX(-10deg);
}

/* Index 2 (中间 CIM平台): 垂直矩形 + 圆角 */
.nav-pos-2 {
  transform: skewX(0deg);
}
.nav-pos-2 .nav-btn-inner {
  height: 42px;
  padding: 0 32px;
}

/* Index 3 (次右): 小角度右斜 + 圆角 */
.nav-pos-3 {
  transform: skewX(-10deg);
}
.nav-pos-3 .btn-text {
  transform: skewX(10deg);
}

/* Index 4 (最右): 大角度右斜 + 圆角 */
.nav-pos-4 {
  transform: skewX(-20deg);
}
.nav-pos-4 .btn-text {
  transform: skewX(20deg);
}
/* ----------------- 交互与文字效果 ----------------- */

.btn-text {
  color: #ffffff;
  font-size: 14px;
  font-weight: 500;
  letter-spacing: 1px;
  white-space: nowrap;
}

.nav-pos-2 .btn-text {
  font-size: 16px;
  font-weight: bold;
}
.nav-btn-wrapper:hover {
  border-color: #4B5CCD;
  background: rgba(75, 90, 200, 0.12); /* 轻微透明紫底 */
  box-shadow: none;
}

/* Active 激活态: 高亮亮紫线框 + 纯净实色填充（无模糊发散） */
.nav-btn-wrapper.active {
  border-color: #4B5CCD;
  background: rgba(85, 85, 85, 0.4);
  box-shadow: none;
}

/* 激活态底部高光青条（改用清晰实线，无模糊发散） */
.active-bottom-line {
  position: absolute;
  bottom: -1.5px;
  left: 4px;
  right: 4px;
  height: 2px;
  background: #00ffff;
  box-shadow: none; /* 移除外发光 */
  border-radius: 1px;
}
</style>
