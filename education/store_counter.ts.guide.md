# Guide: `src/stores/counter.ts`

## File Purpose & Architecture
This file defines a **Pinia Store**. Pinia is the official state management library for Vue 3.
While component `ref`s (like in `App.vue`) handle *local* state, a store handles *global* state. If multiple, unrelated components in your application need to read or modify the exact same data (e.g., user authentication status, a shopping cart, or global map settings), you put that data in a Pinia store.

## Syntax Breakdown (Setup Store Style)

Pinia supports two syntaxes: Options Stores (older, similar to Vuex) and Setup Stores (modern, Composition API style). This file uses the modern Setup Store syntax.

### 1. Store Definition (Fixed Boilerplate)
```typescript
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // ... state, getters, and actions
})
```
- **`defineStore`**: The factory function required to create a store.
- **`'counter'`**: The unique ID of this store. Pinia uses this ID to connect the store to the Vue DevTools.
- **Convention**: The exported function is always named starting with `use` (e.g., `useCounterStore`, `useUserStore`) because it acts as a composable hook.

### 2. State (Reactive Data)
```typescript
import { ref } from 'vue'
const count = ref(0)
```
- In a Setup Store, a simple `ref()` acts as the **state**.
- Any component that imports and uses this store will share this exact `count` variable. When one component changes it, all other components update automatically.

### 3. Getters (Computed Properties)
```typescript
import { computed } from 'vue'
const doubleCount = computed(() => count.value * 2)
```
- In a Setup Store, a `computed()` property acts as a **getter**.
- Getters are used to derive state based on other state. They are cached; `doubleCount` will only recalculate if `count.value` changes.

### 4. Actions (Functions)
```typescript
function increment() {
  count.value++
}
```
- In a Setup Store, any standard function acts as an **action**.
- Actions are used to encapsulate the logic for modifying the state. While components *can* mutate state directly (`store.count++`), it is considered best practice to use actions to keep mutations organized and predictable.

### 5. Exposing the API
```typescript
return { count, doubleCount, increment }
```
- You **must** return an object containing all the state, getters, and actions you want components to be able to access. Anything not returned remains private to the store file.

## Component Interaction
To use this in a component:
```html
<script setup>
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore() // Instantiates or retrieves the global store
// Use in template: {{ store.count }}
// Call action: @click="store.increment()"
</script>
```

## Class/Interface Usage
Pinia setup stores intentionally mirror the standard Vue Composition API syntax (`ref`, `computed`). They do not use classes. The returned object implicitly defines a strongly-typed TypeScript interface for the store, ensuring auto-completion works perfectly in components.