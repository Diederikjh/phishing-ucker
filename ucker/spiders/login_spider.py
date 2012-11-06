

from scrapy.spider import BaseSpider

from scrapy.selector import HtmlXPathSelector
from ucker.items import FormItem
from ucker.items import FrameItem
from ucker.items import InputItem
from scrapy.http import FormRequest, Request

from phishing_uck import getRandomNumberString

def getSizeAppropriateDict(response):
	hxs = HtmlXPathSelector(response)
	sizedInputs = hxs.select("//input[@size]")
	postDict = {}
	for sizedInput in sizedInputs:
		inputName = sizedInput.select("./@name")[0].extract()
		print inputName
		inputSize = sizedInput.select("./@size")[0].extract()
		print inputSize
		postDict[inputName] = getRandomNumberString(int(inputSize))
	return postDict

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
	postDict = getSizeAppropriateDict(response)
	
	#Notice: JAVASCRIPT adds YIPPEE for server to verify running of JS.	
	postDict['JAVASCRIPT'] = 'YIPPEE';
	# Remove user, as Default is appropriate
	del(postDict['user'])
	print postDict
	print "DEBUG NOTE: not executing"
	return
	return [FormRequest.from_response(response,
                 formdata=postDict,
                 callback=self.after_login)]

    def after_login(self, response):
	f = open('response.html', 'w')
	f.write(response.body)
	f.close()
        # continue scraping with authenticated session...

