import pandas as pd

my_data={
    'name':['ali','veli','ayse'],
    'age':[25,30,22],
    'city':['istanbul','ankara','izmir']
}

df=pd.DataFrame(my_data)#load data into a DataFrame object
print(f"pandas DataFrame:\n{df}")

my_series=pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
print(f"pandas Series:\n{my_series}")

print(f"First name in the DataFrame: {my_data['name'][0]}")



print(f"First element in the Series: {my_series[0]}")
print(f"Element 'a' in the Series: {my_series['a']}")


nums = [1, 2, 3]
nums_tuple = tuple(nums)
nums[0] = 10
nums_tuple1 = tuple(nums)
print(nums_tuple1)


def show_data(data):
    for item in data.split('\n'):
        print(f"{item[0]} - {item[1:]}")
        
info = "3 Clara\n4 David"
show_data(info)


def shout(word):
    return word.upper()

result = shout("hello")
print(result)
