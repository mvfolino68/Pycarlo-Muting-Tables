import pandas as pd
import yaml
from template import template

# Load data from the CSV
data = pd.read_csv("fields.csv")

def populate_template(row):
    """Populates the template with values from a row"""
    filled_template = template.copy()
    filled_template["variables"]["field"][0] = row["Column"]
    filled_template["variables"]["table"][0] = f"spark_catalog.{row['Database']}.{row['Table']}"
    return filled_template

# Populate the templates from the CSV data
for index, row in data.iterrows():
    filled_template = populate_template(row)
    yaml_structure = {"montecarlo": {"custom_sql": [filled_template]}}

    # Write the YAML file
    with open(f"monitors_{index}.yaml", "w") as file:
        yaml.dump(yaml_structure, file)
