# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------
# Name:         conf
# Description:  
# Author:       guohuanyang
# Date:         2021/8/9
# Email         guohuanyang@datagrand.com
# -------------------------------------------------------------------------------


ENV = 'public'
START = 0
LIMIT = -1

STATIC_ENV = {
    "public": {
        "extract_url": "http://103.229.214.112:58016/extract",
        "create_task_url": "http://103.229.214.112:58017/api/cms/ocr_extraction/upload",
        "login_url": "http://103.229.214.112:58017/api/cms/login",
        "task_detail_url": "http://103.229.214.112:58017/api/cms/ocr_extraction/record_item?record_id={}",
        "task_retry_url": "http://103.229.214.112:58017/api/cms/ocr_extraction/record_item?record_id={}&request_method=put",
    },
    "test": {
        "extract_url": "http://172.253.32.51:58016/extract",
        "create_task_url": "http://172.253.32.51:58017/api/cms/ocr_extraction/upload",
        "login_url": "http://172.253.32.51:58017/api/cms/login",
        "task_detail_url": "http://172.253.32.51:58017/api/cms/ocr_extraction/record_item?record_id={}",
        "task_retry_url": "http://172.253.32.51:58017/api/cms/ocr_extraction/record_item?record_id={}&request_method=put",
    },
    "product": {
        "extract_url": "http://172.21.121.234:58016/extract",
        "create_task_url": "http://172.21.121.234:25101/api/cms/ocr_extraction/upload",
        "login_url": "http://172.21.121.234:25101/api/cms/login",
        "task_detail_url": "http://172.21.121.234:25101/api/cms/ocr_extraction/record_item?record_id={}",
        "task_retry_url": "http://172.21.121.234:25101/api/cms/ocr_extraction/record_item?record_id={}&request_method=put",
    },
}

CUR_ENV = STATIC_ENV[ENV]

CARDS = [
    ("专利证", "./sample/专利证"),
    ("作品证", "./sample/作品证"),
    ("商标证", "./sample/商标证"),
    ("国土证", "./sample/国土证"),
    ("房权证", "./sample/房权证"),
    ("软件证", "./sample/软件证")]

ACCEPT_SUFFIX = ('jpg', 'jpeg', 'png', 'gif', 'svg', 'bmp', 'tif', 'tiff', 'pdf')

LAND_CERTIFICATE = {
    "权利人": {"name": "land_holder", "type": "str", "func": None, "func_args": ()},
    "证书号": {"name": "land_cert_number", "type": "str", "func": "sort_by_x_index", "func_args": ()},
    "面积": {"name": "land_areas", "type": "str", "func": None, "func_args": ()},
    "座落": {"name": "land_location", "type": "str", "func": None, "func_args": ()},
    "权利期限": {"name": "land_rights", "type": "str", "func": None, "func_args": ()},
    "权利性质": {"name": "land_nature", "type": "str", "func": None, "func_args": ()},
    "用途": {"name": "land_purpose", "type": "str", "func": None, "func_args": ()},
    "共有情况": {"name": "land_ownership", "type": "str", "func": None, "func_args": ()},
    "是否是变更文件": {"name": "is_changed", "type": "str", "func": None, "func_args": ()},
    "模版名称": {"name": "template_name", "type": "str", "func": None, "func_args": ()},
    "留痕图": {"name": "trace_map", "type": "base64", "func": None, "func_args": ()},
}

# 房权证
HOUSE_CERTIFICATE = {
    "证书号": {"name": "house_number", "type": "str", "func": "sort_by_x_index", "func_args": ()},
    "权利人": {"name": "house_holder", "type": "str", "func": None, "func_args": ()},
    "共有情况": {"name": "house_share_condition", "type": "str", "func": None, "func_args": ()},
    "座落": {"name": "house_location", "type": "str", "func": None, "func_args": ()},
    "权利性质": {"name": "house_nature", "type": "str", "func": None, "func_args": ()},
    "用途": {"name": "house_purpose", "type": "str", "func": None, "func_args": ()},
    "建筑面积": {"name": "house_built_areas", "type": "str", "func": None, "func_args": ()},
    "登记时间": {"name": "house_register_date", "type": "str", "func": None, "func_args": ()},
    "是否是变更文件": {"name": "house_is_changed", "type": "str", "func": None, "func_args": ()},
    "模版名称": {"name": "template_name", "type": "str", "func": None, "func_args": ()},
    "留痕图": {"name": "trace_map", "type": "base64", "func": None, "func_args": ()},
}

