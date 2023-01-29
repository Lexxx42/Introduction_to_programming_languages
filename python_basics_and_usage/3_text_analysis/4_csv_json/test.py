import json

input_json = [{"name": "beta", "parents": ["alpha", "gamma"]}, {"name": "gamma", "parents": ["alpha"]},
              {"name": "alpha", "parents": []}, {"name": "delta", "parents": ["gamma", "zeta"]},
              {"name": "epsilon", "parents": ["delta"]}, {"name": "zeta", "parents": []}]

file = json.dumps(input_json)
data_read = json.loads(file)
dict_json = {}

for i, item in enumerate(data_read):
    for parent in item["parents"]:
        if parent not in dict_json:
            dict_json[parent] = {item["name"]}
        else:
            dict_json.get(parent).add(item["name"])
sorted_tuples = sorted(dict_json.items(), key=lambda item: item[0])
dict_json = {k: v for k, v in sorted_tuples}

for key, value in dict_json.items():
    dict_json[key] = set(sorted(value))
print(dict_json)  # parents:children
