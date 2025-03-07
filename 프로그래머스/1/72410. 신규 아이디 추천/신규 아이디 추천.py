#규칙에 맞지 않는 아이디를 입력했을 때, 입력한 아이디와 유사하면서 규칙에 맞는 아이디 추천
import re
def solution(new_id):
    str=new_id.lower()
    str=re.sub('[^a-z0-9\-_.]', '',str)
    str=re.sub('\.+', '.', str)
    str=re.sub('^[.]|[.]$', '',str)
    if str=='':
        str='a'
    str=str[:15]
    str=re.sub('[.]$','',str)
    while len(str) < 3:
        str += str[-1]
    return str