import asyncio
from time import ctime, time

# ฟังก์ชันแสดงผลสำหรับงานแต่ละอย่าง
async def greet_diners(customer):
    # 1. ช่วง Greeting (เรียงลำดับ)
    print(f"{ctime()} Greeting for {customer} ...")
    await asyncio.sleep(1) # สมมติเวลาตามภาพ
    print(f"{ctime()} Greeting for {customer} ...Done!")

async def customer_private_workflow(customer):
    # 2. ช่วงงานแยก (Tasks)
    print(f"{ctime()} [{customer}] Taking Order ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [{customer}] Taking Order ...Done!")
    
    print(f"{ctime()} [{customer}] Cooking Spaghetti ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [{customer}] Cooking Spaghetti ...Done!")
    
    print(f"{ctime()} [{customer}] Manage Bar for Drink ...")
    await asyncio.sleep(1)
    print(f"{ctime()} [{customer}] Manage Bar for Drink ...Done!")
    
    print(f"{ctime()} [{customer}] All served!")

async def main():
    start_time = time()
    customers = ["Task-A", "Task-B", "Task-C"]
    
    # รัน Greeting ทีละคนตามภาพ
    for customer in customers:
        await greet_diners(customer)
    
    print(f"\n{ctime()} --- All customers greeted. Scheduling independent Async Tasks! ---\n")
    
    # รัน Task ของลูกค้าแต่ละคนแบบพร้อมกัน (Concurrent)
    tasks = [asyncio.create_task(customer_private_workflow(c)) for c in customers]
    await asyncio.gather(*tasks)
    
    print(f"\n{ctime()} Finished Entire Restaurant Operation in {time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())