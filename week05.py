import requests


# # 나라 이름 치고 옵션설정 
# url = f"https://wttr.in/jeju?format=%C+%t"
# 도시랑 아이콘 
# https://github.com/chubin/wttr.in
url = f"https://wttr.in/Sapporo?format=3" 
# url = f"https://kin.naver.com/park"
# url = f"https://wttr.in/incheon?&n&Q"
# url = f"https://wttr.in/incheon?&0&Q"
response = requests.get(url)
print(response)
print(response.status_code)
if response.status_code == 200:
    print(response.text.strip())
else:
    print(f"상태 코드 : {response.status_code}")
