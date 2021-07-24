import scrapy
from qiushibaike.items import QiushibaikeItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com/text/']
 
    def parse(self, response):
        i=0 
        data=[]
        # 解析：作者的名称+段子内容
        div_list=response.xpath('//div[@class="col1 old-style-col1"]/div')
        for div in div_list:
            #extract可以将字符串提取出来
            author=div.xpath('./div[1]/a[2]/h2/text()')[0].extract()
            #列表调用了extract()后，则表示将列表中每一个字符串提取出来
            content=div.xpath('./a[1]/div[@class="content"]/span//text()').extract()
            content=''.join(content)
            print(author,content)
            i+=1
            item=QiushibaikeItem()
            item['author']=author
            item['content']=content

            yield item #将item提交给管道 
            print()
            if(i==10):
                break;
        
        return data