list_1 = [item for item in input().replace(" ", "").split(",")]
list_2 = [item for item in input().replace(" ", "").split(",")]

print([item for item in list_1 if item in list_2])
