
from scrapy.spider import BaseSpider

from scrapy.selector import HtmlXPathSelector
from ucker.items import FormItem
from ucker.items import FrameItem
from ucker.items import InputItem

from scrapy.conf import settings

class FormSpider(BaseSpider):
    name = "FormInputSpider"
    #allowed_domains = ["http://www.dmoz.org/"]
    allowed_domains = ["ib.absa.co.za"]
    #allowed_domains = ["idfaclothing.com"]
    start_urls = [
        #"https://ib.absa.co.za/ib/ib.jsp"
	'https://ib.absa.co.za/ib/Authenticate.do'
	#"http://www.dmoz.org/"
    ]
    
    def parse(self, response):
	print(response)
	hxs = HtmlXPathSelector(response)
#	forms = hxs.select('//frame')
	#print(forms)
	forms = hxs.select('//form')
	print(forms)
	actions = []
	items = []
	for form in forms:
		formItem = FormItem()
		a = form.select("@action")
		formItem["actionURL"] = a.extract()
		items.append(formItem)
		inputs = form.select(".//input")
		inputItems = []
		for formInput in inputs:
			inputName = formInput.select("@name").extract()
			inputSize = formInput.select("@size").extract()
			inputMaxlength = formInput.select("@maxlength").extract()
			inputValue = formInput.select("@value").extract()
			inputType = formInput.select("@inputType").extract()
			inputItem = InputItem()
			inputItem["name"] = inputName
			inputItem["size"] = inputSize
			inputItem["maxlength"] = inputMaxlength
			inputItem["value"] = inputValue
			inputItem["inputType"] = inputType
			inputItems.append(inputItem)
		formItem["inputs"] = inputItems
		
	
	return items


