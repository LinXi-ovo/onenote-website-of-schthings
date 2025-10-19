<template>
  <div class="class-schedule">
    <h1>课程表</h1>
    <div class="calendar-container">
      <table class="schedule-table">
        <thead>
          <tr>
            <th class="time-header">时间</th>
            <th v-for="date in schedule.header.dates" :key="date">{{ date }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="slot in timeSlots" :key="slot.id">
            <td class="time-slot">{{ slot.time }}</td>
            <td v-for="day in 7" :key="day" class="course-cell">
              <div v-for="course in getCoursesForSlot(slot.id, day)" 
                   :key="course.id" 
                   class="course-item"
                   :style="{ backgroundColor: course.color }">
                <div class="course-name">{{ course.name }}</div>
                <div class="course-info">{{ course.info }}</div>
                <div class="course-teacher">{{ course.teacher }}</div>
                <div class="course-location">{{ course.location }}</div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { weekSchedule } from '@/data/schedules/weekSchedule'

export default {
  data() {
    return {
      schedule: weekSchedule,
      timeSlots: [
        { id: 1, time: '第01节' },
        { id: 2, time: '第02节' },
        { id: 3, time: '第03节' },
        { id: 4, time: '第04节' },
        { id: 5, time: '第05节' },
        { id: 6, time: '第06节' },
        { id: 7, time: '第07节' },
        { id: 8, time: '第08节' },
        { id: 9, time: '第09节' },
        { id: 10, time: '第10节' },
        { id: 11, time: '第11节' },
        { id: 12, time: '第12节' },
        { id: 13, time: '第13节' },
        { id: 14, time: '第14节' }
      ]
    }
  },
  methods: {
    getCoursesForSlot(slotId, day) {
      return this.schedule.courses.filter(course => {
        const [start, end] = course.timeSlot.split('-').map(Number);
        return course.day === day && slotId >= start && slotId <= end;
      });
    }
  }
}
</script>

<style scoped>
/* 重置和基础样式 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background-color: #f5f5f5;
    line-height: 1.6;
    color: #333;
}

/* 课程表容器 */
.class-schedule {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* 标题样式 */
h1 {
    text-align: center;
    margin-bottom: 20px;
    color: #2c3e50;
    font-size: 24px;
}

/* 日历容器 */
.calendar-container {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
    overflow-x: auto;
}

/* 表格样式 */
.schedule-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    table-layout: fixed;
    min-width: 800px;
}

/* 表头样式 */
.schedule-table th {
    background: #4a90e2;
    color: white;
    padding: 12px 8px;
    text-align: center;
    font-weight: 600;
    border: 1px solid #e0e0e0;
}

.time-header {
    width: 80px;
    min-width: 80px;
}

/* 单元格样式 */
.schedule-table td {
    border: 1px solid #e0e0e0;
    padding: 8px;
    vertical-align: top;
    height: 60px;
    position: relative;
}

.time-slot {
    background: #f8f9fa;
    text-align: center;
    font-weight: 500;
    color: #666;
    width: 80px;
    min-width: 80px;
}

/* 课程项样式 */
.course-item {
    background: #e3f2fd;
    border: 1px solid #bbdefb;
    border-radius: 4px;
    padding: 4px;
    margin-bottom: 4px;
    cursor: pointer;
    transition: all 0.2s ease;
}

.course-item:hover {
    transform: translateY(-1px);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.course-name {
    font-weight: 600;
    color: #1565c0;
    font-size: 14px;
}

.course-info,
.course-teacher,
.course-location {
    font-size: 12px;
    color: #666;
    margin-top: 2px;
}

/* 响应式设计 */
@media (max-width: 768px) {
    .class-schedule {
        padding: 10px;
    }

    .schedule-table th,
    .schedule-table td {
        padding: 6px;
        font-size: 12px;
    }

    .time-header,
    .time-slot {
        width: 60px;
        min-width: 60px;
    }

    .course-name {
        font-size: 12px;
    }

    .course-info,
    .course-teacher,
    .course-location {
        font-size: 11px;
    }
}

/* 清除浮动 */
.clearfix::after {
    content: "";
    display: table;
    clear: both;
}
</style>
