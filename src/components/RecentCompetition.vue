<template>
    <div class="notice-container">
        <!-- 最近比赛通知 -->
        <div class="notice-item" :class="{ 'expired': isCompetitionExpired }">
            <div class="notice-header" @click="toggleCompetition">
                <h2>{{ competitions[0].title }}</h2>
                <div class="notice-dates">
                    <div class="notice-time">发布：{{ competitions[0].publishDate }}</div>
                    <div class="notice-deadline">截止：{{ competitions[0].deadline }}</div>
                </div>
                <span class="toggle-icon">{{ showCompetition ? '▼' : '▶' }}</span>
            </div>
            <div class="notice-content" v-show="showCompetition" v-html="competitions[0].content">
            <h2>一、申报对象</h2>
            <p>全校本科生，以团队形式申报，每个团队3-5人，鼓励跨专业、跨年级组队。</p>
            
            <h2>二、申报时间</h2>
            <p>2025年10月25日-2025年11月15日</p>
            
            <h2>三、项目类型</h2>
            <ul>
                <li>创新训练项目</li>
                <li>创业训练项目</li>
                <li>创业实践项目</li>
            </ul>
            
            <h2>四、申报材料</h2>
            <ol>
                <li>《大学生创新训练计划项目申报书》</li>
                <li>项目计划书</li>
                <li>指导教师推荐意见</li>
            </ol>
            
            <h2>五、申报流程</h2>
            <ol>
                <li>团队组建与选题</li>
                <li>联系指导教师</li>
                <li>提交申报材料</li>
                <li>学院初审</li>
                <li>学校评审</li>
            </ol>
            
            <h2>六、联系方式</h2>
            <p>联系人：教务处创新教育科</p>
            <p>联系电话：020-12345678</p>
            <p>电子邮箱：cxcy@gdut.edu.cn</p>
            <p>办公地点：行政楼302室</p>
            
            <div class="notice-footer">
                <p>请各学院积极组织学生申报，确保项目质量。</p>
                <p>教务处</p>
            </div>
        </div>
        </div>

        <!-- 大一四级笔试考试通知 -->
        <div class="notice-item" :class="{ 'expired': isExamExpired }">
            <div class="notice-header" @click="toggleExam">
                <h2>{{ competitions[1].title }}</h2>
                <div class="notice-dates">
                    <div class="notice-time">发布：{{ competitions[1].publishDate }}</div>
                    <div class="notice-deadline">截止：{{ competitions[1].deadline }}</div>
                </div>
                <span class="toggle-icon">{{ showExam ? '▼' : '▶' }}</span>
            </div>
            <div class="notice-content" v-show="showExam" v-html="competitions[1].content"></div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'RecentCompetition',
    data() {
        return {
            showCompetition: false,
            showExam: false,
            competitions: [
                {
                    title: '2026年校级大学生创新训练计划项目申报',
                    publishDate: '2025年10月20日',
                    deadline: '2025年11月15日',
                    content: `
                        <h2>一、申报对象</h2>
                        <p>全校本科生，以团队形式申报，每个团队3-5人，鼓励跨专业、跨年级组队。</p>

                        <h2>二、申报时间</h2>
                        <p>2025年10月25日-2025年11月15日</p>

                        <h2>三、项目类型</h2>
                        <ul>
                            <li>创新训练项目</li>
                            <li>创业训练项目</li>
                            <li>创业实践项目</li>
                        </ul>

                        <h2>四、申报材料</h2>
                        <ol>
                            <li>《大学生创新训练计划项目申报书》</li>
                            <li>项目计划书</li>
                            <li>指导教师推荐意见</li>
                        </ol>

                        <h2>五、申报流程</h2>
                        <ol>
                            <li>团队组建与选题</li>
                            <li>联系指导教师</li>
                            <li>提交申报材料</li>
                            <li>学院初审</li>
                            <li>学校评审</li>
                        </ol>

                        <h2>六、联系方式</h2>
                        <p>联系人：教务处创新教育科</p>
                        <p>联系电话：020-12345678</p>
                        <p>电子邮箱：cxcy@gdut.edu.cn</p>
                        <p>办公地点：行政楼302室</p>

                        <div class="notice-footer">
                            <p>请各学院积极组织学生申报，确保项目质量。</p>
                            <p>教务处</p>
                        </div>
                    `
                },
                {
                    title: '2025年下半年大一四级笔试考试通知',
                    publishDate: '2025年10月19日',
                    deadline: '2025年12月19日',
                    content: `
                        <h2>一、考试时间</h2>
                        <p>2025年12月19日（星期六）上午 9:00-11:20</p>

                        <h2>二、考试地点</h2>
                        <p>一号教学楼、二号教学楼（具体考场安排见准考证）</p>

                        <h2>三、考生须知</h2>
                        <ol>
                            <li>考生须携带本人身份证和学生证参加考试，缺一不可</li>
                            <li>考生须自备2B铅笔、橡皮、黑色签字笔等考试用品</li>
                            <li>考生须提前30分钟到达考场，开考15分钟后禁止入场</li>
                            <li>考试期间考生须关闭手机等通讯设备，违者按作弊处理</li>
                        </ol>

                        <h2>四、听力设备要求</h2>
                        <p>本次考试采用红外耳机进行听力播放，请各位考生提前准备好红外耳机并确保功能正常。<strong>注意：本次考试不使用调频耳机，请勿准备。</strong></p>

                        <h2>五、准考证领取</h2>
                        <p>请各班学习委员于12月10日前到教务处领取本班准考证</p>

                        <h2>六、联系方式</h2>
                        <p>联系人：教务处考试管理科</p>
                        <p>联系电话：020-87654321</p>
                        <p>电子邮箱：ksk@gdut.edu.cn</p>

                        <div class="notice-footer">
                            <p>请各位考生认真阅读通知，提前做好准备。</p>
                            <p>教务处</p>
                        </div>
                    `
                }
            ]
        }
    },
    computed: {
        isCompetitionExpired() {
            const deadline = new Date('2025-11-15');
            const today = new Date();
            return today > deadline;
        },
        isExamExpired() {
            const deadline = new Date('2025-12-19');
            const today = new Date();
            return today > deadline;
        }
    },
    methods: {
        toggleCompetition() {
            this.showCompetition = !this.showCompetition;
        },
        toggleExam() {
            this.showExam = !this.showExam;
        }
    }
}
</script>

<style scoped>
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
    padding: 0 20px 20px 20px;
    background-color: white;
}

.notice-content h2 {
    color: #34495e;
    margin-top: 25px;
    margin-bottom: 15px;
    font-size: 18px;
    border-bottom: 1px solid #eee;
    padding-bottom: 5px;
}

p, li {
    margin-bottom: 10px;
    color: #555;
}

ul, ol {
    padding-left: 25px;
    margin-bottom: 15px;
}

.notice-footer {
    margin-top: 30px;
    text-align: right;
    color: #666;
}

.notice-footer p {
    margin-bottom: 5px;
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
</style>