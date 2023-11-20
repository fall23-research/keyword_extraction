import sqlite3
import json

table_name = "news_video"
channel_names = ['YTN', 'SBS 뉴스', 'MBCNEWS', 'JTBC News', 'KBS News', '채널A 뉴스', 'MBN News', '뉴스TVCHOSUN', '연합뉴스TV']
channel = channel_names[8]
db_path = "/Users/siwon/Desktop/Fall-23/research/official_news_dataset/covid_news_data.sqlite"

# Connect to the existing SQLite database
conn_existing = sqlite3.connect(db_path)
cursor_existing = conn_existing.cursor()

# Execute an SQL query to retrieve the data from the specified table
cursor_existing.execute(f"SELECT freq_keywords FROM {table_name} WHERE channel_name = '{channel}'")
freq_keywords_data = cursor_existing.fetchall()


# freq_keywords 파싱 및 출력
top_keywords = []
for row in freq_keywords_data:
    first_keyword = row[0].split(",")[0][2:-1]
    top_keywords.append(first_keyword)

# 중복을 제거한 키워드의 set을 만듭니다.
unique_keywords_set = set(top_keywords)

# 각 키워드의 출현 빈도를 계산합니다.
keyword_counts = {keyword: top_keywords.count(keyword) for keyword in unique_keywords_set }

filtered_keywords = {word: count for word, count in keyword_counts.items() if count >= 2}
filtered_keywords.pop("", None)

print(filtered_keywords)

json_data = json.dumps(filtered_keywords)

# JSON 데이터 삽입
cursor_existing.execute('''
    UPDATE news_channel
    SET freq_keywords = ?
    WHERE channel_name = ?
''', (json_data, channel))

# 변경사항 저장
conn_existing.commit()

# 연결 종료
conn_existing.close()
