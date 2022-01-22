import tweepy
from time import sleep
import time
from tweepy.models import Media
from googlesheetRabbit import *
from time import process_time
from urllib.parse import scheme_chars
from twython import Twython

AK = "" 
AKS = ""

AT = ""
ATS = ""

# Authenticate to Twitter
auth = tweepy.OAuthHandler(AK, AKS)
auth.set_access_token(AT, ATS)

# Create API object
api = tweepy.API(auth)
sleep_on_rate_limit=False 

for i in range(20):
    media = api.media_upload('./High/{}.png'.format(i+1)) #사진 파일 이름(사진은 전부 최상위 폴더에 넣어두기
    cell_data = worksheet.acell('C{}'.format(i+3)).value #트윗할 내용이 적힌 엑셀의 칸 
    print(cell_data)
    api.update_status(cell_data, media_ids=[media.media_id])
    time.sleep(40)
