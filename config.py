#!/usr/bin/env python3
from dataclasses import dataclass
import os


@dataclass
class DBConfig:
    host: str
    user: str
    password: str
    database: str


def load_config() -> DBConfig:
    return DBConfig(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "ironbase"),
    )
