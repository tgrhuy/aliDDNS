# aliDDNS
使用阿里云DDNS
##
使用方法:\
1、修改DDNS_settings.py中的accessKeyId和accessSecret为自己阿里云授权的安全ID和KEY\
2、将阿里云上云解析的域名填入DOMAINNAME，如果要直接解析主域名请在前面加@，例如解析aliyun.com和www.aliyun.com
```python
ALIACS = {"accessKeyId": "你的ID我不知道",
          "accessSecret": "你的KEY我也拿不到",
          "zone": "cn-hangzhou"}
IPURL = r'http://200019.ip138.com/'
DOMAINNAME = ["@.aliyun.com","www.aliyun.com"]
```
