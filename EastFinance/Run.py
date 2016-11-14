#coding=utf-8
import sys
import os
sys.path.append(sys.path.append(sys.path.append(os.path.dirname(__file__) + os.sep + '../')))
from config_reader import reader
from config_reader.exceptions import (ConfigKeyNotFoundError,
                                      ConfigParseError,
                                      ConfigTypeCastError)
from Parser import Parser 
from Spider import Crawler
import time

config = reader.ConfigReader([os.environ,"EastFinance/conf.json"])
parser = Parser()
parser.updateTop10()
mode = config.get_boolean("realtime")# False history
t = config.get_int("sleep_time")
page = 0
start_pos = 0
parser.printHtmlHeader()
while True:
	cur_time = time.localtime().tm_hour*60 + time.localtime().tm_min
	if cur_time > 11*60+31 and cur_time < 13*60-2:
		print "I am having a snap"+"\t"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n"
		sleep(60)
		continue
	if False == parser.fetchTrade(str(start_pos),str(page)):
		print "retry"
		time.sleep(t)
		continue
	parser.findTop10Trade()
	if False == mode:
		start_pos = 20*page #do not change order
		page += 1
	print str(page)+"\t"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"\n"
	time.sleep(t)

