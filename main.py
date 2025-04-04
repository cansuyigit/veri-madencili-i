import time
from crawler import Crawler

crawler = Crawler()

start = time.time()
crawler.get_news(3218000, 3224000)
crawler.save_news()
end = time.time()

print(end-start)