from bs4 import BeautifulSoup
import json
import re

def parse_html_to_json(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 提取日期信息
    dates = []
    header_cells = soup.select('thead th.fc-agenda-days th[class*="fc-"]')
    for cell in header_cells:
        dates.append(cell.text.strip())
    
    # 初始化结果字典
    result = {
        'header': {
            'dates': dates
        },
        'courses': []
    }
    
    # 提取课程信息
    events = soup.select('div.fc-event')
    for event in events:
        # 获取课程ID
        course_id = event.select_one('a[onclick]')['onclick'].split("'")[1]
        
        # 获取课程基本信息
        title_divs = event.select('div.fc-event-title > div')
        name = title_divs[0].text.strip()
        info = title_divs[1].text.strip()
        teacher = title_divs[2].text.strip()
        location = title_divs[3].text.strip().replace('...', '')
        
        # 获取时间信息
        time_slot = event.select_one('div.fc-event-time').text.strip()
        
        # 从style属性中提取left值
        style = event.get('style', '')
        left_match = re.search(r'left:\s*(\d+)px', style)
        left_position = int(left_match.group(1)) if left_match else 0
        
        # 根据位置计算是星期几
        day = (left_position - 62) // 129 + 1  # 62是起始位置，129是每天的宽度
        
        # 解析时间段
        start, end = map(int, time_slot.split('-'))
        # 修正时间段，结束时间减1
        corrected_time_slot = f"{start:02d}-{end-1:02d}"
        
        # 添加到结果中
        result['courses'].append({
            'id': course_id,
            'name': name,
            'info': info,
            'teacher': teacher,
            'location': location,
            'timeSlot': corrected_time_slot,
            'day': day,
            'color': '#AEEEEE'
        })
    
    return result

# 读取HTML文件
with open('orginHtml.txt', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 转换并保存为JSON
result = parse_html_to_json(html_content)
with open('HtmlToJson.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
