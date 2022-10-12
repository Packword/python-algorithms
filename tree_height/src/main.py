from src import input, height_tree, create_tree

if __name__ == '__main__':
    data = input.input_data()
    our_tree = create_tree.create_tree(data)
    print(height_tree.height_tree(our_tree, - 1))
