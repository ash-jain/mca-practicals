# Name - Aakash Jain.
# Roll No. - 222010019.
# Subject - Data Mining.
# Assignment - I.

import numpy as np
import pandas as pd

# Write a Python program to do the following operations:
# Library: NumPy/pandas.

# a) Create multi-dimensional array and find its shape and dimension.
mul_dim_array = np.array([
    [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
    ],
    [
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]
])
print("Multi-dimensional Array: \n", mul_dim_array, end='\n\n')

# Shape of the array.
print("Array shape: ", mul_dim_array.shape, end='\n\n')

# Dimensions of the array.
print("Array dimensions: ", mul_dim_array.ndim, end='\n\n')


# b) Create a matrix full of zeros and ones
zero_array = np.zeros((2, 5))
print("Matrix full of Zeroes: \n", zero_array, end='\n\n')

ones_array = np.ones((2, 5))
print("Matrix full of Ones: \n", ones_array, end='\n\n')

# c) Reshape and flatten data in the array
reshaped_array = mul_dim_array.reshape(2, 5, 2)
print("Reshaped array: \n", reshaped_array, end='\n\n')

flattened_array = mul_dim_array.flatten()
print('Flattened array: \n', flattened_array, end='\n\n')


# d) Append data vertically and horizontally
print("Arrays to be appeneded: ")

array_1 = np.array([np.arange(1, 5), np.arange(11, 15)])
array_2 = np.array([np.arange(6, 10), np.arange(16, 20)])

print(array_1, end='\n\n')
print(array_2, end='\n\n')

print("Horizontal append: \n", np.append(array_1, array_2, axis=0), end='\n\n')
print("Vertical append: \n", np.append(array_1, array_2, axis=1), end='\n\n')


# e) Apply indexing and slicing on array
print("Accessing first element of the first column of the first row of first array: ",
      mul_dim_array[0][0][0], end='\n\n')
print("Slicing the first column: \n",  mul_dim_array[:, :, 0], end='\n\n')


# f) Use statistical functions on array - Min, Max, Mean, Median and Standard Deviation
print("Mean of the array: ", flattened_array.mean(), end='\n\n')
print("Median of the array: ", np.median(flattened_array), end='\n\n')
print("Max of the array: ", flattened_array.max(), end='\n\n')
print("Min of the array: ", flattened_array.min(), end='\n\n')
print("Standard deviation of the array: ", flattened_array.std(), end='\n\n')


# For the given data answer the following question:
print("Loading CSV file...")
df = pd.read_csv('hardwareStore.csv')
print("Done. ✅\n")


# 1) Give metadata of the given data?
print("Metadata:")
metadata = df.head()
for column_name in metadata:
    print(column_name.title().replace('_', ' '))
print()


# 2) calculate descriptive statistics of the data. (i.e calculate  Min, Max, Mean, Median and Standard Deviation)
print('Descriptive statistics of the data:')
print(df.describe().drop(labels=['25%', '50%', '75%']).drop(
    labels=['CATEGORY_ID', 'PRODUCT_ID'], axis=1))
print()


# 3) What are unique product id and their product description.
# 4) For the query 3 count the number of entries for each product id and product desc?
unique_ids = sorted(df['PRODUCT_ID'].unique())
counts = df['PRODUCT_ID'].value_counts()
print("Unique product ids, number of instances of ids and their descriptions: ")
for id_ in unique_ids:
    print(id_, counts[id_], df.loc[df['PRODUCT_ID'] == id_]
          [0:1]['DESCRIPTION1'].iloc[0])
print()


# 5) Fetch all the product available at a specific warehouse(i.e say 8).
print("Products available at New Jersey warehouse: \n")
print(df.loc[df['WAREHOUSE_NAME'] == 'New Jersey', ['CATEGORY_ID', 'CATEGORY_NAME', 'PRODUCT_ID', 'PRODUCT_NAME',
      'DESCRIPTION1', 'DESCRIPTION2', 'DESCRIPTION3', 'DESCRIPTION4', 'STANDARD_COST', 'LIST_PRICE', 'QUANTITY']])
print()

# 6) list the details of all the warehouse in a given region?
print("Warehouses available in region 3: ")
print(df.loc[df['REGION_ID'] == 3, ["WAREHOUSE_ID", "WAREHOUSE_NAME",
      "ADDRESS", "POSTAL", "CITY", "STATE", 'COUNTRY']])
print()


# 7) list the various country that fall in a particular region.
print("Countries in 3rd region: ")
print(df.loc[df['REGION_ID'] == 3]['COUNTRY'].unique())
print()


# 8) Find the item wise total cost for all products in a warehouse.
print("Total cost of products at warehouse in Mumbai: ")
warehouse_data = df.loc[df['WAREHOUSE_NAME'] == 'Bombay']
print(sum(warehouse_data['STANDARD_COST'] * warehouse_data['QUANTITY']))
print()


# 9) create a small dataset for region 2 with only 3 warehouses.
print('Small dataset for region 2')
mini_df = df.loc[(df['REGION_ID'] == 2) & ((df['WAREHOUSE_ID'] == 1) | (
    df['WAREHOUSE_ID'] == 2) | (df['WAREHOUSE_ID'] == 3))]
print(mini_df, end='\n\n')

# 10) create a subset of query 9 only with category = 1 and 5.
print('Subset of small dataset')
micro_df = mini_df.loc[(mini_df['CATEGORY_ID'] == 1) |
                       (mini_df['CATEGORY_ID'] == 5)]
print(micro_df)
print()
