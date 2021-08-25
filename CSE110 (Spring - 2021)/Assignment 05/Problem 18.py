# tup_list = [(20, 80), (31, 80), (1, 22), (88, 11), (27, 11)]
tup_list = [(20, "Sad"), (31, "Sad"), (88, "NotSad"), (27, "NotSad")]
ref_list = []

a_dict = {}

for a_tuple in tup_list:
    if a_tuple[1] not in ref_list:
        ref_list.append(a_tuple[1])

for item in ref_list:
    holder = []
    for a_tuple in tup_list:
        if item == a_tuple[1]:
            holder.append(a_tuple)

    a_dict[item] = holder
print(a_dict)
