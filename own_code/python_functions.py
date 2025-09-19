'''
task 1: python function staff_info
'''


# inside makes up the staff_info function
def staff_info():
    # input method for user to enter
    date = input("Enter date: ")
    staff_id = input("Enter staff ID: ")
    staff_name = input("Enter staff name: ")
    # unique id being generated
    counter = +1
    requisition_id = 1000 + counter
    # shows output to user
    print("Printing Staff Information: ")
    print(f"Date: {date}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff name: {staff_name}")
    print(f"Requisition ID: {requisition_id}")
    # returning the data to the function
    return {
        "Date": date,
        "Staff ID": staff_id,
        "Staff Name": staff_name,
        "Requisition ID": requisition_id
    }


'''
task 2: python function requisition_total
'''


def requisition_total():
    # calling the staff_info function
    staff_data = staff_info()
    req_item = int(input("Enter requisition items: "))
    item_name = []
    item_price = []
    # using for loop to capture more inputs for list
    for i in range(req_item):
        n = input(f"enter the name of the item:{i + 1} ")
        item_name.append(n)
        p = float(input(f"enter the price:{i + 1} "))
        item_price.append(p)
    for i in range(req_item):
        print(item_name[i], ":", item_price[i])
    # compute total value of requisition items
    total = 0
    for prices in item_price:
        total = prices + total

    print(f"total:{total}")
    return total, staff_data


'''
task3: python function requisition_approval
'''


def requisition_approval():
    # using requisition_total function as input
    total, staff_data = requisition_total()
    default_status = "Pending"
    approval_status = None
    # using if statement for automatic Approved
    if total <= 500:
        status = "Approved"
    else:
        status = "Pending"
    # assigning aproval refrence number and string manipulation applied
    requisition_id = "REQ" + str(1000)
    # arn is approval refrence number and following the rule
    arn = staff_data["Staff ID"] + requisition_id[-3:]
    print(f"Total: {total}")
    print(f"Status: {status}")
    if status == "Approved":
        print(f"Approval Reference Number: {arn}")
    return staff_data["Date"], requisition_id, staff_data["Staff ID"], staff_data["Staff Name"], total, status, arn


'''
task 4: python function display_requisitions
'''


def display_requisitions(date, requisition_id, staff_id, staff_name, total, status, arn):
    # display staff basic information and total requisitions
    print("Printing Requisitions: ")
    print(f"Date: {date}")
    print(f"Requisition ID: {requisition_id}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Total: {total}")
    print(f"Status: {status}")
    print(f"Approval Reference Number: {arn}")