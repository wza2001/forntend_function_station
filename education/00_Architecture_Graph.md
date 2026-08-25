---
cssClass: wide-page
---

> [!multi-column|no-wrap]
>
>> [!note] Project Architecture Graph
>> ## Component Hierarchy & Data Flow (组件层级与数据流)
>> ```mermaid
>> graph TD
>>     %% Core Initialization (核心初始化)
>>     index[index.html<br/>Browser Entry] -->|loads| main[src/main.ts<br/>Vue Root Instantiation]
>>     main -->|mounts| App[src/App.vue<br/>Root Layout Dashboard]
>>     main -->|injects| Router[src/router/index.ts<br/>Vue Router]
>>     main -->|injects| Pinia[src/stores/counter.ts<br/>Pinia State Management]
>>
>>     %% Routing (路由)
>>     Router -.->|routes to /| HomeView[src/views/HomeView.vue]
>>     Router -.->|routes to /map| MapDashboardView[src/views/MapDashboardView.vue]
>>     Router -.->|routes to /homework| HomeworkView[src/views/HomeworkView.vue]
>>     Router -.->|lazy loads| AboutView[src/views/AboutView.vue]
>>
>>     %% Map Dashboard Nesting
>>     MapDashboardView -->|imports & renders| ViewMap[src/components/ViewMap.vue<br/>3D MapLibre Canvas]
>>     MapDashboardView -->|imports & renders| SpatialChart1[src/components/SpatialChart.vue<br/>ECharts Pie Chart]
>>     MapDashboardView -->|imports & renders| SpatialChart2[src/components/SpatialChart.vue<br/>ECharts Bar Chart]
>>     MapDashboardView -->|imports & renders| MapControls[src/components/MapControls.vue<br/>UI Controls]
>>     MapDashboardView -->|imports & renders| DataPanel[src/components/DataPanel.vue<br/>Data Table]
>>
>>     %% Homework Dashboard Nesting
>>     HomeworkView -->|imports & renders| PanelSection[src/components/homework/PanelSection.vue<br/>Layout Wrapper]
>>     HomeworkView -->|imports & renders| SecurityStats[src/components/homework/SecurityStats.vue<br/>Stats UI]
>>     HomeworkView -->|imports & renders| AlarmList[src/components/homework/AlarmList.vue<br/>List UI]
>>     HomeworkView -->|imports & renders| BlacklistCard[src/components/homework/BlacklistCard.vue<br/>Card UI]
>>     HomeworkView -->|imports & renders| BaseChart[src/components/homework/BaseChart.vue<br/>ECharts Wrapper]
>>     HomeworkView -->|imports & renders| BottomNav[src/components/homework/BottomNav.vue<br/>Nav UI]
>>
>>     %% Data Flow / Props (数据流/Props传递)
>>     MapDashboardView -.->|props: geojsonUrl| ViewMap
>>     MapDashboardView -.->|props: chartOption| SpatialChart1
>>     MapDashboardView -.->|props: chartOption| SpatialChart2
>>     MapDashboardView -.->|emits: preset-clicked, mode-changed| MapControls
>>
>>     HomeworkView -.->|props: title| PanelSection
>>     HomeworkView -.->|props: totalPeople...| SecurityStats
>>     HomeworkView -.->|props: alarms| AlarmList
>>     HomeworkView -.->|props: count| BlacklistCard
>>     HomeworkView -.->|props: option| BaseChart
>>     HomeworkView -.->|v-model:activeIndex| BottomNav
>>
>>     %% External Libraries (外部库)
>>     ViewMap -.->|initializes| MapLibre((MapLibre GL JS))
>>     SpatialChart1 -.->|initializes| ECharts((ECharts Core))
>>     SpatialChart2 -.->|initializes| ECharts
>>     BaseChart -.->|initializes| ECharts
>>
>>     %% Styling for Nodes
>>     classDef core fill:#2c3e50,stroke:#34495e,stroke-width:2px,color:#fff;
>>     classDef component fill:#42b983,stroke:#2c3e50,stroke-width:2px,color:#fff;
>>     classDef plugin fill:#e67e22,stroke:#d35400,stroke-width:2px,color:#fff;
>>     classDef external fill:#8e44ad,stroke:#e67e22,stroke-width:4px,color:#fff,shape:circle;
>>
>>     class index,main core;
>>     class App,ViewMap,SpatialChart1,SpatialChart2,HomeView,AboutView,MapDashboardView,HomeworkView,MapControls,DataPanel,PanelSection,SecurityStats,AlarmList,BlacklistCard,BaseChart,BottomNav component;
>>     class Router,Pinia plugin;
>>     class MapLibre,ECharts external;
>> ```
>
>> [!info] Graph Explanation (图表说明)
>> ## File Relationships (文件关系)
>> [[education/src/main.ts.guide]], [[education/src/App.vue.guide]]
>>
>> ## Project Relationships Breakdown (项目关系解析)
>>
>> This Mermaid graph illustrates the overall architecture of your Vue 3 application.
>> (这个 Mermaid 图表展示了你 Vue 3 应用程序的整体架构。)
>>
>> ### 1. The Root Path (根路径)
>> - **`index.html`** is the absolute entry point loaded by the browser. It contains a `<script>` tag that immediately fetches `src/main.ts`.
>>   (`index.html` 是浏览器加载的绝对入口点。它包含一个 `<script>` 标签，会立即获取 `src/main.ts`。)
>> - **`src/main.ts`** is the master conductor. It creates the Vue application and injects the global plugins (**Vue Router** and **Pinia**). Finally, it mounts **`App.vue`** to the DOM.
>>   (`src/main.ts` 是总指挥。它创建了 Vue 应用程序并注入了全局插件（**Vue Router** 和 **Pinia**）。最后，它将 **`App.vue`** 挂载到 DOM 上。)
>>
>> ### 2. Component Hierarchy (组件层级)
>> - **`MapDashboardView.vue`** acts as a main layout view for the map. It orchestrates the map and overlay components.
>>   (`MapDashboardView.vue` 充当地图的主要布局视图。它协调地图和覆盖组件。)
>> - **`HomeworkView.vue`** acts as a main layout view for the homework dashboard, orchestrating various layout sections and data-driven child components in `src/components/homework/`.
>>
>> ### 3. Data Flow via Props (通过 Props 的数据流)
>> - The dashed arrows (`-.->`) show how data is passed down following Vue's strict "One-Way Data Flow" principle.
>>   (虚线箭头 (`-.->`) 显示了数据是如何遵循 Vue 严格的“单向数据流”原则向下传递的。)
>> - The dashboard views act as "Smart Containers", managing state and passing it down to "Dumb Presentational Components".
>>
>> ### 4. Third-Party Integrations (第三方集成)
>> - The leaf components (the components at the end of the tree, like `ViewMap.vue`, `SpatialChart.vue`, and `BaseChart.vue`) are responsible for wrapping complex, non-Vue JavaScript libraries.
>>   (叶子组件（位于组件树末端的组件，如 `ViewMap.vue`、`SpatialChart.vue` 和 `BaseChart.vue`）负责封装复杂的、非 Vue 的 JavaScript 库。)
