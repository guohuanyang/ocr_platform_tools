# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         test
# Description:  
# Author:       guohuanyang
# Date:         2021/8/13
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------


from fuzzywuzzy import fuzz
from fuzzywuzzy import process

query_text = "报告期各期发行人收入中直接、间接销售给小米的金额及占比、销售内容,相关在手订单情况,该股东入股前后前述销售模式、销售金额等是否发生明显变化;"
search_text_1 = '3、小米产业基金入股发行人主要是由于看好发行人所处行业前景、业务布局、在细分领域的竞争力和市场占有率及抗风险能力等,小米产业基金入股的价格定价公允;发行人已在《招股说明书》中补充披露了小米产业基金入股发行人的原因、入股价格是否公允,报告期各期发行人收入中直接、间接销售给小米的金额及占比、销售内容,相关在手订单情况,该股东入股前后前述销售模式、销售金额等是否发生明显变化等事项进行了补充披露。2020年9月,小米通讯技术有限公司与发行人签署了《采购框架合同》,发行人成为小米通讯技术有限公司的FPC产品的直接供应商,小米产业基金入股发行人并非小米将发行人纳入FPC产品直接供应商的主要考虑因素,小米将发行人纳入FPC产品直接供应商与小米产业基金入股没有直接关系,小米产业基金入股发行人之后小米与发行人直接合作具有合理性;发行人与小米开展直接合作的相关流程与小米开发其他同类供应商的一般流程一致,审核周期在正常周期范围内;小米产业基金及小米公司不存在与发行人业务、销售等经营相关的约定或利益安排,不存在利益输送安排。'
search_text_2 = '四、披露小米长江产业基金合伙企业(有限合伙)入股发行人的原因、入股价格是否公允;报告期各期发行人收入中直接、间接销售给小米的金额及占比、销售内容,相关在手订单情况,该股东入股前后前述销售模式、销售金额等是否发生明显变化;小米将公司纳入FPC产品的直接供应商的时间、背景,是否与该股东入股发行人有关,销售收入及在手订单情况;是否存在与发行人业务、销售等经营相关的约定或利益安排'
x = fuzz.partial_ratio(query_text, search_text_1)

y = fuzz.partial_ratio(query_text, search_text_2)

print(x)
print(y)


x = process.extract(query_text, [search_text_1])
y = process.extract(query_text, [search_text_2])
print(x)
print(y)


import requests
import uuid
import json


def generate_request_id():
    return str(uuid.uuid4())


img_path = "/Users/guohuanyang/Downloads/问题文档/7.南凌物联网综合运营支撑平台系统.pdf"

json_data = {"file_type": "wanli",
             "recognition_category": "document",
             "rotate_category": "document",
             "make_2layer_pdf": False,
             "desalt_signet": True,
             "char_info": True}
json_str = json.dumps(json_data)
post_tuple = {"file": open(img_path, "rb"), "data": json_str}
response = requests.post("http://ysocr.datagrand.cn/ysocr/ocr", files=post_tuple)
print(response.text)
