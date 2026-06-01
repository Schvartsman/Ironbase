#!/usr/bin/env python3
from pathlib import Path

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

    def detect_final_status(self,filepath:str)->str:
        parent_folder=Path(filepath).parent.name
        if parent_folder.endswith("Final"):
            return "Final"
        return "Not final"

    def upload_file(self, table_name: str, filepath: str) -> None:
        self.repository.create_table(table_name)

        source_method = self.detect_method(filepath)
        final_status = self.detect_final_status(filepath)

        records = ExcelParser.parse(filepath)

        for overlap, pvalue, fdr in records:
            self.repository.insert_row(
                tname,
                overlap,
                pvalue,
                fdr,
                sourcemethod,
                finalstatus,
                agegroup
            )
