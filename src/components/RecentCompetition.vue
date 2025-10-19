<template>
    <div class="competition-notice">
        <h1>2026年校级大学生创新训练计划项目申报通知</h1>
        <div class="notice-content">
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
                <p>2025年10月20日</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'RecentCompetition',
    data() {
        return {
            // 可以在这里添加数据属性
        }
    }
}
</script>

<style scoped>
.competition-notice {
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
</style>