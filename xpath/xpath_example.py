'''
xpath解析原理：
    1.实例化一个etree对象，且需要将被解析的页面源码数据加载到该对象中。
        如何实例化一个etree对象？
            1.将本地的html文档中的源码加载到etree对象里  etree.parse（filepath）
            2.可以将互联网上获取的源码数据加载到该对象中  etree.HTML('page_text')
    2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获
        xpath('xpath表达式')
    3.xpath表达式
        /:表示从根节点开始定位，表示的是一个层级                                                 r= tree.xpath('/html/body/div')
        //:表示的是多个层级，作用在两个层级之间      当一个层级的子层级只有一个时可以这么使         r= tree.xpath('/html//div')   
          :也可以表示从任意位置开始定位                                                         r= tree.xpath('//div')

        属性定位://div[@class="song"]                      通用写法:tag[@attrName="attrValue"]   当属性有多个时：tag[@attrName1="attrValue1"][@attrName2="attrValue2"][@attrName3="attrValue3"]
        索引定位://div[@class="song"]/p[3]  注意此处的索引不是从0开始 而是从1开始

        取文本：取标签中间存储的文本内容
            /text()     获取的是标签中直系的文本内容
            //text()    获取标签中的全部文本内容
        取属性：取标签对应的属性值
            /@attrName  ex:img/@src

'''
from lxml import etree
#必须写这一句 不知道为什么
parser=etree.HTMLParser(encoding='utf-8')
#实例化好了一个etree对象，并将被解析的源码加载到了tree这个对象中
tree=etree.parse('info.html',parser=parser)
#xpath表达式可以根据层级关系实现标签定位
r= tree.xpath('/html/body//div [@class="hzbtabs"]/span//text()')#从外节点html一层一层到body再到div定位
print(r)