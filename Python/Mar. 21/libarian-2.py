def get_and_sort_last_names():
    last_names = []
    for i in range(5):
        full_name = input("Name: ")
        parts = full_name.split()
        last_name = parts[-1]
        last_names.append(last_name)
    last_names.sort()
    print(last_names)

get_and_sort_last_names()