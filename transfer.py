

import sys
import re
import os

path = '/Users/icream/Documents/blog/source/_posts'
files = os.listdir(path)
# print(files)
for x in files:
    if '.md' not in x:
        continue
    try:
        with open(path+'/'+x, 'r') as f:
            content = f.read()
            pattern = re.compile(r'img-\n')
            pa = re.compile(r'x-oss-\n')
            pb = re.compile(r'upload-\n')
            pc = re.compile(r'auto-\n')
        line = re.sub(pattern, 'img-', content)
        if line == '':
            line = content
        line = re.sub(pa, 'x-oss-', line)
        if line == '':
            line = content
        line = re.sub(pb, 'upload-', line)
        if line == '':
            line = content
        line = re.sub(pc, 'auto-', line)
        # print(line)
        if line != '':
            with open(path+'/'+x, 'w') as f:
                f.write(line)
    except:
        print('error   ',x)
    # print(path+'/'+x)


