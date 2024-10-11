# tools/pg_query.py

from typing import Type
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel, Field
from crewai_tools import BaseTool  # Adjust the import path as necessary
import json


class SQLExecutionToolInput(BaseModel):
    sql_query: str = Field(..., description="The SQL query to execute.")


class SQLExecutionTool(BaseTool):
    name: str = "Execute SQL Query"
    description: str = (
        "Executes SQL queries against a PostgreSQL database and returns the results."
    )
    args_schema: Type[BaseModel] = SQLExecutionToolInput

    db_uri: str = Field(
        ...,
        description="The database URI in the format postgresql://user:password@host:port/dbname",
    )

    def _run(self, sql_query: str) -> str:
        """Executes a SQL query and returns the results as a JSON string."""
        try:
            # Connect to the PostgreSQL database
            with psycopg2.connect(self.db_uri) as connection:
                with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                    # Execute the SQL query
                    cursor.execute(sql_query)

                    # If the query returns data, fetch and return it
                    if cursor.description:
                        results = cursor.fetchall()
                        if results:
                            return json.dumps(results, default=str)
                        else:
                            return "No Relevant Data Returned from Query"
                    else:
                        # For queries that don't return data (e.g., INSERT, UPDATE)
                        connection.commit()
                        return json.dumps(
                            [
                                {
                                    "status": "Query executed successfully with no returned data."
                                }
                            ]
                        )
        except Exception as e:
            # Handle exceptions and return the error message
            return json.dumps([{"error": str(e)}])

    async def _arun(self, sql_query: str) -> str:
        """Asynchronous execution is not implemented."""
        raise NotImplementedError("Asynchronous execution is not implemented.")
