"""
Configuration settings for the ToDo List API.
The definition of the different configuration settings is contained here:
- Development Configuration
- Production Configuration
"""


class Config:
    """
    The definition of the global configuration is defined here.
    Attributes such as SECRET_KEY are the same no matter the platform used.
    """

    SECRET_KEY = 'i-am-super-awesome'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(Config):
    """
    The configuration settings for development mode is defined here.
    Attributes such as SQLALCHEMY_DATABASE_URI, DEBUG are different for other
    modes, so they are defined in a class called DevelopmentConfig.
    """

    SQLALCHEMY_DATABASE_URI = 'postgres://zdvbmfxp:M_o8e7nHBqgbJ7R4hzxIWco_ekEuxsBn@babar.elephantsql.com:5432/zdvbmfxp'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class ProductionConfig(Config):
    """
    The configuration settings for production mode is defined here.
    Attributes such as SQLALCHEMY_DATABASE_URI, DEBUG are different for other
    modes, so they are defined in a class called ProductionConfig.
    """

    SQLALCHEMY_DATABASE_URI = 'postgres://zdvbmfxp:M_o8e7nHBqgbJ7R4hzxIWco_ekEuxsBn@babar.elephantsql.com:5432/zdvbmfxp'


# Object containing the different configuration classes.
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
