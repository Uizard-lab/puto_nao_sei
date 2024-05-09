#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd 
import requests
import time


# In[8]:


#pip install beautifulsoup4


# In[9]:


from bs4 import BeautifulSoup


# In[12]:


url=('https://www.numbeo.com/cost-of-living/in/Lisbon')
response=requests.get(url)


# In[16]:


soup= BeautifulSoup(response.content, 'html.parser')


# In[54]:


import requests
from bs4 import BeautifulSoup

url = 'https://www.numbeo.com/cost-of-living/in/Lisbon'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all div elements with class "category_title"
    category_divs = soup.find_all('div', class_='category_title')

    # Extract and print the text of each div
    for category_div in category_divs:
        print(category_div.text.strip())
else:
    print("Failed to retrieve the webpage.")


# In[63]:


import requests
from bs4 import BeautifulSoup

url = 'https://www.numbeo.com/cost-of-living/in/Lisbon'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    

    # Find all tr elements
    rows = soup.find_all('tr')

    # Iterate over the rows and extract the content for the specified columns
    for row in rows:
        # Check if the first column contains "Meal, Inexpensive Restaurant"
        first_column = row.find('td')
        if first_column and "Meal, Inexpensive Restaurant" in first_column.text:
            # Extract content for Restaurant column
            restaurant = first_column.text.strip()
            print(f"Restaurant: {restaurant}")

            # Extract content for Edit column
            edit_column = row.find('td', class_='priceValue')
            if edit_column:
                edit_price = edit_column.text.strip()
                print(f"Edit: {edit_price}")

            # Extract con1tent for Range column
            range_column = row.find('td', class_='priceBarTd')
            if range_column:
                range_values = range_column.find_all('span', class_='barTextRight')
                if len(range_values) == 2:
                    range_low = range_values[0].text.strip()
                    range_high = range_values[1].text.strip()
                    print(f"Range: {range_low} - {range_high}")

else:
    print("Failed to retrieve the webpage.")


# In[64]:


import requests
from bs4 import BeautifulSoup

url = 'https://www.numbeo.com/cost-of-living/in/Lisbon'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all div elements with class "category_title"
    category_divs = soup.find_all('div', class_='category_title')

    # Extract and print the text of each div
    for category_div in category_divs:
        print(category_div.text.strip())    

    # Find all tr elements
    rows = soup.find_all('tr')

    # Iterate over the rows and extract the content for each column
    for row in rows:
        # Extract content for Restaurant column
        restaurant_column = row.find('td')
        if restaurant_column:
            restaurant = restaurant_column.text.strip()
            print(f"Restaurant: {restaurant}")

        # Extract content for Edit column
        edit_column = row.find('td', class_='priceValue')
        if edit_column:
            edit_price = edit_column.text.strip()
            print(f"Edit: {edit_price}")

        # Extract content for Range column
        range_column = row.find('td', class_='priceBarTd')
        if range_column:
            range_values = range_column.find_all('span', class_='barTextRight')
            if len(range_values) == 2:
                range_low = range_values[0].text.strip()
                range_high = range_values[1].text.strip()
                print(f"Range: {range_low} - {range_high}")

else:
    print("Failed to retrieve the webpage.")


# In[66]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.numbeo.com/cost-of-living/in/Lisbon'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all tr elements
    rows = soup.find_all('tr')

    # Initialize lists to store data
    data = []

    # Iterate over the rows and extract the content for each column
    for row in rows:
        # Extract content for each column
        columns = [td.text.strip() for td in row.find_all('td')]
        data.append(columns)

    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save DataFrame to a CSV file
    df.to_csv('cost_of_living_data.csv', index=False)

    print("Data saved successfully.")
else:
    print("Failed to retrieve the webpage.")


# In[155]:


# Read the CSV file into a DataFrame
df = pd.read_csv('cost_of_living_data.csv')

# Rename the columns
df.columns = ['Category', 'Price', 'Range']

