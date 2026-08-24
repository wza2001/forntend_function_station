---
cssClass: wide-page
title: base.css
type: Stylesheet
version: 1.0.0
dependencies: []
routes: []
parent_components: []
child_components: []
tags: [vue3, css, variables, theme]
---

# 🧩 Stylesheet: `assets/base.css`

> [!abstract] File Overview / 文件概览
> `base.css` defines the application's design system using CSS Custom Properties (Variables). It provides a palette of colors and handles automatic Light/Dark mode switching based on the user's operating system preferences.
> `base.css` 使用 CSS 自定义属性（变量）定义了应用程序的设计系统。它提供了一个调色板，并根据用户操作系统的偏好处理自动亮/暗模式切换。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```css
>> /* color palette from <https://github.com/vuejs/theme> */
>> :root {
>>   --vt-c-white: #ffffff;
>>   --vt-c-white-soft: #f8f8f8;
>>   --vt-c-white-mute: #f2f2f2;
>>
>>   --vt-c-black: #181818;
>>   --vt-c-black-soft: #222222;
>>   --vt-c-black-mute: #282828;
>>
>>   --vt-c-indigo: #2c3e50;
>>
>>   --vt-c-divider-light-1: rgba(60, 60, 60, 0.29);
>>   --vt-c-divider-light-2: rgba(60, 60, 60, 0.12);
>>   --vt-c-divider-dark-1: rgba(84, 84, 84, 0.65);
>>   --vt-c-divider-dark-2: rgba(84, 84, 84, 0.48);
>>
>>   --vt-c-text-light-1: var(--vt-c-indigo);
>>   --vt-c-text-light-2: rgba(60, 60, 60, 0.66);
>>   --vt-c-text-dark-1: var(--vt-c-white);
>>   --vt-c-text-dark-2: rgba(235, 235, 235, 0.64);
>> }
>>
>> /* semantic color variables for this project */
>> :root {
>>   --color-background: var(--vt-c-white);
>>   --color-background-soft: var(--vt-c-white-soft);
>>   --color-background-mute: var(--vt-c-white-mute);
>>
>>   --color-border: var(--vt-c-divider-light-2);
>>   --color-border-hover: var(--vt-c-divider-light-1);
>>
>>   --color-heading: var(--vt-c-text-light-1);
>>   --color-text: var(--vt-c-text-light-1);
>>
>>   --section-gap: 160px;
>> }
>>
>> @media (prefers-color-scheme: dark) {
>>   :root {
>>     --color-background: var(--vt-c-black);
>>     --color-background-soft: var(--vt-c-black-soft);
>>     --color-background-mute: var(--vt-c-black-mute);
>>
>>     --color-border: var(--vt-c-divider-dark-2);
>>     --color-border-hover: var(--vt-c-divider-dark-1);
>>
>>     --color-heading: var(--vt-c-text-dark-1);
>>     --color-text: var(--vt-c-text-dark-2);
>>   }
>> }
>>
>> *,
>> *::before,
>> *::after {
>>   box-sizing: border-box;
>>   margin: 0;
>>   font-weight: normal;
>> }
>>
>> body {
>>   min-height: 100vh;
>>   color: var(--color-text);
>>   background: var(--color-background);
>>   transition:
>>     color 0.5s,
>>     background-color 0.5s;
>>   line-height: 1.6;
>>   font-family:
>>     Inter,
>>     -apple-system,
>>     BlinkMacSystemFont,
>>     'Segoe UI',
>>     Roboto,
>>     Oxygen,
>>     Ubuntu,
>>     Cantarell,
>>     'Fira Sans',
>>     'Droid Sans',
>>     'Helvetica Neue',
>>     sans-serif;
>>   font-size: 15px;
>>   text-rendering: optimizeLegibility;
>>   -webkit-font-smoothing: antialiased;
>>   -moz-osx-font-smoothing: grayscale;
>> }
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Architecture (核心逻辑与架构)
>>
>> ### CSS Custom Properties (Variables)
>> - **Base Palette**: The first `:root` block defines static colors (e.g., `--vt-c-white`, `--vt-c-black`).
>> - **Semantic Variables**: The second `:root` block maps those static colors to functional names (e.g., `--color-background`, `--color-text`). This abstraction allows components to use `--color-text` without knowing if it's currently black or white.
>>
>> ### Responsive Theming (Dark Mode)
>> - `@media (prefers-color-scheme: dark)`: This media query detects if the user's OS or browser is set to Dark Mode. If so, it reassigns the semantic variables (e.g., `--color-background` becomes black instead of white).
>>
>> ### Typography & Smooth Transitions
>> - **`transition`**: Adding `color 0.5s, background-color 0.5s;` to the `body` ensures that when the user switches between light and dark mode, the UI fades smoothly rather than snapping harshly.
>> - **`font-family`**: Implements a robust fallback system (Inter -> Apple System -> Segoe UI, etc.) ensuring native-looking text rendering across macOS, Windows, and Linux.