def phone_book():
  """
  Thi function creates a phone book dictionary and interacts with the user.
  """

  phone_numbers = {}  # Initialize an empty dictionary to store names and phone numbers

  while True:  # Start an infinite loop that continues until the user enters nothing
    name = input("Enter a name (or press Enter to exit): ")  # Ask the user for a name

    if not name:  # Check if the user entered nothing (pressed Enter)
      break  # If they entered nothing, exit the loop

    if name in phone_numbers:  # Check if the name is already in the dictionary
      print(f"{name}'s phone number is: {phone_numbers[name]}")  # If it's there, print the phone number
    else:
      phone_number = input(f"Enter {name}'s phone number: ")  # If it's not there, ask for the phone number
      phone_numbers[name] = phone_number  # Add the name and phone number to the dictionary

  print("Final phone book:", phone_numbers)  # Print the final dictionary

phone_book() #call the function

#Tips to make it more interesting:

#Add Address or Email:
#    person_info = {} #dictionary for multiple info
#    # ...
#    # inside the else portion of the loop
#    address = input(f"Enter {name}'s address: ")
#    email = input(f"Enter {name}'s email: ")
#    person_info[name] = {"phone": phone_number, "address": address, "email": email}
#    # ...
#    # print the dictionary differently to show all the data.

#Format Phone Numbers:
#    #add a function to format the numbers.
#    #def format_phone_number(number):
#        #remove any non-digit characters
#        #digits = ''.join(filter(str.isdigit, number))
#        #if len(digits) == 10:
#            #return f"({digits[:3]})-{digits[3:6]}-{digits[6:]}"
#        #else:
#            #return "Invalid number"
#    #phone_number = format_phone_number(phone_number)