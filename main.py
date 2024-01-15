from csv_diff import load_csv, compare
import json

file1 = "2024-01-09_-_Worker_and_Temporary_Worker.csv"
file2 = "2024-01-10_-_Worker_and_Temporary_Worker.csv"
file3_empty = "empty.csv"

key = "Organisation Name"

diff: dict[str, str] = {};

try:
    file1_dict = load_csv(open(file1), key)
    file2_dict = load_csv(open(file2), key)
    if file1_dict and file2_dict:
            diff = compare(file1_dict, file2_dict)
            # write diff to a json file:
            with open('diff.json', 'w') as f:
                json.dump(diff, f)
            added = diff['added']
            print(added)
    else:
        print("One of the files is empty")
except:
     print("One of the files is empty or not in the correct format")
     exit()

print(" ADDED: ============ ============ ============ ============ ============ ============")
for i in added:
    print(
        f"""{i['Organisation Name']} ||| {i['Type & Rating']} ||| {i['Town/City']} ||| {i['County']} ||| {i['Route']}""")

print(" REMOVED: ============ ============ ============ ============ ============ ============")
removed = diff['removed']
for i in removed:
    print(
        f"""{i['Organisation Name']} ||| {i['Type & Rating']} ||| {i['Town/City']} ||| {i['County']} ||| {i['Route']}""")

print(" CHANGED: ============ ============ ============ ============ ============ ============")
changed = diff['changed']

print(changed)