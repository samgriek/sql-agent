# tasks/pg_tasks.py

from textwrap import dedent
from crewai import Task

class PostgreSQLTasks:
    def create_sql_developer_task(self, user_question, database_description, agent):
        return Task(
            description=dedent(f"""\
                **Objective:** Construct a valid and efficient PostgreSQL SQL query to address the user's question, utilizing the provided database schema.

                **Instructions:**
                - Carefully analyze the user's question and the database description.
                - Formulate an SQL query that accurately retrieves the required data.
                - Ensure the query adheres to best practices and is optimized for performance.
                - If the user's question is not relevant to the database schema, respond with 'No Relevant Tables in DB'.

                **User Question:**
                {user_question}

                **Database Description:**
                {database_description}
                """),
            expected_output=dedent("""\
                **Deliverable:**
                - A fully functional PostgreSQL SQL query ready for execution.
                - The query should be formatted for readability.
                - Include comments if necessary to explain complex parts of the query.
                """),
            agent=agent,
        )

    def create_sql_execution_task(self, user_question, agent):
        return Task(
            description=dedent(f"""\
                **Objective:** Execute the provided SQL query and return the complete results.

                **Instructions:**
                - Use the appropriate tools to execute the SQL query against the database.
                - Provide the full set of results obtained from the query execution.
                - If no data is returned, respond with 'No Relevant Data Returned from Query'.

                **User Question:**
                {user_question}
                """),
            expected_output=dedent("""\
                **Deliverable:**
                - A complete and formatted presentation of the query results.
                - If applicable, include any messages or warnings generated during execution.
                - In case of no data, the exact message 'No Relevant Data Returned from Query'.
                """),
            agent=agent,
        )

    def create_data_analyst_task(self, user_question, agent):
        return Task(
            description=dedent(f"""\
                **Objective:** Analyze the provided dataset to extract meaningful insights related to the user's question.

                **Instructions:**
                - Thoroughly examine the data set provided.
                - Identify and articulate 2 to 3 key insights that answer or relate to the user's question.
                - If no insights can be gleaned, respond with 'No Insights Gleaned from the Data'.

                **User Question:**
                {user_question}

                """),
            expected_output=dedent("""\
                **Deliverable:**
                - A detailed report highlighting 2 to 3 significant insights.
                - Each insight should include:
                  - A clear statement of the finding.
                  - Supporting evidence from the data.
                  - An explanation of its relevance to the user's question.
                - If no insights are found, provide the exact message 'No Insights Gleamed from the Data'.
                """),
            agent=agent,
        )
