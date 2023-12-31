import os


if __name__ == '__main__':
    API_KEY = os.getenv('API_KEY', None)
    ENDPOINT_SCHEMA_URL = os.getenv('ENDPOINT_SCHEMA_URL', None)
    API_SECRET_KEY = os.getenv('API_SECRET_KEY', None)
    BOOTSTRAP_SERVER = os.getenv('BOOTSTRAP_SERVER', None)
    SCHEMA_REGISTRY_API_KEY = os.getenv('SCHEMA_REGISTRY_API_KEY', None)
    SCHEMA_REGISTRY_API_SECRET = os.getenv('SCHEMA_REGISTRY_API_SECRET', None)
    MONGO_DB_URL = os.getenv('MONGO_DB_URL', default=None)

    print(API_KEY)
    print(ENDPOINT_SCHEMA_URL)
    print(API_SECRET_KEY)
    print(BOOTSTRAP_SERVER)
    print(SCHEMA_REGISTRY_API_KEY)
    print(SCHEMA_REGISTRY_API_SECRET)
    print(MONGO_DB_URL)
