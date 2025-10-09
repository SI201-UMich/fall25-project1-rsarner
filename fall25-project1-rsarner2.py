
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


from unittest.gui import TestCaseGui

class MyTests(TestCaseGui):
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

MyTests().main()



# 1. main()
    1. Runs the program……
2. load_superstore
    1. Read...
3. get_totals - green function 
    1. Use once for discounts and once for profits 
    2. Arguments data /  numerical and categorical 
    3. Create the total profits for the following columns/given category 
        1. Input - data (csv) and column (numerical  and categorical columns)
            1. Discount and state (list of values)
                1. Sales and region 
        2. Output -  
            1. Categorical variable - key 
            2. Numerical variable - value 
                1. (Dictionaries) 



            4. get_percentage (percentage, region)
                1. Input - Total sales per person (from get_totals)
                2. Output - dictionary of the percentage of sales per each region  




#print(data)

