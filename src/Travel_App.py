import pandas as pd
import pandas as pd
df = pd.read_csv('/Users/ritaoliveira/Desktop/cost_of_living_data.csv',sep=',', quotechar='"')
# Drop rows with NaN values
df = df.dropna()
# Rename the columns
df.columns = ['Category', 'Price', 'Range']
# Reset the index after dropping rows
df = df.reset_index(drop=True)
#dfs=df.insert(0, 'Type', df.pop('Type'))
#df['Type'] = 'Restaurant'
# Move the 'Type' column to the first position
# Change the 'Type' column for the first 6 rows to 'Restaurant'
df.loc[:7, 'Type'] = 'Restaurant'
df.loc[8:26, 'Type'] = 'Market'
df.loc[27:34, 'Type'] = 'Transportation'
df.loc[35:37, 'Type'] = 'Utilities (Monthly)'
df.loc[38:40, 'Type']= 'Sports And Leisure'
df.loc[41:42, 'Type']='Childcare'
df.loc[43:46, 'Type']='Clothing And Shoes'
df.loc[47:50, 'Type']='Rent Per Month'
df.loc[51:52, 'Type']='Buy Apartment Price'
df.loc[53:,'Type']='Salaries And Financing'

df.insert(0, 'Type', df.pop('Type'))

import json
# Get unique types from the 'Type' column
unique_types = df['Type'].unique()

# Convert to a list
unique_types_list = unique_types.tolist()

# Convert the list to JSON
unique_types_json = json.dumps(unique_types_list)

print(unique_types_json)
import json

# Sample JSON string representing unique types
unique_types_json ='["Restaurant", "Transportation", "Rent Per Day", "Others"]'
#'["Restaurant", "Market", "Transportation", "Utilities (Monthly)", "Sports And Leisure", "Childcare", "Clothing And Shoes", "Rent Per Month", "Buy Apartment Price", "Salaries And Financing"]'
 
# Parse JSON to list
unique_types_list = json.loads(unique_types_json)
 
# Function to select categories
def select_categories(unique_types_list):
    print("Select categories to include in the expense calculation:")
    for i, category in enumerate(unique_types_list):
        print(f"{i + 1}. {category}")
    selected_indices = input("Enter the indices of the categories separated by commas (e.g., 1,2,3): ")
    selected_indices = [int(index.strip()) - 1 for index in selected_indices.split(",")]
    selected_categories = [unique_types_list[index] for index in selected_indices]
    return selected_categories
 
# Function to calculate average expenses per selected category
 
def calculate_avg_expenses(selected_categories, df):
    avg_expenses_per_category = {}
    for category in selected_categories:
        # Convert 'Price' column to string and then remove non-numeric characters (including commas)
        df['Price'] = df['Price'].astype(str).str.replace('€', '').str.replace(',', '')
        # Convert the cleaned 'Price' column to float
        df['Price'] = df['Price'].astype(float)
        avg_expense = df[df['Type'] == category]['Price'].mean()
        avg_expenses_per_category[category] = avg_expense
    return avg_expenses_per_category
 
 
# Function to calculate total expenses for selected categories and number of days
 
def calculate_total_expenses(selected_categories, num_days):
    total_expenses = {}
    for category in selected_categories:
        if category == 'Restaurant':
            avg1 = df.loc[0, 'Price'].mean()
            avg2 = df.loc[1, 'Price'].mean() / 2
            avg3 = df.loc[2, 'Price'].mean()
            avg_restaurant = (avg1 + avg2) / 2 + avg3
            total_expenses[category] = avg_restaurant * num_days
        elif category == 'Transportation':
            avg_transportation = df[df['Type'] == 'Transportation']['Price'].mean()
            total_expenses[category] = avg_transportation * num_days
        elif category == 'Rent Per Day':
            avg_rent = df[df['Type'] == 'Rent Per Month']['Price'].mean()
<<<<<<< Updated upstream
            avg_rent_per_day = avg_rent / 30
            # Add the average rent per day to the selected categories
            selected_categories.append(avg_rent_per_day)

            total_expenses[category] = avg_rent * num_days
        elif category in ['Utilities (Monthly)', 'Sports And Leisure', 'Clothing And Shoes']:
            other_categories = ['Utilities (Monthly)', 'Sports And Leisure', 'Clothing And Shoes']
            avg_others = df[df['Type'].str.contains('|'.join(other_categories))]['Price'].mean()
            total_expenses[category] = avg_others * num_days
=======
            # Add the average rent per day to the selected categories                       
            total_expenses[category] = (avg_rent / 30) * num_days
        elif category == 'Others':
            avg_utility=df[df['Type'] == 'Utilities (Monthly)']['Price'].mean()
            avg_sports= df[df['Type'] == 'Sports And Leisure']['Price'].mean()
            avg_clothing=df[df['Type'] == 'Clothing And Shoes']['Price'].mean()
            avg_others = avg_utility + avg_sports + avg_clothing           
            # Handle the 'Others' category here
            # For example, calculate the mean of all categories not explicitly handled
            #other_categories = ['Utilities (Monthly)', 'Sports And Leisure', 'Clothing And Shoes']
            #avg_other = df[~df['Type'].isin(other_categories)]['Price'].mean()
            total_expenses[category] = avg_others * num_days    
>>>>>>> Stashed changes
    return total_expenses
 
 
# Take user input for category selection
selected_categories = select_categories(unique_types_list)
 
# Take user input for number of days
num_days = int(input("Enter the number of days you will stay: "))
 
# Calculate average expenses per selected category
avg_expenses_per_category = calculate_avg_expenses(selected_categories, df)
 
# Calculate total expenses for selected categories and number of days
total_expenses = calculate_total_expenses(avg_expenses_per_category, num_days)
 
# Convert the dictionary to JSON
results_json = json.dumps(total_expenses)
# Convert the dictionary to JSON
results_json = json.dumps(total_expenses)
 
# Remove the surrounding curly braces
results_json = results_json[1:-1]
results_json = results_json.replace('"', '')
results_json = results_json.replace(',', '', 1)  # Remove the first comma
 
print(results_json)