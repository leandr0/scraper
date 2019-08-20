# -*- coding: utf-8 -*-
#!/usr/bin/python3

import re
import regex_json
import os
import time
import random

def regex():
    print('It works')

def main(html):
 
    rg = re.compile('(urn:li:fs_memberBadges:[-_a-zA-Z0-9]+&quot;,&quot;)(publicIdentifier&quot;:&quot;)([-a-zA-Z0-9À-ÖØ-öø-ÿ]+)(?:&quot;)',re.MULTILINE)

    results = rg.findall(html)
    exclude = 'UNKNOWN'
    try:
        i = 0
        while i < len(results):
            tuple = results[i] 
            line = tuple[2]
            if line != exclude:
                   time.sleep(random.randint(2,6)) 
                   print("++ Acessando perfil : [ "+ line +" ]")
                   os.system('/usr/local/bin/scrapeli --user='+line+' > '+'profiles/'+line+'.json')
                   #EU AMO A VANESSA !!!
                   #os.system('cp profiles/'+line+'.json profiles/'+line+'_original.json' )
                   regex_json.parse(line,'profiles/'+line+'.json')
                   #content_file = open('profiles/'+line+'.json', 'r')
                   #txt = content_file.read()
            i += 1
    except Exception:
        pass