import scrapy
from scrapy.selector import Selector
from catfilm.items import CatfilmItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        result_list = []
        item = CatfilmItem()
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies:
            if len(result_list) == 10:
                break
            name = movie.xpath('./div[@class="movie-hover-title"][1]/span/text()').extract_first()
            movie_type = movie.xpath('./div[@class="movie-hover-title"][2]/text()').extract()[1].strip()
            online_time = movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()').extract()[1].strip()
            # print(name)
            # print(movie_type)
            # print(online_time)
            # print("--------")
            movie_info = {
                "name": name,
                "movie_type": movie_type,
                "online_time": online_time
            }

            result_list.append(movie_info)
        item['result_list'] = result_list
        yield item


