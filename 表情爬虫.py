# -*- coding:utf-8 -*-
import urllib
import re

#2打开网页下载对应的图片
url0='http://qq.yh31.com'
try:
    for i in range(1,100):
        if i==1:
            url='http://qq.yh31.com/zjbq/0551964.html'
            content=urllib.urlopen(url).read()
            body=content.find('<body>')
            overflow=content.find('c_content_overflow',body)
            c_bot_fy=content.find('c_bot_fy',body)

            img=content.find('img src=',overflow)
            alt=content.find('alt',img)

            bar=content[overflow:c_bot_fy]
            picture=re.findall('img src="(.*?)"',bar)

            for index in picture:
                print picture
                data=urllib.urlopen(url0+index)

                #3下载图片（命名，文件夹，格式）
                #name=name
                #format=format()
                name=index.split('/')
                print name
                f=file(name[3],'wb')
                f.write(data.read())
                f.close

            else:
                print'page 1 complete!'

        else:
            url = 'http://qq.yh31.com/zjbq/0551964'+'_'+ str(i) +'.html'
            content = urllib.urlopen(url).read()
            body = content.find('<body>')
            overflow = content.find('c_content_overflow', body)
            c_bot_fy=content.find('c_bot_fy',body)

            img = content.find('img src=', overflow)
            alt = content.find('alt', img)

            bar=content[overflow:c_bot_fy]
            picture=re.findall('img src="(.*?)"',bar)

            for index in picture:
                print picture
                data = urllib.urlopen(url0 + index)

                # 3下载图片（命名，文件夹，格式）
                # name=name
                # format=format()
                name = index.split('/')
                print name
                f = file(name[3], 'wb')
                f.write(data.read())
                f.close

            else:
                print'page '+str(i)+' complete!'

except IOError,e:
    print e
