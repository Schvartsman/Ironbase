#!/usr/bin/env python3
from typing import List, Tuple
from mysql.connector.connection import MySQLConnection


class GeneRepository:
    def __init__(self, db):
        self.db = db

    def create_table(self, tname: str) -> None:
        query = f"""
        CREATE TABLE IF NOT EXISTS `{table_name}` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            OverlapGenes TEXT,
            Pvalue FLOAT,
            FDR FLOAT,
            SourceMethod VARCHAR(64),
            FinalStatus VARCHAR(32),
            AgeGroup VARCHAR(20)
        )
        """
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

    def insert_row(
        self,
        tname: str,
        overlap: str,
        pvalue: float,
        fdr: float,
        sourcemethod: str,
        finalstatus: str,
        agegoup: str
    ) -> None:
        query = f"""
        INSERT INTO `{table_name}`
        (OverlapGenes, Pvalue, FDR, SourceMethod, FinalStatus, AgeGroup)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (overlapgenes, pvalue, fdr, sourcemethod, finalstatus, agegroup))
            conn.commit()

    def search_by_gene(
        self,
        tname: str,
        gene: str
    ) -> List[Tuple]:
        query = f"""
        SELECT OverlapGenes, Pvalue, FDR, SourceMethod, FinalStatus, AgeGroup
        FROM `{table_name}`
        WHERE OverlapGenes LIKE %s
        """

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (f"%{gene}%",))
            return cursor.fetchall()

    def list_tables(self) -> List[str]:
        query = "SHOW TABLES"

        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return [row[0] for row in cursor.fetchall()]
