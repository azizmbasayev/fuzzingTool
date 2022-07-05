import requests
header={"Cookie": "PHPSESSID=932rf68vc34y3fc898ky53bs64e756h62"}
url="http://10.10.10.90"
file=open("fuzzing.txt","r")
content=file.read()
file.close()

for i in content.splitlines():
	print(i)
	url_request=url+str(i)
	result=requests.get(url=url_request,headers=header)
	print ("Status Code:") + result.status_code