---
cssClass: wide-page
---

# 📄 MapControls.vue / 地图控件组件

> [!info] File Purpose & Architecture / 文件用途与架构
> The `MapControls.vue` component is responsible for providing the user interface controls overlaid on the main map view. It handles interactions like resetting the camera posture and serves as a separation of concerns from the core MapLibre rendering logic.
> `MapControls.vue` 组件负责提供叠加在主地图视图上的用户交互控件。它处理诸如重置相机姿态等交互，实现了与核心 MapLibre 渲染逻辑的关注点分离。

---

## 🔗 File Relationships / 文件关联

- **Parent/Importers (父级/引入者):** [[ViewMap]] or main layout component
- **Children/Imported (子级/被引入者):** Element Plus icons/components
- **Architecture Graph (架构图):** [[00_Architecture_Graph]]

---

## 📖 Complete Code & Architectural Breakdown / 完整源码与架构解析

> [!two-column]
> > [!code] Source Code
> > ```vue
> > <template>
> >   <div class="map-controls-overlay">
> >     <button @click="resetCamera">Reset View</button>
> >   </div>
> > </template>
> >
> > <script setup lang="ts">
> > import { inject } from 'vue';
> > // Assume MapLibre map instance is provided by parent
> > // 假设 MapLibre map 实例由父组件提供
> >
> > // Left Column: Raw Code
> > const resetCamera = () => {
> >   map.flyTo({ center: [54.363, 24.496], zoom: 14.5 });
> > };
> > </script>
> > ```
>
> > [!note] Architectural Breakdown
> > ### 📦 Imports Breakdown / 导入解析
> > Imports Vue composition API functions.
> > 导入 Vue 组合式 API 函数。
> >
> > **Fixed Boilerplate (固定模板代码):**
> > - Vue core imports / Vue 核心导入
> >
> > **Flexible/Common Syntax (灵活/通用语法):**
> > - Icon components, state stores / 图标组件、状态存储
> >
> > ---
> > ### 🧱 Component Nesting & Hierarchy / 组件嵌套与层级
> > Simple UI overlay containing interaction buttons.
> > 包含交互按钮的简单 UI 叠加层。
> >
> > ---
> > ### ⚙️ Syntax Breakdown & Function/Method Details / 语法解析与函数/方法详情
> > **Right Column: Explanation**
> > - Uses `map.flyTo` for smooth linear camera interpolation.
> > - Resets coordinates back to Abu Dhabi downtown core.
> >
> > **Flexible/Common Syntax (灵活/通用语法):**
> > - MapLibre GL instance method calling / 调用 MapLibre GL 实例方法
> >
> > ---
> > ### 🏗️ Class/Interface Usage / 类与接口使用情况
> > Currently no complex types needed for this specific method
> > 目前此特定方法不需要复杂类型
