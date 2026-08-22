# Guide: `src/components/spatialchart.vue`

## File Purpose & Architecture
This file is a reusable, wrapper Vue Component designed to render ECharts data visualizations.
Architecturally, it abstracts away the complex import and setup processes required by ECharts. Instead of writing ECharts initialization logic in every single view, you import this component and simply pass it the configuration data.

## Component Nesting & Hierarchy
- **Parent**: Can be used by any component, currently used by `App.vue`.
- **Child**: Utilizes `<v-chart>` (from the `vue-echarts` library) as its core child component.
- **Communication**: It receives instructions exclusively via the `chartOption` prop from its parent.

## Syntax Breakdown

### 1. ECharts Tree-Shaking Imports (Flexible/ECharts Syntax)
```typescript
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { PieChart, BarChart } from 'echarts/charts';
import { TitleComponent, TooltipComponent, LegendComponent, GridComponent } from 'echarts/components';
import VChart from 'vue-echarts';

use([ CanvasRenderer, PieChart, BarChart, TitleComponent, TooltipComponent, LegendComponent, GridComponent ]);
```
- **Purpose**: ECharts is a massive library. If you imported the entire library (`import * as echarts from 'echarts'`), your final application bundle would be huge and slow to load.
- **Mechanism**: The `echarts/core` module allows you to import *only* the specific charts (Pie, Bar) and components (Title, Tooltip) you actually need. The `use([])` function registers these specific modules with the core ECharts engine. This technique is called "Tree-shaking."

### 2. Defining Props (Fixed Boilerplate)
```typescript
defineProps<{
  chartOption: Record<string, any>;
}>();
```
- **Purpose**: This component requires the parent to provide a `chartOption` object.
- **TypeScript `Record<string, any>`**: This is a TypeScript utility type. It essentially means "an object where the keys are strings, and the values can be absolutely anything (`any`)."
  - *Note*: While `any` defeats some purposes of TypeScript, ECharts configuration objects are notoriously complex and deeply nested. Using `Record<string, any>` is a common pragmatic shortcut, though importing explicit `EChartsOption` types is better for strictness.

### 3. Template Usage (Vue Syntax)
```html
<v-chart class="chart" :option="chartOption" autoresize />
```
- `<v-chart>`: This is the component provided by the `vue-echarts` wrapper library.
- `:option="chartOption"`: Binds the prop passed from the parent directly to the underlying ECharts instance.
- `autoresize`: A specific prop provided by `vue-echarts` that automatically listens to window resize events and redraws the canvas so the chart doesn't distort.

## Styling (Scoped)
```css
.wrapper_chart { width: 100%; height: 320px; }
.chart { width: 100%; height: 100%; }
```
- **Constraint Handling**: ECharts canvases absolutely require their parent containers to have a defined height and width. If the container is `0x0`, the chart will simply not render. This wrapper ensures a default height of `320px`, while filling `100%` of whatever width the parent gives it.

## Class/Interface Usage
This component leverages functional imports and composition rather than object-oriented classes. The TypeScript type `Record<string, any>` acts as a structural interface defining the shape of the expected props.