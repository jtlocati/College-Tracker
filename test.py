data = {
    "var1": "one",
    "var2": "two",
    "var3": "three"
}

new_list = []

for i in range(3):
    i = i + 1
    new_list.append(data[f"var{i}"])

print(new_list)