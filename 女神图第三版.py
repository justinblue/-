# -*- coding:utf-8 -*-
import urllib

#2打开网页下载对应的图片
url0='http://qq.yh31.com'
try:
    for i in range(1,100):
        if i==1:
            url='http://qq.yh31.com/zjbq/0551964.html'
            content=urllib.urlopen(url).read()
            body=content.find('<body>')
            overflow=content.find('c_content_overflow',body)

            img=content.find('img src=',overflow)
            alt=content.find('alt',img)

            bar=content[alt:alt+2]

            while len(bar)<50:
                picture=content[img+9:alt-2]
                print picture
                data=urllib.urlopen(url0+picture)

                #3下载图片（命名，文件夹，格式）
                #name=name
                #format=format()
                name=picture.split('/')
                print name
                f=file('E:\python\download\\'+name[-2]+'.'+name[-1],'wb')
                f.write(data.read())
                f.close

                img=content.find('img src=',alt)
                bar = content[alt:img]
                alt=content.find('alt',img)


            else:
                print'page 1 complete!'

        else:
            url = 'http://qq.yh31.com/zjbq/0551964'+'_'+ str(i) +'.html'
            content = urllib.urlopen(url).read()
            body = content.find('<body>')
            overflow = content.find('c_content_overflow', body)

            img = content.find('img src=', overflow)
            alt = content.find('alt', img)

            bar = content[alt:alt + 2]

            while len(bar) < 50:
                picture = content[img + 9:alt - 2]
                print picture
                data = urllib.urlopen(url0 + picture)

                # 3下载图片（命名，文件夹，格式）
                # name=name
                # format=format()
                name = picture.split('/')
                print name
                f = file('E:\python\download\\' + name[-2] + '.' + name[-1], 'wb')
                f.write(data.read())
                f.close

                img = content.find('img src=', alt)
                bar = content[alt:img]
                alt = content.find('alt', img)


            else:
                print'page '+str(i)+' complete!'

except IOError,e:
    print e