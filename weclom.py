import requests
url = 'https://notify-api.line.me/api/notify'
token = 'bcc7ebccb3634b0ca2e532b607ab8de4'
msg = 'hello'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
print(headers)
r = requests.post(url, headers=headers , data = {'message':msg})
print r.text
