<template>
    <div class="todo-list">
        <h2>Todo List</h2>
        <!-- 添加输入框和按钮 -->
        <div class="add-item">
            <input 
                v-model="newItem" 
                @keyup.enter="addItem"
                placeholder="添加新的待办事项"
            >
            <button @click="addItem">添加</button>
        </div>
        
        <ul>
            <li v-for="(item, index) in todoItems" :key="index">
                <!-- 添加checkbox -->
                <input 
                    type="checkbox" 
                    v-model="item.completed"
                >
                <!-- 根据完成状态添加样式 -->
                <span v-if="!item.isLink" :class="{ completed: item.completed }">{{ item.text }}</span>
                <a v-else :href="item.url" target="_blank" :class="{ completed: item.completed }">{{ item.text }}</a>
                <!-- 删除按钮 -->
                <button @click="deleteItem(index)" class="delete-btn">删除</button>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'TodoList',
    data() {
        return {
            newItem: '',  // 新输入的待办事项
            todoItems: [
                { text: "吃饭", completed: false },
                { text: "睡觉", completed: false },
                { text: "去github给开发者点一颗star 💗", completed: false, isLink: true, url: "https://github.com/LinXi-ovo/onenote-website-of-schthings" }
            ]
        };
    },
    methods: {
        // 添加新事项
        addItem() {
            if (this.newItem.trim()) {
                this.todoItems.push({
                    text: this.newItem,
                    completed: false
                });
                this.newItem = '';  // 清空输入框
            }
        },
        // 删除事项
        deleteItem(index) {
            this.todoItems.splice(index, 1);
        }
    }
}
</script>

<style scoped>
.todo-list {
    max-width: 500px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.add-item {
    margin-bottom: 20px;
    display: flex;
    gap: 10px;
}

.add-item input {
    flex: 1;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

.add-item button {
    padding: 8px 16px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    display: flex;
    align-items: center;
    padding: 10px;
    margin: 5px 0;
    background-color: #f9f9f9;
    border-radius: 4px;
}

li span, li a {
    margin: 0 10px;
    flex: 1;
}

.completed {
    text-decoration: line-through;
    color: #888;
}

li a {
    color: inherit;
    text-decoration: none;
}

li a:hover {
    text-decoration: underline;
}

.delete-btn {
    padding: 5px 10px;
    background-color: #ff4444;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.delete-btn:hover {
    background-color: #cc0000;
}
</style>
