#coding=utf-8
import sys
from Parser import Parser 
from UI.UI import UI
basepath = "/Users/tiansheng/Documents/workspace/python_project/"
#basepath = "/root/"
sys.path.append(basepath)
from Spider import Crawler
import time

ui = UI()
parser = Parser()
parser.updateTop10()
t = 2
page = 0
start_pos = 0
parser.printHtmlHeader()
while True:
	parser.fetchTrade(str(start_pos),str(page))
	parser.findTop10Trade()
	start_pos = 20*page #do not change order
	page += 1
	print str(page)+"\t"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n"
	time.sleep(t)
