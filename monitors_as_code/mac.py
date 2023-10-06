import pandas as pd
import yaml
from template import template

data = pd.read_csv("fields.csv")

def populate_template(row):
    filled_template = template.copy()
    filled_template["variables"]["field"][0] = row["Column"]
    filled_template["variables"]["table"][0] = f"{row['Database']}.{row['Table']}"
    return filled_template

for index, row in data.iterrows():
    filled_template = populate_template(row)
    yaml_structure = {"montecarlo": {"custom_sql": [filled_template]}}

    if pd.notnull(row['Namespace']):
        yaml_structure["namespace"] = row['Namespace']

    # Use the database, table, and column names in the filename
    filename = f"monitor_{row['Database']}_{row['Table']}_{row['Column']}.yaml"
    with open(filename, "w") as file:
        yaml.dump(yaml_structure, file)
