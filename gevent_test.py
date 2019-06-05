# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 18:26
# @Author  : wcl
# @File    : gevent_test.py
# @Software: PyCharm
from gevent import monkey

monkey.patch_socket()
import gevent
import urllib2


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0)


def url_look(url):
    print('GET:%s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


if __name__ == "__main__":
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)

    g1.join()
    g2.join()
    g3.join()

    gevent.joinall(
        [
            # gevent.spawn(url_look, 'https://www.python.org/'),
            gevent.spawn(url_look, 'https://www.baidu.com/'),
            # gevent.spawn(url_look, 'https://www.yahoo.com/'),
            # gevent.spawn(url_look, 'https://github.com/'),
        ]
    )
