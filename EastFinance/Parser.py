#coding=utf-8
import sys
basepath = "/Users/tiansheng/Documents/workspace/python_project/"
#basepath = "/root/"
sys.path.append(basepath)
import json
from Spider.Crawler import Crawler

class Parser(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.top10 = list()
		self.crawler = Crawler()
		self.jobj = None
		self.htmlPath = basepath + "test.html"

	def printHtmlHeader(self):
		head = '<html lang="zh-CN"><head><meta charset="utf-8"><style type="text/css"> body,table{font-size:12px; } table{table-layout:fixed; empty-cells:show; border-collapse: collapse; margin:0 auto; } td{height:30px; } h1,h2,h3{font-size:12px; margin:0; padding:0; } .table{border:1px solid #cad9ea; color:#666; } .table th {background-repeat:repeat-x; height:30px; } .table td,.table th{border:1px solid #cad9ea; padding:0 1em 0; } .table tr.alter{background-color:#f5fafe; } </style></head>'
		body = '<table width="90%" class="table"> <tr> <th>日期</th> <th>时间</th> <th>用户</th> <th>方向</th> <th>证券代码</th> <th>证券名称</th> <th>成交价格</th> <th>成交前</th><th>成交后</th> </tr> '
		self.writeFile(head+body)

	def writeFile(self,content):
		#if !os.file.isfile(self.htmlPath):
		#	os.file.
		f2 = open(self.htmlPath,'a')
		f2.write(content)
		f2.close()

	def updateTop10(self):
		#url = "http://spzhcs.eastmoney.com/rtcs1?type=rtcs_get_rank&khqz=116&rankType=0&recIdx=0&recCnt=20&rankid=1&userId="
		#res = crawler.fetch_url(url=url)
		self.top10 = ["1862113294062566",
		"6438013861173624",
		"9310094719273070",
		"8096014763275768",
		"7812212495398148",
		"6229014760997974",
		"6346113846404544",
		"9707513801914802",
		"8578013772618202",
		"3453094249465624"
		]

	def fetchTrade(self,start_pos=None,page = None):
		if None != page or None != start_pos:
			url = "http://spzhcs.eastmoney.com/rtcs1?type=rtcs_expert_trade&khqz=116&rankType=0&recIdx="+start_pos+"&recCnt=20&rankid=" + page + "&userId="
		else:
			url = "http://spzhcs.eastmoney.com/rtcs1?type=rtcs_expert_trade&khqz=116&rankType=0&recIdx=0&recCnt=20&rankid=0&userId="
		cs = Crawler()
		res = cs.fetch_url(url=url)
		self.jobj = json.loads(res)

	def findTop10Trade(self):
		#print json.dumps(self.jobj['data'])
		tr =""
		for record in self.jobj['data']:
			#if record['userid'] not in self.top10:
			#	continue
			tr += "".join(['<tr> ',
				'<td>'+record['tzrq'].encode("utf8")+'</td>',
				'<td>'+record['tzsj'].encode("utf8")+'</td>',
				'<td>'+record['uidNick'].encode("utf8")+'</td>',
				'<td>'+record['mmbz'].encode("utf8")+'</td>',
				'<td>'+record['stkMktCode'].encode("utf8")+'</td>',
				'<td>'+record['stkName'].encode("utf8")+'</td>',
				'<td>'+record['cjjg'].encode("utf8")+'</td>',
				'<td>'+record['hold1'].encode("utf8")+'</td>',
				'<td>'+record['hold2'].encode("utf8")+'</td>',
				'</tr>'])
		self.writeFile(tr)



