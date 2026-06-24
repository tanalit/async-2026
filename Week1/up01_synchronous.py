from time import sleep, ctime, time

def update_cup_number(customer_name):
    print(f"Start making coffee for {customer_name} at {ctime()}")
    sleep(3)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"Finished making coffee for {customer_name} at {ctime()}")

def make_coffee(customer_name):
    update_cup_number(customer_name)

def main():
    customers = ["Alice", "Bob", "Charlie"]
    for customer in customers:
        make_coffee(customer)

if __name__ == "__main__":
    main()