import re

# url 저장하는 함수
def my_url(page):
    # search 패턴과 일치하는 첫 번째 위치를 찾는 함수
    meta_tag = re.search(r'<meta property="og:url" content="(https://\S+)"/>',page)
    
    if meta_tag:
        return meta_tag.group(1)
    return None

# 단어 찾기
def word_count(word, page):
    # 대소문자 구분 없이 검색하기 위해 모두 소문자로 변환
    word = word.lower()
    
    # HTML 태그 제거 (내용만 추출)
    content = re.sub(r'<[^>]+>', ' ', page).lower()
    
    # 알파벳이 아닌 문자를 공백으로 변환하여 단어 경계 처리
    content = re.sub(r'[^a-z]', ' ', content)
    
    # 단어 분리 후 카운트
    words = content.split()
    count = words.count(word)
    
    return count

# 외부 링크 찾기

def extract_links(page):
    links = re.findall(r'<a href="(https://\S+)"', page)
    return links

# url 비교하기
def url_count(pages, pages_url, basic_score):
    link_score = [0]*len(pages_url)
    
    for i, page in enumerate(pages):
        links = extract_links(page)
        if links: # 외부 링크 페이지가 있다면
            link_count = len(links)
            #각 링크에 해당하는 페이지에 점수 부여
            for link in links:
                if link in pages_url:
                    idx = pages_url.index(link)
                    link_score[idx] += basic_score[i] / link_count
                    
            
    return link_score

def solution(word, pages):
    
    answer = 0
    pages_url = [] # 각 페이지의 url을 담았음 a.com, b.com
    basic_score = [] # 기본 점수 3,1,1
    link_score = [] # 링크 점수 
    
    
    # [1] 기본점수와 외부링크 정리
    for i in range(len(pages)):
        basic_score.append(word_count(word,pages[i]))    
    
    # [2] 각 페이지의 url 저장
    for page in pages:
        url = my_url(page)
        pages_url.append(url)
        
    # [3] 링크 점수
    link_score = url_count(pages,pages_url,basic_score)
    
    match_score=[]
    
    for i in range(len(pages)):
        match_score.append(basic_score[i]+link_score[i])
    
    max_score = max(match_score)
    answer = match_score.index(max_score)
    return answer

