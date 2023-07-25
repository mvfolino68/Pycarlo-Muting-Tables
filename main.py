from pycarlo.core import Client, Mutation, Query, Session
import datetime
import argparse
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


# Create a client with your MCD ID and MCD Token. Create an API key at https://getmontecarlo.com/settings/api
mcdId = os.getenv('MCD_ID')
mcdToken = os.getenv('MCD_TOKEN')
client = Client(session=Session(mcd_id=mcdId, mcd_token=mcdToken))
warehouse_id = "f16b0826-4049-42f1-a883-16e7d3c62590"  # Data warehouse ID

# Calculate the last week number, last month number and year in UTC
now = datetime.datetime.utcnow()
year = now.isocalendar()[0]
week_number = now.isocalendar()[1] - 1
last_month = now.month - 1

# Mute last week's tables
def mute_last_week(year, week_number):
    rule_regex = f"(.*:.*..*weekly_{year}_{week_number})"  # Regular expression for last week
    action = True  # true to mute / false to unmute

    my_input = {"dw_id": warehouse_id, "rule_regex": rule_regex, "mute": action}

    # Apply the mutation and print the result
    mutation = Mutation()
    mutation.toggle_mute_with_regex(input=my_input).__fields__("client_mutation_id")
    print(client(mutation))

# Mute last month's tables
def mute_last_month(year, last_month):
    rule_regex = f"(.*:.*..*{year}_{last_month})"  # Regular expression for last month
    action = True  # true to mute / false to unmute

    my_input = {"dw_id": warehouse_id, "rule_regex": rule_regex, "mute": action}

    # Apply the mutation and print the result
    mutation = Mutation()
    mutation.toggle_mute_with_regex(input=my_input).__fields__("client_mutation_id")
    print(client(mutation))



# Print variables
print(f"Year: {year}")
print(f"Week number: {week_number}")
print(f"Last month: {last_month}")
print(now.isocalendar())

if __name__ == "__main__":
    # allow user to select a function to run
    parser = argparse.ArgumentParser(description='Mute tables.')
    parser.add_argument('--last_week', action='store_true', help='Mute last week tables')
    parser.add_argument('--last_month', action='store_true', help='Mute last month tables')

    args = parser.parse_args()

    if args.last_week:
        mute_last_week(year, week_number)
    if args.last_month:
        mute_last_month(year, last_month)
