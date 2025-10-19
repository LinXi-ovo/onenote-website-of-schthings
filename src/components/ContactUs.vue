<template>
  <div class="contact-us">
    <h2>联系我们</h2>
    <div class="contact-form">
      <div v-if="successMessage" class="success-message">
        {{ successMessage }}
      </div>
      <form @submit.prevent="submitForm">
        <div class="form-group" :class="{ 'has-error': errors.name }">
          <label for="name">该如何称呼您？</label>
          <input 
            type="text" 
            id="name" 
            v-model="formData.name" 
            @blur="validateField('name')"
            :class="{ 'error': errors.name }"
            required
          >
          <span v-if="errors.name" class="error-text">{{ errors.name }}</span>
        </div>
        <div class="form-group" :class="{ 'has-error': errors.email }">
          <label for="email">邮箱</label>
          <input 
            type="email" 
            id="email" 
            v-model="formData.email" 
            @blur="validateField('email')"
            :class="{ 'error': errors.email }"
            required
          >
          <span v-if="errors.email" class="error-text">{{ errors.email }}</span>
        </div>
        <div class="form-group" :class="{ 'has-error': errors.message }">
          <label for="message">留言</label>
          <textarea 
            id="message" 
            v-model="formData.message" 
            @blur="validateField('message')"
            :class="{ 'error': errors.message }"
            required
          ></textarea>
          <span v-if="errors.message" class="error-text">{{ errors.message }}</span>
        </div>
        <div class="form-actions">
          <button type="submit" :disabled="isLoading || !isFormValid" class="submit-btn">
            <span v-if="isLoading" class="loading-spinner"></span>
            {{ isLoading ? '提交中...' : '提交' }}
          </button>
          <button type="button" @click="resetForm" class="reset-btn" :disabled="isLoading">
            重置
          </button>
        </div>
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>
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
      },
      errors: {
        name: '',
        email: '',
        message: ''
      },
      isLoading: false,
      errorMessage: '',
      successMessage: '',
      isFormSubmitted: false
    }
  },
  computed: {
    isFormValid() {
      return Object.keys(this.errors).every(key => !this.errors[key]) && 
             Object.keys(this.formData).every(key => this.formData[key].trim());
    }
  },
  methods: {
    async submitForm() {
      // 验证整个表单
      if (!this.validateAllFields()) {
        return;
      }

      // 清除之前的消息
      this.errorMessage = '';
      this.successMessage = '';
      
      // 设置加载状态
      this.isLoading = true;

      try {
        // 创建提交数据
        const submissionData = {
          ...this.formData,
          timestamp: new Date().toISOString()
        };

        // 提交到后端
        await this.submitToBackend(submissionData);
        
        // 显示成功消息
        this.successMessage = '感谢您的留言，我们会尽快回复！';
        this.isFormSubmitted = true;
        
        // 重置表单
        this.resetForm();
        
        // 5秒后清除成功消息
        setTimeout(() => {
          this.successMessage = '';
        }, 5000);
        
      } catch (error) {
        console.error('提交失败:', error);
        this.errorMessage = `提交失败: ${error.message || '请稍后重试'}`;
      } finally {
        this.isLoading = false;
      }
    },
    
    validateField(field) {
      const value = this.formData[field].trim();
      
      // 清除该字段之前的错误
      this.errors[field] = '';
      
      // 验证字段
      switch (field) {
        case 'name':
          if (!value) {
            this.errors.name = '请输入您的姓名';
          }
          break;
        case 'email':
          if (!value) {
            this.errors.email = '请输入邮箱地址';
          } else if (!this.isValidEmail(value)) {
            this.errors.email = '请输入有效的邮箱地址';
          }
          break;
        case 'message':
          if (!value) {
            this.errors.message = '请输入留言内容';
          } else if (value.length < 10) {
            this.errors.message = '留言内容至少需要10个字符';
          }
          break;
      }
      
      return !this.errors[field];
    },
    
    validateAllFields() {
      let isValid = true;
      
      // 验证所有字段
      Object.keys(this.formData).forEach(field => {
        if (!this.validateField(field)) {
          isValid = false;
        }
      });
      
      return isValid;
    },
    
    isValidEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return re.test(email);
    },
    
    async submitToBackend(data) {
      try {
        // 使用环境变量中的API基础URL，如果未定义则使用默认值
        const apiBaseUrl = process.env.VUE_APP_API_BASE_URL || 'http://localhost:3000';
        const response = await fetch(`${apiBaseUrl}/api/contact`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(data)
        });

        if (!response.ok) {
          // 尝试从响应中获取错误信息
          let errorMessage = 'Network response was not ok';
          try {
            const errorData = await response.json();
            errorMessage = errorData.message || errorMessage;
          } catch (e) {
            console.warn('无法解析错误响应:', e);
          }
          throw new Error(errorMessage);
        }

        return response.json();
      } catch (error) {
        // 更详细的错误处理
        if (error.name === 'TypeError' && error.message.includes('fetch')) {
          throw new Error('无法连接到服务器，请检查网络连接');
        } else {
          throw new Error(`提交失败: ${error.message || '未知错误'}`);
        }
      }
    },
    
    resetForm() {
      this.formData = {
        name: '',
        email: '',
        message: ''
      };
      
      // 清除所有错误
      this.errors = {
        name: '',
        email: '',
        message: ''
      };
      
      // 清除消息
      this.errorMessage = '';
      this.successMessage = '';
      this.isFormSubmitted = false;
    }
  }
}
</script>

