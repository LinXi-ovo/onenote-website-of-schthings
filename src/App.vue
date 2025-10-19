<template>
  <div id="app">
    <TopNav 
    @changePage="changePage"
    ></TopNav> 

    <HelloWorld 
     :msg="`Welcome ${userName}`"
     :count="parentCount"
     />


    <HomePage 
    v-show="currentPage=='HomePage'"
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
  data () {
    return {
      userName: 'defulter',
      parentCount: 2000,
      currentPage: 'HomePage'
    }
  },
  methods: {
    changePage(pageName){
      this.currentPage = pageName;
    }
  } 
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
