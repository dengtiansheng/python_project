import sys
from Parser import Parser 
sys.path.append("/Users/tiansheng/Documents/workspace/python_project/")
from Spider import Crawler
import time

parser = Parser()
parser.updateTop10()
t = 2
page = 0
start_pos = 0
print parser.top10
while page < 100:
	parser.fetchTrade(str(start_pos),str(page))
	parser.findTop10Trade()
	start_pos = 20*page #do not change order
	page += 1
	time.sleep(t)
