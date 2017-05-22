#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 要启用的浏览器driver, 因为有些人PhantomJS配置可能有问题，默认使用Firefox(容易配置).
# 具体参考selenium的浏览器环境配置
browser_driver = 'PhantomJS'  # 可以替换为Chrome
# 百度用户名
user_name = 'klqbtnsns123'
# 百度密码
password = '11223344'
# 百度登陆链接
login_url = ('https://passport.baidu.com/v2/?login&tpl=mn&u='
             'http%3A%2F%2Fwww.baidu.com%2F')
# 一周
one_week_trend_url = ('http://index.baidu.com/?tpl=trend&type=0'
                      '&area=0&time=12&word={word}')
# 区间
time_range_trend_url = ('http://index.baidu.com/?tpl=trend&type=0&area=0'
                        '&time={start_date}|{end_date}&word={word}')
# api
all_index_url = ('http://index.baidu.com/Interface/Search/getAllIndex/'
                 '?res={res}&res2={res2}&startdate={start_date}'
                 '&enddate={end_date}')
# 图片信息的api
index_show_url = ('http://index.baidu.com/Interface/IndexShow/show/?res='
                  '{res}&res2={res2}&classType=1&res3[]={enc_index}'
                  '&className=view-value&{t}'
                  )
# 判断登陆状态的地址
user_center_url = 'http://i.baidu.com/'
# 判断登陆的标记
login_sign = 'http://passport.baidu.com/?logout'
# 线程数
num_of_threads = 40
# 要获取趋势的类别，默认是三种趋势都获取。all代表整体趋势，pc代表PC趋势, wise代表移动趋势
index_type_list = ['all']  #, 'pc', 'wise'
#关键字列表
key_list = ['insta360', 'gear 360', 'theta s', 'ZMER', 'VR相机', '全景相机', '360相机', 'GoPro']