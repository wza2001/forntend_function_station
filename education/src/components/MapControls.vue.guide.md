---
cssClass: wide-page
title: MapControls.vue
type: Component
version: 1.0.0
dependencies:
  - "vue: ^3.3.0"
  - "element-plus: ^2.3.8"
routes: []
parent_components: ["[[education/src/views/MapDashboardView.vue.guide]]"]
child_components: []
tags: [vue3, component, element-plus, composition-api, ui-controls]
---

# 🧩 Component: `MapControls.vue`

> [!abstract] Component Overview / 组件概览
> `MapControls.vue` provides the user interface controls overlaid on the main map view. It acts as an event emitter, capturing user intent (like changing camera presets or toggling 2D/3D modes) and passing those instructions up to the parent component, which orchestrates the actual map changes.
> `MapControls.vue` 提供叠加在主地图视图上的用户交互控件。它充当事件发射器，捕获用户意图（如更改相机预设或切换 2D/3D 模式）并将这些指令传递给父组件，由父组件协调实际的地图更改。

---

> [!multi-column|no-wrap]
>
>> [!code] Source Code
>> ```vue
>> <template>
>>   <div class="map-controls">
>>     <el-card class="controls-card" :body-style="{ padding: '12px' }">
>>       <div class="control-group">
>>         <span class="group-title">Camera Presets</span>
>>         <el-button-group>
>>           <el-button type="primary" size="small" @click="emit('preset-clicked', 'downtown')">Downtown</el-button>
>>           <el-button type="primary" size="small" @click="emit('preset-clicked', 'overview')">Overview</el-button>
>>         </el-button-group>
>>       </div>
>>
>>       <el-divider class="divider" />
>>
>>       <div class="control-group">
>>         <span class="group-title">View Mode</span>
>>         <el-switch
>>           v-model="is3D"
>>           active-text="3D"
>>           inactive-text="2D"
>>           inline-prompt
>>           style="--el-switch-on-color: #3b82f6; --el-switch-off-color: #64748b"
>>           @change="handleModeChange"
>>         />
>>       </div>
>>     </el-card>
>>   </div>
>> </template>
>>
>> <script setup lang="ts">
>> // Fixed Boilerplate Imports
>> import { ref } from 'vue'
>>
>> // Flexible/Common Syntax
>> const is3D = ref(true)
>>
>> const emit = defineEmits<{
>>   (e: 'preset-clicked', preset: 'downtown' | 'overview'): void
>>   (e: 'mode-changed', is3D: boolean): void
>> }>()
>>
>> const handleModeChange = (val: string | number | boolean) => {
>>   emit('mode-changed', val as boolean)
>> }
>> </script>
>>
>> <style scoped>
>> /* [Styles truncated for brevity] */
>> </style>
>> ```
>
>> [!note] Architectural Breakdown
>>
>> ## 🏗️ 1. Core Logic & Reactivity (核心逻辑与响应式)
>>
>> ### Composition API State / 响应式状态
>> - **`is3D` (ref<boolean>)**: A local reactive state bound to the `<el-switch>`. It visually represents whether the map is currently in 3D mode.
>>
>> ## 🔄 2. State Flow: Props & Emits (状态流转：输入与输出)
>>
>> ### 📥 Props
>> - None. The component is entirely driven by user interaction and local state.
>>
>> ### 📤 Emits (Outputs / 输出)
>> This component is a classic "dumb" or "presentation" component. It doesn't modify the map directly; instead, it uses `defineEmits` to strictly type and emit events up to the smart parent (`MapDashboardView`).
>>
>> | Event Name | Payload Type | Description |
>> | :--- | :--- | :--- |
>> | `preset-clicked` | `'downtown' \| 'overview'` | Fired when a camera preset button is clicked. (点击相机预设按钮时触发。) |
>> | `mode-changed` | `boolean` | Fired when the 2D/3D toggle switch changes. (2D/3D 切换开关改变时触发。) |
>>
>> ## ⏳ 3. Lifecycle & DOM Interaction (生命周期与DOM交互)
>>
>> - The component relies entirely on Vue's declarative rendering and Element Plus's internal DOM management. No direct DOM manipulation or complex lifecycle hooks are required.
>>
>> ## 🛠️ 4. Comprehensive Function & Method Catalog (函数与方法目录)
>>
>> ### Inline Template Event Handlers
>> - `@click="emit('preset-clicked', 'downtown')"`: Directly emits the event without needing a wrapper function in the script block. This is concise and preferred for simple event proxying.
>>
>> ### `handleModeChange`
>> - **Purpose**: Bridges the `el-switch` change event to the strongly-typed Vue `emit`.
>> - **Trigger**: User toggles the switch. Element Plus passes the new value as the first argument.
>> - **Signature**: `(val: string | number | boolean) => void`
>> - **Mechanism**: Casts the generic payload `val` to `boolean` (since we know our switch operates on booleans) and emits it via `'mode-changed'`.
>>
>> ## 🚨 5. Pitfalls, Bugs & Performance (陷阱、Bug与性能优化)
>>
>> > [!info] Strict Typing with defineEmits
>> > Using the TypeScript syntax `defineEmits<{ (e: 'event', payload: Type): void }>()` provides crucial IDE autocomplete and compile-time checking for parent components listening to these events, preventing silent bugs caused by typoed event names or incorrect payload types.
