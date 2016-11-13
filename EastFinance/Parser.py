#coding=utf-8
import sys
basepath = "/Users/tiansheng/Documents/workspace/python_project/"
#basepath = "/root/"
sys.path.append(basepath)
import json
from Spider.Crawler import Crawler
from Mail.Email import Email
import time

class Parser(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.top10 = list()
		self.crawler = Crawler()
		self.jobj = None
		self.htmlPath = basepath + "test.html"
		self.logPath = basepath + "log"
		self.tickIDSet = set()
		self.mailer = Email()

	def printHtmlHeader(self):
		head = '<html lang="zh-CN"><head><meta charset="utf-8"><style type="text/css"> body,table{font-size:12px; } table{table-layout:fixed; empty-cells:show; border-collapse: collapse; margin:0 auto; } td{height:30px; } h1,h2,h3{font-size:12px; margin:0; padding:0; } .table{border:1px solid #cad9ea; color:#666; } .table th {background-repeat:repeat-x; height:30px; } .table td,.table th{border:1px solid #cad9ea; padding:0 1em 0; } .table tr.alter{background-color:#f5fafe; } </style></head>'
		body = '<table width="90%" class="table"> <tr> <th>日期</th> <th>时间</th> <th>用户</th> <th>方向</th> <th>证券代码</th> <th>证券名称</th> <th>成交价格</th> <th>成交前</th><th>成交后</th> </tr> '
		self.writeFile(self.htmlPath,head+body)

	def writeFile(self,filepath,content):
		#if !os.file.isfile(self.htmlPath):
		#	os.file.
		f2 = open(filepath,'a')
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

	def formatDate(self,day):
		#20161111
		return day[0:4]+"/"+day[4:6]+"/"+day[6:8]

	def formatTime(self,time):
		#5000000
		return time[0:2]+":"+time[2:4]+":"+time[4:6]

	def findTop10Trade(self):
		#print json.dumps(self.jobj['data'])
		tr = ""
		log = ""
		for record in self.jobj['data']:
			#if already in set,skip
			tickID = record['tzrq']+record['tzsj']+record['userid']
			if tickID in self.tickIDSet:
				continue
			else:
				self.tickIDSet.add(tickID)\
			#store data ,even if not top10
			item = "\t".join([self.formatDate(record['tzrq']),
				self.formatTime(record['tzsj']),
				record['uidNick'],
				record['ranking'],
				record['mmbz'],
				record['stkMktCode'],
				record['stkName'],
				record['cjjg'],
				record['hold1'],
				record['hold2']
				]).encode("utf8")
			log += item
			log += "\n"
			if record['userid'] not in self.top10:
				continue
			self.mailer.sendmail(item,item,"87403102@qq.com,149641004@qq.com")
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
			tr += "\n"
		self.writeFile(self.htmlPath,tr)
		self.writeFile(self.logPath,log)



