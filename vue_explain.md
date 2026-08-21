# Vue 3 + TypeScript 项目文件架构与功能指南

---

## 1. 根目录核心配置文件

| 配置文件 | 作用与功能说明 |
| :--- | :--- |
| **`index.html`** | 前端单页应用 (SPA) 的唯一 HTML 挂载入口，包含 `#app` 根容器与脚本引入。 |
| **`package.json`** | 项目元数据、依赖包列表（Vue、Router、Pinia 等）以及执行脚本命令（`dev`, `build`, `test` 等）。 |
| **`vite.config.ts`** | Vite 构建与开发服务器核心配置（插件引入、路径别名 `@`、端口、反向代理 Proxy）。 |
| **`env.d.ts`** | TypeScript 全局环境类型声明文件（声明 `.vue` 单文件组件模块类型及环境变量）。 |
| **`eslint.config.ts`** | ESLint 代码规范与静态检查配置文件。 |
| **`tsconfig.json`** | TypeScript 项目根配置文件（通过 References 关联各个子配置）。 |
| **`tsconfig.app.json`** | 专门针对 `src/` 业务应用代码的 TypeScript 编译与类型校验规则。 |
| **`tsconfig.node.json`** | 专门针对 Node.js 运行环境文件（如 `vite.config.ts`）的 TypeScript 配置。 |
| **`tsconfig.vitest.json`**| 针对单元测试环境（Vitest）的 TypeScript 类型配置。 |
| **`vitest.config.ts`** | Vitest 单元测试运行器配置文件。 |
| **`playwright.config.ts`** | Playwright 端到端 (E2E) 自动化测试全局配置文件。 |
| **`README.md`** | 项目文档与运行指令说明。 |

---

## 2. 自动化测试目录 (`e2e/`)

| 路径 | 说明 |
| :--- | :--- |
| **`e2e/tsconfig.json`** | 专供 E2E 测试代码使用的 TypeScript 类型配置。 |
| **`e2e/vue.spec.ts`** | Playwright E2E 测试脚本示例（模拟真实浏览器打开页面并断言关键文本）。 |

---

## 3. 静态资源目录 (`public/`)

| 路径 | 说明 |
| :--- | :--- |
| **`public/favicon.ico`** | 浏览器标签页展示的网站图标（该目录文件不经打包，可直接按根路径访问）。 |

---

## 4. 业务源码核心目录 (`src/`)

### 4.1 核心入口与根组件
* **`src/main.ts`**：Vue 整个工程的应用入口，负责创建 Vue 实例、注册 Pinia、Vue Router 并挂载到 DOM。
* **`src/App.vue`**：根组件，所有子页面与全局布局（如全屏背景、全局导航栏）的母版容器。

### 4.2 静态资源 (`src/assets/`)
* **`src/assets/base.css`**：底层 CSS 变量定义与基础重置样式（色彩体系、字体标准等）。
* **`src/assets/main.css`**：全局布局与通用样式，通常在该文件中引入 `base.css`。
* **`src/assets/logo.svg`**：Vue 官方矢量 Logo 图标。

### 4.3 路由与状态管理 (`src/router/` & `src/stores/`)
* **`src/router/index.ts`**：Vue Router 路由表配置文件，绑定 URL 路径（如 `/`、`/about`）与对应的页面视图。
* **`src/stores/counter.ts`**：Pinia 全局状态管理仓库示例（使用组合式 API 定义共享状态与操作方法）。

### 4.4 页面视图 (`src/views/`)
* **`src/views/HomeView.vue`**：系统首页视图组件。
* **`src/views/AboutView.vue`**：关于页面视图组件。

### 4.5 通用组件与测试 (`src/components/`)
* **`src/components/HelloWorld.vue`**：基础欢迎展示组件（演示 Props 传参）。
* **`src/components/TheWelcome.vue`**：首页内容引导整合组件。
* **`src/components/WelcomeItem.vue`**：可复用的单条引导卡片组件（使用 Slot 插槽）。
* **`src/components/icons/`**：内置的 SVG 矢量图标组件库：
  * `IconCommunity.vue`：社区图标
  * `IconDocumentation.vue`：文档图标
  * `IconEcosystem.vue`：生态图标
  * `IconSupport.vue`：支持图标
  * `IconTooling.vue`：工具链图标
* **`src/components/__tests__/HelloWorld.spec.ts`**：针对 `HelloWorld.vue` 组件编写的 Vitest 单元测试用例。

---

## 5. 项目完整层级一览

```text
frontend/
├── e2e/                           # 端到端自动化测试
│   ├── tsconfig.json
│   └── vue.spec.ts
├── public/                        # 纯静态资源 (不参与 Vite 编译)
│   └── favicon.ico
├── src/                           # 业务开发源码
│   ├── assets/                    # 参与构建的样式与静态图
│   │   ├── base.css
│   │   ├── logo.svg
│   │   └── main.css
│   ├── components/                # 可复用 UI 视图组件
│   │   ├── icons/                 # SVG 图标组件
│   │   │   ├── IconCommunity.vue
│   │   │   ├── IconDocumentation.vue
│   │   │   ├── IconEcosystem.vue
│   │   │   ├── IconSupport.vue
│   │   │   └── IconTooling.vue
│   │   ├── __tests__/             # 组件单元测试
│   │   │   └── HelloWorld.spec.ts
│   │   ├── HelloWorld.vue
│   │   ├── TheWelcome.vue
│   │   └── WelcomeItem.vue
│   ├── router/                    # 路由配置
│   │   └── index.ts
│   ├── stores/                    # Pinia 全局状态管理
│   │   └── counter.ts
│   ├── views/                     # 完整页面视图 (View/Page)
│   │   ├── AboutView.vue
│   │   └── HomeView.vue
│   ├── App.vue                    # 根组件
│   ├── env.d.ts                   # 环境类型声明
│   └── main.ts                    # 应用启动入口
├── eslint.config.ts               # 代码规范配置
├── index.html                     # HTML 挂载模板
├── package.json                   # 项目依赖与运行脚本
├── playwright.config.ts           # E2E 测试配置
├── README.md                      # 项目说明
├── tsconfig.app.json              # 应用 TS 配置
├── tsconfig.json                  # 根 TS 配置
├── tsconfig.node.json             # 构建设施 TS 配置
├── tsconfig.vitest.json           # 单元测试 TS 配置
├── vite.config.ts                 # Vite 构建配置
└── vitest.config.ts               # Vitest 配置