<style scoped>
.contact-us {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Arial', sans-serif;
}

h2 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 30px;
  font-weight: 600;
  font-size: 2rem;
}

.contact-form {
  background: #f9f9f9;
  padding: 25px;
  border-radius: 8px;
  margin-bottom: 30px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.form-group {
  margin-bottom: 20px;
  position: relative;
}

.form-group.has-error {
  margin-bottom: 10px;
}

label {
  display: block;
  margin-bottom: 8px;
  color: #333;
  font-weight: 500;
}

input,
textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  transition: border-color 0.3s, box-shadow 0.3s;
  box-sizing: border-box;
}

input:focus,
textarea:focus {
  border-color: #42b983;
  outline: none;
  box-shadow: 0 0 0 2px rgba(66, 185, 131, 0.2);
}

input.error,
textarea.error {
  border-color: #ff4444;
}

textarea {
  height: 120px;
  resize: vertical;
}

.form-actions {
  display: flex;
  gap: 15px;
  margin-top: 25px;
}

.submit-btn,
.reset-btn {
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.submit-btn {
  background-color: #42b983;
  color: white;
  flex-grow: 1;
}

.submit-btn:hover:not(:disabled) {
  background-color: #3aa876;
}

.reset-btn {
  background-color: #f0f0f0;
  color: #666;
}

.reset-btn:hover:not(:disabled) {
  background-color: #e0e0e0;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
  opacity: 0.7;
}

.loading-spinner {
  display: inline-block;
  width: 16px;
  height: 16px;
  margin-right: 8px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  border-top-color: #fff;
  animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-text {
  color: #ff4444;
  font-size: 14px;
  margin-top: 5px;
  display: block;
}

.error-message {
  color: #ff4444;
  margin-top: 15px;
  text-align: center;
  padding: 10px;
  background-color: rgba(255, 68, 68, 0.1);
  border-radius: 4px;
}

.success-message {
  color: #42b983;
  margin-bottom: 20px;
  text-align: center;
  padding: 12px;
  background-color: rgba(66, 185, 131, 0.1);
  border-radius: 4px;
  font-weight: 500;
}

.contact-info {
  text-align: center;
  padding: 20px;
  background: #f0f0f0;
  border-radius: 8px;
  margin-top: 30px;
}

.contact-info h3 {
  color: #2c3e50;
  margin-bottom: 15px;
  font-weight: 600;
}

.contact-info p {
  margin: 10px 0;
  color: #666;
  font-size: 16px;
}

/* 响应式设计 */
@media (max-width: 600px) {
  .contact-us {
    padding: 15px;
  }
  
  .contact-form {
    padding: 20px;
  }
  
  .form-actions {
    flex-direction: column;
  }
  
  .submit-btn,
  .reset-btn {
    width: 100%;
  }
}
</style>
