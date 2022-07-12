class Config:
    SECRET_KEY = 'ade856f07576deb1f86bb2b12fb627d3619986f98116cc835205bd2db7a9'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://odya:o030101@127.0.0.1:5432/trav'
    DEBUG = True


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///prod_data.db'
    DEBUG = False


config = {
    "default":DevConfig,
    "dev": DevConfig,
    "prod": ProdConfig
}