def height_tree(tree, current_root):
    all_results = []
    if current_root not in tree.keys():
        return 0
    for children in tree[current_root]:
        all_results.append(height_tree(tree, children))
    return 1 + max(all_results)
