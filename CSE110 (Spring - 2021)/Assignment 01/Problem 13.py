seconds = int(input("Input: "))

seconds = seconds % (24 * 3600)
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60

print("Output: Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)
