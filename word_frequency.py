# -*- coding: utf-8 -*-

"""
transcript가 들어오면 자주 사용된 keywords TOP 10개를 추출해서 DB에 저장하는 코드
TOP 10개 output format: [('요양', 6), ('확진', 6), ('사망자', 5), ('시설', 5), ('병원', 5), ('환자', 3), ('집단', 3), ('고령', 2), ('자가', 2), ('치료', 2)]
* 10개 추출 시 단어가 1자리 (e.g. 개, 명, 달)인 것은 제외
* 최종 10개 빈도수가 1번인거는 아예 제거해서 마지막 결과가 10개 미만이 될 수 있음
* sqlite db 안에 output format인 배열을 그대로 넣기 위해 line 46에서 array -> string 처리를 해주어서 이후 이 값을 코드에서 재사용할 시 parsing하는 작업이 필요함
"""

from konlpy.tag import Okt
from collections import Counter
import sqlite3

table_name = "news_covid_video"
db_path = "/Users/siwon/Desktop/Fall-23/research/official_news_dataset/news_dataset.sqlite"

# Connect to the existing SQLite database
conn_existing = sqlite3.connect(db_path)
cursor_existing = conn_existing.cursor()

# Execute an SQL query to retrieve the data from the specified table
cursor_existing.execute(f'SELECT video_id, text_display FROM {table_name}')
transcripts = cursor_existing.fetchall()

# Close the read-only database connection
conn_existing.close()

# Connect to the same database for updating
conn_update = sqlite3.connect(db_path)
cursor_update = conn_update.cursor()

# Tokenization with KoNLPy
okt = Okt()

for video_id, transcript in transcripts:
    tokens = okt.pos(transcript, stem=True, norm=True)

    # Filter nouns and adjectives (you can customize this based on your requirements)
    filtered_tokens = [word for word, pos in tokens if pos in ['Noun'] and len(word) > 1]

    # Frequency count
    word_freq = Counter(filtered_tokens)
    most_freq_words = word_freq.most_common(10)

    frequent_words_str = ', '.join([f"('{word}', {freq})" for word, freq in most_freq_words if freq > 1])

    # frequent_words 컬럼 업데이트
    update_query = f"UPDATE your_table_name SET frequent_words = '{frequent_words_str}' WHERE video_id = '{video_id}';"
    cursor_update.execute(update_query)

conn_update.close()
