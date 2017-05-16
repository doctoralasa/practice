#!/usr/bin/env python3
# -*- coding: utf-8 -*-
payload={'wd':'待搜索内容','rn':'100'}#search parameters,including content and the number of search results
r=requests.get("http://www.baidu.com/s",params=payload)#get the http requests 'r' from the search engine such as baidu
print(r.url)#print the changed url from the website
r.encoding#get the code style such as utf-8 or iso -8859-1
r.encoding='utf-8'#ustylze the utf-8 coding style to get the website

