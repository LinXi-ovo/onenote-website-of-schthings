<template>
    <div class="notice-container">
        <h1 class="page-title">社团招新通知</h1>
        
        <!-- AITA社团招新通知 -->
        <div class="notice-item" :class="{ 'expired': isAITAExpired }">
            <div class="notice-header" @click="toggleAITA">
                <h2>AITA社团招新结果通知</h2>
                <div class="notice-dates">
                    <div class="notice-time">发布：2025年10月19日</div>
                    <div class="notice-deadline">截止：2026年6月30日</div>
                </div>
                <span class="toggle-icon">{{ showAITA ? '▼' : '▶' }}</span>
            </div>
            <div class="notice-content" v-show="showAITA" v-html="aitaContent"></div>
        </div>

        <div class="feedback-notice">
            <p>如果信息不全，您可以<a href="#/contact">点击联系我们</a>跟我反馈，我很乐意更新上来，也感谢您的贡献！</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ClubRecruit',
    data() {
        return {
            showAITA: false,
            aitaContent: `
                <p>❗️未入选的同学可以根据我们的培养方案进行学习，今年11月～明年6月可投长期招新简历。</p>
                <p>邮箱：aita@ai.email.cn</p>
                <p>✅AITA培养方案暨自学指南：<a href="https://z0abki9lxvn.feishu.cn/docx/Rjzjd4CzqoYZ2NxVygecR3Dtn2b?from=from_copylink" target="_blank">点击查看</a></p>
                
            `
        }
    },
    computed: {
        isAITAExpired() {
            const deadline = new Date('2026-06-30');
            const today = new Date();
            return today > deadline;
        }
    },
    methods: {
        toggleAITA() {
            this.showAITA = !this.showAITA;
        }
    }
}
</script>

<style scoped>
.page-title {
    text-align: center;
    color: #2c3e50;
    margin-bottom: 30px;
    font-size: 24px;
}

.notice-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
    font-family: "Microsoft YaHei", sans-serif;
    line-height: 1.6;
}

.notice-item {
    margin-bottom: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.notice-header {
    background-color: #f5f7fa;
    padding: 15px 20px;
    display: flex;
    align-items: center;
    cursor: pointer;
    transition: background-color 0.3s;
}

.notice-header:hover {
    background-color: #e9ecf0;
}

.notice-header h2 {
    margin: 0;
    color: #2c3e50;
    font-size: 18px;
    flex-grow: 1;
}

.notice-dates {
    display: flex;
    flex-direction: column;
    margin-right: 15px;
}

.notice-time {
    color: #7f8c8d;
    font-size: 14px;
}

.notice-deadline {
    color: #e74c3c;
    font-size: 14px;
    font-weight: bold;
}

.toggle-icon {
    color: #2c3e50;
    font-size: 16px;
    margin-left: 10px;
}

.notice-content {
    padding: 20px;
    background-color: white;
}

.notice-content p {
    margin-bottom: 15px;
    color: #555;
}

.notice-content a {
    color: #3498db;
    text-decoration: none;
}

.notice-content a:hover {
    text-decoration: underline;
}

/* 过期通知样式 */
.notice-item.expired {
    opacity: 0.7;
    background-color: #f8f8f8;
}

.notice-item.expired .notice-header {
    background-color: #f0f0f0;
    text-decoration: line-through;
}

.notice-item.expired h2 {
    color: #95a5a6;
}

/* 添加过渡效果 */
.notice-content {
    transition: all 0.3s ease;
}

/* 反馈提示样式 */
.feedback-notice {
    margin-top: 20px;
    padding: 15px;
    background-color: #f8f9fa;
    border-radius: 8px;
    text-align: center;
    color: #6c757d;
    font-size: 14px;
}

.feedback-notice a {
    color: #3498db;
    text-decoration: none;
}

.feedback-notice a:hover {
    text-decoration: underline;
}
</style>