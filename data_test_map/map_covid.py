import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据
file = open('covid.txt','r',encoding="utf-8")
data_read = file.read()
file.close()
# 获得数据
data_dict = json.loads(data_read)
province_list = data_dict['areaTree'][0]['children']
data_list = [] # 存储省份名称和确诊人数

name_map = {
    '台湾': '台湾省',
    '香港': '香港特别行政区',
    '澳门': '澳门特别行政区',
    '内蒙古': '内蒙古自治区',
    '新疆': '新疆维吾尔自治区',
    '宁夏': '宁夏回族自治区',
    '西藏': '西藏自治区',
    '广西': '广西壮族自治区',
    '北京': '北京市',
    '天津': '天津市',
    '上海': '上海市',
    '重庆': '重庆市',
    # 其他省份名称保持不变
}

for province_data in province_list:
    province_name = province_data['name'] # 省份名称
    province_confirm = province_data['total']['confirm'] # 确诊人数
    # 使用 name_map 进行名称映射，如果没有映射则根据情况添加"省"或"自治区"
    if province_name in name_map:
        mapped_name = name_map[province_name]
    elif province_name in ['北京', '天津', '上海', '重庆']:
        mapped_name = province_name + '市'
    else:
        mapped_name = province_name + '省'
    data_list.append((mapped_name,province_confirm))


map = Map()
map.add("各省疫情地图",data_list,maptype='china',is_map_symbol_show=False)
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(is_show=True,
                                  is_piecewise=True,
                                  pieces=[
                                      {'min':1,'max':99,'label':'1-99','color':'#CCFFFF'},
                                      {'min':100,'max':999,'label':'100-999','color':'#FFFF99'},
                                      {'min':1000,'max':4999,'label':'1000-4999','color':'#FF9966'},
                                      {'min':5000,'max':9999,'label':'5000-9999','color':'#FF6666'},
                                      {'min':10000,'max':99999,'label':'10000-99999','color':'#CC3333'},
                                      {'min':100000,'label':'100000+','color':'#990033'}]
                    )
    )
map.render("全国疫情地图.html")