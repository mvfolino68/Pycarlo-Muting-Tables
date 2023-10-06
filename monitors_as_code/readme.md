
# Monte Carlo Monitors as Code Script

This project is a Python script that leverages Monte Carlo's Monitors as Code capabilities. Follow the instructions below to prepare your environment and run the script. The script will create monitors for each field in the `fields.csv` file. You just provide the `database`, `table`, `column` and `namespace` names in the CSV file.

example `fields.csv`:

   ```csv
   "Database","Table","Column","Namespace"
   "prod","table_a","field_a","prod"
   "prod","table_a","field_b","prod"
   "prod","table_b","field_a","prod"
   "prod","table_b","field_b","prod"
   ```

## Instructions

1. **Install Requirements**

   Run the following command to install the necessary python packages:

   ```sh
   pip install -r requirements.txt
   ```

2. **Prepare Fields CSV**

   Create a CSV file named `fields.csv` in the `monitors_as_code` directory (where `mac.py` resides). This file should have the headers "Database", "Table", "Column", "Namespace" and a row for each field you want to create a monitor for. See the example above.

3. **Customize `mac.py` or `template.py`**

   Make any adjustments to the `mac.py` to match your needs. You can also use the `template.py` file as a starting point and make any adjustments to that file.

4. **Run the Script**

   Execute the script with the following command:

   ```sh
   python3 mac.py
   ```

5. **Review the Output**

   The script will output Monitors as Code YAML files in the `monitors_as_code` directory. You can review these files and make any adjustments as needed.

6. **Use Monte Carlo CLI to Deploy**

   Use the Monte Carlo CLI to deploy the monitors to your environment. See the [Monte Carlo CLI documentation](https://docs.getmontecarlo.com/docs/using-the-cli) for setup instructions.

   ```sh
   montecarlo monitors apply 
   ```

## Additional Resources

- [Monte Carlo Monitors as Code Documentation](https://docs.getmontecarlo.com/docs/monitors-as-code)
- [Monte Carlo Monitors as Code Overview](https://docs.getmontecarlo.com/docs/monitors-as-code-1)

## Support

Should you encounter any issues or have further questions, feel free to raise an issue in this repository.
