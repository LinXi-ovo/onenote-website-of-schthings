<template>
  <div class="page-container">
    <h1 class="page-title">友情通知</h1>
    <div class="card">
      <h2>敬请期待</h2>
      <p>这个页面正在建设中，我们很快会为您带来精彩的内容！</p>
    </div>
    <div class="card">
      <h2>特别鸣谢</h2>
      <p>感谢所有支持和赞助本项目的个人和组织：</p>
      <ul>
        <li>感谢学校信息技术部门提供的技术支持</li>
        <li>感谢所有参与测试和提供反馈的同学们</li>
        <li>感谢开源社区提供的优秀工具和框架</li>
      </ul>
      <p>因为有你们，这个平台才能不断进步和完善！</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FriendlyNotice',
  data() {
    return {
      // 这里可以添加数据
    }
  }
}
</script>

<style scoped>
.card {
  margin-bottom: 30px;
}

.card h2 {
  color: #2c3e50;
  margin-bottom: 15px;
  font-size: 1.5rem;
}

.card p {
  margin-bottom: 15px;
  line-height: 1.6;
}

.card ul {
  margin-left: 20px;
  margin-bottom: 15px;
}

.card li {
  margin-bottom: 8px;
}
</style>
