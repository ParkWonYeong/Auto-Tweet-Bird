# Auto-Tweet-Bird

This is an automatic tweet response project based on Python in 2021.
I created a server by installing Ubuntu on the AWS EC2 instance.
Then, established a program that responds to Mentions with keywords in the Twitter API account approved by the Developer Platform.
I used the jupiter notebook environment to implement the response.

## Goals

* The function that was planned to be implemented.
  - **Random Response**
    + The server is up and running, so it provides a 24-hour response.

  - **Reserved Tweets**
    + You can also upload regular tweets, not replies, at specific times.


## Implementation System

* Random Response
  - It is auto_bot function about Random Response.
  - The Answers are saved on the Google sheet.
  - Skip if the keyword is not in the answer.

  ```
  
  def auto_bot():
    print(mention.full_text)  # print the mention's text
    k=3
    for k in range(3, 39): #range(3, final n +2)
        #Tweet + Time(Korea)
        now = datetime.datetime.now()
        korea_time = now + timedelta(hours=9)
        t = str(korea_time.strftime("%Y-%m-%d %H:%M:%S"))
        if KW[k] in mention.full_text: # if mentioned tweet include keyword
            print("ID for the mention above: " + str(mention.id))
            row_data = worksheet.row_values(k+3)[2:] # keyword answer
            print(row_data)
            last_scanned_id = mention.id
            write_last_id(last_scanned_id, id_file)
            AN = random.choice(row_data)
            try:
                api.update_status("@" + mention.user.screen_name + " " + AN + "\n\n[" + t
                                              + "]", in_reply_to_status_id=mention.id)
            except tweepy.errors.Forbidden:
                pass
            print("Replied to @" + mention.user.screen_name + ' ' + AN)
            target_content = "True"
            time.sleep(60)
           
            break
            
        elif k<38 : # k < final n + 1
            print("@" + mention.user.screen_name + ' 의 답변에서 '
                  + 'B%d번째 ' % (k) + '키워드를 찾을 수 없음')
            target_content = "True"
            k = k+1
            

        else: # else, tweet disclude keyword
            print("@" + mention.user.screen_name + ' 의 답변에서 '
                  + '키워드가 존재하지 않음')
            last_scanned_id = mention.id
            write_last_id(last_scanned_id, id_file)
            target_content = "True"
            time.sleep(60)
            break
        
  ```
  
* Reserved Tweets
  - It is auto_bot function about Random Response.
  - The Answers are saved on the Google sheet.
  - Skip if the keyword is not in the answer.

  ```
  def job():
      ## call particular sheet ##
      cell_data = worksheet.acell('C3').value # select Excel sheet Written Tweet
      print(cell_data)
      api.update_status(cell_data)

  schedule.every().day.at("18:19").do(job) #time
  ```
  

## Conclusion
- Overall, I was satisfied with the requirements of the desired functionality,
  but there were some errors in the process of printing images and text together.
- Scheduled tweets are already available free of charge in a Twitter PC environment, so we've focused on the implementation experience.
- I could see the principles of the various autobots currently used on Twitter.
