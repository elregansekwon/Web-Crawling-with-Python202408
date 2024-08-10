import requests
from bs4 import BeautifulSoup

# 1단계: 타겟 웹페이지로 GET 요청 보내기
url = 'https://example-music-site.com'  # 크롤링할 음악 웹사이트의 URL
response = requests.get(url)

# 2단계: 웹페이지의 HTML 내용 파싱하기
soup = BeautifulSoup(response.text, 'html.parser')

# 3단계: 특정 요소(예: 음악 제목, 아티스트) 찾기
# 예시로 모든 노래 제목을 가져오기
song_titles = soup.find_all('h2', class_='song-title')

# 4단계: 추출된 데이터 출력
for i, title in enumerate(song_titles, start=1):
    print(f"{i}. {title.text.strip()}")

# 추가로 필요한 기능은 여기서 구현할 수 있습니다.
