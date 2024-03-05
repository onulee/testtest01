from konlpy.tag import Okt
import operator  # operator.itemgetter를 사용하기 위해 모듈 임포트

news1 = '''국혁신당 초대 당 대표에 조국 전 법무부 장관이 선출됐다.
3일 새 정당 조국혁신당은 검찰 독재의 조기종식과 민주공화국 가치 회복을 기치로 내걸고 정식 창당했다.
이날 조국혁신당은 경기도 고양시 킨텍스에서 당원 등 3000여명이 참석한 가운데 중앙당 창당대회를 열고 조 전 장관을 당 대표로 추대했다.
조 대표는 수락 연설에서 재인 정부 검찰개혁의 책임자로서 정치검사의 준동을 막지 못하고 검찰 공화국 탄생을 막아내지 못한 과오에 대해 국민 여러분께 머리 숙여 사과드린다"고 밝혔다.
그는 나 조국은 결자해지의 심정으로 윤석열 검찰 독재정권을 하루빨리 종식해야 하는 소명이 운명적으로 주어졌다며 나는 돌아갈 다리를 불살랐다"고 강조했다.
이어 나는 지난 5년간 무간지옥 속에 갇혀 있었다. 온 가족이 도륙되는 상황을 견뎌야 했다"며 "피와 땀으로 지켜온 민주공화국의 가치를 
파괴하는 윤석열 정권의 역주행을 더 이상 지켜볼 수 없었다. 그래서 정치 참여를 결심하고 창당을 결심했다"고 설명했다.
조국혁신당은 현재까지 6개 시·도당에 총 5만명 넘는 당원이 모였다고 밝혔다. 이날 창당대회에는 조정식 더불어민주당 사무총장도 참석했다.
'''
okt = Okt()
news1_lists = okt.nouns(news1)

counter = {}
for news1_list in news1_lists:
    if news1_list not in counter:
        if len(news1_list)<=1:
            continue
        counter[news1_list]=0
    counter[news1_list] +=1

counter2 = sorted(counter.items(), key=operator.itemgetter(1),reverse=True)
print("-"*20)
print(dict(counter2))
print("-"*20)
        
print(counter)

#------------------------------------------------
from wordcloud import WordCloud

wc = WordCloud(font_path='C:/workspace/NanumBarunGothic.ttf', 
               background_color="white", width=1000, height=1000,max_words=100,max_font_size=300)

wc.generate_from_frequencies(counter)
wc.to_file('C:/workspace/rating.png')