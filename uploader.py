#!/usr/bin/env python3
from db.repository import GeneRepository
from services.excel_parser import ExcelParser


class UploadService:
    def __init__(self, repository: GeneRepository):
        self.repository = repository

    def upload_file(self, table_name: str, filepath: str) -> None:
        self.repository.create_table(table_name)

        records = ExcelParser.parse(filepath)

        for overlap, pvalue, fdr in records:
            self.repository.insert_row(
                table_name,
                overlap,
                pvalue,
                fdr
            )
