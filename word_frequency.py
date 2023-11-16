# -*- coding: utf-8 -*-

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