# 商标注册证/商标查册/商标档案
TRADEMARK_CERTIFICATE = {
    "证书号": {"name": "trademark_number", "type": "str", "func": None, "func_args": ()},
    "权利人": {"name": "trademark_unit", "type": "str", "func": None, "func_args": ()},
    "商标名称": {"name": "trademark_name", "type": "image", "func": None, "func_args": ()},
    "核定使用商品": {"name": "trademark_goods", "type": "str", "func": None, "func_args": ()},
    "注册日期": {"name": "trademark_date", "type": "str", "func": None, "func_args": ()},
    "有效期至": {"name": "trademark_valid_until", "type": "str", "func": None, "func_args": ()},
    "类别": {"name": "trademark_type", "type": "str", "func": None, "func_args": ()},
    "是否是变更文件": {"name": "trademark_is_changed", "type": "str", "func": None, "func_args": ()},
    "留痕图": {"name": "trace_map", "type": "base64", "func": None, "func_args": ()},
    "变更日期": {"name": "modify_date", "type": "base64", "func": None, "func_args": ()},
}

# 专利
PATENT_CERTIFICATE = {
    "权利人": {"name": "patent_holder", "type": "str", "func": None, "func_args": ()},
    "证书号": {"name": "patent_certification_number", "type": "str", "func": None, "func_args": ()},
    "专利号": {"name": "patent_number", "type": "str", "func": None, "func_args": ()},
    "专利名称": {"name": "patent_name", "type": "str", "func": None, "func_args": ()},
    "专利类型": {"name": "patent_type", "type": "str", "func": None, "func_args": ()},
    "专利申请日": {"name": "patent_limited_term", "type": "str", "func": None, "func_args": ()},
    "授权公告日": {"name": "patent_published_date", "type": "str", "func": None, "func_args": ()},
    "是否是变更文件": {"name": "patent_is_changed", "type": "str", "func": None, "func_args": ()},
    "留痕图": {"name": "trace_map", "type": "base64", "func": None, "func_args": ()},
    "变更日期": {"name": "modify_date", "type": "base64", "func": None, "func_args": ()},
}

# 软件著作证
SOFTWARE_COPYRIGHT = {
    "权利人": {"name": "software_holder", "type": "str", "func": None, "func_args": ()},
    "证书号": {"name": "software_certificate_number", "type": "str", "func": None, "func_args": ()},
    "登记号": {"name": "software_register_number", "type": "str", "func": None, "func_args": ()},
    "软件名称": {"name": "software_name", "type": "str", "func": None, "func_args": ()},
    "权利取得方式": {"name": "software_acquisition_method", "type": "str", "func": None, "func_args": ()},
    "开发完成日期": {"name": "software_finished_date", "type": "str", "func": None, "func_args": ()},
    "首次发表日期": {"name": "software_published_date", "type": "str", "func": None, "func_args": ()},
    "登记日期": {"name": "software_register_date", "type": "str", "func": "repr_char", "func_args": ("，,.。",)},
    "权利范围": {"name": "software_range", "type": "str", "func": None, "func_args": ()},
    "是否是变更文件": {"name": "software_is_changed", "type": "str", "func": None, "func_args": ()},
    "留痕图": {"name": "trace_map", "type": "base64", "func": None, "func_args": ()},
}

# 作品著作证
WORK_CERTIFICATE = {
    "权利人": {"name": "work_holder", "type": "str", "func": None, "func_args": ()},
    "编号": {"name": "work_number", "type": "str", "func": None, "func_args": ()},
    "登记号": {"name": "work_register_number", "type": "str", "func": None, "func_args": ()},
    "作品名称": {"name": "work_name", "type": "str", "func": None, "func_args": ()},
    "创作完成日期": {"name": "work_finished_date", "type": "str", "func": None, "func_args": ()},
    "作品类别": {"name": "work_type", "type": "str", "func": None, "func_args": ()},
    "首次发表日期": {"name": "work_published_date", "type": "str", "func": None, "func_args": ()},
    "登记日期": {"name": "work_register_date", "type": "str", "func": "repr_char", "func_args": ("，,.。",)},
    "是否是变更文件": {"name": "work_is_changed", "type": "str", "func": None, "func_args": ()},
    "留痕图": {"name": "trace_map", "type": "base64", "func": None, "func_args": ()},
}

LAND_TEMPLATE_NAME = "招商证券-国土证"
PATENT_TEMPLATE_NAME = "招商证券-专利"
WORK_TEMPLATE_NAME = "招商证券-作品著作权"
TRADEMARK_TEMPLATE_NAME = "招商证券-商标注册"
SOFTWARE_TEMPLATE_NAME = "招商证券-软件著作权"
HOUSE_TEMPLATE_NAME = "招商证券-房权证"
COMMON_TEMPLATE_NAME = "common"

TEMPLATE_NAME_DICT = {
    LAND_TEMPLATE_NAME: LAND_CERTIFICATE,
    PATENT_TEMPLATE_NAME: PATENT_CERTIFICATE,
    WORK_TEMPLATE_NAME: WORK_CERTIFICATE,
    TRADEMARK_TEMPLATE_NAME: TRADEMARK_CERTIFICATE,
    SOFTWARE_TEMPLATE_NAME: SOFTWARE_COPYRIGHT,
    HOUSE_TEMPLATE_NAME: HOUSE_CERTIFICATE,
    COMMON_TEMPLATE_NAME: {}
}
