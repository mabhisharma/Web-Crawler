#!/usr/bin/python3.5

import threading
from queue import Queue
from spider import spider
from general import *
from domain import *

PROJECT_NAME = input("Please Enter the Project Name :\n")
HOMEPAGE = input("Please Enter a valid Homepage URL which you want to crawl :\n")
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def create_spiders():
	for _ in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()


def work():
	while True:
		url = queue.get()
		spider.crawl_page(threading.current_thread().name,url)
		queue.task_done()

		



def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()

def crawl():
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links)>0:
		print(str(len(queued_links)) + ' Links in queue')
		create_jobs()



create_spiders()
crawl()