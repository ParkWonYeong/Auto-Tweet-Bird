import gspread
from oauth2client.service_account import ServiceAccountCredentials

#랜덤 키워드 시트
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

#json 파일명 적기
json_file_name = 'twitter-bot-12-aaa4a11846e0.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)

gc = gspread.authorize(credentials)

#문서 url 적기
spreadsheet_url = 'https://docs.google.com/spreadsheets/your_spreadsheed_url'

# 스프레드시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택하기
worksheet = doc.worksheet('KeyWord(TabName)')

