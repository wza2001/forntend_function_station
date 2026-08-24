---
cssClass: wide-page
title: stores/counter.ts
type: Store
version: 1.0.0
dependencies:
  - "pinia: ^2.1.0"
routes: []
parent_components: []
child_components: []
tags: [vue3, pinia, state-management, composition-api]
---

# 🧩 Store: `counter.ts`

> [!abstract] File Overview / 文件概览
> This file defines a Pinia store using the Composition API style. Pinia is the official state management library for Vue 3, replacing Vuex. It allows data and functions to be shared globally across multiple, unrelated components.
> 此文件使用组合式 API 风格定义了一个 Pinia store。Pinia 是 Vue 3 的官方状态管理库，取代了 Vuex。它允许数据和函数在多个不相关的组件之间全局共享。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```typescript
>> import { ref, computed } from 'vue'
>> import { defineStore } from 'pinia'
>>
>> export const useCounterStore = defineStore('counter', () => {
>>   const count = ref(0)
>>   const doubleCount = computed(() => count.value * 2)
>>   function increment() {
>>     count.value++
>>   }
>>
>>   return { count, doubleCount, increment }
>> })
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Reactivity (核心逻辑与响应式)
>>
>> ### Composition API Setup Store (Setup Store 语法)
>> Pinia supports two syntaxes: Option Stores (similar to Vuex) and Setup Stores (similar to Vue 3 `<script setup>`). This file uses the Setup Store syntax, which is more flexible and integrates perfectly with TypeScript.
>>
>> - **`defineStore('counter', ...)`**: Registers the store with Pinia under the unique ID `'counter'`.
>>
>> ### State Equivalents
>> - **State (状态)**: `const count = ref(0)` acts as the state. It is the single source of truth for the counter value.
>> - **Getters (计算属性)**: `const doubleCount = computed(...)` acts as a getter. It automatically recalculates whenever `count` changes and is cached for performance.
>> - **Actions (动作)**: `function increment() { ... }` acts as an action. It encapsulates the logic used to mutate the state.
>>
>> ## 🔄 2. State Flow (状态流转)
>>
>> - **Exposure**: The `return { count, doubleCount, increment }` statement exposes these internal variables and functions to any component that imports and executes `useCounterStore()`.
>>
>> ## 🚨 4. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!warning] Destructuring Reactivity Loss / 解构导致响应式丢失
>> > **Issue:** If a component does `const { count } = useCounterStore()`, the `count` variable becomes a static primitive and loses its reactivity. The UI will not update when the store changes.
>> > **Solution:** Always use Pinia's `storeToRefs()` when destructuring state, e.g., `const { count } = storeToRefs(useCounterStore())`. Methods like `increment` can be destructured normally.
