# -*- coding: utf-8 -*-

from konlpy.tag import Okt
from collections import Counter

# Sample Korean text (replace this with your YouTube transcript)
sample_text = "국내 코로나 일부 사망자가 천 명을 넘어섰습니다 지난해 2월 첫 사망자가 나온 지 1년도 안 됐는데 네 자릿수 사망자를 기록했습니다 특히 친한 한 달 사이 사망자가 급증했습니다 요양 시설에서 지병이 있던 고령의 환자들이 이 따라 세상을 떠나고 있습니다 힘 필중 이자 많다 구급차로 한자를 옮깁니다 이곳에서는 이달 들어서만 4명이 숨졌습니다 호라 1 9학점 단점을 받고 2주 말입니다 9 첨에 한 요양병원에서 는 10년 가까이 숨졌습니다 현재까지 전국의 요양시설 10여 곳에서 1000명 넘는 확진 자가 나왔습니다 이 가운데 대결 명이 숨졌습니다 10% 나 됩니다 코라 1 9 전체 사망률 보다 6배 가 넘습니다 모두 7 80대 고령자 입니다 원래 아이 텀 병도 있습니다 바로 치료를 받아도 위험한 상황 그런데 제 때 치료를 받지도 못했습니다 병상이 부족했기 때문 동일 집단 동리 도 문제였습니다 확증 자와 b 확진 자를 잘 9분하지 못했습니다 한사람만 걸려도 순식간에 번졌습니다 현저한 자를 가려 내 서 물른 따로 수용해야 되겠죠 혼절을 병원에 보내야 돼요 너 한 자를 빼고 난 다음에는 그 다음 사람들은 분석을 해야 됩니다 환자와 얼마나 접착에 냐에 따라 거 1 쩝 책 족자 일간 적중 특강 운 해서 정부는 뒤늦게 대책을 지나 요양 시설 등의 4 확진 자가 나오면 진급 때 응 팀을 보내기로 했습니다 불가피한 경우에만 짧게 동해의 집단 경리를 하기로 했습니다 확진 자는 곧바로 다른 곳으로 옮기기로 했습니다 뭐 약자가 계시는 요양 병원 요양 시설에서 는 확진 환자가 중증으로 악화되고 음매 사망으로 이어지는 경우가 많아 선제적인 당 역 관리가 매우 중요합니다 지금도 요양병원 등 집단 시설에서 감염은 계속되고 있습니다 고령층 사망자 대해 죽이면 확진 짤에 분리하고 팔리 치료받을 수 있는 전담 병원이나 병상을 일이 확보 있나요 jtbc 김필 중"

# Tokenization with KoNLPy
okt = Okt()
tokens = okt.pos(sample_text, stem=True, norm=True)

# Filter nouns and adjectives (you can customize this based on your requirements)
filtered_tokens = [word for word, pos in tokens if pos in ['Noun'] and len(word) > 1]

# Frequency count
word_freq = Counter(filtered_tokens)
most_freq_words = word_freq.most_common(10)

frequent_words_str = ', '.join([f"('{word}', {freq})" for word, freq in most_freq_words if freq > 1])

# Print the most common words
print(frequent_words_str)
