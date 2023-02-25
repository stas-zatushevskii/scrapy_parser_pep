import scrapy
import re

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']


    def parse(self, response):
        href = []
        for tr in response.css('a.pep::attr(href)').getall():
            if tr not in href:
                href.append(tr)
        for link in href[1:-2]:
            result = 'https://peps.python.org/' + link
            yield response.follow(result, callback=self.parse_pep)


    def parse_pep(self, response):
        words = response.css('h1.page-title::text').get()
        word = words.split(' – ')

        data = {
                'number': re.findall(r'\d+', word[0]),
                'name': word[-1],
                'status': response.css(
                    'dt:contains("Status") + dd').css('abbr::text').get()
            }
        yield PepParseItem(data)
