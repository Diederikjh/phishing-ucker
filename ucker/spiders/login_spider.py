

from scrapy.spider import BaseSpider

from scrapy.selector import HtmlXPathSelector
from ucker.items import FormItem
from ucker.items import FrameItem
from ucker.items import InputItem
from scrapy.http import FormRequest, Request

from phishing_uck import getRandomNumberString

class LoginSpider(BaseSpider):
    name = "LoginSpider"
    allowed_domains = ["dmoz.org"]
    #allowed_domains = ["absa.co.za"]
    #allowed_domains = ["idfaclothing.com"]
    start_urls = [
        #"https://ib.absa.co.za/ib/ib.jsp"
	#'https://ib.absa.co.za/ib/Authenticate.do'
	"http://www.dmoz.org/"
    ]
    def parse(self, response):
	print(getRandomNumberString(5))
	#print formdata
	#formdata={'AccessAccount': '123456789111111', 'PIN': '12345'},
        return [FormRequest.from_response(response,
                    formdata={'q': 'foo'},
                    callback=self.after_login)]

    def after_login(self, response):
        print response
	print response.body

        # continue scraping with authenticated session...


class AbsaSpider(BaseSpider):
    name = "AbsaLoginSpider"
    allowed_domains = ["absa.co.za"]
    start_urls = [
	'https://ib.absa.co.za/ib/Authenticate.do'
    ]
    def parse(self, response):
	return [FormRequest.from_response(response,
                 #Notice: JAVASCRIPT adds YIPPEE for server to verify running of JS.
                 formdata={'AccessAccount': '123456789', 'PIN': '12345', 'JAVASCRIPT': 'YIPPEE'},
                 callback=self.after_login)]

    def after_login(self, response):
	f = open('response.html', 'w')
	f.write(response.body)
	f.close()
        print response


        # continue scraping with authenticated session...

