
###MY CALCULATIONS: 
    #   discount - What is the sum/total value of discounts in each state?  
    #    sales - What is the percentage of sales that goes towards each region?  
#AI USAGE: I will be using AI to set a framework for my test cases 

##The output of my data will take a csv file form. My calculations are structured in terms of catagorical variables that represent the numbers. 
##For example, when calculating the sum of discounts in each state, I will be analyzing the distributions of discounts across each state and its numerical data. 

import csv

def load_csv(myfile):
    with open(myfile, "r") as file:
         lines = file.readlines()
    return lines 
    

data = load_csv("/Users/rosesarner/Desktop/SI201/fall25-project1-rsarner2/SampleSuperstore.csv")
print(f"sample row: {data[6]}")
print(f"numer of rows: {len(data)}")
print(f"list of the variables: {data[0].strip().split(",")}")


import unittest

class MyTests(unittest.TestCase):
    def testOne(self):
        
        sample = [
            {"State": "CA", "Region": "West", "Sales": 100.0, "Discount": 0.20, "Profit": 5.0},
            {"State": "CA", "Region": "West", "Sales": 50.0,  "Discount": 0.00, "Profit": 2.0},
            {"State": "NY", "Region": "East", "Sales": 80.0,  "Discount": 0.10, "Profit": -1.0},
        ]

        # 1) USUAL: discounts by state (matches your diagram use #1)
        self.assertEqual(
            get_totals(sample, "Discount", "State"),
            {"CA": 0.20, "NY": 0.10},
            "Tested get_totals on discounts grouped by State"
        )

        # 2) USUAL: sales by region (matches your diagram use #2)
        self.assertEqual(
            get_totals(sample, "Sales", "Region"),
            {"West": 150.0, "East": 80.0},
            "Tested get_totals on sales grouped by Region"
        )

        # 3) EDGE: empty dataset -> empty dict
        self.assertEqual(
            get_totals([], "Sales", "Region"),
            {},
            "Edge case: empty input list returns empty dict"
        )

        # 4) EDGE: numeric values as strings (common when reading CSV) should still sum
        sample_str_nums = [
            {"State": "CA", "Region": "West", "Sales": "10.5", "Discount": "0.05"},
            {"State": "CA", "Region": "West", "Sales": "4.5",  "Discount": "0.00"},
        ]
        self.assertEqual(
            get_totals(sample_str_nums, "Sales", "Region"),
            {"West": 15.0},
            "Edge case: numeric strings are handled (cast/parse) and summed"
        )

#MyTests().main()

#first code
def load_superstore(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numerical fields to floats if possible
            for key, value in row.items():
                try:
                    row[key] = float(value)
                except ValueError:
                    row[key] = value.strip()
            data.append(row)
    return data


# ---------------------------------------------------------
# Function: get_totals
# Calculates total numerical values grouped by a categorical variable
# ---------------------------------------------------------
def get_totals(data, numerical, categorical):
    totals = {}
    for entry in data:
        cat_value = entry[categorical]
        num_value = entry[numerical]
        if isinstance(num_value, (int, float)):
            totals[cat_value] = totals.get(cat_value, 0) + num_value
        else:
            num_value = float(num_value)
            totals[cat_value] = totals.get(cat_value, 0) + num_value
    return totals


# ---------------------------------------------------------
# Function: get_percentage
# Converts totals into percentages for each category
# ---------------------------------------------------------
def get_percentage(total_dict):
    total_sum = sum(total_dict.values())
    if total_sum == 0:
        return {k: 0 for k in total_dict}
    return {k: round((v / total_sum) * 100, 2) for k, v in total_dict.items()}


# ---------------------------------------------------------
# Function: write_results
# Writes a dictionary’s results to a CSV file
# ---------------------------------------------------------
def write_results(filename, data_dict, header1, header2):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([header1, header2])
        for k, v in data_dict.items():
            writer.writerow([k, v])


# ---------------------------------------------------------
# Function: main
# Loads data, computes totals & percentages, and writes results
# ---------------------------------------------------------
def main():
    data = load_superstore("/Users/rosesarner/Desktop/SI201/fall25-project1-rsarner2/SampleSuperstore.csv")

    # Example 1: Total Discounts by State
    discount_totals = get_totals(data, "Discount", "State")
    discount_percentages = get_percentage(discount_totals)
    write_results("/Users/rosesarner/Desktop/SI201/fall25-project1-rsarner2/discounts_by_state.csv", discount_percentages, "State", "Discount %")

    # Example 2: Total Sales by Region
    sales_totals = get_totals(data, "Sales", "Region")
    sales_percentages = get_percentage(sales_totals)
    write_results("/Users/rosesarner/Desktop/SI201/fall25-project1-rsarner2/sales_by_region.csv", sales_percentages, "Region", "Sales %")

    print("Files created: discounts_by_state.csv and sales_by_region.csv")






