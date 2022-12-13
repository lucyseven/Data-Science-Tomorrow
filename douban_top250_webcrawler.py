#safaridriver --enable
import requests
import re
import csv

#reference
#https://www.bilibili.com/video/BV1YV4y1p78G/?spm_id_from=333.880.my_history.page.click&vd_source=4f0d76cc04aafd14943dfcce095cf5e6
#https://www.bilibili.com/video/BV1Nt4y1H72R/?spm_id_from=autoNext&vd_source=4f0d76cc04aafd14943dfcce095cf5e6
#tell the website it's a browser view
#accept chinese

headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
           "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.+\
           36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
           "Accept-Language": 'zh-CN,zh;q=0.9'}
    
    
    
f = open ("douban_top250_movie_data_lu.csv", mode = "a", encoding = 'utf-8-sig', newline ='')
    
csvwriter = csv.writer(f)
    
        
for i in range(0,10):
        url = f'https://movie.douban.com/top250?start={i*25}&filter='
    
    

        resp = requests.get(url, headers = headers)
        
        
        page_content = resp.text
        
        #  data
        obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                         r'<p class="">.*?<br>(?P<year>.*?)&nbsp.*?'
                         r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                         r'<span>(?P<number>.*?)</span>', re.S)
        
        #start to match
        result = obj.finditer(page_content)
        
        
        for it in result:
            # print(it.group("name"))
            # print(it.group("score"))
            # print(it.group("number"))
            # print(it.group("year").strip())
            
            dic = it.groupdict()
            dic['year'] = dic['year'].strip()
            csvwriter.writerow(dic.values())
f.close()
print("over")
