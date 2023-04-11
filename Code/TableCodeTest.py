import pandas as pd

# create a list of inputs
inputs = ['input1', 'input2', 'input3', 'input4']

# create a pandas dataframe with the inputs as the row index
df = pd.DataFrame(index=inputs)

# add a column to the dataframe called "Power output" with some example values
df['Power output'] = [10, 20, 30, 40]

# print the dataframe
print(df)