# Drop rows with NaN values
df = df.dropna()

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


# In[216]:


df.insert(0, 'Type', df.pop('Type'))
df


# # USERS

# In[252]:


class Categories:
    User_Lock = Lock()    
    class Category:
        def __init__(self,food, transportation,rent,others):
            self.food = food
            self.transportation = transportation
            self.rent= rent
            self.others=others
            
        def load_user(self):
            with User.User_Lock:
                with open("../repo/users.json", "r") as file:
                    self.user = json.load(file, object_hook=lambda x: Users.User(**x))

        def store_users(self):
            with User.User_Lock:
                with open("../repo/users.json", "w") as file:
                    json.dump(self.user, file, default=lambda x: x.__dict__, indent=4)
        
        def add_drink(self, drink_name, alcohol_percentage):
            self.drinks_consumed.append((drink_name, alcohol_percentage))

        def getBac(self):
            user1.calculate_bac()
            return self.bac
    def getName(self):
        return self.name 
    
    def getAge(self):
        return self.age
    
    def getEatean(self):
        return self.eatean
    
    def getEmail(self):
        return self.email
    
    def getWeight(self):
        return self.weight   
    
    def getDateOfBirth(self):
        return self.dateOfBirth
    
    def getGender(self):
        return self.gender
    
    def getemergencyContact1(self):
        return self.emergencyContact1
    
    def getemergencyContact2(self):
        return self.emergencyContact2
    
    def getemergencyContact3(self):
        return self.emergencyContact3   
    
    def setName(self,new_name):
        self.name = new_name 
    
    def setAge(self,new_age):
        self.age = new_age
        
    def setEatean(self,new_eatean):
        self.eatean = new_eatean  
        
    def setEmail(self,new_email):
        self.email= new_email 
        
    def setWeight(self,new_weight):
        self.weight= new_weight
            
    def setdateOfBirth(self,new_dateOfBirth):
        self.dateOfBirth= new_dateOfBirth 
        
    def setGender(self,new_gender):
        self.gender= new_gender   
        
    def setEmergencyContact1(self,new_emergencyContact1):
        self.emergencyContact1= new_emergencyContact1     
        
    def setEmergencyContact2(self,new_emergencyContact2):
        self.emergencyContact2= new_emergencyContact2    
        
    def setEmergencyContact3(self,new_emergencyContact3):
        self.emergencyContact3= new_emergencyContact3      
    
   

# Example usage
user1 = User("John", 25, 0,'rita@gmail.com','Avenida',70, "male",2,911,112,123)
user1.add_drink("Corona Extra", "4.6%")
user1.add_drink("Heineken", "5%")
user1.add_drink("Guinness Draught", "4.2%")

bac = user1.calculate_bac()
print(f"{user1.name}'s Blood Alcohol Concentration (BAC): {user1.bac}%")<


# # GET CATEGORY_LIST()

# In[242]:


# Get unique types from the 'Type' column
unique_types = df['Type'].unique()

# Convert to a list
unique_types_list = unique_types.tolist()

# Convert the list to JSON
unique_types_json = json.dumps(unique_types_list)

print(unique_types_json)


# import json
# 
# #Sample JSON string representing unique types
# unique_types_json = '["Restaurant", "Market", "Transportation", "Utilities (Monthly)", "Sports And Leisure", "Childcare", "Clothing And Shoes", "Rent Per Month", "Buy Apartment Price", "Salaries And Financing"]'
# 
# #Parse JSON to list
# unique_types_list = json.loads(unique_types_json)
# 
# #Select categories at indices 0, 2, 3, 4, 5, and 6
# selected_categories1 = [unique_types_list[i] for i in [0, 2, 3, 4, 6 ,7]]
# 
# selected_categories1

# In[277]:


import json

# Sample JSON string representing unique types
unique_types_json = '["Restaurant", "Market", "Transportation", "Utilities (Monthly)", "Sports And Leisure", "Childcare", "Clothing And Shoes", "Rent Per Month", "Buy Apartment Price", "Salaries And Financing"]'

