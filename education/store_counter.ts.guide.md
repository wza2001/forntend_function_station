<div style="display: flex; gap: 20px; font-family: sans-serif; align-items: stretch; height: 100vh;">

<div style="flex: 1; min-width: 0; overflow-y: auto; padding: 20px; border-right: 2px solid #ddd; background-color: #f6f8fa;">

# `src/stores/counter.ts`

## Full Original Source Code (完整原始源代码)
```typescript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
```

</div>

<div style="flex: 1; min-width: 0; overflow-y: auto; padding: 20px; background-color: #ffffff;">

# Guide Explanation (指南说明)

## Imports Breakdown (导入部分解析)
- `import { ref, computed } from 'vue'`: Imports Vue's Composition API functions. `ref` creates the actual state variables, and `computed` creates reactive getters that automatically update when the state they depend on changes.
  (导入 Vue 的组合式 API 函数。`ref` 创建实际的状态变量，而 `computed` 创建响应式的 getters，它们会在其依赖的状态改变时自动更新。)
- `import { defineStore } from 'pinia'`: Imports Pinia's factory function. This is required to define a new global store and hook it into the Vue DevTools and application context.
  (导入 Pinia 的工厂函数。这是定义新的全局 store 并将其挂接到 Vue DevTools 和应用程序上下文中所必需的。)

## File Purpose & Architecture (文件用途与架构)
This file defines a **Pinia Store**. Pinia is the official state management library for Vue 3.
(此文件定义了一个 **Pinia Store (存储)**。Pinia 是 Vue 3 的官方状态管理库。)
While component `ref`s (like in `App.vue`) handle *local* state, a store handles *global* state. If multiple, unrelated components in your application need to read or modify the exact same data (e.g., user authentication status, a shopping cart, or global map settings), you put that data in a Pinia store.
(虽然组件的 `ref`（比如在 `App.vue` 中）处理的是*局部*状态，但 store 处理的是*全局*状态。如果应用程序中多个不相关的组件需要读取或修改完全相同的数据（例如，用户身份验证状态、购物车或全局地图设置），你就会将这些数据放入 Pinia store 中。)

## Syntax Breakdown (Setup Store Style) (语法解析：Setup Store 风格)

Pinia supports two syntaxes: Options Stores (older, similar to Vuex) and Setup Stores (modern, Composition API style). This file uses the modern Setup Store syntax.
(Pinia 支持两种语法：Options Stores（较旧的，类似于 Vuex）和 Setup Stores（现代的，组合式 API 风格）。此文件使用的是现代的 Setup Store 语法。)

### 1. Store Definition (Fixed Boilerplate) (Store 定义：固定样板代码)
```typescript
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // ... state, getters, and actions
})
```
- **`defineStore`**: The factory function required to create a store.
  (创建 store 所需的工厂函数。)
- **`'counter'`**: The unique ID of this store. Pinia uses this ID to connect the store to the Vue DevTools.
  (此 store 的唯一 ID。Pinia 使用此 ID 将 store 连接到 Vue DevTools。)
- **Convention (约定)**: The exported function is always named starting with `use` (e.g., `useCounterStore`, `useUserStore`) because it acts as a composable hook.
  (导出的函数总是以 `use` 开头命名（例如，`useCounterStore`、`useUserStore`），因为它充当了一个可组合的 hook 函数。)

### 2. State (Reactive Data) (状态：响应式数据)
```typescript
import { ref } from 'vue'
const count = ref(0)
```
- In a Setup Store, a simple `ref()` acts as the **state**.
  (在 Setup Store 中，一个简单的 `ref()` 就充当了**状态 (state)**。)
- Any component that imports and uses this store will share this exact `count` variable. When one component changes it, all other components update automatically.
  (任何导入并使用此 store 的组件都将共享这个完全相同的 `count` 变量。当一个组件更改它时，所有其他组件都会自动更新。)

### 3. Getters (Computed Properties) (Getters：计算属性)
```typescript
import { computed } from 'vue'
const doubleCount = computed(() => count.value * 2)
```
- In a Setup Store, a `computed()` property acts as a **getter**.
  (在 Setup Store 中，一个 `computed()` 属性就充当了 **getter**。)
- Getters are used to derive state based on other state. They are cached; `doubleCount` will only recalculate if `count.value` changes.
  (Getters 用于基于其他状态派生出新的状态。它们是被缓存的；`doubleCount` 只有在 `count.value` 发生变化时才会重新计算。)

### 4. Actions (Functions) (Actions：函数)
```typescript
function increment() {
  count.value++
}
```
- In a Setup Store, any standard function acts as an **action**.
  (在 Setup Store 中，任何标准函数都充当了 **action**。)
- Actions are used to encapsulate the logic for modifying the state. While components *can* mutate state directly (`store.count++`), it is considered best practice to use actions to keep mutations organized and predictable.
  (Actions 用于封装修改状态的逻辑。虽然组件*可以*直接修改状态（`store.count++`），但使用 actions 来保持状态修改的组织性和可预测性被认为是一种最佳实践。)

### 5. Exposing the API (暴露 API)
```typescript
return { count, doubleCount, increment }
```
- You **must** return an object containing all the state, getters, and actions you want components to be able to access. Anything not returned remains private to the store file.
  (你**必须**返回一个对象，其中包含你希望组件能够访问的所有 state、getters 和 actions。任何未返回的内容都会在 store 文件中保持私有。)

## Component Interaction (组件交互)
To use this in a component (要在组件中使用它):
```html
<script setup>
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore() // Instantiates or retrieves the global store (实例化或检索全局 store)
// Use in template (在模板中使用): {{ store.count }}
// Call action (调用 action): @click="store.increment()"
</script>
```

## Class/Interface Usage (类/接口使用)
Pinia setup stores intentionally mirror the standard Vue Composition API syntax (`ref`, `computed`). They do not use classes. The returned object implicitly defines a strongly-typed TypeScript interface for the store, ensuring auto-completion works perfectly in components.
(Pinia setup stores 有意地模仿了标准的 Vue 组合式 API 语法（`ref`、`computed`）。它们不使用类。返回的对象隐式地为 store 定义了一个强类型的 TypeScript 接口，从而确保自动补全在组件中完美工作。)

</div>
</div>