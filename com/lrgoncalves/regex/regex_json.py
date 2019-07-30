# -*- coding: utf-8 -*-
#!/usr/bin/python3

import re
import regex_personal_information

def parse(profile,filename):

    with open(filename, 'r') as content_file:
        txt = content_file.read()

    re0='\':\s+u\"'
    re1='\':\s+u\''
    re2=',\s+\''	
    re3='{\''
    re4='\':'	
    re5='u\''
    re6='\":\s*\''
    re7='\'}'
    re8='\','
    re9='\\\\'
    re10='None'
    re11='\']'
    re12='u\"'
    re13='\[\''
    re14='\''
    re15='\s{2}'
    
    rg = re.compile(re0,re.MULTILINE)
    txt = re.sub(rg, '\': \'', txt)

    rg = re.compile(re1,re.MULTILINE)
    txt = re.sub(rg, '\': \'', txt)

    rg = re.compile(re2,re.MULTILINE)
    txt = re.sub(rg, ', "', txt)

    rg = re.compile(re3,re.MULTILINE)
    txt = re.sub(rg, '{"', txt)

    rg = re.compile(re4,re.MULTILINE)
    txt = re.sub(rg, '":', txt)

    rg = re.compile(re5,re.MULTILINE)
    txt = re.sub(rg, '"', txt)

    rg = re.compile(re6,re.MULTILINE)
    txt = re.sub(rg, '": "', txt)

    rg = re.compile(re7,re.MULTILINE)
    txt = re.sub(rg, '"}', txt)

    rg = re.compile(re8,re.MULTILINE)
    txt = re.sub(rg, '",', txt)

    rg = re.compile(re9,re.MULTILINE)
    txt = re.sub(rg, '', txt)

    rg = re.compile(re10,re.MULTILINE)
    txt = re.sub(rg, '"None"', txt)

    rg = re.compile(re11,re.MULTILINE)
    txt = re.sub(rg, '"]', txt)

    rg = re.compile(re12,re.MULTILINE)
    txt = re.sub(rg, '"', txt)

    rg = re.compile(re13,re.MULTILINE)
    txt = re.sub(rg, '["', txt)

    rg = re.compile(re14,re.MULTILINE)
    txt = re.sub(rg, '', txt)

    rg = re.compile(re15,re.MULTILINE)
    txt = re.sub(rg, '', txt)

    with open(filename, "w") as f:
        f.write(txt)

    regex_personal_information.parse(profile,filename)

    

def hextranslate(s):
        res = ''
        for i in range(len(s)/2):
                realIdx = i*2
                res = res + chr(int(s[realIdx:realIdx+2],16))
        return res
