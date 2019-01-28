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

cookies = {
    'bcookie': 'v=2&d91f4901-af8f-416e-8a08-732acb42b47d',
    '_ga': 'GA1.2.606731500.1530723486',
    'visit': 'v=1&M',
    'JSESSIONID': 'ajax:3303526130608665324',
    'bscookie': 'v=1&20180704165823552a490b-9e99-4e2d-80ee-11cf1edc6766AQHL_AQs2NK3QJitZzVGEiX2TBWRDkgT',
    '_lipt': 'CwEAAAFoFlv7fB8FfzK8gliBF9JEy5d33vioyFw-w7tL3TDQ63KztnLbUTJVv9ejYKl5PlZ7QnuYcXTlyt4g14zTwBrRnCU6a4qu-w9Usem2sNPpqfQMc_KzvgAofhIE2EqDuWK5XFy2CBedc4uHhcrW8vKHiqIKLm_jGUXmNKRP9cAtGR_Jk6X0YSxEgEE9o1iCY9QxMgsPWvh9TV125m41-QrY581cIj4Qc82nt5c3aLBY8BniH-zdNjgkTBDnVSrk_jX748ikHRCE3fH9flMd1q6VfigTIdaO-y2f-dIEYu8xIL594WFR3ps7nMV4qDcS65Nika0ZYgYefgAFZZ_M6RTllcMOi15xIZn4Lu4rOefuKoQdn3hCraQd7x0gcnK7Tq1pqkOEu2q_SrWnzubKFlDq8aBbG5N4BQFIfMKX-E0WItriSfkh-c7XlcspcLSjvKO8NoQQa4zCRwKSTkWHZi4voddHcgH9UM7Kymtu8XuE2Tjsrar-sK8',
    '_guid': '00b4eb3c-43ec-49b8-8b76-804bf72567cf',
    'UserMatchHistory': 'AQJcY0CBNego7wAAAWfqtC3X_X0TUd2mNfZFyT04AVBjaVK9u7K4LZqghQru9VSP_XGHr10iNgN6PJOwQ46efTCRT2jr9FV2Yq5V8YvxMHwlqLmvxJo3LGCLoGbso9ZgEFFIww',
    'li_oatml': 'AQFze67PDN2-RQAAAWfqtCq6B1vtrh5TJx8yMHjODr6pBmXF4XKzWnB5NxOBwlMDBG3pgWkMHI2JNk8IYW7beLx3A7MP75Dx',
    'PLAY_SESSION': '5772ee0202d66578556e9756f3480bbc492920eb-chsInfo=522db8a3-11b9-4068-ab1a-30ee56d029ed+premium_nav_upsell_text',
    '__ssid': 'e923fe65-2dfb-4cad-8ad5-ae280294904a',
    'sdsc': '1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D',
    'lidc': 'b=VB05:g=2208:u=1077:i=1546563055:t=1546632285:s=AQHi2hDU7lAyPLMDaifvJsK7bozzBpWJ',
    '_gat': '1',
    'li_at': 'AQEDAQHDpq0B5ZvpAAABaBZW3-IAAAFoOmNj4k0ADtCIe3dOW4W8DbgVkymXq-nyIr7O3lq-1iSZkR-CxZ-42jrguwReznk3VpHmhro8kdT974m7-ZuiQfbRQCKLU-JIfWq8mgaF2eKK2XSVB2bkXg2R',
    'liap': 'true',
    'sl': 'v=1&nL7aQ',
    'lang': 'v=2&lang=en-us',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Accept': 'application/vnd.linkedin.normalized+json',
    'Accept-Language': 'en-US',
    'Referer': 'https://www.linkedin.com/in/vera-cristina-de-f-vaz-68061866/',
    'X-LI-Lang': 'en_US',
    'X-LI-Track': '{"clientVersion":"1.2.5542","osName":"web","timezoneOffset":-2,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
    'X-li-page-instance': 'urn:li:page:d_flagship3_background;jXHPDGQUTLiBEeJ4beuSfA==',
    'Csrf-Token': 'ajax:3303526130608665324',
    'X-RestLi-Protocol-Version': '2.0.0',
    'x-li-prefetch': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}

response = requests.get('https://www.linkedin.com/voyager/api/growth/emailsPrefill', headers=headers, cookies=cookies)

print(response.text)
