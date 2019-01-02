# #找目标url

#找到大分类的url接口
# """
# http://mce.mogucdn.com/jsonp/multiget/3?
# callback=jQuery211015894426054406874_1537145503076
# &pids=110119
# &appPlat=pc&_=1537145503077
# """

#找到大分类下的小分类的url接口
# """
# http://mce.mogucdn.com/jsonp/multiget/3?
# callback=jQuery211015894426054406874_1537145503076
# &pids=109499%2C109520%2C109731%2C109753%2C110549
# %2C109779%2C110548%2C110547%2C109757%2C109793%
# 2C109795%2C110563%2C110546
# %2C110544&appPlat=pc&_=1537145503080
# """


#找到分类列表的url
# """
# http://list.mogujie.com/search?callback=jQuery21102640581843429468_1537146104048
# &_version=8193&ratio=3%3A4&cKey=15&page=53
# &sort=pop&ad=0&fcid=50244&action=clothing
# &acm=3.mce.1_10_1hh4q.109499.0.sPJDrr3RvSKoZ.pos_1-m_407649-sd_119-mf_15261_1047915-idx_0-mfs_96-dm1_5000
# &ptp=1._mf1_1239_15261.0.0.95Ca1nOq&_=1537146104101
# """

import requests
import re
import json
def get_big_categorypid():
    
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    url = 'http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery211015894426054406874_1537145503076&pids=110119&appPlat=pc&_=1537145503077'
    response = requests.get(url,headers=header)
    
    print(response.status_code)
    # print(response.text)
    #写一个正则匹配ｊｓｏｎ字符串
    pattern = re.compile('.*?\((.*?)\)',re.S)
    #获取ｊｓｏｎ字符串
    data = re.findall(pattern,response.text)[0]
    #将json字符串转换为python对象
    json_data = json.loads(data)
    # print(json_data)
    print(type(json_data))
    category_list = json_data['data']['110119']['list']
    # print(category_list)
    categoryPid_list = []
    for item in category_list:
        categoryPid_list.append(item['categoryPid'])
    
    print('%2C'.join(categoryPid_list))

    return '%2C'.join(categoryPid_list)

def get_small_category(pids):
    pass
    #找到大分类下的小分类的url接口
    url = """http://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery211015894426054406874_1537145503076&pids=%s&appPlat=pc&_=1537145503080""" % pids

    print(url)
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    response = requests.get(url,headers=header)

    print(response.status_code)
    # print(response.text)
    #写一个正则匹配ｊｓｏｎ字符串
    pattern = re.compile('.*?\((.*?)\)',re.S)
    #获取ｊｓｏｎ字符串
    data = re.findall(pattern,response.text)[0]
    #将json字符串转换为python对象
    json_data = json.loads(data)
    # print(json_data)
    small_category_dict = {}
    for categoryid,categorydata in json_data['data'].items():
        print(categorydata['list'])
        for item in categorydata['list']:
            title = item['title']
            # 'http://list.mogujie.com/book/skirt/50004?acm=3.mce.1_10_1hddc.109520.0.4Q3KNr3RGdAV5.pos'
            pattern = re.compile('\d+')
            result = re.search(pattern,item['link'])
            small_categoryid = result.group()
            small_category_dict[title] = small_categoryid

    
    return small_category_dict


def get_data_by_fcid(fcid,endpage):

    for page in range(1,endpage+1):
        url = '''
        http://list.mogujie.com/search?callback=jQuery21102640581843429468_1537146104048
        &_version=8193&ratio=3%3A4&cKey=15&page=%s
        &sort=pop&ad=0&fcid=%s&action=clothing
        &acm=3.mce.1_10_1hh4q.109499.0.sPJDrr3RvSKoZ.pos_1-m_407649-sd_119-mf_15261_1047915-idx_0-mfs_96-dm1_5000
        &ptp=1._mf1_1239_15261.0.0.95Ca1nOq&_=1537146104101
        ''' % (str(page),fcid)

        header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }

        response = requests.get(url,headers=header)

        print(response.status_code)

        #解析数据


        #存储数据

        





    

if __name__ == '__main__':
   pids = get_big_categorypid()
   small_category_dict = get_small_category(pids)
   print(small_category_dict)

   key = input('请输入要获取的分类名称:')
   endpage = int(input('请输入要获取的页码:'))
   fcid = small_category_dict[key]
   print(fcid)

   get_data_by_fcid(fcid,endpage)






