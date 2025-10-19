<template>
  <div id="app">
    <TopNav
      :currentPage="currentPage"
      @changePage="changePage"
    ></TopNav>

    <HelloWorld
      v-if="false"
      :msg="`Welcome ${userName}`"
      :count="parentCount"
    />

    <HomePage
      v-show="currentPage=='HomePage'"
      @changePage="changePage"
    ></HomePage>

    <onlineClassTaskWebsite
      v-show="currentPage=='onlineClassTaskWebsite'"
    ></onlineClassTaskWebsite>

    <TodoList
      v-show="currentPage=='TodoList'"
    ></TodoList>

    <ContactUs
      v-show="currentPage=='ContactUs'"
    ></ContactUs>

    <devTest
      v-show="currentPage=='DevTest'"
    ></devTest>

    <ClubRecruit
      v-show="currentPage=='ClubRecruit'"
    ></ClubRecruit>

    <ClassSchedule
      v-show="currentPage=='ClassSchedule'"
    ></ClassSchedule>

    <RecentCompetition
      v-show="currentPage=='RecentCompetition'"
    ></RecentCompetition>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import OnlineClassTaskWebsite from './components/onlineClassTaskWebsite.vue';
import TopNav from './components/TopNav.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    TopNav,
    OnlineClassTaskWebsite,
    TodoList: () => import('./components/TodoList.vue'),
    HomePage: () => import('./components/HomePage.vue'),
    ContactUs: () => import('./components/ContactUs.vue'),
    devTest: () => import('./components/DevTest.vue'),
    ClubRecruit: () => import('./components/ClubRecruit.vue'),
    ClassSchedule: () => import('./components/ClassSchedule.vue'),
    RecentCompetition: () => import('./components/RecentCompetition.vue')
  },
  data() {
    return {
      userName: 'defulter',
      parentCount: 2000,
      currentPage: 'HomePage'
    }
  },
  methods: {
    changePage(pageName) {
      this.currentPage = pageName;
      // 滚动到页面顶部
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  background-color: #f8f9fa;
  line-height: 1.6;
}

#app {
  min-height: 100vh;
}

/* 全局按钮样式 */
.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}

.btn-secondary {
  background-color: transparent;
  color: #667eea;
  border: 1px solid #667eea;
}

.btn-secondary:hover {
  background-color: rgba(102, 126, 234, 0.1);
}

/* 卡片样式 */
.card {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
  padding: 20px;
  margin-bottom: 20px;
  transition: all 0.3s ease;
}

.card:hover {
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.12);
  transform: translateY(-3px);
}

/* 表单样式 */
.form-group {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
}

.form-input {
  width: 100%;
  padding: 10px 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

.form-input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
}

/* 页面容器 */
.page-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

/* 页面标题 */
.page-title {
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 30px;
  position: relative;
  padding-bottom: 15px;
}

.page-title::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 60px;
  height: 3px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 3px;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .page-container {
    padding: 15px;
  }

  .page-title {
    font-size: 1.5rem;
  }
}
</style>