import scrapy


class FirstSpider(scrapy.Spider):
    #爬虫文件的名称：就是爬虫源文件的唯一标识 一般在终端请确定后就不改了
    name = 'first'
    
    # 允许的域名：用来限定start_url列表中那些url可以进行请求发送  但因为不好用所以都被注释掉
    # allowed_domains = ['www.xxx.com']
    
    #起始的url列表：该列表中存放的url会被scrapy自动发送请求
    start_urls = ['https://www.baidu.com/','https://www.sogou.com/']

    #用于数据解析,response参数用于接收请求成功后的的响应对象
    def parse(self, response):
        print(response1)
