"""
['Zain', 'Javed']
{
"key1": "value",
"key2": "value2",
"name": "Zain",
"fname": Javed
}
"""

st1_dict = {"name": "Zain","fname": "Javed"}
st2_dict = {"fname": "Sultan", "name": "Zainab"}
st3_dict = {"fname": "Sultan", "name": "Zainab", "class": 8}

# dictn.keys(), dictn.values(), dictn.items() -> iterable in key values
# print(st3_dict['name'])
# for i in st3_dict:
#     print(st3_dict[i])
#     print(st1_dict[i])
#     print(st2_dict[i])


# for key,value in st3_dict.items():
#     print(key, value)
print(st3_dict.get('name'))
print(st3_dict.get('fname'))
print(st3_dict.get('class'))














