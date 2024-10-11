# agents/pg_agents.py

from tools.pg_query import SQLExecutionTool
from textwrap import dedent
from crewai import Agent
from llms import get_chat_llm


class PostgreSqlAgents:
    def sql_developer_agent(self):
        return Agent(
            role="PostgreSQL Query Developer",
            goal="Construct a valid and optimized SQL query that accurately answers the user's question based on the provided database description.",
            tools=[],
            backstory=dedent("""\
                You are a seasoned PostgreSQL expert with extensive experience in designing and querying complex databases. Your deep understanding of SQL and database schemas allows you to translate user questions into efficient and accurate SQL queries. You pride yourself on writing clean, optimized code and are meticulous in ensuring that your queries are both syntactically correct and performant. Your attention to detail and commitment to best practices make you an invaluable resource in database query development.
                """),
            prompt=dedent("""\
                **Objective:** Formulate the most accurate and efficient SQL query to address the user's question.

                **Instructions:**
                - Review the user's question and the database description carefully.
                - Construct a valid PostgreSQL SQL query that retrieves the required data.
                - Ensure the query is optimized for performance and adheres to best practices.
                - If the user's question is not relevant to the database, reply with 'No Relevant Tables in DB'.

                **User Question:**
                {user_question}

                **Database Description:**
                {database_description}
                """),
            verbose=True,
            llm=get_chat_llm(
                model="gpt-4o-mini",
                json_mode=False,
                max_tokens=5000,
            ),
            function_calling_llm=get_chat_llm(
                model="gpt-4o-mini",
                max_tokens=5000,
                json_mode=False,
            ),
            max_iter=20,
            allow_delegation=False,
            cache=True,
            memory=True,
        )

    def sql_execution_agent(self):
        return Agent(
            role="PostgreSQL Query Executor",
            goal="Execute the provided SQL Query and provide the complete results even if there are none",
            tools=[self.sql_execution_tool()],
            backstory=dedent("""\
                You are a meticulous database administrator with expertise in executing SQL queries. Your precision ensures accurate and complete results, including handling cases where queries return no data.
                """),
            prompt=dedent("""\
                **Objective:** Execute the SQL query and return all results obtained.

                **Instructions:**
                - Use your tools to execute the provided SQL query.
                - Provide a complete and formatted presentation of the results.
                - Include any relevant messages or warnings from the execution process.
                - If no data is returned, respond with 'No Relevant Data Returned from Query'.

                """),
            verbose=True,
            llm=get_chat_llm(
                model="gpt-4o-mini",
                json_mode=False,
                max_tokens=5000,
            ),
            function_calling_llm=get_chat_llm(
                model="gpt-4o-mini",
                max_tokens=5000,
                json_mode=False,
            ),
            max_iter=20,
            allow_delegation=True,
            cache=True,
            memory=True,
        )

    def sql_execution_tool(self):
        return SQLExecutionTool(
            db_uri="postgresql://postgres:password@localhost:54321/dvdrental"
        )

    def data_analyst(self):
        return Agent(
            role="Data Analyst",
            goal="Analyze the data to extract and present 2 to 3 meaningful insights relevant to the user's question.",
            tools=[],
            backstory=dedent("""\
                You are an experienced data analyst with a keen eye for detail and a passion for uncovering actionable insights from complex datasets. With a strong background in statistical analysis and data visualization, you excel at interpreting data to tell a compelling story. You are adept at identifying trends, patterns, and anomalies that can provide valuable information to stakeholders. Your analytical skills and ability to communicate findings clearly make you an essential asset in decision-making processes.
                """),
            prompt=dedent("""\
                **Objective:** Analyze the data to uncover key insights related to the user's question.

                **Instructions:**
                - Examine the provided data thoroughly.
                - Identify and articulate 2 to 3 significant insights that answer or relate to the user's question.
                - Support each insight with evidence from the data.
                - If no insights can be gleaned, respond with 'No Insights Gleamed from the Data'.

                **User Question:**
                {user_question}
                """),
            verbose=True,
            llm=get_chat_llm(
                model="gpt-4o-mini",
                json_mode=False,
                max_tokens=5000,
            ),
            function_calling_llm=get_chat_llm(
                model="gpt-4o-mini",
                max_tokens=5000,
                json_mode=False,
            ),
            max_iter=20,
            allow_delegation=False,
            cache=True,
            memory=True,
        )

    def manager_agent(self):
        return Agent(
            role="SQL Query and Analysis Crew Manager",
            goal="Effectively manage the SQL Query and Analysis Crew to answer the user's question comprehensively.",
            backstory=dedent("""\
                You are a highly skilled project manager with expertise in coordinating technical teams in the field of data analysis and database management. Your role is to oversee the SQL Developer, SQL Executor, and Data Analyst agents to ensure they collaborate efficiently to answer complex user questions. You are responsible for assigning tasks, ensuring clear communication, and integrating the outputs from each team member to deliver a coherent and insightful final result to the user.
                """),
            prompt=dedent("""\
                **Objective:** Manage your team to provide a complete and accurate answer to the user's question.

                **Instructions:**
                - Review the user's question and understand the requirements.
                - Coordinate with your team members (SQL Developer, SQL Executor, Data Analyst) to ensure each task is assigned and executed properly.
                - Monitor the progress of each agent, providing guidance and support as needed.
                - Integrate the outputs from all agents to form a cohesive and comprehensive response.
                - Ensure that any issues or obstacles are addressed promptly.

                **User Question:**
                {user_question}

                **Team Members:**
                - SQL Developer Agent
                - SQL Execution Agent
                - Data Analyst Agent

                **Resources:**
                - Database Description: {database_description}

                **Notes:**
                - Maintain clear communication with your team.
                - Focus on delivering high-quality results to the user.
                - Handle any exceptions or errors gracefully, providing alternative solutions if necessary.
                """),
            llm=get_chat_llm(
                model="gpt-4o",
                json_mode=False,
                max_tokens=4000,
            ),
            verbose=True,
            max_iter=20,
            allow_delegation=True,
            cache=True,
            memory=True,
        )
