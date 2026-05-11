#!/usr/bin/env python3
from Pathlib import Path

from db.repository import GeneRepository
from services.excel_parser import ExcelParser

class UploadService:
    def __init__(self, repository: GeneRepository):
        self.repository = repository

    def detect_method(self,filepath: str)->str:
        filename = Path(filepath).stem
        if filename.endswith("_RVA-SV"):
            return "RVA"
        if filename.endswith("_GuidedAssembly-SV"):
            return "GuidedAssembly"
        raise ValueError(f"Cannot detect source method from filename: {filename}")

    def upload_file(self, table_name: str, filepath: str) -> None:
        self.repository.create_table(table_name)

        source_method = self.detect_method(filepath)
        records = ExcelParser.parse(filepath)

        for overlap, pvalue, fdr in records:
            self.repository.insert_row(
                table_name,
                overlap,
                pvalue,
                fdr,
                source_method
            )
