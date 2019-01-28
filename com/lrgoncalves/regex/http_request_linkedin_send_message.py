# -*- coding: utf-8 -*-
#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=publicIdentifier%22:%22leandrorgoncalves%22&2

import re
import sys
import os
import sys
import requests
from com.lrgoncalves.regex.utils.regex import regex
import sys

conversation = '6487494236966002688'

cookies = {
    'bcookie': 'v=2&d91f4901-af8f-416e-8a08-732acb42b47d',
    '_ga': 'GA1.2.606731500.1530723486',
    'visit': 'v=1&M',
    'JSESSIONID': 'ajax:3303526130608665324',
    'bscookie': 'v=1&20180704165823552a490b-9e99-4e2d-80ee-11cf1edc6766AQHL_AQs2NK3QJitZzVGEiX2TBWRDkgT',
    '_lipt': 'CwEAAAFoIMX5p2youJAMBqtqx_5fcl8JgbUMn1DUwrk_punM_NG147QUZBYf5Z75bgmnEiW0jOrc74G7tUYnyEiY8V6INcakE97JgrZLgpAl82aOwchvkY2l-PPTslFoV5NaEsUXP2FaLFxIFqnVm5KibtdUHe5k3xdWEBnmRTxsUjohuCV5Ys1ZgDW0KC-NzHXcLEsmr_TX1kl8KTZKsU4K5afs4th5sE9mj5rqJzw_tPTQgQPkv2H0sWPx_gN1S5Zw27mfuplOdflwnZ6skvV9alzLOELHU3JrE3JF2RhKVZUzUajQZWnpiWPYfer8qYLbodvFvppPZJ04HZzHauZakPB_R3GfxXgRkAtr9eO_Pq8goL6IUIlqxh1mP8ul8NCOZdvWcK0oVxmyT7spiZTYcnFxkbyW_Eg8k5cDtMjUorWjaSu6JiWvQGZLzKuNqpD94BTTuoZURR5qQ8kLMDVy5gpynY7nw5BU3MGzgrBxdqQ',
    '_guid': '00b4eb3c-43ec-49b8-8b76-804bf72567cf',
    'UserMatchHistory': 'AQJcY0CBNego7wAAAWfqtC3X_X0TUd2mNfZFyT04AVBjaVK9u7K4LZqghQru9VSP_XGHr10iNgN6PJOwQ46efTCRT2jr9FV2Yq5V8YvxMHwlqLmvxJo3LGCLoGbso9ZgEFFIww',
    'li_oatml': 'AQFze67PDN2-RQAAAWfqtCq6B1vtrh5TJx8yMHjODr6pBmXF4XKzWnB5NxOBwlMDBG3pgWkMHI2JNk8IYW7beLx3A7MP75Dx',
    '__ssid': 'e923fe65-2dfb-4cad-8ad5-ae280294904a',
    'lidc': 'b=VB05:g=2211:u=1081:i=1546738104:t=1546777811:s=AQF73VLDkixe7pQJCbxQC4twZfhxzDCX',
    'li_at': 'AQEDAQHDpq0B5ZvpAAABaBZW3-IAAAFoOmNj4k0ADtCIe3dOW4W8DbgVkymXq-nyIr7O3lq-1iSZkR-CxZ-42jrguwReznk3VpHmhro8kdT974m7-ZuiQfbRQCKLU-JIfWq8mgaF2eKK2XSVB2bkXg2R',
    'liap': 'true',
    'sl': 'v=1&nL7aQ',
    'lang': 'v=2&lang=en-us',
    'sdsc': '1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Accept': 'application/vnd.linkedin.normalized+json+2.1',
    'Accept-Language': 'en-US',
    'Referer': 'https://www.linkedin.com/messaging/compose/',
    'x-li-lang': 'en_US',
    'x-li-track': '{"clientVersion":"1.2.5593","osName":"web","timezoneOffset":-2,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
    'x-li-page-instance': 'urn:li:page:d_flagship3_messaging;mn4qCqiiRWq09CzM7aLklg==',
    'csrf-token': 'ajax:3303526130608665324',
    'x-restli-protocol-version': '2.0.0',
    'content-type': 'application/json; charset=utf-8',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}

params = (
    ('action', 'create'),
)

message = 'Testing'

data = '${"eventCreate":{"originToken":"2614bb32-75b1-4a33-8cee-e187d3dea5c0","value":{"com.linkedin.voyager.messaging.create.MessageCreate":{"body":"'+message+'","attachments":[],"attributedBody":{"text":"'+message+'","attributes":[]},"mediaAttachments":[]}}},"dedupeByClientGeneratedToken":false}'

response = requests.post('https://www.linkedin.com/voyager/api/messaging/conversations/'+conversation+'/events', headers=headers, params=params, cookies=cookies, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://www.linkedin.com/voyager/api/messaging/conversations/6381464523810828289/events?action=create', headers=headers, cookies=cookies, data=data)

print(response.text)
