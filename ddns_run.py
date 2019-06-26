#!/usr/bin/env python
#coding=utf-8
import sys
from ddns_main import upmydns
import time
import requests
from aliyunsdkcore.client import AcsClient
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordInfoRequest import DescribeDomainRecordInfoRequest
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
import json
from DDNS_settings import ALIACS,IPURL,DOMAINNAME

client = AcsClient(ALIACS["accessKeyId"], ALIACS["accessSecret"], ALIACS["zone"])

getdomainLIST = DescribeDomainRecordsRequest()
getdomainLIST.set_accept_format('json')


def ddns_run():
    ###gerIP###
    r = requests.get(IPURL)
    txt = r.text
    ipaddr = txt[txt.find("[") + 1: txt.find("]")]
    print(ipaddr)
    ######
    for dm in DOMAINNAME:
        dm = dm.split(".")
        getdomainLIST.set_DomainName("{}.{}".format(dm[-2],dm[-1]))
        response = str(client.do_action_with_exception(getdomainLIST),encoding='utf-8')
        response = json.loads(response)
        INFO = response['DomainRecords']['Record']
        for i in INFO:
            if i['RR'] == dm[0]:
                print(i)
                if i['Value'] == ipaddr and i['RR']==dm[0]:
                    print("Current IP:{}\nDomain IP:{}\nDomain Record is not change!!\n######################".format(ipaddr,i['Value']))
                else:
                    i['Value'] = ipaddr
                    upmydns(i)
                    print("Current IP:{}\nDomain IP:{}\nDomain Record update!\n@@@@@@@@@@@@@@@@@@@".format(ipaddr, i['Value']))
if __name__ == '__main__':
    while True:
        try:
            ddns_run()
            time.sleep(300)
        except Exception as e:
            time.sleep(10)
            print(e)
            pass
