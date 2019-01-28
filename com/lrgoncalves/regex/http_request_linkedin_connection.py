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
    '_lipt': 'CwEAAAFoHzf8zXLR6mK53j9q-F96LOrEHHrmoKWoecZ6U0ggDaBrIgMNqsfaAv5HnXX2yWhAFFsHqt1rhh6BLSNbnhQFOjNBRCAzwv-3uznPIujBvRoO-SNFC5fCQ5gVtpl5glldyqqDqt900MWTfVkyF6m9fUDYOvwEO6_f2pqjy7MjHrlNDU8vY1Sih9bFg_1ThkoIo8g_aPnMHyHWywRJ6dBSWJ3jiWNLAnOuZ_eidT6hhdlrxxCoii8WwG7o9WKelxG26lEp0mz7EKWC3ljgjl2Z-tFJclAjbkWt3eQfF7YLwcosoj30pjM0DQHeZLr3DjeYTWMyDYZ_3dvGWlEPTuVh0KnJnC_5FU9W-C6j_6mHLd606Yc4NTWVntOmf8FcMpg5eqFeBVYLS9GmXqkCSh-vGcXNIRLeMR7oMQBufJpdevA9kIPZPygkpKgY-DuZ-blKu60HYE4KpgJ_WOxjbOHCl8nGHZ1Q_ypJCIpyGgI',
    '_guid': '00b4eb3c-43ec-49b8-8b76-804bf72567cf',
    'UserMatchHistory': 'AQJcY0CBNego7wAAAWfqtC3X_X0TUd2mNfZFyT04AVBjaVK9u7K4LZqghQru9VSP_XGHr10iNgN6PJOwQ46efTCRT2jr9FV2Yq5V8YvxMHwlqLmvxJo3LGCLoGbso9ZgEFFIww',
    'li_oatml': 'AQFze67PDN2-RQAAAWfqtCq6B1vtrh5TJx8yMHjODr6pBmXF4XKzWnB5NxOBwlMDBG3pgWkMHI2JNk8IYW7beLx3A7MP75Dx',
    '__ssid': 'e923fe65-2dfb-4cad-8ad5-ae280294904a',
    'lidc': 'b=VB05:g=2211:u=1081:i=1546737600:t=1546777811:s=AQHCQ3ilI9uleUxDhWhHZeJX0MIpm4OL',
    'li_at': 'AQEDAQHDpq0B5ZvpAAABaBZW3-IAAAFoOmNj4k0ADtCIe3dOW4W8DbgVkymXq-nyIr7O3lq-1iSZkR-CxZ-42jrguwReznk3VpHmhro8kdT974m7-ZuiQfbRQCKLU-JIfWq8mgaF2eKK2XSVB2bkXg2R',
    'liap': 'true',
    'sl': 'v=1&nL7aQ',
    'lang': 'v=2&lang=en-us',
    'sdsc': '1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D',
    '_gat': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Accept': 'application/vnd.linkedin.normalized+json+2.1',
    'Accept-Language': 'en-US',
    'Referer': 'https://www.linkedin.com/in/carolineoliveirarh/',
    'x-li-lang': 'en_US',
    'x-li-track': '{"clientVersion":"1.2.5593","osName":"web","timezoneOffset":-2,"deviceFormFactor":"DESKTOP","mpName":"voyager-web"}',
    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;ufaQKPoiT9qkfc48vpPYDg==',
    'csrf-token': 'ajax:3303526130608665324',
    'x-restli-protocol-version': '2.0.0',
    'content-type': 'application/json; charset=utf-8',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}

data = {
  '{"emberEntityName":"growth/invitation/norm-invitation","invitee":{"com.linkedin.voyager.growth.invitation.InviteeProfile":{"profileId":"ACoAACjCzGYBR0A3QfzXOkZA3Byt-4jMoEE9zyA"}},"trackingId":"iWAHrProR0W6bsxYemVQkQ': '="}'
}

response = requests.post('https://www.linkedin.com/voyager/api/growth/normInvitations', headers=headers, cookies=cookies, data=data)

print(response.text)
