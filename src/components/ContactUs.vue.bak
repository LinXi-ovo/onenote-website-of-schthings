<template>
  <div class="contact-us">
    <h2>联系我们</h2>
    <div class="contact-form">
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="name">该如何称呼您？</label>
          <input type="text" id="name" v-model="formData.name" required>
        </div>
        <div class="form-group">
          <label for="email">邮箱</label>
          <input type="email" id="email" v-model="formData.email" required>
        </div>
        <div class="form-group">
          <label for="message">留言</label>
          <textarea id="message" v-model="formData.message" required></textarea>
        </div>
        <button type="submit">提交</button>
      </form>
    </div>
    <div class="contact-info">
      <h3>联系方式</h3>
      <p>邮箱：2809837498@qq.com</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContactUs',
  data() {
    return {
      formData: {
        name: '',
        email: '',
        message: ''
      }
    }
  },
  methods: {
    submitForm() {
      // 这里可以添加表单提交逻辑
      alert('感谢您的留言，我们会尽快回复！');
      // 重置表单
      this.formData = {
        name: '',
        email: '',
        message: ''
      }
    }
  }
}
</script>

<style scoped>
.contact-us {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

h2 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 30px;
}

.contact-form {
  background: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #333;
}

input, textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

textarea {
  height: 120px;
  resize: vertical;
}

button {
  background-color: #42b983;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #3aa876;
}

.contact-info {
  text-align: center;
  padding: 20px;
  background: #f0f0f0;
  border-radius: 8px;
}

.contact-info h3 {
  color: #2c3e50;
  margin-bottom: 15px;
}

.contact-info p {
  margin: 10px 0;
  color: #666;
}
</style>
