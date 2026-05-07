#!/usr/bin/env python3
import tkinter as tk
from gui.windows import UploadWindow, SearchWindow
from services.uploader import UploadService
from db.repository import GeneRepository


class App(tk.Tk):
    def __init__(
        self,
        upload_service: UploadService,
        repository: GeneRepository
    ):
        super().__init__()

        self.upload_service = upload_service
        self.repository = repository

        self.title("Wolf Database Manager")
        self.geometry("400x250")

        self._build_ui()

    def _build_ui(self):
        tk.Button(
            self,
            text="Upload Excel",
            command=self.open_upload
        ).pack(pady=20)

        tk.Button(
            self,
            text="Search Gene",
            command=self.open_search
        ).pack(pady=20)

    def open_upload(self):
        UploadWindow(self, self.upload_service)

    def open_search(self):
        SearchWindow(self, self.repository)
