<template>
  <header class="top-nav">
    <div class="nav-container">
      <div class="logo">
        <h2>学术资源中心</h2>
      </div>
      <nav class="nav-links">
        <a
          v-for="link in links"
          :key="link.id"
          :href="link.url"
          :class="['nav-link', { 'active': isActive(link.pageName) }]"
          @click.prevent="changePage(link.pageName)"
        >
          {{ link.text }}
        </a>
      </nav>
      <div class="menu-toggle" @click="toggleMenu">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'TopNav',
  props: {
    currentPage: {
      type: String,
      default: 'HomePage'
    }
  },
  data() {
    return {
      isMenuOpen: false,
      links: [
        { id: 1, text: '首页', url: '#', pageName: "HomePage" },
        { id: 2, text: '线上作业', url: '#', pageName: "onlineClassTaskWebsite" },
        { id: 3, text: 'TodoList', url: '#', pageName: "TodoList" },
        { id: 4, text: '社团招新', url: '#', pageName: "ClubRecruit" },
        { id: 5, text: '最近比赛', url: '#', pageName: "RecentCompetition" },
        { id: 6, text: '计科3课表查询', url: '#', pageName: "ClassSchedule" },
        { id: 7, text: 'DevTest', url: '#', pageName: "DevTest" },
        { id: 999, text: '联系我们', url: '#', pageName: "ContactUs" }
      ]
    };
  },
  methods: {
    changePage(pageName) {
      this.$emit('changePage', pageName);
      this.isMenuOpen = false;
    },
    isActive(pageName) {
      return this.currentPage === pageName;
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    }
  }
}
</script>

<style scoped>
.top-nav {
  background-color: #ffffff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  height: 70px;
}

.logo h2 {
  color: #2c3e50;
  font-weight: 700;
  margin: 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nav-links {
  display: flex;
  gap: 25px;
}

.nav-link {
  text-decoration: none;
  color: #2c3e50;
  font-weight: 500;
  padding: 8px 15px;
  border-radius: 4px;
  transition: all 0.3s ease;
  position: relative;
}

.nav-link:hover {
  color: #667eea;
}

.nav-link.active {
  color: #667eea;
}

.nav-link.active::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 3px;
}

.menu-toggle {
  display: none;
  flex-direction: column;
  cursor: pointer;
}

.bar {
  width: 25px;
  height: 3px;
  background-color: #2c3e50;
  margin: 3px 0;
  transition: 0.3s;
}

@media (max-width: 768px) {
  .nav-links {
    position: fixed;
    top: 70px;
    right: -100%;
    width: 100%;
    height: calc(100vh - 70px);
    background-color: #ffffff;
    flex-direction: column;
    align-items: center;
    padding-top: 50px;
    transition: 0.5s;
    box-shadow: -2px 0 10px rgba(0, 0, 0, 0.1);
  }

  .nav-links.active {
    right: 0;
  }

  .menu-toggle {
    display: flex;
  }

  .menu-toggle.active .bar:nth-child(1) {
    transform: rotate(-45deg) translate(-5px, 6px);
  }

  .menu-toggle.active .bar:nth-child(2) {
    opacity: 0;
  }

  .menu-toggle.active .bar:nth-child(3) {
    transform: rotate(45deg) translate(-5px, -6px);
  }
}
</style>