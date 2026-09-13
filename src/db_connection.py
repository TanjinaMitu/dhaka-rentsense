import yaml
from sqlalchemy import create_engine

def get_mysql_engine():
    """Reads YAML settings and returns SQLAlchemy database engine."""
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)["mysql"]
        
    connection_uri = f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    return create_engine(connection_uri)