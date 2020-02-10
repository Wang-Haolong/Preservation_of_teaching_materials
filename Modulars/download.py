#By Wang Haolong
import requests as re
import threading as th
import os

Max_Threads=5

class Crawler:
    '''To download a book'''

    def __init__(self, path, url):
        '''init'''
        self.path=path
        self.url=url
        self.url_list=[]
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        self.create_path()
        self.get_url()
        self.start_downloading()

    def create_path(self):
        '''Create path to save files'''
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        print('保存路径获取成功')

    def get_url(self):
        '''get urls from the html file'''
        self.html_file = re.get(self.url, headers = self.headers).content.decode('utf-8').splitlines()
        self.flag = False
        self.url_temp=''
        for i in self.html_file[292]:
            if i == '"':
                if self.flag == False:
                    self.flag = True
                else:
                    if 'http' in self.url_temp and 'jpeg' in self.url_temp:
                        self.url_list.append(self.url_temp)
                    self.url_temp = ''
                    self.flag = False
            elif self.flag:
                self.url_temp += i
        print('资源url获取成功，共' + str(len(self.url_list)) + '个')

    def getpic(self, id, url):
        '''Download an save files'''
        with open(self.path + '\\' + 'page' + str(id) + '.jpeg', 'wb') as goal_file:
            goal_file.write(re.get(url, headers = self.headers).content)

    def start_downloading(self):
        '''start'''
        cnt = 0
        threads = []
        while len(self.url_list) or len(threads):
            for thread in threads:
                if not thread.is_alive():
                    threads.remove(thread)
            while len(threads) < Max_Threads and len(self.url_list):
                thread = th.Thread(target= self.getpic, args= (cnt, self.url_list.pop(0)))
                thread.setDaemon(True)
                thread.start()
                threads.append(thread)
                cnt += 1