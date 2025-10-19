<template>
    <div class="online-tasks">
        <h1>线上作业与考试</h1>

        <div class="urgent-notice">
            <h2>重要通知：实验室准入考试</h2>
            <div class="notice-content">
                <p>请25级班委转发通知同学：实验室准入考试仍有大部分新生未完成考试，请再次提醒学生尽快完成，以免对之后的教学实验课程造成影响。</p>
                <p>《关于开展揭阳校区2025年实验室安全知识在线学习与考试的通知》已发布（<a href="https://jyxq.gdut.edu.cn/info/1065/5909.htm" target="_blank">查看详情</a>）。</p>
                <div class="notice-requirements">
                    <h3>要求：</h3>
                    <ol>
                        <li>请各系部通知25级新生进行学习、考试</li>
                        <li>参与学习人员需在线学习通过后方可进行考试</li>
                        <li>安全考试不通过者不予进入实验室进行实验</li>
                        <li>学生考试合格后，在"实验室安全考试系统"下载《实验室安全考试合格证书》及《实验室安全承诺书》</li>
                        <li>经本人签名后，以班级为单位于11月16日前送交行政楼307设备设施管理办公室备案</li>
                    </ol>
                </div>
            </div>
        </div>

        <div class="platform-links">
            <h2>常用平台链接</h2>
            <div class="links-container">
                <a
                v-for="link in links"
                :key="link.id"
                :href="link.url"
                class="nav-link"
                :target="link.id === 4 ? '_self' : '_blank'"
                >
                {{ link.text }}
                </a>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'OnlineClassTaskWebsite',
    data() {
        return {
            links: [
                { id:1, text: '智慧树', url: 'https://coursehome.zhihuishu.com/courseHome/1000069995#teachTeam' },
                { id:2, text: 'anyview', url: 'https://anyview.gdut.edu.cn/' },
                { id:3, text: 'Classvia', url: 'https://classviva.hkust-gz.edu.cn/login/index.php' },
                {id:4, text: '调整本地集成网页(旧)(dev)', url: "vuecli-vue2-brand1/public/各种汇总/点我开始.html"},
                { id:998, text: '等你添加更多', url: '#' }
            ]
        };
    }
}
</script>

<style scoped>
.online-tasks {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
    font-family: "Microsoft YaHei", sans-serif;
    line-height: 1.6;
}

h1 {
    text-align: center;
    color: #2c3e50;
    margin-bottom: 30px;
    font-size: 24px;
}

h2 {
    color: #34495e;
    margin-top: 25px;
    margin-bottom: 15px;
    font-size: 20px;
    border-bottom: 1px solid #eee;
    padding-bottom: 5px;
}

h3 {
    color: #34495e;
    margin-top: 15px;
    margin-bottom: 10px;
    font-size: 18px;
}

.urgent-notice {
    background-color: #fff3cd;
    border: 1px solid #ffeeba;
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 30px;
}

.notice-content p {
    margin-bottom: 15px;
    color: #856404;
}

.notice-requirements {
    margin-top: 15px;
}

.notice-requirements ol {
    padding-left: 25px;
    margin-bottom: 15px;
}

.notice-requirements li {
    margin-bottom: 8px;
    color: #856404;
}

.platform-links {
    margin-top: 30px;
}

.links-container {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-top: 15px;
}

.nav-link {
    display: inline-block;
    padding: 8px 15px;
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    color: #42b983;
    text-decoration: none;
    transition: all 0.3s ease;
}

.nav-link:hover {
    background-color: #e9ecef;
    transform: translateY(-2px);
}

a {
    color: #42b983;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
</style>