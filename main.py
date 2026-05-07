#!/usr/bin/env python3
from config import load_config
from logger import setup_logger
from db.connection import Database
from db.repository import GeneRepository
from services.uploader import UploadService
from gui.app import App


def main():
    setup_logger()
    config = load_config()

    db = Database(config)
    repository = GeneRepository(db)
    upload_service = UploadService(repository)

    app = App(upload_service, repository)
    app.mainloop()


if __name__ == "__main__":
    main()
