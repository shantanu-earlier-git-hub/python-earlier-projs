from flask import Flask
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../templates', static_folder='../static')

### radis config
# Configure the cache to use Redis
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_REDIS_HOST'] = 'localhost' # Or your Redis server IP/hostname
app.config['CACHE_REDIS_PORT'] = 6379
app.config['CACHE_REDIS_DB'] = 0
app.config['CACHE_DEFAULT_TIMEOUT'] = 300 # Default timeout in seconds

cache = Cache(app)


### db config
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:passw0rd@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_BINDS'] = {
    'mysql_db': 'mysql+pymysql://root:passw0rd@localhost:3306/mysql_db'
    # 'pg_logs': 'postgresql://username:password@localhost/logs_db'
}

db = SQLAlchemy()

db.init_app(app)
