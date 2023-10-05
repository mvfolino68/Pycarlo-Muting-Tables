
# Monte Carlo Monitors as Code Script

This project is a Python script that leverages Monte Carlo's Monitors as Code capabilities. Follow the instructions below to prepare your environment and run the script. The script will create monitors for each field in the `fields.csv` file. You just provide the database, table, and column names in the CSV file.

example `fields.csv`:

   ```csv
   "Database","Table","Column"
   "prod","table_a","field_a"
   "prod","table_a","field_b"
   "prod","table_b","field_a"
   "prod","table_b","field_b"
   ```

## Instructions

1. **Install Requirements**

   Run the following command to install the necessary python packages:

   ```sh
   pip install -r requirements.txt
   ```

2. **Prepare Fields CSV**

   Create a CSV file named `fields.csv` in the `monitors_as_code` directory (where `mac.py` resides). This file should have the headers "Database", "Table", "Column".

3. **Customize Script**

   Make any adjustments to the `mac.py` to match your needs.

4. **Run the Script**

   Execute the script with the following command:

   ```sh
   python3 mac.py
   ```

## Additional Resources

- [Monte Carlo Monitors as Code Documentation](https://docs.getmontecarlo.com/docs/monitors-as-code)
- [Monte Carlo Monitors as Code Overview](https://docs.getmontecarlo.com/docs/monitors-as-code-1)

## Support

Should you encounter any issues or have further questions, feel free to raise an issue in this repository.
