#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 作业1

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

cookie = '__mta=145070987.1595758244099.1595758296920.1595758356932.5; uuid_n_v=v1; uuid=433F6110CF2811EABF2811F0086C462EE0F4C0061CCA40F990B26644A7B6D706; _csrf=64ff3298da507f09f0911d9428813c5140a3da0f6dec4431308bdaff88d84951; mojo-uuid=3bfc10f8b84214f980927c74343b56c4; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595758244; _lxsdk_cuid=1738a9a709cc8-02baca730d2198-15336650-1fa400-1738a9a709dc8; _lxsdk=433F6110CF2811EABF2811F0086C462EE0F4C0061CCA40F990B26644A7B6D706; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595775064; __mta=145070987.1595758244099.1595758356932.1595775064643.6; _lxsdk_s=1738bbe79bc-510-3f1-954%7C%7C1'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
headers = {
    "User-Agent": user_agent,
    "Cookie": cookie
  }


url = "https://maoyan.com/films?showType=3"

response = requests.get(url, headers=headers)
bs_info = bs(response.text, 'html.parser')

result_list = []
for item in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    if len(result_list) == 10:
        break

    titles = item.find_all('div', attrs={'movie-hover-title'})

    movie_info = {
        "name": titles[0].find('span').text,
        "movie_type": titles[1].find_all(text=True)[2].strip(),
        "online_time": titles[3].find_all(text=True)[2].strip()
    }

    result_list.append(movie_info)

movie_df = pd.DataFrame(data=result_list)
movie_df.to_csv('./result1.csv', encoding='utf8', index=False, header=False)



