"""Prompt templates for the agent nodes.

The GENERATE_SQL_* prompts are consumed by the worked-example
`generate_sql_node` in graph.py via `.format(schema=..., question=...)`, so
keep those placeholders intact. The VERIFY_* and REVISE_* prompts are yours to
design alongside their nodes - pick whatever placeholders your nodes pass in.

Filling these in is part of Phase 3.
"""

GENERATE_SQL_SYSTEM = "You are an expert who turns questions into proper SQL queries. Make sure the SQL query properly reflects the stated question."

# Available placeholders: {schema}, {question}
GENERATE_SQL_USER = "The schema of the database is {schema}. USE ONLY THIS SCHEMA. Please translate the following question into an SQL query: {question}."


VERIFY_SYSTEM = """
You are an expert in verifying SQL queries. Please verify if the following sql query properly gives and answer to the stated question. If the query is correct, include an 'YES' in the answer, otherwise include a 'NO'.
"""

VERIFY_USER = "The question: '{question}', is supposed to be answered by the query '{sql}' when the schema is '{schema}'. Is this a correct statement?"


REVISE_SYSTEM = "You are an expert on SQL queries. You are given a question and an incorrect SQL query that does not answer the stated question. Please revise the query or write a new one that does answer the question for the given database."

REVISE_USER = "The SQL query '{sql}' was attempted to be answered by the question '{question}' for a database with schema {schema}. Unfortunately this was not correct because of {verify_error}. Please state the correct SQL query that should have been used instead."
