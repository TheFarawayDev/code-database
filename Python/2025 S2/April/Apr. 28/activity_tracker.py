#Defaults to "my_list.txt" if name is not specified.
def write_list_to_txt(my_list, filename="my_list.txt"):
    try:
        with open(filename, 'w') as file:
            for item in my_list:
                file.write(str(item) + "\n")
        #Once the action of writing is completed successfully is done then it will print the name of file and the fact of completeion.
        print(f"List written to {filename}!")
    #Error Handling
    except Exception as e:
        print(f"Error: {e}")

#Usage of Example Code
activities = ['Running', 'Swimming', 'Cycling', 'Yoga', 'Dancing']
write_list_to_txt(activities, "simple_output.txt")