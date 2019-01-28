# -*- coding: utf-8 -*-
#!/usr/bin/python3

import re
import sys
import os
import regex_json

def search_profile(profile_id):
    
        li_at = 'AQEDAQN3SSICVq9LAAABaDqD3IUAAAFoXpBghU0AaerldNpKYo8AEdkwS9V1fguW5hrClGc-qZQhPF_8A-nQulSxVpjvbbphK55fpa7D0V3UrKFVWCVuY9sTB1LM9dCO6M6O4KlKJ4rJGO7ICnP3bvhn'
    
        cookies = {
            'bcookie': 'v=2&d91f4901-af8f-416e-8a08-732acb42b47d',
            '_ga': 'GA1.2.606731500.1530723486',
            'visit': 'v=1&M',
            'JSESSIONID': 'ajax:2015441533510487230',
            'bscookie': 'v=1&20180704165823552a490b-9e99-4e2d-80ee-11cf1edc6766AQHL_AQs2NK3QJitZzVGEiX2TBWRDkgT',
            '_lipt': 'CwEAAAFoNPlnI4V8xAP1sekGrkEJS_liPU34IlwHHg4Q1n53iyrhnZA-g0BgsXkEZXxeZrBspH14kC_uGlZ1btmrGH9hdopCayc_Ay58num0A_jZQIZrSwkcYrtOr9ZBkwWCzOfg-C6XqgRcPNoD46Sh0xlhYsVgIPABPWCD3R28rmUC0aLf3EOBN78g0JYh21-gEeVAoo4mhQr9kSgz2xSNJ-lKFi0YEilwvz-njJjfQUpeghrlCRkFCaGNTRjk6NKdmsC9NztZcyHvl7leGYwzj5Vv8SiZE3V2BTt4TVVxdAqCg0P8j_wnYsQuD61CCE65BmFxsvThJfaDodgP_xnmR5qa3cwgCa13U_kMR-EeYzzCQdARzewVp0svxJaqRnSUXwxvIAJRMQZn0nBOiT0wYLpQbJnhKKawdT9wujjB5v4CuIjw0ngQd7T2yrHbWG3dz7kKoiQf1GeXx2Uteyp7wnz2nhrEb-I4IH4ur53Gb2q-fLN3oeK0IQ',
            '_guid': '00b4eb3c-43ec-49b8-8b76-804bf72567cf',
            'UserMatchHistory': 'AQL4TAVg_nJqdAAAAWg0-XRs5U5vxFQev9qkbIA2kscRfXqIAT_AgsQ9AScXWTJBO0tUW20ONogsE9UUP95cfLOgU3htu6_9OuC-hZdI7cl_7KeSkagnsObfexkY-mh61ktFcA',
            'li_oatml': 'AQFze67PDN2-RQAAAWfqtCq6B1vtrh5TJx8yMHjODr6pBmXF4XKzWnB5NxOBwlMDBG3pgWkMHI2JNk8IYW7beLx3A7MP75Dx',
            '__ssid': 'e923fe65-2dfb-4cad-8ad5-ae280294904a',
            'sdsc': '22%3A1%2C1547087498667%7ECAOR%2C0dN8ZvnfDoG6VKEujLKLWTfw66JI%3D',
            'lidc': 'b=VB54:g=1955:u=444:i=1547088913:t=1547165486:s=AQGKe6B4O5H8xnteIJ6Ict71s-Nydj0U',
            'jobs_hru': 'false',
            'li_at': li_at,
            'liap': 'true',
            'sl': 'v=1&zIdr6',
            'lang': 'v=2&lang=en-us',
            'li_a': 'AQJ2PTEmc2FsZXNfY2lkPTU3NTEyNDAwNSUzQSUzQTE1NjEyOTQwNd95TQKb5t9ANjdp1MjZXaJufqdc',
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
        
        params = (
            ('_ntb', 'fgqtukqBS3mrZO2IOx5jCw=='),
        )
        
        #response = requests.get('https://www.linkedin.com/sales/people/'+profile_id+',NAME_SEARCH,psAB', headers=headers, params=params, cookies=cookies)
        
        #file = open("../profiles/"+profile_id+".html ", "w")  
        #file.write(response.text) 
        #file.close()
        
        os.system('/usr/local/bin/scrapeli --user='+profile_id+' > '+'profiles/'+profile_id+'.json')
        regex_json.parse('profiles/'+profile_id+'.json')  