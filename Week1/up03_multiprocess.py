from time import sleep, ctime, time
import multiprocessing

def update_cup_number(customer_name):
    print(f"Start making coffee for {customer_name} at {ctime()}")
    sleep(3)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"Finished making coffee for {customer_name} at {ctime()}")

def make_coffee(customer_name):
    update_cup_number(customer_name)

def main():
    customers = ["Alice", "Bob", "Charlie"]
    processes = []
    for customer in customers:
        process = multiprocessing.Process(target=make_coffee, args=(customer,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()