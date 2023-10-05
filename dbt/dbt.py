from pycarlo.core import Client, Query, Session
from pycarlo.features.dbt.dbt_importer import DbtImporter
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_client():
    """Create a client with your MCD ID and MCD Token. Create an API key at https://getmontecarlo.com/settings/api"""
    mcd_id = os.getenv("MCD_ID")
    mcd_token = os.getenv("MCD_TOKEN")
    return Client(session=Session(mcd_id=mcd_id, mcd_token=mcd_token))

def get_resource_id(client):
    """Get the resource ID of the first warehouse connected to the user's account"""
    query = Query()
    query.get_user().account.warehouses.__fields__("name", "connection_type", "uuid")
    warehouses = client(query).get_user.account.warehouses
    warehouse_list = []
    if len(warehouses) > 0:
        for val in warehouses:
            warehouse_list.append(val.uuid)
    else:
        print("Error: no warehouses connected")
    return warehouse_list

def import_dbt_run(dbt_importer, project_name, job_name, resource_id):
    """Import a dbt run into Monte Carlo. This function assumes that the dbt run results are in the current directory."""
    manifest_path = Path("manifest.json")
    run_results_path = Path("run_results.json")
    logs_path = Path("logs.txt")
    project_name = "my_dbt_project" # these are the names of the dbt project and job that you want to import
    job_name = "my_dbt_job" # these are the names of the dbt project and job that you want to import

    dbt_importer.import_run(
        manifest_path=manifest_path,
        run_results_path=run_results_path,
        logs_path=logs_path,
        project_name=project_name,
        job_name=job_name,
        resource_id=resource_id,
    )

def main():
    """Main function that runs the dbt import"""
    print("Starting dbt import...")
    client = create_client()
    resource_id = get_resource_id(client)[0] # get the first warehouse. This may be different for your account
    dbt_importer = DbtImporter(mc_client=client)
    import_dbt_run(dbt_importer, "my_dbt_project", "my_dbt_job", resource_id) 

if __name__ == "__main__":
    main()
