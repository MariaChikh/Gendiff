import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    union_keys = set(file1.keys()).union(file2.keys())

    diff = {}
    for key in union_keys:

        if key in file1 and key not in file2:
            diff[key] = f"  - {key}: {file1[key]}"

        elif key not in file1 and key in file2:
            diff[key] = f"  + {key}: {file2[key]}"

        elif file1[key] != file2[key]:
            diff[key] = f"  - {key}: {file1[key]}\n  + {key}: {file2[key]}"

        else:
            diff[key] = f"    {key}: {file1[key]}"

    sorted_diff = dict(sorted(diff.items()))
    result = '{\n' +'\n'.join(sorted_diff.values())+'\n}\n'
    return result.lower()

