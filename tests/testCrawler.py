import sys
sys.path.append("/Users/tiansheng/Documents/workspace/python_project/")
from Spider.Crawler import Crawler
def processFuc(url):
    return "http://d.xxx.com/search/" + url + "-.html"

def test_fetch_all():
    url = "http://d.xxx.com/search/%E6%89%8B%E6%9C%BA-.html"
    cs = Crawler()
    cs.prepareUrl("keyword", processFuc)
    cs.fetch_all()

def test_fetch_github_trend():
    url = "http://45.78.15.223:5000/results/dump/githup.txt"
    cs = Crawler()
    res = cs.fetch_url(url=url)
    print res

"""
type=rtcs_expert_trade
&khqz=116
&rankType=0
&recIdx=0
&recCnt=20
&rankid=
0&userId=
"""
def fetch_caifu():
    url = "http://spzhcs.eastmoney.com/rtcs1?type=rtcs_expert_trade&khqz=116&rankType=0&recIdx=0&recCnt=20&rankid=0&userId="
    cs = Crawler()
    res = cs.fetch_url(url=url)
    print res

if __name__=='__main__':
    #test_fetch_all()
    #test_fetch_github_trend()
    fetch_caifu()