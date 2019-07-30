# -*- coding: utf-8 -*-
#!/usr/bin/python3

import re
import sys
import data_access
import base64
from bson.binary import Binary as BsonBinary
import hashlib

def parse(profile,filename):

    try:
        with open(filename, 'r') as content_file:
            txt = content_file.read()
            
            print("+++ Parseando JSON : [ "+profile+" ]")  
            
            print("+++ Profile : [ "+txt+" ]")  
            
            txt         = find_personal_info(txt)
            company     = find_company(txt[:])
            email       = find_email(txt)
            location    = find_location(txt)
            name        = find_name(txt)
            phone       = find_phone(txt)   
            head_line   = find_headline(txt)
            data        = text_to_bits(txt)
            
            json = """{  
                        \"company\" : \"$company\",
                        \"email\" : \"$email\",
                        \"location\" : \"$location\",
                        \"name\" : \"$name\",
                        \"phone\" : \"$phone\",
                        \"headline\" : \"$headline\",
                        \"profile\" : \"$profile\",
                        \"hash\" : \"$hash\"
                        ,\"data\" : \"$data\"
                        } """
                        
            json = replace_json(json,'$company', company)
            json = replace_json(json,'$email', email)
            json = replace_json(json,'$location', location)
            json = replace_json(json,'$name', name)
            json = replace_json(json,'$phone', phone)
            json = replace_json(json,'$headline', head_line)
            json = replace_json(json,'$profile', 'https://www.linkedin.com/in/'+profile)
            json = replace_json(json,'$hash', hashlib.sha512(profile.encode()).hexdigest())
            json = replace_json(json,'$data', data)
            
            print("+++ JSON : [ "+json+" ]")  
            
            data_access.insert(json)
            
    except Exception as error :
        print("invalid json: %s" % error)
        pass

def find_personal_info(txt):
        pattern = '(?:personal_info\"\:).+?(?=\,\s\"summary)'
        txt = find_pattern(pattern, txt)
        return txt  

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def find_company(txt):
        pattern ='(?:company\"\:).+(?=\,\s\"connec)'
        txt = find_pattern(pattern, txt)
        txt = replace('company', txt)
        txt = replace(':', txt)
        txt = replace('\"', txt)
        txt = replace(',', txt)
        #print('company found >> '+txt)
        return txt  

def find_email(txt):
        pattern = '(?:email\"\:).+(?=\,\s\"foll)'
        txt = find_pattern(pattern, txt)
        txt = replace('email', txt)
        txt = replace(':', txt)
        txt = replace('\"', txt)
        txt = replace(',', txt)
        #print('email found >> '+txt)
        return txt  

def find_location(txt):
        pattern ='(?:location\"\:).+(?=\,\s\"name)'
        txt = find_pattern(pattern, txt)
        txt = replace('location', txt)
        txt = replace(':', txt)
        txt = replace('\"', txt)
        #txt = replace(',', txt)
        #print('location found >> '+txt)
        return txt  

def find_name(txt):
        pattern ='(?:name\"\:).+(?=\,\s\"phone)'
        txt = find_pattern(pattern, txt)
        txt = replace('name', txt)
        txt = replace(':', txt)
        txt = replace('\"', txt)
        txt = replace(',', txt)
        #print('name found >> '+txt)
        return txt  

def find_phone(txt):
        pattern ='(?:phone\"\:).+(?=\,\s\"school)'
        txt = find_pattern(pattern, txt)
        txt = replace('phone', txt)
        txt = replace(':', txt)
        txt = replace('\"', txt)
        txt = replace(',', txt)
        #print('phone found >>'+txt)
        return txt  
     
     
def find_headline(txt):
        pattern ='(?:headline\"\:).+(?=\,\s\"image)'
        txt = find_pattern(pattern, txt)
        txt = replace('headline', txt)
        txt = replace(':', txt)
        txt = replace('\"', txt)
        txt = replace(',', txt)
        #print('headline found >> '+txt)
        return txt  
     
     
def replace(chr,txt):
        txt = re.sub(chr, '', txt)
        return txt

def replace_json(src,pattern,value):
        return src.replace(pattern, value)

def find_pattern(pattern,txt):
        #rg = re.compile(pattern,re.MULTILINE)
        return re.search(pattern, txt).group() 


if __name__ == "__main__":
    print("++++ Inserindo JSON : [ "+sys.argv[1]+" ]")            
    parse(sys.argv[2], sys.argv[1])