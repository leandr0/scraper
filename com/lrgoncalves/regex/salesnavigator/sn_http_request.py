# -*- coding: utf-8 -*-
#!/usr/bin/python3
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=publicIdentifier%22:%22leandrorgoncalves%22&2

import re
import sys
import os
import sys
import requests
import sys
import sn_http_request_profile

#filename = sys.argv[1]

url = 'https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22es%3A0%22%2C%22mx%3A0%22%2C%22ar%3A0%22%2C%22co%3A0%22%5D&facetIndustry=%5B%22134%22%2C%2234%22%5D&keywords=Exportar&origin=FACETED_SEARCH'
path = os.path.join('folder_name', 'file_name')

print('Path >>> '+path)
print('USER >>>> '+ os.environ.get('USER'))
print(sys.prefix)

print('Separated path >>> ' + os.sep)


#print(filename)

li_at = 'AQEDAQN3SSIAPmafAAABaJBhClUAAAFotG2OVU0ACSaSFDWSvDFR37hrk4rMGNyjQDPNN6fECq7qZQzb95oK0l084noUA-7sCbbIfZaKw06rdnkgbDov6IrwVlSJZ1H3y4PORiTvE_vR8iqeKA-lIdGU'

os.environ["LI_AT"] = li_at

os.environ["PATH"] = '$PATH:/Users/digitallam/workspace/'

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
    'sdsc': '22%3A1%2C1547085477683%7ECAOR%2C0OvqlUHRLtcuPHzntqGMiTv1AYU8%3D',
    'lidc': 'b=VB54:g=1955:u=444:i=1547085706:t=1547165486:s=AQHpCIoKLDdfstIhidj6UB93caizuXGS',
    'jobs_hru': 'false',
    'li_at': li_at ,
    'liap': 'true',
    'sl': 'v=1&zIdr6',
    'lang': 'v=2&lang=en-us',
    'li_a': 'AQJ2PTEmc2FsZXNfY2lkPTU3NTEyNDAwNSUzQSUzQTE1NjEyOTQwNYy8pAPzp-1bO2TYYdiwVLlQkz2M',
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

found = True
i = 1
while (found and (i <= 1) ) :
    params = (
    ('companySize', 'B,C,D,E,F,G,H,I'),
    ('function', '25,6,9,21'),
    ('geo', 'fr:0,gb:0,nl:0,es:0,br:6368,it:0,cl:0,ar:0,ua:0,pt:0,no:0,uy:0,nl:5682'),
    ('industry', '141,34,134,23,142,63,65,74,32,22,66,148'),
    ('keywords', 'Exporter'),
    ('logHistory', 'false'),
    ('logId', '7336515363'),
    ('page', i),
    ('preserveScrollPosition', 'false'),
    ('searchSessionId', 'fgqtukqBS3mrZO2IOx5jCw=='),
    ('seniority', '4,6,5,7,10,9,8'),
    )
    response = requests.get('https://www.linkedin.com/sales/search/people', headers=headers, params=params, cookies=cookies)

    if response.status_code != 200:
        found = False
    else:
        file = open("profiles/search.html ", "w")  
        file.write(response.text) 
        file.close()
        html = response.text   
    i += 1

rg = re.compile('(urn:li:fs_salesProfile:\()([-_a-zA-Z0-9]+)(,NAME_SEARCH,psAB\))',re.MULTILINE)
#m = rg.search(txt)
print(html)
results = rg.findall(html)


exclude = 'UNKNOWN'

i = 0
while i < 5:
    #len(results):
    tuple = results[i] 
    line = tuple[1]
    if line != exclude:
        sn_http_request_profile.search_profile(line) 
        #os.system('/usr/local/bin/scrapeli --user='+line+' > '+'../profiles/'+line+'.json')
        #regex_json.parse('profiles/'+line+'.json')
    i += 1