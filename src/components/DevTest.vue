<template>
    <div class="contact-us">
      <h2>联系我们</h2>
      <div class="contact-form">
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="name">姓名</label>
            <input type="text" id="name" v-model="formData.name" required>
            <span class="error" v-if="errors.name">{{ errors.name }}</span>
          </div>
          <div class="form-group">
            <label for="email">邮箱</label>
            <input type="email" id="email" v-model="formData.email" required>
            <span class="error" v-if="errors.email">{{ errors.email }}</span>
          </div>
          <div class="form-group">
            <label for="phone">电话</label>
            <input type="tel" id="phone" v-model="formData.phone" required>
            <span class="error" v-if="errors.phone">{{ errors.phone }}</span>
          </div>
          <div class="form-group">
            <label for="message">留言</label>
            <textarea id="message" v-model="formData.message" required></textarea>
            <span class="error" v-if="errors.message">{{ errors.message }}</span>
          </div>
          <button type="submit" :disabled="isSubmitting">
            {{ isSubmitting ? '提交中...' : '提交' }}
          </button>
        </form>
      </div>
      <div class="contact-info">
        <h3>联系方式</h3>
        <p>电话：123-456-7890</p>
        <p>邮箱：contact@example.com</p>
        <p>地址：示例地址123号</p>
      </div>
      <!-- 添加提交状态提示 -->
      <div v-if="submitStatus" :class="['submit-status', submitStatus.type]">
        {{ submitStatus.message }}
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
          phone: '',
          message: ''
        },
        errors: {},
        isSubmitting: false,
        submitStatus: null
      }
    },
    methods: {
      validateForm() {
        this.errors = {};
        
        if (!this.formData.name.trim()) {
          this.errors.name = '请输入姓名';
        }
        
        if (!this.formData.email.trim()) {
          this.errors.email = '请输入邮箱';
        } else if (!this.isValidEmail(this.formData.email)) {
          this.errors.email = '请输入有效的邮箱地址';
        }
        
        if (!this.formData.phone.trim()) {
          this.errors.phone = '请输入电话号码';
        } else if (!this.isValidPhone(this.formData.phone)) {
          this.errors.phone = '请输入有效的电话号码';
        }
        
        if (!this.formData.message.trim()) {
          this.errors.message = '请输入留言内容';
        }
        
        return Object.keys(this.errors).length === 0;
      },
      
      isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
      },
      
      isValidPhone(phone) {
        return /^[\d\s-()]+$/.test(phone);
      },
      
      
      async submitForm() {
        if (!this.validateForm()) {
            return;
        }
        
        this.isSubmitting = true;
        
        try {
            const response = await fetch('http://localhost:3000/api/contact', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.formData)
            });
            
            if (!response.ok) {
            throw new Error('提交失败');
            }
            
            this.submitStatus = {
            type: 'success',
            message: '感谢您的留言，我们会尽快回复！'
            };
            
            // 重置表单
            this.formData = {
            name: '',
            email: '',
            phone: '',
            message: ''
            };
            
        } catch (error) {
            this.submitStatus = {
            type: 'error',
            message: '提交失败，请稍后重试'
            };
        } finally {
            this.isSubmitting = false;
            
            // 3秒后清除状态提示
            setTimeout(() => {
            this.submitStatus = null;
            }, 3000);
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
  
  .error {
    color: #ff4444;
    font-size: 14px;
    margin-top: 5px;
    display: block;
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
  
  button:disabled {
    background-color: #cccccc;
    cursor: not-allowed;
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
  
  .submit-status {
    margin-top: 20px;
    padding: 10px;
    border-radius: 4px;
    text-align: center;
  }
  
  .submit-status.success {
    background-color: #d4edda;
    color: #155724;
  }
  
  .submit-status.error {
    background-color: #f8d7da;
    color: #721c24;
  }
  </style>
  