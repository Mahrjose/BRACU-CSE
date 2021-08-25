def list_item_filter(a_list):
    dual_item_list = []
    for item in a_list:
        if item not in dual_item_list:
            dual_item_list.append(item)
        elif item in dual_item_list and dual_item_list.count(item) < 2:
            dual_item_list.append(item)
    removed = len(a_list) - len(dual_item_list)
    print(f"Removed: {removed}")
    return dual_item_list


# Function Call
print(list_item_filter([1, 2, 3, 3, 3, 3, 4, 5, 8, 8]))
print(list_item_filter([10, 10, 15, 15, 20]))
