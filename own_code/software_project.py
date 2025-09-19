# global requisition ID counter
requisition_counter = 10000


# class called RequisitionSystem
class RequisitionSystem:
    all_requisitions = []

    # track for Statistics
    total_submitted = 0
    total_approved = 0
    total_pending = 0
    total_not_approved = 0

    # shared data from part A
    def __init__(self, date, staff_id, staff_name):
        global requisition_counter
        requisition_counter += 1
        self.requisition_id = requisition_counter
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.status = "Pending"
        self.items = []
        self.total = 0.0
        self.approval_reference = "Not available"

        RequisitionSystem.all_requisitions.append(self)
        RequisitionSystem.total_submitted += 1
        RequisitionSystem.total_pending += 1

    # method allow the staff to submit basic information.
    def staff_info(self):
        self.date = input("Enter date (DD/MM/YYYY): ")
        self.staff_id = input("Enter staff ID: ")
        self.staff_name = input("Enter staff name: ")

    # method accept a staff list of requisition items with the cost of each and then return the total
    def requisitions_details(self):
        req_item = int(input("Enter number of requisition items: "))
        for i in range(req_item):
            name = input(f"Enter item name {i + 1}: ")
            price = float(input(f"Enter item price {i + 1}: "))
            self.items.append((name, price))
        self.total = sum(price for _, price in self.items)

    def add_items(self, item_list):
        self.items = item_list
        self.total = sum(price for _, price in item_list)

    # method should decide if a requisition is approved or not based on the requisition total
    def requisition_approval(self):
        if self.total <= 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
            RequisitionSystem.total_approved += 1
            RequisitionSystem.total_pending -= 1

    # function manager can respond to a pending requisition by marking it as Approved or Not approved
    def respond_requisition(self, manager_decision):
        if self.status == "Pending":
            RequisitionSystem.total_pending -= 1
            if manager_decision.lower() == "approved":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
                RequisitionSystem.total_approved += 1
            elif manager_decision.lower() == "not approved":
                self.status = "Not approved"
                self.approval_reference = "Not available"
                RequisitionSystem.total_not_approved += 1

    # to print information for all the requisition objects
    def display_requisition(self):
        print(f"\nDate: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.total:.0f}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference}")

    # method to contain information on requisition statistics
    @classmethod
    def display_all_requisitions(cls):
        print("\nPrinting Requisitions:")
        for req in cls.all_requisitions:
            req.display_requisition()

    # return the statistical information
    @classmethod
    def requisition_statistics(cls):
        print("\nDisplaying the Requisition Statistics")
        print(f"The total number of requisitions submitted: {cls.total_submitted}")
        print(f"The total number of approved requisitions: {cls.total_approved}")
        print(f"The total number of pending requisitions: {cls.total_pending}")
        print(f"The total number of not approved requisitions: {cls.total_not_approved}")