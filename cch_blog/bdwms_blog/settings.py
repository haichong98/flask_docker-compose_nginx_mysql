import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# 判断是哪个系统
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    '''注意配置文件必须大写！！！！！！！'''
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')  # 加密相关使用的秘钥，这里还只是开发时使用

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # 设定sqlalchemy的配置，不跟踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    # 设置ckeditor
    CKEDITOR_ENABLE_CSRF = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image'  # 设置ckeditor图片文件上传的方法

    # 设置邮箱
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('bdwms', MAIL_USERNAME)

    BDWMS_BLOG_EMAIL = os.getenv('BDWMS_BLOG_EMAIL')  # 管理员邮箱地址
    BDWMS_BLOG_POST_PER_PAGE = 10  # 每页文章数量
    BDWMS_BLOG_MANAGE_POST_PER_PAGE = 15
    BDWMS_BLOG_COMMENT_PER_PAGE = 15  # 评论数目
    # ('theme name', 'display name')
    BDWMS_BLOG_THEMES = {'white': 'White', 'black': 'Black'}
    BDWMS_BLOG_SLOW_QUERY_THRESHOLD = 1

    BDWMS_BLOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    BDWMS_BLOG_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


class DevelopmentConfig(BaseConfig):
    '''开发数据库路径'''
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    '''测试配置'''
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(BaseConfig):
    '''生产配置'''
    CACHE_TYPE = 'redis'  # 设置缓存类型
    CACHE_REDIS_URL = 'redis://:@redis:6379/0'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))  # 生产环境使用设定的数据库


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
