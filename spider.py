#!/usr/bin/python3.5
from urllib.request import urlopen
from link_finder import LinkFinder
from general import *
from domain import *

class spider:

	project_name = ''
	base_url = ''
	domain_name = ''
	queue_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()



	def __init__(self, project_name, base_url, domain_name):
		spider.project_name = project_name
		spider.base_url = base_url
		spider.domain_name = domain_name
		spider.queue_file = spider.project_name + '/queue.txt'
		spider.crawled_file = spider.project_name + '/crawled.txt'
		self.boot()
		self.crawl_page('FirstPage', spider.base_url)


	
	def boot(self):
		create_folder(spider.project_name)
		create_list(spider.project_name, spider.base_url)
		spider.queue = file_to_set(spider.queue_file)
		spider.crawled = file_to_set(spider.crawled_file)

	@staticmethod
	def crawl_page(thread_name, page_url):
		if page_url not in spider.crawled:
			print(thread_name + ' Now Crawling ' + page_url)
			print('Queue ' + str(len(spider.queue)) + ' | Crawled ' + str(len(spider.crawled)))
			spider.add_links_to_queue(spider.gather_links(page_url))
			spider.queue.remove(page_url)
			spider.crawled.add(page_url)
			spider.update_files()

	@staticmethod
	def gather_links(page_url):
		html_string = ''
		try:
			response = urlopen(page_url)
			if 'text/html' in response.getheader('Content-Type'):
				html_bytes = response.read()
				html_string = html_bytes.decode('utf-8')
			finder = LinkFinder(spider.base_url, page_url)
			finder.feed(html_string)	
		except:
			print("Error : Cannot Crawl the Page " + page_url)
			return set()
		return finder.page_links()


	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if (url in spider.queue) or (url in spider.crawled):
				continue
			if spider.domain_name != get_domain_name(url):
				continue
			spider.queue.add(url)


	@staticmethod
	def update_files():
		set_to_file(spider.queue, spider.queue_file)
		set_to_file(spider.crawled, spider.crawled_file)


