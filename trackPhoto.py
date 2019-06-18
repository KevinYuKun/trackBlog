import sys,re,os
from urllib import request
import requests
import shutil
def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.mkdir(path)

def remove(path):
    file = os.listdir(path)
    for x in file:
        if '.DS_Store' in x:
            continue
        if '.md' not in x:
            shutil.rmtree(path+'/'+x)
            print('delete {} successful'.format(x))



path = '/Users/icream/Documents/blog/source/_posts'
files = os.listdir(path)
# 删除已下载图片
# remove(path)

for x in files:
    if 'md' in x:
        try:
            with open(path + '/' + x, 'r') as f:
                content = f.read()
                pattern = re.compile(r'!\[.*\][(](.*)[)]')
                lines = re.findall(pattern,content)
                print('-----------------{}------------'.format(x))
                # 文件夹名字
                fileName = re.compile(r'(.*)\.md')
                name = re.findall(fileName,x)
                removeDul = sorted(set(lines),key=lines.index)
                for y in range(len(removeDul)):
                    try:
                        newFileName = path+'/'+name[0]
                        mkdir(newFileName)
                        r = requests.get(removeDul[y],timeout=10)
                        # print(newFileName+'/'+str(y)+'.jpg')
                        with open(newFileName+'/'+str(y)+'.jpg','wb') as w:
                            w.write(r.content)
                    except:
                        print('download or save error')
                print("{}--------爬去完毕".format(x))
        except:
            print("open error----{}".format(x))


