import requests

#url = f"https://wttr.in/jeju?format=%C+%t"
#?format=%C+%t → 출력 포맷 설정 (%C = 날씨 상태////// %t = 기온)

url_today = "https://wttr.in/incheon?format=Weather:+%C,+Temp:+%t,+Humidity:+%h,+Wind:+%w"
#?format=%C+%t+%h+%w /날씨상태 + 기온 + 습도 + 바람
url_forecast = "https://wttr.in/incheon?3n"
#3일치 예보를 n(간단하게) 뽑을 수 있음

#현재날씨
res = requests.get(url_today)
if res.status_code ==200:
    print("[Incheon Current Weather]")
    print(res.text.strip())
else:
    print(f"상태 코드: {res.status_code}")

#성공이면 response.text.strip() (날씨 텍스트) 출력하고
#실패면 상태 코드 출력.

# 3일치 예보
res = requests.get(url_forecast)
if res.status_code == 200:
    print("\n[Incheon 3-day Forecast]")
    print(res.text.strip())
else:
    print(f"상태 코드: {res.status_code}")

# url = f"https://kin.naver.com/park"
# url = f"https://wttr.in/incheon?&n&Q"
# url = f"https://wttr.in/incheon?&0&Q"

#response = requests.get(url)
#GET 요청

#print(response)
#print(response.status_code)
#HTTP 상태 코드 출력////200 = 성공
#if response.status_code == 200:
#    print(response.text.strip())
#else:
#    print(f"상태 코드 : {response.status_code}")


