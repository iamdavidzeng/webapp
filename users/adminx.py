#!/usr/bin/env python
# -*- coding:utf-8 -*-


import xadmin
from xadmin import views


class BaseSetting(object):
    # enable_themes = True  # 打开主题功能
    use_bootswatch = True


# 针对全局的
class GlobalSettings(object):
    site_title = "个人博客后台管理"  # 系统名称
    site_footer = "D4vidz"  # 底部版权栏
    menu_style = "accordion"  # 将菜单栏收起来

    # global_models_icon = {
    #     UserProfile: "glyphicon glyphicon-user", SMS: "fa fa-cloud"
    # }  # 设置models的全局图标


# 注册，注意一个是BaseAdminView，一个是CommAdminView
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