# Parse JSON to list
unique_types_list = json.loads(unique_types_json)

# Select categories at indices 0, 2, 3, 4, 5, and 6
selected_categories = [unique_types_list[i] for i in [0, 2, 3, 4, 6, 7]]

# Convert the average rent from per month to per day (assuming 30 days)
avg_rent_per_month =  avg_rent # Example average rent per month
avg_rent_per_day = avg_rent / 30

# Add the average rent per day to the selected categories
selected_categories.append(avg_rent_per_day)

print(selected_categories)


# Merge selected categories and rename as 'Others'
merged_category = 'Others'
other_categories = ['Utilities (Monthly)', 'Sports And Leisure', 'Clothing And Shoes']

# Check if any of the other categories are present in the selected categories
if any(category in selected_categories for category in other_categories):
    # Remove the individual categories and add the merged category
    selected_categories = [category for category in selected_categories if category not in other_categories]
    selected_categories.append(merged_category)

print(selected_categories)


# # GET PRICE-BY-CATEGORY

# In[ ]:


import json

# Sample JSON string representing unique types
unique_types_json = '["Restaurant", "Market", "Transportation", "Utilities (Monthly)", "Sports And Leisure", "Childcare", "Clothing And Shoes", "Rent Per Month", "Buy Apartment Price", "Salaries And Financing"]'

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

# Function to calculate total expenses for selected categories and number of days
def calculate_total_expenses(selected_categories, num_days):
    total_expenses = {}
    for category in selected_categories:
        if category == 'Restaurant':
            avg1 = df.loc[0, 'Price'].mean()
            avg2 = df.loc[1, 'Price'].mean() / 2
            avg3 = df.loc[2, 'Price'].mean()
            avg_restaurant = (avg1 + avg3) / 2 + avg3
            total_expenses[category] = avg_restaurant * num_days
        elif category == 'Transportation':
            avg_transportation = df[df['Type'] == 'Transportation']['Price'].mean()
            total_expenses[category] = avg_transportation * num_days
        elif category == 'Rent Per Month':
            avg_rent = df[df['Type'] == 'Rent Per Month']['Price'].mean()
            total_expenses[category] = avg_rent * num_days
        elif category in ['Utilities (Monthly)', 'Sports And Leisure', 'Clothing And Shoes']:
            other_categories = ['Utilities (Monthly)', 'Sports And Leisure', 'Clothing And Shoes']
            avg_others = df[df['Type'].str.contains('|'.join(other_categories))]['Price'].mean()
            total_expenses[category] = avg_others * num_days
    return total_expenses


selected_categories = select_categories(unique_types_list)

# Take user input for number of days
num_days = int(input("Enter the number of days you will stay: "))

# Calculate total expenses for selected categories and number of days
total_expenses = calculate_total_expenses(selected_categories, num_days)

# Convert the dictionary to JSON
results_json = json.dumps(total_expenses)

# Remove the surrounding curly braces
results_json = results_json[1:-1]
results_json = results_json.replace('"', '')
results_json = results_json.replace(',', '', 1)  # Remove the first comma

print(results_json)


# In[263]:


import json

# Sample JSON string representing unique types
unique_types_json = '["Restaurant", "Market", "Transportation", "Utilities (Monthly)", "Sports And Leisure", "Childcare", "Clothing And Shoes", "Rent Per Month", "Buy Apartment Price", "Salaries And Financing"]'

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
        avg_expense = df[df['Type'] == category]['Price'].mean()
        avg_expenses_per_category[category] = avg_expense
    return avg_expenses_per_category





# Function to calculate total expenses for selected categories and number of days
def calculate_total_expenses(avg_expenses_per_category, num_days):
    total_expenses = {}
    for category, avg_expense in avg_expenses_per_category.items():
        total_expenses[category] = avg_expense * num_days
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

