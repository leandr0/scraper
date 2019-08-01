# -*- coding: utf-8 -*-
#!/usr/bin/python3
import re
import sys
import os
import sys
import requests
import regex
import sys
import time
import random

li_at = 'AQEDAQHDpq0EVIPIAAABbAHq-rYAAAFsSljYZE4AXjZ7Bmpk2pHMMqGlx-O3iozxKCbZquK6aSjG98q9rYvqVLmztHUC-huW-xIK2lq_8WuvvRlpbvwARU84cuSyR7vpcp15pOeA20jZ3F86Z7Fvytmj'

os.environ["LI_AT"] = li_at

li_at = os.environ["LI_AT"]

cookies = {
    'bcookie': 'v=2&d91f4901-af8f-416e-8a08-732acb42b47d',
    '_ga': 'GA1.2.606731500.1530723486',
    'sl': 'v=1&bC0fF',
    'visit': 'v=1&M',
    'li_at': li_at,
    'JSESSIONID': 'ajax:4638424466061806728',
    'liap': 'true',
    'bscookie': 'v=1&20180704165823552a490b-9e99-4e2d-80ee-11cf1edc6766AQHL_AQs2NK3QJitZzVGEiX2TBWRDkgT',
    '_lipt': 'CwEAAAFn9zs_4KCM1jqM5v4JgFSQ6-CtRh5NdCgFHnnBjrDw8mVT7pkEfYjor3NRbUF1NMvD1-HS-ZRg30cy8VWTvp-MGaDn3ftFhBpboqTkvKQf6-SCZn5eD26MNIseqsnQE8OAAAYrmWqKq1HJ00AiVINe_ZsNUSxqj6bclmcw13o8HokYy-1-tm58RYIHhPJYYtgCcVgfWMjCSm8aAwG6Bp56hVag68bpIf_UQ89sEjgpWeH9nTgkL-gOYleHBDsU1UILrACNqVnAyFxjKU2W023WAE4IZuNCVUv066sW4LfwqknFD1s7ZDRT61sd1_GcpgXJj6v9GZCDb1uSZaN5tqqeeKdAR5jJgNxu_62IVc98uUYewy6D9R3FvWiGH6sRPvKTOH4BuYE7TAZEfaeFhnCHrLlY7W-Hc_wLfqAi5ufRaqs9AoPiaYFGmGWiFMJ5ClrWte0wfjFYlBuZBBtp5U6vBA9GZjNvTdLb0ZRsi6o6mAQyPKwk27cHiRHYG9y45tj2fmxbk-R6',
    '_guid': '00b4eb3c-43ec-49b8-8b76-804bf72567cf',
    'UserMatchHistory': 'AQJcY0CBNego7wAAAWfqtC3X_X0TUd2mNfZFyT04AVBjaVK9u7K4LZqghQru9VSP_XGHr10iNgN6PJOwQ46efTCRT2jr9FV2Yq5V8YvxMHwlqLmvxJo3LGCLoGbso9ZgEFFIww',
    'li_oatml': 'AQFze67PDN2-RQAAAWfqtCq6B1vtrh5TJx8yMHjODr6pBmXF4XKzWnB5NxOBwlMDBG3pgWkMHI2JNk8IYW7beLx3A7MP75Dx',
    'lidc': 'b=VB05:g=2204:u=1075:i=1546041137:t=1546121238:s=AQG2ru5SYukZGjK5omdjZcZMfU8V5DLX',
    'PLAY_SESSION': '5772ee0202d66578556e9756f3480bbc492920eb-chsInfo=522db8a3-11b9-4068-ab1a-30ee56d029ed+premium_nav_upsell_text',
    'lang': 'v=2&lang=en-us',
    '__ssid': 'e923fe65-2dfb-4cad-8ad5-ae280294904a',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}

titles = ["CXO", "COO", "Exporter Manager", "Director", "President", "Chairman", "CEO"]
t_lenght =  len(titles)
t = 0
while (t < 1) : #t_lenght) :
    found = True
    i = 1
    print("Searching by position title : [ "+titles[t]+" ]")
    while (found and (i <= 1) ) :
        params = (
                    ('facetGeoRegion', '["es:0","fr:0","ec:0","cl:0","mx:0","pe:0","pt:0","br:0"]'), 
                    ('facetIndustry', '["142","66","63","34","148","22","65","116","134","23"]'), 
                                ('title', titles[t]),
                    ('origin', 'FACETED_SEARCH'),
                    ('page', i),
                )
        print("+ Accessing page : [ "+ str(i) +" ]")
        http_request = requests.get('https://www.linkedin.com/search/results/people/', headers=headers, params=params, cookies=cookies)
        if http_request.status_code != 200:
            found = False
        else:
            regex.main(http_request.text)
        time.sleep(random.randint(2,4))   
        i += 1
    t += 1