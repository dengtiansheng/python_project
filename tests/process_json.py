#coding=utf-8
import sys,os
import json
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf8')
f = open(r'')
result_file=open(r'','w')
for line in f.readlines():
    cols = line.split('\t')
    if len(cols) < 2:
        continue
    j = json.loads(cols[1])
    for item in j['goodsInfos']:
        print json.dumps(item)
        #result_file.write(cols[0].encode("utf8")+"\t"+item['iid']+"\n")
        print cols[0].encode("utf8") + "\t" + item['iid'] + "\n"
result_file.close()
