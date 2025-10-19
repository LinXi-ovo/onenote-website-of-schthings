<<<<<<< HEAD
# vuecli-vue2-brand1

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


----------
# 代码风格
在 Vue 开发中，不同部分的命名有不同的规范，这些规范不仅影响代码可读性，还可能影响代码的正确性。以下是具体说明：


### 1. 组件相关命名规则
#### （1）组件名（`name` 选项）
- **规范**：推荐使用 **PascalCase（帕斯卡命名法，首字母大写）**，如 `TodoList`、`UserProfile`。
- **原因**：
  - 符合 Vue 官方风格指南，区分组件与普通变量。
  - 在单文件组件（`.vue`）和 JSX 中，PascalCase 组件名更易识别（如 `<TodoList />`）。
  - 避免与 HTML 内置标签（如 `<div>`、`<span>`）冲突。

#### （2）组件导入与注册
- **导入时**：变量名建议与组件名保持一致（PascalCase），例如：
  ```javascript
  import TodoList from './TodoList.vue'; // 导入时用 PascalCase
  ```
- **注册时**：
  - 局部注册：键名用 PascalCase（与导入名一致）：
    ```javascript
    components: {
      TodoList // 等价于 TodoList: TodoList
    }
    ```
  - 全局注册：同样推荐 PascalCase：
    ```javascript
    Vue.component('TodoList', TodoList);
    ```
- **模板中使用**：
  - 可以用 PascalCase（`<TodoList />`）或 kebab-case（`<todo-list />`），Vue 会自动转换。
  - 推荐在 HTML 模板中用 kebab-case（更符合 HTML 标签规范），在 JSX 中用 PascalCase。


### 2. CSS 类名（`class` 属性）
- **规范**：推荐使用 **kebab-case（短横线命名法）**，如 `todo-list`、`completed-item`。
- **原因**：
  - 符合 CSS 命名传统（CSS 类名对大小写不敏感，kebab-case 更易读）。
  - 与 HTML 标签的属性命名风格一致（如 `<div class="todo-list">`）。
- **示例**：
  ```vue
  <template>
    <div class="todo-list"> <!-- 正确：kebab-case -->
      <div class="todo-item">...</div>
    </div>
  </template>
  ```


### 3. 数据属性与方法命名
- **规范**：使用 **camelCase（驼峰命名法）**，如 `todoItems`、`addTodo`。
- **原因**：
  - 符合 JavaScript 变量命名规范。
  - 在模板中使用时，Vue 支持自动转换（如 `addTodo` 可在模板中写为 `add-todo`，但建议保持一致）。
- **示例**：
  ```javascript
  data() {
    return {
      todoItems: [] // 正确：camelCase
    };
  },
  methods: {
    addTodo() { ... } // 正确：camelCase
  }
  ```


### 4. 命名冲突的影响
- **直接错误**：若组件名与内置属性/方法重名（如 `name: 'data'`），会直接导致 Vue 内部逻辑冲突，出现运行时错误。
- **隐晦问题**：若组件名与数据属性名相同（如 `name: 'todoList'` 且 `data() { return { todoList: [] } }`），虽然不一定报错，但会导致：
  - 模板中引用 `todoList` 时，可能被误认为是组件而非数据。
  - 代码可读性下降，维护者难以区分组件与数据。
- **团队协作障碍**：不规范的命名会导致团队成员理解成本升高，增加沟通成本。


### 总结表格
| 内容         | 推荐命名风格       | 示例               |
|--------------|--------------------|--------------------|
| 组件名（`name`） | PascalCase         | `TodoList`         |
| 组件导入/注册 | PascalCase         | `import TodoList`  |
| 模板中使用组件 | kebab-case         | `<todo-list />`    |
| CSS 类名      | kebab-case         | `class="todo-list"`|
| 数据/方法     | camelCase          | `todoItems`、`addTodo` |

遵循这些规范能显著提升代码的可读性、一致性和可维护性，减少潜在的命名冲突问题。"# vue2-vscode-vuecli-brand1-frontEnd" 


"# vue2-vscode-vuecli-brand1-frontEnd" 
"# onenote-website-of-schthings" 
"# onenote-website-of-schthings" 
"# onenote-website-of-schthings" 
"# onenote-website-of-schthings" 
"# onenote-website-of-schthings" 
"# onenote-website-of-schthings" 
"# onenote-website-of-schthings" 

=======

# onenote-website-of-schthings
一站式查看需要用的schthings

>>>>>>> dde1ad8a6c67a5e928345aa3708276f70f690b0a
"# onenote-website-of-schthings" 
"# onenote-website-of-schthings" 
"# onenote-website-of-schthings" 
"# onenote-website-of-schthings"
>>>>>>> git init git add . git commit -m "first commit" git branch -M main git remote add origin https://github.com/LinXi-ovo/onenote-website-of-schthings.git git push -u origin main
>>>>>>> 
"# onenote-website-of-schthings" 
"# onenote-website-of-schthings" 
"# onenote-website-of-schthings" 
