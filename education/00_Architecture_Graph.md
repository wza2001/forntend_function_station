---
cssClass: wide-page
---

> [!two-column]
> > [!code] Architecture Graph

> > ```mermaid
> > graph TD
> >     %% Core Initialization (核心初始化)
> >     index[index.html<br/>Browser Entry] -->|loads| main[src/main.ts<br/>Vue Root Instantiation]
> >     main -->|mounts| App[src/App.vue<br/>Root Layout Dashboard]
> >     main -->|injects| Router[src/router/index.ts<br/>Vue Router]
> >     main -->|injects| Pinia[src/stores/counter.ts<br/>Pinia State Management]
> >
> >     %% Component Nesting (组件嵌套)
> >     App -->|imports & renders| ViewMap[src/components/ViewMap.vue<br/>3D MapLibre Canvas]
> >     App -->|imports & renders| SpatialChart1[src/components/spatialchart.vue<br/>ECharts Pie Chart]
> >     App -->|imports & renders| SpatialChart2[src/components/spatialchart.vue<br/>ECharts Bar Chart]
> >
> >     %% Data Flow / Props (数据流/Props传递)
> >     App -.->|props: geojsonUrl| ViewMap
> >     App -.->|props: chartOption| SpatialChart1
> >     App -.->|props: chartOption| SpatialChart2
> >
> >     %% External Libraries (外部库)
> >     ViewMap -.->|initializes| MapLibre((MapLibre GL JS))
> >     SpatialChart1 -.->|initializes| ECharts((ECharts Core))
> >     SpatialChart2 -.->|initializes| ECharts
> >
> >     %% Routing (路由)
> >     Router -.->|routes to| HomeView(src/views/HomeView.vue)
> >     Router -.->|lazy loads| AboutView(src/views/AboutView.vue)
> >
> >     %% Styling for Nodes
> >     classDef core fill:#2c3e50,stroke:#34495e,stroke-width:2px,color:#fff;
> >     classDef component fill:#42b983,stroke:#2c3e50,stroke-width:2px,color:#fff;
> >     classDef plugin fill:#e67e22,stroke:#d35400,stroke-width:2px,color:#fff;
> >     classDef external fill:#8e44ad,stroke:#e67e22,stroke-width:4px,color:#fff,shape:circle;
> >
> >     class index,main core;
> >     class App,ViewMap,SpatialChart1,SpatialChart2,HomeView,AboutView component;
> >     class Router,Pinia plugin;
> >     class MapLibre,ECharts external;
> > ```
>
> > [!note] Architectural Breakdown
> > ## File Relationships (文件关系)
> > [[education/src/main.ts.guide]], [[education/src/App.vue.guide]]
> >
> > ## Project Relationships Breakdown (项目关系解析)
> >
> > This Mermaid graph illustrates the overall architecture of your Vue 3 application.
> > (这个 Mermaid 图表展示了你 Vue 3 应用程序的整体架构。)
> >
> > ### 1. The Root Path (根路径)
> > - **`index.html`** is the absolute entry point loaded by the browser. It contains a `<script>` tag that immediately fetches `src/main.ts`.
> >   (`index.html` 是浏览器加载的绝对入口点。它包含一个 `<script>` 标签，会立即获取 `src/main.ts`。)
> > - **`src/main.ts`** is the master conductor. It creates the Vue application and injects the global plugins (**Vue Router** and **Pinia**). Finally, it mounts **`App.vue`** to the DOM.
> >   (`src/main.ts` 是总指挥。它创建了 Vue 应用程序并注入了全局插件（**Vue Router** 和 **Pinia**）。最后，它将 **`App.vue`** 挂载到 DOM 上。)
> >
> > ### 2. Component Hierarchy (组件层级)
> > - **`App.vue`** acts as the parent layout. It is responsible for orchestrating the visual layout of the screen.
> >   (`App.vue` 充当父布局。它负责协调屏幕的视觉布局。)
> > - It directly imports and nests **`ViewMap.vue`** (to render the full-screen 3D map) and **`spatialchart.vue`** (used multiple times to render the floating UI charts).
> >   (它直接导入并嵌套了 **`ViewMap.vue`**（用于渲染全屏 3D 地图）和 **`spatialchart.vue`**（多次使用以渲染悬浮的 UI 图表）。)
> >
> > ### 3. Data Flow via Props (通过 Props 的数据流)
> > - The dashed arrows (`-.->`) show how data is passed down. **`App.vue`** holds the raw configuration data (like `pieOption` and `barOption`) and passes it *down* to the child **`spatialchart.vue`** components using Vue props.
> >   (虚线箭头 (`-.->`) 显示了数据是如何向下传递的。**`App.vue`** 掌握着原始配置数据（如 `pieOption` 和 `barOption`），并使用 Vue props 将其*向下*传递给子组件 **`spatialchart.vue`**。)
> > - This follows Vue's strict "One-Way Data Flow" principle: parents pass data down to children; children never mutate parent data directly.
> >   (这遵循了 Vue 严格的“单向数据流”原则：父组件向下传递数据给子组件；子组件决不能直接修改父组件的数据。)
> >
> > ### 4. Third-Party Integrations (第三方集成)
> > - The leaf components (the components at the end of the tree, like `ViewMap.vue` and `spatialchart.vue`) are responsible for wrapping complex, non-Vue JavaScript libraries.
> >   (叶子组件（位于组件树末端的组件，如 `ViewMap.vue` 和 `spatialchart.vue`）负责封装复杂的、非 Vue 的 JavaScript 库。)
> > - `ViewMap.vue` encapsulates **MapLibre GL JS**, protecting Vue's reactivity system from the map's heavy internal state.
> >   (`ViewMap.vue` 封装了 **MapLibre GL JS**，保护 Vue 的响应式系统免受地图沉重的内部状态影响。)
> > - `spatialchart.vue` abstracts the complex tree-shaking setup required by **ECharts Core**, providing a clean, reusable `<v-chart>` interface for the rest of the app.
> >   (`spatialchart.vue` 抽象了 **ECharts Core** 所需的复杂摇树优化设置，为应用程序的其余部分提供了一个干净的、可重用的 `<v-chart>` 接口。)
