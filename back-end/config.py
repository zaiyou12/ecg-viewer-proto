import os
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__name__))
parent_dir = Path(basedir).parent
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    # DATABASE_URL = os.environ.get('DEV_DATABASE_URL') or \
    #     'sqlite://' + os.path.join(basedir, 'sqlite.db')
    # DATABASE_URL = os.environ.get('DEV_DATABASE_URL') or os.path.abspath("data/ecg_meta.db")
    DATABASE_URL = os.path.join(parent_dir, "data/ecg_meta.db")
    DATA_ROOT_DIR = os.path.join(parent_dir)

class TestConfig(Config):
    TESTING = True
    DATABASE_URL = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite://' + os.path.join(basedir, 'sqlite.db')

class ProdConfig(Config):
    DATABASE_URL = os.environ.get('DATABASE_URL')

config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,

    'default': DevConfig
}
