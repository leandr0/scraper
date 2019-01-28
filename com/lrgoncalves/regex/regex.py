# -*- coding: utf-8 -*-
#!/usr/bin/python3

import re
import regex_json
import os

def regex():
    print('It works')

def main(html):
    #with open(sys.argv[1], 'r') as content_file:
    #with open(filename, 'r') as content_file:
        #txt = content_file.read()
#rg = re.compile(re1+re2+re3+re4,re.IGNORECASE|re.DOTALL)
    rg = re.compile('(urn:li:fs_memberBadges:[-_a-zA-Z0-9]+&quot;,&quot;)(publicIdentifier&quot;:&quot;)([-a-zA-Z0-9À-ÖØ-öø-ÿ]+)(?:&quot;)',re.MULTILINE)
#m = rg.search(txt)
    results = rg.findall(html)
    exclude = 'UNKNOWN'
#f = open("myfile.txt", "w")
    
    i = 0
    while i < 2:#len(results):
        tuple = results[i] 
        line = tuple[2]
        if line != exclude: 
               os.system('/usr/local/bin/scrapeli --user='+line+' > '+'profiles/'+line+'.json')
               regex_json.parse('profiles/'+line+'.json')
        i += 1