---
cssClass: wide-page
title: main.css
type: Stylesheet
version: 1.0.0
dependencies: []
routes: []
parent_components: ["[[education/src/main.ts.guide]]"]
child_components: []
tags: [vue3, css, global-styles, layout]
---

# 🧩 Stylesheet: `assets/main.css`

> [!abstract] File Overview / 文件概览
> `main.css` provides the critical global CSS reset and foundational layout constraints for the application. It ensures that the app takes up the full viewport, which is especially important for WebGL canvases like MapLibre.
> `main.css` 为应用程序提供了关键的全局 CSS 重置和基础布局约束。它确保应用程序占据整个视口，这对于像 MapLibre 这样的 WebGL 画布尤为重要。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```css
>> /* src/assets/main.css */
>> *,
>> *::before,
>> *::after {
>>   box-sizing: border-box;
>> }
>>
>> html,
>> body {
>>   width: 100%;
>>   height: 100%;
>>   margin: 0;
>>   padding: 0;
>>   overflow: hidden; /* 彻底禁止页面滚动条 */
>>   background-color: #0f172a;
>> }
>>
>> #app {
>>   width: 100%;
>>   height: 100%;
>>   max-width: none !important; /* 覆盖 Vue 默认的 1280px 限制 */
>>   margin: 0 !important;
>>   padding: 0 !important;
>>   position: relative;
>>   overflow: hidden;
>> }
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Architecture (核心逻辑与架构)
>>
>> ### CSS Reset
>> - `box-sizing: border-box`: A standard reset ensuring padding and borders are included in the element's total width and height, preventing unexpected layout shifts.
>>
>> ### Viewport Locking (Full Screen App)
>> - `html, body { width: 100%; height: 100%; overflow: hidden; }`: This is critical for dashboard or map-based applications. It locks the body to exactly the browser window's size and disables native scrolling (`overflow: hidden`).
>> - `background-color: #0f172a`: Sets a dark slate default background color.
>>
>> ### Vue Root Override
>> - `#app`: Targets the root div where Vue mounts.
>> - `max-width: none !important;`: Crucial fix. Default Vite/Vue templates often constrain the `#app` div to `1280px` wide and center it. This overrides that behavior so the app can stretch edge-to-edge on large monitors.
>>
>> ## 🚨 4. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!important] The `!important` Flag / `!important` 标志
>> > **Usage:** While `!important` is generally discouraged in CSS, it is correctly used here in the global stylesheet to force-override default framework scaffolding (like the `1280px` limit) ensuring the core architectural layout (full-screen) cannot be accidentally broken by scoped component styles.
