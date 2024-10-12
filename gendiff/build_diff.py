def build_diff(tree1, tree2):
    diff = {}
    union_keys = set(tree1.keys()).union(tree2.keys())
    for key in union_keys:

        if key in tree1 and key not in tree2:
            diff[key] = ('removed', tree1[key])

        elif key not in tree1 and key in tree2:
            diff[key] = ('added', tree2[key])

        elif tree1[key] == tree2[key]:
            diff[key] = ('unchanged', tree1[key])

        elif isinstance(tree1[key], dict) and isinstance(tree2[key], dict):
            diff[key] = ('nested', build_diff(tree1[key], tree2[key]))

        else:
            diff[key] = ('changed', tree1[key], tree2[key])

    return diff
