import requests

city = "Daegu"
url = f"https://wttr.in/{city}?format=%C+%t"
# url = f"https://kin.naver.com/park"
# url = f"https://wttr.in/incheon?&n&Q"
# url = f"https://wttr.in/incheon?&0&Q"

# response = requests.get(url)
# print(response)
# print(response.status_code)

# if response.status_code == 200:
#     print(response.text.strip())
# else:
#     print(f"상태 코드 : {response.status_code}")

response = requests.get(url)

if response.status_code == 200:
    weather = response.text.strip()
    print(f"{city}의 날씨는 {weather} 입니다.")
else:
    print(f"날씨 정보를 가져오지 못했습니다. 상태 코드: {response.status_code}")