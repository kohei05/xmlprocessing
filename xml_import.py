# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:21:03 2016

@author: 航平
"""

import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pylab as plt
from matplotlib.font_manager import FontProperties
from function import *
#ファイルのインポート
#ファイル名を入力
print('処理するファイル名を入力してください')
FileName = input('>>')

tree = ET.parse(FileName)
elem = tree.getroot()

#nodeの形状の定義
ShapeDef()#Square,Elipse,Edge,Hexagonを定義

G = nx.Graph()#無向グラフの作成

es = elem.findall(".//mxCell")
for e in es:
    Style = e.get('style')
    Value = e.get('value')
    Relation = (e.get('source'),e.get('target'))
    print(e.tag,e.attrib)#ノードのすべての属性を表示
    #print(e.get('style'))#styleのみを表示
    if Style==Square:
        print('実体:' + Value)#valueのみを表示
        G.add_node('実体:' + Value)
    elif Style==Elipse:
        print('属性:' + Value)#valueのみを表示
        G.add_node('属性:' + Value)
    elif Style==Hexagon:
        print('関係:' + Value)#valueのみを表示
        G.add_node('関係:' + Value)
    elif Style==Edge:
        print('エッジ:' + str(Relation))
        #G.add_edge(e.get('source'),e.get('target'))

pos = nx.spring_layout(G)#最適位置計算
nx.draw_networkx_nodes(G, pos, node_size=200, node_color="w")
nx.draw_networkx_edges(G, pos, width=1)
text_items = nx.draw_networkx_labels(G, pos ,font_size=5, font_family='Hiragino Kaku Gothic ProN',font_color="r")
    
font_prop = FontProperties(fname=r'C:\WINDOWS\Fonts\meiryo.ttc')
for t in text_items.values():
    t.set_fontproperties(font_prop)

plt.xticks([])
plt.yticks([])
plt.show()