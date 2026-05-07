#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, messagebox
from services.uploader import UploadService
from db.repository import GeneRepository


class UploadWindow(tk.Toplevel):
    def __init__(self, master, upload_service: UploadService):
        super().__init__(master)

        self.upload_service = upload_service
        self.title("Upload Excel")
        self.geometry("400x200")

        self._build_ui()

    def _build_ui(self):
        tk.Label(self, text="Table Name:").pack(pady=5)

        self.table_entry = tk.Entry(self)
        self.table_entry.pack(pady=5)

        tk.Button(
            self,
            text="Select Excel File",
            command=self.upload
        ).pack(pady=10)

    def upload(self):
        table_name = self.table_entry.get().strip()

        if not table_name:
            messagebox.showerror("Error", "Table name required")
            return

        filepath = filedialog.askopenfilename(
            filetypes=[("Excel files", "*.xlsx *.xls")]
        )

        if not filepath:
            return

        try:
            self.upload_service.upload_file(
                table_name,
                filepath
            )
            messagebox.showinfo("Success", "Upload completed")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))


class SearchWindow(tk.Toplevel):
    def __init__(self, master, repository: GeneRepository):
        super().__init__(master)

        self.repository = repository
        self.title("Search Gene")
        self.geometry("500x300")

        self._build_ui()

    def _build_ui(self):
        tk.Label(self, text="Table Name:").pack(pady=5)
        self.table_entry = tk.Entry(self)
        self.table_entry.pack(pady=5)

        tk.Label(self, text="Gene:").pack(pady=5)
        self.gene_entry = tk.Entry(self)
        self.gene_entry.pack(pady=5)

        tk.Button(
            self,
            text="Search",
            command=self.search
        ).pack(pady=10)

        self.result_box = tk.Text(self, height=8)
        self.result_box.pack(pady=10)

    def search(self):
        table_name = self.table_entry.get().strip()
        gene = self.gene_entry.get().strip()

        if not table_name or not gene:
            messagebox.showerror("Error", "All fields required")
            return

        try:
            results = self.repository.search_by_gene(
                table_name,
                gene
            )

            self.result_box.delete("1.0", tk.END)

            for row in results:
                self.result_box.insert(
                    tk.END,
                    f"{row}\n"
                )

        except Exception as e:
            messagebox.showerror("Error", str(e))
