from time import sleep, ctime, time
import threading

def update_cup_number(customer_name):
    print(f"Start making coffee for {customer_name} at {ctime()}")
    sleep(3)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"Finished making coffee for {customer_name} at {ctime()}")

def make_coffee(customer_name):
    update_cup_number(customer_name)

def main():
    customers = ["Alice", "Bob", "Charlie"]
    threads = []
    for customer in customers:
        thread = threading.Thread(target=make_coffee, args=(customer,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()