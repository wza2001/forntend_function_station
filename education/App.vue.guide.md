# Guide: `src/App.vue`

## File Purpose & Architecture
`src/App.vue` is the "Root Component" of your Vue application. It is the topmost component in the component tree, loaded directly by `main.ts`.
In this specific project, `App.vue` acts as a layout container or "dashboard wrapper". It defines the structure of the screen, layering a full-screen 3D map (`ViewMap`) underneath floating UI elements (charts via `spatialchart`).

## Syntax Breakdown

### `<script setup lang="ts">` (Fixed Boilerplate)
- **`script setup`**: This is the modern Composition API syntactic sugar in Vue 3. It compiles the script block into the component's `setup()` function. Variables and functions declared here are automatically available to the `<template>` without needing to explicitly `return` them.
- **`lang="ts"`**: Tells Vite to process this script as TypeScript, enabling static type checking.

### Flexible/Common Syntax (Business Logic)
#### `ref` Initialization
```typescript
import { ref } from 'vue';
const barOption = ref({ ... });
const pieOption = ref({ ... });
```
- **`ref()`**: A core Vue function that creates a reactive reference to a value. If the inner value (`.value`) changes, Vue automatically triggers a re-render of the template where this `ref` is used.
- **Usage**: Here, `ref` holds complex objects containing ECharts configurations. While these configs are static initially, wrapping them in `ref` is best practice in case you want to dynamically update the charts later (e.g., updating data from an API).

## Component Nesting & Hierarchy

### Parent-Child Relationships
`App.vue` is the **Parent**, and it imports and uses two **Child** components:
1. `ViewMap`
2. `spatialchart` (used twice)

### Passing Props to Children
```html
<ViewMap geojson-url="/abudhabi_city_buildings.geojson" />
<spatialchart :chart-option="pieOption" />
```
- **Static Prop**: `geojson-url="..."` passes a plain string to `ViewMap`.
- **Dynamic Prop (v-bind)**: `:chart-option="pieOption"` uses the `:` shorthand for `v-bind`. It passes the reactive `pieOption` object to the `spatialchart` component.

## CSS Styling (Scoped)
```vue
<style scoped>
```
- **`scoped`**: A crucial Vue feature. It ensures that the CSS defined in this block only applies to elements within `App.vue`. Vue achieves this by automatically appending unique data attributes (like `data-v-xyz`) to the HTML elements and CSS selectors.

### Layout Logic
- `.dashboard-root`: Uses `position: relative` with `100vw`/`100vh` to fill the entire screen and establish a positioning context for children.
- `.first_parts`: Uses `position: absolute; z-index: 10;` to float the charts *above* the map, which sits at `z-index: 0` (defined in `ViewMap.vue`).

## Class/Interface Usage
This file does not define custom classes or interfaces. The TypeScript engine infers the type of `barOption` and `pieOption` based on the provided object literals. In a larger application, you might import an `EChartsOption` interface from the `echarts` package to strictly type these `ref`s.