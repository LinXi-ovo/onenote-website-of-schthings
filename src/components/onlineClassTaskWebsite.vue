<template>
    <div class="OnePage">
      <a 
      v-for="link in links" 
      :key="link.id"
      :href="link.url"
      class="nav-link"
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
        links: [{ id:1,text: '智慧树', url: 'https://coursehome.zhihuishu.com/courseHome/1000069995#teachTeam' },
                { id:2,text: 'anyview', url: 'https://anyview.gdut.edu.cn/' },
                { id:3,text: 'Classvia', url: 'https://classviva.hkust-gz.edu.cn/login/index.php' },
                {id:4,text: '调整本地集成网页(旧)(dev)', url: "vuecli-vue2-brand1/public/各种汇总/点我开始.html"},
                { id:998,text: '等你添加更多', url: '#' }
              ]
      };
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
  