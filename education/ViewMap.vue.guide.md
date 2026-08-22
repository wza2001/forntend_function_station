# Guide: `src/components/ViewMap.vue`

## File Purpose & Architecture
This file is a Vue Component dedicated to rendering a 3D Map using MapLibre GL JS.
Architecturally, it isolates all map-related logic from the rest of the application. It receives data instructions (via props) from its parent (`App.vue`) and manages a complex third-party library (`MapLibre`) within its own lifecycle.

## Component Nesting & Hierarchy
- **Parent**: `App.vue`. The parent dictates *where* the map goes and *what* data it should load (via the `geojsonUrl` prop).
- **Child**: None. This is a leaf component.

## Syntax Breakdown

### 1. Props Definition (Fixed/TypeScript Syntax)
```typescript
const props = withDefaults(
  defineProps<{
    geojsonUrl?: string;
  }>(),
  {
    geojsonUrl: '/abudhabi_city_buildings.geojson'
  }
);
```
- **`defineProps`**: A compiler macro in `<script setup>` used to declare what props the component accepts. Here it uses TypeScript type arguments (`<{ geojsonUrl?: string; }>`) to enforce that `geojsonUrl` is a string and is optional (`?`).
- **`withDefaults`**: A helper function to provide default values for optional props. If the parent doesn't provide a URL, it defaults to the local Abu Dhabi file.

### 2. DOM Referencing
```html
<div ref="mapContainer" class="map-view-container"></div>
```
```typescript
const mapContainer = ref<HTMLElement | null>(null);
```
- **Template Ref (`ref="mapContainer"`)**: Vue's way of directly interacting with a DOM element. The `mapContainer` variable in the script is bound to this `<div>`.
- MapLibre needs a raw HTML element to attach the map canvas to. We cannot pass it just a Vue component.

### 3. State Management
```typescript
let mapInstance: Map | null = null;
```
- Notice this is a standard `let` variable, **not** a `ref`.
- **Why?** MapLibre's `Map` object is highly complex and manages its own internal state. Making it a reactive Vue `ref` would cause Vue to deeply track thousands of internal map properties, causing severe performance issues. It is a best practice to keep heavy third-party instances out of Vue's reactivity system.

## Lifecycle Hooks & Functions

### `onMounted` (Fixed Boilerplate)
- **Purpose**: A Vue lifecycle hook that runs *after* the component has been inserted into the DOM.
- **Trigger**: Called automatically by Vue during component creation.
- **Action**: It initializes the MapLibre `Map` instance. It *must* happen here because MapLibre requires the `mapContainer` `<div>` to actually exist in the browser DOM before it can render.

#### Inside `onMounted` (Flexible/MapLibre Logic):
1. **Instantiation**: `new Map({...})` sets up the visual parameters (center, zoom, pitch).
2. **Event Listeners**: `mapInstance.on('load', ...)` waits for the base map style to finish downloading before adding custom data.
3. **Adding Data**:
   - `addSource`: Registers the GeoJSON data URL.
   - `addLayer`: Tells the map *how* to draw the data. Uses `fill-extrusion` to draw 3D buildings based on the `height` property in the GeoJSON.

### `onUnmounted` (Fixed Boilerplate)
- **Purpose**: Runs right before the component is destroyed (removed from the DOM).
- **Trigger**: Called automatically by Vue (e.g., if you navigated to a different page using Vue Router).
- **Action**: `mapInstance?.remove();` destroys the WebGL context and frees up memory. This is crucial for preventing memory leaks in Single Page Applications (SPAs).

## Class/Interface Usage
- **`Map` (from 'maplibre-gl')**: An imported Class. `new Map(...)` creates a specific instance of the map engine.
- **TypeScript Generics (`ref<HTMLElement | null>`)**: Explicitly tells TypeScript that `mapContainer` will eventually hold an HTML element, but starts as `null` (before `onMounted` runs).