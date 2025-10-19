<template>
  <div class="home-page">
    <section class="hero-section">
      <div class="hero-content">
        <h1 class="hero-title">学术资源中心</h1>
        <p class="hero-subtitle">您的学习、竞赛与社团活动一站式平台</p>
        <div class="hero-buttons">
          <button class="btn-primary" @click="navigateToPage('onlineClassTaskWebsite')">查看线上作业</button>
          <button class="btn-secondary" @click="navigateToPage('RecentCompetition')">最新比赛信息</button>
        </div>
      </div>
      <div class="hero-image">
        <img src="../assets/hero-image.svg" alt="学习资源" v-if="false">
        <div class="placeholder-image">
          <div class="icon-container">
            <div class="icon book"></div>
            <div class="icon pencil"></div>
            <div class="icon laptop"></div>
          </div>
        </div>
      </div>
    </section>

    <section class="features-section">
      <h2 class="section-title">功能特色</h2>
      <div class="features-grid">
        <div class="feature-card" @click="navigateToPage('onlineClassTaskWebsite')">
          <div class="feature-icon">📚</div>
          <h3>线上作业</h3>
          <p>便捷查看和提交各科作业，不错过任何截止日期</p>
        </div>
        <div class="feature-card" @click="navigateToPage('TodoList')">
          <div class="feature-icon">✅</div>
          <h3>任务清单</h3>
          <p>高效管理您的学习任务，提升时间管理能力</p>
        </div>
        <div class="feature-card" @click="navigateToPage('ClubRecruit')">
          <div class="feature-icon">👥</div>
          <h3>社团招新</h3>
          <p>了解最新社团招新信息，找到志同道合的伙伴</p>
        </div>
        <div class="feature-card" @click="navigateToPage('RecentCompetition')">
          <div class="feature-icon">🏆</div>
          <h3>竞赛信息</h3>
          <p>获取最新学科竞赛资讯，挑战自我，展示才华</p>
        </div>
        <div class="feature-card" @click="navigateToPage('ClassSchedule')">
          <div class="feature-icon">📅</div>
          <h3>课程表查询</h3>
          <p>随时查看课程安排，合理规划学习时间</p>
        </div>
        <div class="feature-card" @click="navigateToPage('ContactUs')">
          <div class="feature-icon">📧</div>
          <h3>联系我们</h3>
          <p>有任何问题或建议？欢迎与我们联系</p>
        </div>
      </div>
    </section>

    <section class="stats-section">
      <div class="stats-container">
        <div class="stat-item">
          <div class="stat-number">500+</div>
          <div class="stat-label">活跃用户</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">100+</div>
          <div class="stat-label">线上作业</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">20+</div>
          <div class="stat-label">合作社团</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">30+</div>
          <div class="stat-label">年度竞赛</div>
        </div>
      </div>
    </section>

    <section class="cta-section">
      <div class="cta-content">
        <h2>加入我们的学习社区</h2>
        <p>与志同道合的伙伴一起学习、成长、挑战自我</p>
        <button class="btn-primary" @click="navigateToPage('ContactUs')">立即加入</button>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  methods: {
    navigateToPage(pageName) {
      this.$emit('changePage', pageName);
    }
  }
}
</script>

<style scoped>
.home-page {
  width: 100%;
  min-height: calc(100vh - 70px);
  background-color: #f8f9fa;
}

/* Hero Section */
.hero-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 60px 5%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  overflow: hidden;
}

.hero-content {
  max-width: 50%;
  animation: fadeInUp 0.8s ease;
}

.hero-title {
  font-size: 3.2rem;
  font-weight: 700;
  margin-bottom: 20px;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 1.4rem;
  margin-bottom: 30px;
  opacity: 0.9;
}

.hero-buttons {
  display: flex;
  gap: 20px;
}

.btn-primary, .btn-secondary {
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background-color: white;
  color: #667eea;
}

.btn-primary:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}

.btn-secondary {
  background-color: transparent;
  color: white;
  border: 2px solid white;
}

.btn-secondary:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

.hero-image {
  width: 45%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.placeholder-image {
  width: 100%;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.icon-container {
  position: relative;
  width: 300px;
  height: 300px;
}

.icon {
  position: absolute;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.2);
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 40px;
  animation: float 6s ease-in-out infinite;
}

.icon.book {
  top: 20px;
  left: 110px;
  animation-delay: 0s;
}

.icon.pencil {
  top: 150px;
  left: 40px;
  animation-delay: 2s;
}

.icon.laptop {
  top: 150px;
  right: 40px;
  animation-delay: 4s;
}

/* Features Section */
.features-section {
  padding: 80px 5%;
  text-align: center;
}

.section-title {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 60px;
  position: relative;
  display: inline-block;
}

.section-title::after {
  content: '';
  position: absolute;
  bottom: -10px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 2px;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

.feature-card {
  background-color: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
  cursor: pointer;
}

.feature-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 20px;
}

.feature-card h3 {
  font-size: 1.5rem;
  color: #2c3e50;
  margin-bottom: 15px;
}

.feature-card p {
  color: #6c757d;
  line-height: 1.6;
}

/* Stats Section */
.stats-section {
  background-color: #f8f9fa;
  padding: 60px 5%;
}

.stats-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  max-width: 1000px;
  margin: 0 auto;
}

.stat-item {
  text-align: center;
  padding: 20px;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #667eea;
  margin-bottom: 10px;
}

.stat-label {
  font-size: 1.1rem;
  color: #6c757d;
}

/* CTA Section */
.cta-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 80px 5%;
  text-align: center;
  color: white;
}

.cta-content h2 {
  font-size: 2.5rem;
  margin-bottom: 20px;
}

.cta-content p {
  font-size: 1.2rem;
  margin-bottom: 30px;
  opacity: 0.9;
}

.cta-section .btn-primary {
  background-color: white;
  color: #667eea;
}

/* Animations */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes float {
  0% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-20px);
  }
  100% {
    transform: translateY(0px);
  }
}

/* Responsive Design */
@media (max-width: 992px) {
  .hero-section {
    flex-direction: column;
    text-align: center;
  }

  .hero-content {
    max-width: 100%;
    margin-bottom: 40px;
  }

  .hero-image {
    width: 100%;
  }

  .hero-title {
    font-size: 2.5rem;
  }

  .hero-subtitle {
    font-size: 1.2rem;
  }

  .features-grid {
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  }
}

@media (max-width: 768px) {
  .hero-section {
    padding: 40px 5%;
  }

  .hero-title {
    font-size: 2rem;
  }

  .hero-subtitle {
    font-size: 1rem;
  }

  .hero-buttons {
    flex-direction: column;
    align-items: center;
  }

  .btn-primary, .btn-secondary {
    width: 200px;
  }

  .section-title {
    font-size: 2rem;
  }

  .stats-container {
    flex-direction: column;
  }

  .stat-item {
    margin-bottom: 20px;
  }

  .cta-content h2 {
    font-size: 2rem;
  }
}
</style>