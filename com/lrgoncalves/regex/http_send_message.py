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
import hashlib

thread = '6534527170818162688'

cookies = {
    'bcookie': '%22v%3D2%26d91f4901-af8f-416e-8a08-732acb42b47d%22&_ga=GA1.2.606731500.1530723486&visit=v%3D1%26M&JSESSIONID=%22ajax%3A2282914038942601067%22&bscookie=%22v%3D1%2620180704165823552a490b-9e99-4e2d-80ee-11cf1edc6766AQHL_AQs2NK3QJitZzVGEiX2TBWRDkgT%22&__ssid=e923fe65-2dfb-4cad-8ad5-ae280294904a&_lipt=CwEAAAFqvTMGfHRQEil5d8cGKzAYpkHtpCLKI7jPksgBadUDbS2IMV9q1JHVs2RznOpNjB1bltQke9W4do8fU4KMW6FkpLwkCzYUnRsIc58X-MMfFZi7DcO9YMqbxORJfCHfMIeeEClxiX_R429Bn46FCKpoB4VXBfHexBkDwg9u-2hLbmLuOomX7FlZDQ2dAZYP76wVxvBe9wrXK1prsQC2oabtbg1hq7Ma1Yau9HQKcxYaiJXNMBlZD6v99nNf9irDb4C3PlHsB-XeBLM8r6FBZzuLfu2PsyOPBYWZVcSxjnIOx40KniCS1yhvKIeaAegdjF5eZjjVhdcUFpBaAHz5d7lLviHuD6GtJ9X5Zqim9-1CJXMU8RaoiR1zykVGbEVtEE-jNIv49XWIQH3Nf9LWYFnBiIqQlWBVQtTRacWxoGwNw6za6MhDpWIoP3DzK0077ZvO2RBLXU3k3_hUhoyg0OLpbwO9_dB4mV4eGMm0qetgNZ-d-tjQIBQqc9dyU11EVhPT&UserMatchHistory=AQL2bilo5WjrDgAAAWq9Mwy4QH_qhGelhawTVu2MiyjCeQe-i-vy2NzWOmv2vQnyNAxsAq3LXpec5rO9R5pfc23agq40cJ52i6kbtns6AVfi3EvpQcmxREOt5NrLXwAsGtG0pAZluUfgCCMdGqJz4oGEovWLMbtf2yQF59OL2RZwr8nO43gWJ_dV5NdBwtdfczTLQh0r611Lf7g4Qjb1Nsrm6EKCZORFKOTH&_guid=10c1071c-edac-4d91-b690-ef821126ee3e&li_oatml=AQG2TcTIsS3mawAAAWoo0Yf02oshiHArhZc6XlJLCMYKERvbVj9lXZGG2ywv2bTfKVw_RUyxAXS7D76b4I_H-_lBtwM9R5R0&AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-1303530583%7CMCIDTS%7C18031%7CMCMID%7C40137488523848488101540573511830298450%7CMCOPTOUT-1557895838s%7CNONE%7CvVersion%7C3.3.0&lidc=%22b%3DTB05%3Ag%3D2543%3Au%3D1267%3Ai%3D1557952429%3At%3D1558034350%3As%3DAQHnXu9TQsgWpK0wabFTsyGfBf_l6Ekb%22&AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1&sl=v%3D1%26JByo4&li_at=AQEDAQHDpq0FFVnqAAABarl5hNoAAAFq3YYI2k4AfVowNVjbR2Y3vCpBvELVsU3wzNNv9-JaprK760OZvflQLax4TM4Ng2Ug2fR5T7PoH47CpqzcLaKf6ZM3iVKNAWbtlBjokyO-MHw73NXaUDpR0v_-&liap=true&lang=v%3D2%26lang%3Den-us&_gat=1',
}

headers = {
    'Host': 'www.linkedin.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0',
    'Accept': 'application/vnd.linkedin.normalized+json+2.1',
    'Accept-Language': 'en-US',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.linkedin.com/messaging/compose/',
    'x-li-lang': 'en_US',
    'x-li-track': '{clientVersion:1.3.961,osName:web,timezoneOffset:-3,deviceFormFactor:DESKTOP,mpName:voyager-web}',
    'x-li-page-instance': 'urn:li:page:d_flagship3_messaging;MLJuiicuTCW29rVL63hdJg==',
    'csrf-token': 'ajax:2282914038942601067',
    'x-restli-protocol-version': '2.0.0',
    'content-type': 'application/json; charset=utf-8',
    'Content-Length': '339',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}

params = (
    ('action', 'create'),
)

message = 'Fala Biba'

data = '''{keyVersion:LEGACY_INBOX,
            conversationCreate:{   
                eventCreate:{
                    originToken:8bf211db-6b2e-4706-8ab7-095fa0bb0d4e,
                    value:{
                        com.linkedin.voyager.messaging.create.MessageCreate:{
                            attributedBody:{
                                text:'+message+',
                                attributes:[]
                                },
                                attachments:[]}}},
                                recipients:[ACoAAAVuJVsBunXcIaWZeaJtRN1LKISQ7xwCbAE],
                                subtype:MEMBER_TO_MEMBER}}'''



response = requests.post('https://www.linkedin.com/voyager/api/messaging/conversations', headers=headers, params=params, cookies=cookies, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://www.linkedin.com/voyager/api/messaging/conversations?action=create', headers=headers, cookies=cookies, data=data)
