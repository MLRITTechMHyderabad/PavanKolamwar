def merging_dict(dict1, dict2):
    ans = dict1.copy()
    for i in dict2:
        if i not in ans:
            ans[i] = dict2[i]
        else:
            ans[i].append(dict2[i])
    return ans
dict1 = {"name1": ["Alice"], "age1": [25], "city1": ["New York"]}
dict2 = {"name1": "Bob", "age1": 30, "city1": "Los Angeles"}
print(merging_dict(dict1, dict2))