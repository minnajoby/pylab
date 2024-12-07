my_dic={'name1':'afna','name2':'ashik', 'name3':'kenza','name4':'hazin'}
sort_asc=dict(sorted(my_dic.items()))
print("sorting by keys in ascending order",sort_asc)
sort_dec=dict(sorted(my_dic.items(),reverse=True))
print("sorting by key in descending order",sort_dec)

