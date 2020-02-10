#By Wang Haolong
import os
class Item:
    '''Store and get Book resources'''

    def __init__(self, name, url):
        '''init'''
        self.name=name
        self.url=url

    def get(self):
        '''Get the resource'''
        import Modulars.download as do
        print('开始下载' + self.name)
        path = os.getcwd() + '\\' + self.name + '\\'
        do.Crawler(self.name, self.url)
        print(self.name + '下载完成')


class Sunject:
    '''A subject'''
    def __init__(self, name):
        '''init'''
        self.name = name
        self.catalog = {}

    def add_book(self, name, url):
        '''add a new book to the catalog'''
        self.catalog[name] = Item(self.name + name, url)

    def get_book(self, id):
        '''download a book'''
        self.catalog[id].get()