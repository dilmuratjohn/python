from baike_crawler import url_manager, html_downloader, html_outputer, html_parser

class Crawler(object):

    def __init__(self):
        self.urls = url_manager.url_manager()
        self.downloader = html_downloader.html_downloader()
        self.parser = html_parser.html_parser()
        self.outputer = html_outputer.html_outputer()

    def craw(self,root_url,url_amount):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print ('crawling %d : %s ...' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == url_amount:
                    break
                count += 1
            except:
                print('Crawling failure ')

        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    url_amount=1000
    obj_Crawler = Crawler()
    obj_Crawler.craw(root_url,url_amount)
