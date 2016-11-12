import sys
sys.path.append("/Users/tiansheng/Documents/workspace/python_project/")
import json
from Spider.Crawler import Crawler

class Parser(object):
	"""docstring for ClassName"""
	def __init__(self):
		self.top10 = list()
		self.crawler = Crawler()
		self.jobj = None

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
		for record in self.jobj['data']:
			if record['userid'] not in self.top10:
				continue
			print "\t".join([
				record['tzrq'],
				record['tzsj'],
				record['userid'],
				record['uidNick'],
				record['mmbz'],
				record['stkMktCode'],
				record['stkName'],
				record['cjjg'],
				record['hold1'],
				record['hold2']
				]).encode("utf8")



