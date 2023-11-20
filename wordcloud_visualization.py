from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import sqlite3
import json

font_path = "C:/Users/siwon/AppData/Local/Microsoft/Windows/Fonts/IBMPlexSansKR-SemiBold.ttf"

# 폰트 등록
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 자주 사용된 단어를 담은 딕셔너리
table_name = "news_channel"
db_path = "/Users/siwon/Desktop/Fall-23/research/official_news_dataset/covid_news_data.sqlite"
channel_names = ['YTN', 'SBS 뉴스', 'MBCNEWS', 'JTBC News', 'KBS News', '채널A 뉴스', 'MBN News', '뉴스TVCHOSUN', '연합뉴스TV']
channel = channel_names[8]

# Connect to the existing SQLite database
conn_existing = sqlite3.connect(db_path)
cursor_existing = conn_existing.cursor()

# Execute an SQL query to retrieve the data from the specified table
cursor_existing.execute(f"SELECT freq_keywords FROM {table_name} WHERE channel_name = '{channel}'")
freq_keywords_data = cursor_existing.fetchall()[0][0]
parsed_keywords = json.loads(freq_keywords_data)

# WordCloud 객체 생성
wordcloud = WordCloud(width=800, height=400, background_color='white', font_path=font_path).generate_from_frequencies(parsed_keywords)


# 워드 클라우드를 이미지로 출력
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()