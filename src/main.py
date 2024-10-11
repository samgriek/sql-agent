# main.py

from dotenv import load_dotenv

load_dotenv()

from pathlib import Path
import sys

from crewai import Crew, Process
from agents.pg_agents import (
    PostgreSqlAgents as pg_agents,
)  # Assuming you have this in agents/pg_agents.py
from tasks.pg_tasks import (
    PostgreSQLTasks as pg_tasks,
)  # Assuming you have this in tasks/pg_tasks.py


def main():
    print("## Welcome to the SQL Query and Analysis Crew")
    print("----------------------------------------------")

    # Get the user question
    if len(sys.argv) > 1:
        user_question = " ".join(sys.argv[1:])
    else:
        user_question = input("Please enter your question:\n")

    # Read the database description from database.md
    database_description_path = Path("database.md")
    if not database_description_path.is_file():
        print("Error: 'database.md' file not found.")
        return

    with open(database_description_path, "r") as file:
        database_description = file.read()

    # Initialize agents
    agents = pg_agents()
    manager_agent = agents.manager_agent()
    sql_developer_agent = agents.sql_developer_agent()
    sql_execution_agent = agents.sql_execution_agent()
    data_analyst_agent = agents.data_analyst()

    # Create Tasks
    tasks = pg_tasks()
    sql_developer_task = tasks.create_sql_developer_task(
        user_question,
        database_description,
        sql_developer_agent,
    )
    sql_execution_task = tasks.create_sql_execution_task(
        user_question,
        sql_execution_agent,
    )
    data_analyst_task = tasks.create_data_analyst_task(
        user_question,
        data_analyst_agent,
    )

    # Set context relationships between tasks
    sql_execution_task.context = [sql_developer_task]
    data_analyst_task.context = [sql_execution_task]

    # Create Crew
    crew = Crew(
        manager_agent=manager_agent,
        agents=[sql_developer_agent, sql_execution_agent, data_analyst_agent],
        tasks=[sql_developer_task, sql_execution_task, data_analyst_task],
        process=Process.hierarchical,
    )

    # Start the process
    print("\n--- Starting the crew process... ---\n")
    inputs = {
        "user_question": user_question,
        "database_description": database_description,
    }
    result = crew.kickoff(inputs=inputs)

    # Print final insights
    print("\n\n################################################")
    print("## Here are the insights")
    print("################################################\n")
    print(result)


if __name__ == "__main__":
    main()
