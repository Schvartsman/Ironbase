#!/usr/bin/env python3
from mysql.connector import pooling
from config import DBConfig


class Database:
    def __init__(self, config: DBConfig):
        self.pool = pooling.MySQLConnectionPool(
            pool_name="wolf_pool",
            pool_size=5,
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database,
        )

    def get_connection(self):
        return self.pool.get_connection()
