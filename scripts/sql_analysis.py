import pandas as pd
from sqlalchemy import create_engine

# Connect database
engine = create_engine('sqlite:///jobs.db')

# SQL query
query = '''
SELECT Job_City,
COUNT(*) AS total_jobs
FROM jobs
GROUP BY Job_City
ORDER BY total_jobs DESC
'''

# Read SQL query result
result = pd.read_sql(query, engine)

print(result)