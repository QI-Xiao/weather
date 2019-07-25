# -*- coding: 'utf-8' -*-

import requests

while True:
    city = input('请输入城市,回车退出:\n')
    if not city:
        break

    try:
        req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    except:
        print ('查询失败')
        break

    # print(req.text)
    dic_city = req.json() # 转换为字典
    # print(dic_city)

    city_data = dic_city.get('data')  # 没有’data‘的话返回 None

    if city_data:
        city_forecast = city_data['forecast'][0] # 下面的都可以换成'get'方法
        print(city_forecast.get('date'))
        print(city_forecast.get('high'))
        print(city_forecast.get('low'))
        print(city_forecast.get('type'))
    else:
        print('未获得')
