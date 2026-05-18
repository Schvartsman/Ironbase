#!/usr/bin/env python3
from typing import List, Tuple
from pathlib import Path
import pandas as pd


class ExcelParser:

    @staticmethod
    def parse(filepath: str) -> List[Tuple[str, float, float]]:
        df = pd.read_excel(filepath)

        if df.empty:
            raise ValueError("Excel file is empty")

        required_columns = ["OverlapGenes", "Pvalue", "FDR"]
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing column: {col}")

        records = []

        for _, row in df.iterrows():
            records.append(
                (
                    str(row["OverlapGenes"]),
                    float(row["Pvalue"]),
                    float(row["FDR"]),
                    age_group,
                )
            )

        return records

    @staticmethod
    def detect_age_group(path:str) -> str:
        parts=[p.lower() for p in Path(path).parts]
        if any("pediatric" in p for p in parts):
            return "Pediatric"
        if any("adult" in p for p in parts):
            return "Adult"
        return ""