print(results_json)


# In[254]:


#numero de dias de estadia* categorias q nos interessam


# In[258]:


##SIMULADOR

def calculate_expenses(num_days, avg_expenses_per_category):
    total_expenses = 0
    for category, avg_expense in zip(selected_categories, avg_expenses_per_category):
        total_expenses += num_days * avg_expense
    return total_expenses

# Take user input for the number of days
num_days = int(input("Enter the number of days you will stay: "))

# Take user input for the average expenses per category
avg_expenses_per_category = []
for category in selected_categories:
    category= int(input("Category: "))
    avg_expense = num_days*avg_expenses_per_category.append(avg_expense)
    #avg_expense = float(input(f"Enter the average expense for {avg_restaurant}: "))
    avg_expenses_per_category.append(avg_expense)

# Calculate total expenses
#total_expenses = calculate_expenses(num_days, avg_expenses_per_category)
print("Total expenses:", avg_expense)


# # AVERAGE MERDAS

# In[222]:


# Calculate the average of rows with 'Restaurant' in the 'Type' column
avg1 = df.loc[0, 'Price'].mean()
avg2=(df.loc[1, 'Price'].mean())/2
avg3=df.loc[2, 'Price'].mean()

avg_restaurant = (avg1 + avg3)/2 + avg3
print('Average Restaurant:', avg_restaurant)

# Calculate the average of rows with 'Market' in the 'Type' column
#avg_markets = df[df['Type'] == 'Market']['Price'].mean()
#print('Average Market:', avg_markets)

# Calculate the average of rows with 'Transportation' in the 'Type' column
avg_transportation = df[df['Type'] == 'Transportation']['Price'].mean()
print('Average Transportation:', avg_transportation)

# Calculate the average of rows with 'Rent' in the 'Type' column
avg_rent = df[df['Type'] == 'Rent Per Month']['Price'].mean()
print('Average Rent:', avg_rent)

# Define a list of strings representing the categories to include in 'Others'

other_categories = ['Utilities (Monthly)', 'Sports And Leisure','Clothing And Shoes']

# Filter rows where the 'Type' column contains any of the specified strings
avg_others = df[df['Type'].str.contains('|'.join(other_categories))]['Price'].mean()

print('Average Others:', avg_others)


# #df['Price'] = df['Price'].str.extract(r'(\d+\.\d+)').astype(float)
# #Calculate the average of rows 1, 2, and 3
# avg1 = df.loc[0, 'Price'].mean()
# avg2=(df.loc[1, 'Price'].mean())/2
# avg3=df.loc[2, 'Price'].mean()
# 
# #Calculate the average of rows 4, 5, 6, and 7
# #avg2 = df.loc[3:7, 'Price'].mean()
# 
# #Averages
# avg_restaurant = (avg1 + avg3)/2 + avg3
# #print('Average Restaurant:', avg_restaurant)
# ------
# avg_markets=df.loc[8:26, 'Price'].mean()
# print('Average Market:', avg_markets)
# 
# avg_transportation=df.loc[27:34, 'Price'].mean()
# print('Average Transportation:', avg_transportation)
# 
# avg_rent=df.loc[47:50, 'Price'].mean()
# print('Average Rent:', avg_rent)
# 
# avg_others=df.loc[35:46, 'Price'].mean()
# #print('Average Others:', avg_others)

# In[179]:


import pandas as pd

# Assuming df is your DataFrame
cost_of_living = df.to_excel('CostOfLiving.xlsx', index=False)


# # save merdas

# In[176]:


import pandas as pd
travel = pd.read_csv('/Users/ritaoliveira/Desktop/cost_of_living_data.csv', sep=',', quotechar='"')
travel = travel.dropna()


# #PASSAR PARA JSON
# travel_json = travel.to_json(orient='records')
# 
# #Save JSON to a file
# with open('travel_cost_of_living.json', 'w') as file:
#     file.write(travel_json)

# In[ ]:




