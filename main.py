#By Wang Haolong
print("此程序由王浩龙制作\n\n")
import Modulars.Subject as su
import threading as th
import time
word = ''
catalog={}
catalog['语文'] = su.Sunject('语文')
catalog['数学'] = su.Sunject('数学')
catalog['英语'] = su.Sunject('英语')
catalog['物理'] = su.Sunject('物理')
catalog['化学'] = su.Sunject('化学')
catalog['生物'] = su.Sunject('生物')
catalog['政治'] = su.Sunject('政治')
catalog['地理'] = su.Sunject('地理')
catalog['历史'] = su.Sunject('历史')
catalog['语文'].add_book('必修三', 'https://mp.weixin.qq.com/s?__biz=MzIwOTYxMDM0OQ==&mid=100025456&idx=3&sn=73d0593b37b93873c76a2686f7332fa9&scene=19#wechat_redirect')
catalog['数学'].add_book('必修四', 'https://mp.weixin.qq.com/s?__biz=MzIwOTYxMDM0OQ==&mid=100025447&idx=4&sn=e04c7a4702db78583ebac9edeab8a4f8&scene=19#wechat_redirect')
catalog['英语'].add_book('必修三', 'https://mp.weixin.qq.com/s?__biz=MzIwOTYxMDM0OQ==&mid=100025267&idx=3&sn=bb554e6ddea8c4d39e69a3540c52fd79&scene=19#wechat_redirect')
catalog['物理'].add_book('必修二', 'https://mp.weixin.qq.com/s?__biz=MzIwOTYxMDM0OQ==&mid=100025492&idx=2&sn=c85ba8507315ec2ed4f84efe574ff8f3&scene=19#wechat_redirect')
catalog['生物'].add_book('必修二', 'https://mp.weixin.qq.com/s?__biz=MzIwOTYxMDM0OQ==&mid=100025511&idx=2&sn=0ab63615c533a0a9531681683bb5a419&scene=19#wechat_redirect')
catalog['政治'].add_book('必修二', 'https://mp.weixin.qq.com/s?__biz=MzIwOTYxMDM0OQ==&mid=100025574&idx=2&sn=eed50bc77d91136fc22426020dc09562&scene=19#wechat_redirect')
catalog['地理'].add_book('必修二', 'https://mp.weixin.qq.com/s?__biz=MzIwOTYxMDM0OQ==&mid=100025580&idx=2&sn=d17b3e5c71ee2336ed74f66ebdf356ba&scene=19#wechat_redirect')
catalog['历史'].add_book('必修二', 'https://mp.weixin.qq.com/s?__biz=MzIwOTYxMDM0OQ==&mid=100025567&idx=2&sn=3401e724b4e5b08e01adfc6315b96917&scene=19#wechat_redirect')
while True:
    word = input('请输入需下载的科目\n不输入默认下载全部\n输入"exit"退出:\n')
    if word != 'exit':
        if word:
            if word in catalog:
                print('该科目目前有:')
                for i,j in catalog[word].catalog.items():
                    print(i)
                item = input('请输入需下载的项目:\n')
                if item in catalog[word].catalog:
                    catalog[word].get_book(item)
                else:
                    print('暂无此项，请重试')
            else:
                print('暂无此项，请重试')
        else:
            threads=[]
            for i in catalog.values():
                for j in i.catalog.values():
                    threads.append(th.Thread(target= j.get))
            print('开始任务')
            for thread in threads:
                thread.setDaemon(True)
                thread.start()
            while len(threads):
                for thread in threads:
                    if not thread.is_alive():
                        threads.remove(thread)
            print('已全部完成!')
    else:
        print('谢谢使用！')
        time.sleep(2)
        exit()