# SQL Query and Analysis Crew

Welcome to the **SQL Query and Analysis Crew** project! This application leverages the power of AI agents to generate, execute, and analyze SQL queries based on user questions. It integrates with a PostgreSQL database and uses OpenAI's GPT models to process and analyze data.

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
  - [Agents](#agents)
  - [Tool](#tool)
  - [Tasks](#tasks)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Database Setup](#database-setup)
  - [Environment Variables](#environment-variables)
  - [Installation](#installation)
- [Running the Application](#running-the-application)
- [How It Works](#how-it-works)
  - [Workflow](#workflow)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

This project demonstrates how AI agents can collaborate to interpret a user's question, generate an appropriate SQL query, execute it against a PostgreSQL database, and analyze the results to provide meaningful insights. It's an example of using hierarchical agent management and tool integration to automate data analysis tasks.

## Project Overview

### Agents

The application employs four main agents, each with a specific role:

1. **Manager Agent**: Oversees the entire process, coordinating between agents to ensure the user's question is answered comprehensively.

2. **SQL Developer Agent**: Generates a valid and optimized SQL query based on the user's question and the database schema.

3. **SQL Execution Agent**: Executes the SQL query against the PostgreSQL database and retrieves the results.

4. **Data Analyst Agent**: Analyzes the data returned by the SQL execution agent to extract 2 to 3 meaningful insights relevant to the user's question.

### Tool

- **SQLExecutionTool**: A custom tool that connects to a PostgreSQL database, executes SQL queries, and returns the results. It is used by the SQL Execution Agent to interact with the database.

### Tasks

Each agent performs specific tasks:

- **SQL Developer Task**: Generate a SQL query to answer the user's question.

- **SQL Execution Task**: Execute the SQL query and obtain results.

- **Data Analyst Task**: Analyze the data and provide insights.

The Manager Agent coordinates these tasks, ensuring smooth execution and integration of outputs.

## Setup Instructions

### Prerequisites

- **Python 3.8 or higher**
- **Docker and Docker Compose** (for setting up the PostgreSQL database)
- **An OpenAI API key** (to access GPT models)

### Database Setup

The project includes a Docker Compose file to set up a PostgreSQL database. The database schema and data are based on the `dvdrental` sample database.

To set up the database, follow the instructions in the [setup_db.md](setup_db.md) file.

### Environment Variables

Create a `.env` file in the root directory of the project to store environment variables. This file should include your OpenAI API key.

```env
OPENAI_API_KEY=your-openai-api-key-here
```

**Note:** Replace `your-openai-api-key-here` with your actual OpenAI API key. Do not share this key publicly.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/sql-query-analysis-crew.git
   cd sql-query-analysis-crew
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

After setting up the database and environment variables:

1. **Ensure the PostgreSQL database is running:**

   ```bash
   docker-compose up -d
   ```

2. **Run the application:**

   ```bash
   python main.py
   ```

3. **Enter your question when prompted:**

   ```plaintext
   ## Welcome to the SQL Query and Analysis Crew
   ----------------------------------------------
   Please enter your question:
   ```

   For example:

   ```plaintext
   How many customers rented more than 5 movies in July?
   ```

4. **Wait for the agents to process your question.**

5. **View the insights provided:**

   ```plaintext
   ################################################
   ## Here are the insights
   ################################################

   [Agent outputs with insights]
   ```

## How It Works

### Workflow

1. **User Input**: The user enters a question in natural language.

2. **Manager Agent Coordination**:
   - The Manager Agent receives the question and orchestrates the workflow.
   - Assigns the SQL Developer Agent to generate the SQL query.

3. **SQL Developer Agent**:
   - Analyzes the user's question and database schema.
   - Generates an optimized SQL query.

4. **SQL Execution Agent**:
   - Executes the SQL query using the `SQLExecutionTool`.
   - Retrieves the results from the database.

5. **Data Analyst Agent**:
   - Analyzes the data returned.
   - Extracts 2 to 3 meaningful insights related to the user's question.

6. **Manager Agent**:
   - Integrates the outputs from all agents.
   - Presents the final insights to the user.

## Project Structure

```plaintext
├── agents
│   └── pg_agents.py          # Definitions of the agents
├── tasks
│   └── pg_tasks.py           # Definitions of the tasks
├── tools
│   └── pg_query.py           # SQLExecutionTool implementation
├── main.py                   # Entry point of the application
├── requirements.txt          # Python dependencies
├── setup_db.md               # Database setup instructions
├── database.md               # Database schema description
├── docker-compose.yml        # Docker configuration for PostgreSQL
├── .env                      # Environment variables (not tracked by git)
└── README.md                 # This file
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

**Disclaimer**: This project is for educational purposes and demonstrates the use of AI agents in automating data analysis tasks. Ensure you comply with OpenAI's usage policies when using their API.