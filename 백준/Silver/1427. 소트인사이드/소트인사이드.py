arr = input()
listed_arr = []
for i in arr:
    listed_arr.append(int(i))
print(str(sorted(listed_arr, reverse=True)).replace(',', '').replace(' ', '').replace('[', '').replace(']', ''))