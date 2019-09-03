from bs4 import BeautifulSoup
import ssl
from urllib import request
import time



def getDetail(direct,url,year):
    ssl._create_default_https_context = ssl._create_stdlib_context
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    data = request.urlopen(url).read()

    data = data.decode('UTF-8')

    soup = BeautifulSoup(data, 'html.parser')

    # tables = soup.fine_all(name='table', attrs={'class': 'border'})
    # print(tables)
    trs = soup.table.tbody.find_all('tr')
    # print(trs)
    with open(direct, 'w') as f:
        courseNum = 0
        trackNum = 0
        validNum = 0
        errNum = 0
        for x in trs:
            # print(x)
            # print(x.td.a.string)
            courseNum += 1
            if (x.td.a != None):
                # print("-------------------")
                flag = 0
                ADK = '  '
                comment = ''
                for y in x.children:
                    if flag == 2:
                        courseName = str(y.string)
                    if flag == 3 and str(y.string) == 'X':
                        ADK = 'ADK'
                    if flag == 4 and str(y.string) != ' ':
                        comment = str(y.string)
                    flag += 1

                # print(courseName)
                # print(ADK)
                # print(comment)
                validNum += 1
                webUrl = str(x.td.a['href'])
                # 那个写网页的单词都拼错。
                # 改成现在的year，网页会自动跳转
                # 如果不是current就代表这个课程网页没更新过
                webUrl = webUrl.replace('current', str(year))
                webUrl = webUrl.replace('curren', str(year))
                webStr = x.td.a.string
                print(webUrl)
                # webUrl = 'http://www.handbook.unsw.edu.au/postgraduate/courses/2020/COMP9041.html'
                if webStr == None:
                    webStr = x.td.a.contents[0]
                req = request.Request(webUrl, headers=headers)
                code = request.urlopen(url).getcode()

                # 定义_dict记录数据
                _dict = {}
                _dict['url'] = webUrl
                _dict['course'] = webStr
                _dict['courseName'] = courseName
                _dict['ADK'] = ADK
                _dict['comment'] = comment
                # print(code)
                if (code == 200):
                    try:
                        courseData = request.urlopen(req).read()
                        courseData.decode('UTF-8')
                        soup = BeautifulSoup(courseData, 'html.parser')
                    except:
                        print("网页404")
                        errNum += 1
                        continue

                    # 查询具体数值
                    trackNum += 1
                    result = soup.find_all(name='div', attrs={'class': 'o-attributes-table-item'})

                    # print(soup)
                    for y in result:
                        try:
                            key = str(y.strong.string).strip()
                            value = str(y.p.string).strip()
                        except:
                            continue
                        print("{}     {:<50}".format(key, value))

                        _dict[key] = value

                    #  查询是否有前置课
                    result = soup.find_all(name='div', attrs={'class': 'a-card-text m-toggle-text has-focus'})
                    if len(result) != 0:
                        _dict['pre'] = str(result[0].div.string)

                # string = webStr +"   "+ _dict['courseName'] +"   "+_dict['ADK'].rjust(80)+ _dict.get('Offering Terms', '没写T几').rjust(75)+"    "+ _dict.get('pre','没有前置课')
                string = "{:>8}  {:>58}  {:>6}  {:>35}      {}".format(webStr,_dict['courseName'],_dict['ADK'],_dict.get('Offering Terms', '没写T几'),_dict.get('pre','没有前置课'))

                f.write(string+"\n")
                # print("{}   {:<12s} ".format(webUrl,str(webStr)))
        print("总数: {}  有效:   {}    爬取:  {}  404: {}".format(courseNum,validNum,trackNum,errNum))







# if __name__ == "main":
url = 'http://www.engineering.unsw.edu.au/study-with-us/current-students/academic-information/electives/pg-electives'
year = time.localtime(time.time())[0]
direct = '/Users/icream/Desktop/course.txt'
# 明年的
# direct == 存放地址
getDetail(direct,url,year+1)
print('打印成功')