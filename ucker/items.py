# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class FormItem(Item):
    actionURL = Field()
    inputs = Field()

class InputItem(Item):
    name = Field()
    size = Field()
    maxlength = Field()
    value = Field()
    inputType = Field()


class FrameItem(Item):
    srcURL = Field()
    
