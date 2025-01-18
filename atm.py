#program for calculating of atm
#atm
try:
    amount = int(input("Enter the total amount: "))

    # Calculate the number of 500 notes
    num_500 = amount // 500
    amount %= 500  # Remaining amount after using 500 notes


    # Calculate the number of 300 notes
    num_300 = amount // 200
    amount %= 200  # Remaining amount after using 200 notes



    # Calculate the number of 100 notes
    num_100 = amount // 100
    amount %= 100  # Remaining amount after using 100 notes



    # Print the results
    print("*" * 50)
    print(f"\t\tNumber of 500 notes: {num_500}")
    print(f"\t\tNumber of 200 notes: {num_300}")
    print(f"\t\tNumber of 100 notes: {num_100}")
    print("*" * 20,"The End", "*"*20)
except:
    print("*" * 50)
    print("don't type symbol, alphabets, alphanumeric, float value")
    print("please enter amount value like this example is given below ")
    print("Ex:- 4500 rs, 800 rs, 4700 rs")
    print("*"*30, "The End", "*"*30)