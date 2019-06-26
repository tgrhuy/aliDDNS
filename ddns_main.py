#!/usr/bin/env python
#coding=utf-8
import sys
from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from DDNS_settings import ALIACS

def upmydns(info):
    set_Value = info['Value']
    set_Type = info["Type"]
    set_RR = info['RR']
    set_RecordId = info['RecordId']
    client = AcsClient(ALIACS["accessKeyId"], ALIACS["accessSecret"], ALIACS["zone"])
    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')
    request.set_Value(set_Value)
    request.set_Type(set_Type)
    request.set_RR(set_RR)
    request.set_RecordId(set_RecordId)
    response = client.do_action_with_exception(request)
    print(str(response, encoding='utf-8'))
# def setbatch(IP):
#     for i in INFO:
#         i["set_Value"] = IP
#         upmydns(i)
#         print(i)

# if __name__ == '__main__':
#     IP = sys.argv[1]
#     # IP = "8.8.8.8"
#     setbatch(IP)






