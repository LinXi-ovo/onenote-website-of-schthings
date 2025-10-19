<template>
    <div class="TopNav">
      <a 
      v-for="link in links" 
      :key="link.id"
      :href="link.url"
      class="nav-link"
      @click.prevent="changePage(link.pageName)"
      >
      {{ link.id > 1 ? "  |  " : "" }}{{ link.text }}
    </a>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HelloWorld',
    props: {
      msg: String,
      count: {
        type: Number,
        default: 100,
        required: true
      }
    },
    data() {
      return { 
        links: [{ id:1,text: '首页', url: '#' ,pageName:"HomePage"},
                { id:2,text: '线上作业', url: '#', pageName:"onlineClassTaskWebsite" },
                { id:3,text: 'TodoList', url: '#', pageName:"TodoList" },
                { id:4,text: '社团招新', url: '#', pageName:"ClubRecruit" },
                {id:5,text: '最近比赛', url: '#', pageName:"RecentCompetition" },
                {id:6,text: '计科3课表查询', url: '#', pageName:"ClassSchedule" },
                {id:7,text: 'DevTest', url: '#', pageName:"DevTest" },
                { id:999,text: '联系我们', url: '#', pageName:"ContactUs" }]
      };
    },
    methods: {
      changePage(pageName){
        this.$emit('changePage',pageName);
    }
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  </style>
  