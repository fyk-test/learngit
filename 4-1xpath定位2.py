#! /usr/bin/env python
#coding=utf-8

#通过python的lxml库，利用xpath进行HTML的解析

#xpath 路径选择表达式定位

'''
xpath常用规则
nodename        选取此节点的所有节点
/               从当前节点选取所有子节点
//              从当前节点选取子孙节点
.               选取当前节点
..              选取当前节点的父节点
@               选取属性
'''
from lxml import etree
html = etree.parse('./test.html',etree.HTMLParser())
#result = etree.tostring(html)
#获取所有节点
result = html.xpath('//*')
print('所有节点',result)

#子节点
result = html.xpath('//li/a')
print('子节点是：',result)

#属性匹配 <li class=item-0>tessst  tesdg</li>
result = html.xpath('//li[@class="item-0"]')
print('通过属性匹配节点',result)

#属性获取 <a href='link1.html'>first text</a>
result = html.xpath('//li/a/@href')
print('获取节点属性',result)

#获取文本
result = html.xpath('//li[@class="item-0"]//text()')
print('文本内容',result)
