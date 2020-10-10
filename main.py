import re
import modules.product as product
import modules.order as order
import modules.report as report
import modules.member as member
try:
    while (1):
        print("********************* Laundry Menu *******************")
        print("[1]. Add Order")
        print("[2]. Product Management")
        print("[3]. Member Management")
        print("[4]. Report")
        print("[x]. Exit")
        menu = input("Please select menu   => ")

        if menu == '1':
            order.list_menu()
        elif menu == '2':
            product.list_menu()
        elif menu == '3':
            member.list_menu()
        elif menu == '4':
            report.list_menu()
        elif menu == 'x':
            break
        else:
            print("Incorrect menu.")
    print("Bye!")
except Exception as e:
    print("Something wrong on main.py")