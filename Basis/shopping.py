# Author:Colin

product_list = [
    ("iphone", 5800),
    ("Mac Pro", 9800),
    ("Bike", 800),
    ("Watch", 10600),
    ("Coffee", 31),
    ("Book", 120),
]

shopping_list = []

salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("choose item you wanna by:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary))
                else:
                    print("insufficient money!\033[41;1m your balance :[%s],sorry...\033[0m" %(salary))
            else:
                print("product is not exist!", user_choice)
        elif user_choice == "q":
            print("-----shopping list-----")
            for p in shopping_list:
                print(p)
            print("Your current balance :", salary)
            exit()
        else:
            print("invalid input")

        # for item in product_list:
            #print(product_list.index(item),item)

        break
else:
    print("invalid salary...")
    exit()