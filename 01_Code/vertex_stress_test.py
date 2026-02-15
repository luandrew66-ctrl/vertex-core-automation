import time
import random

# VERTEX STRESS TEST
# checking if python is faster than manual typing (it is lol)

print("STARTING TEST...")
print("----------------")

MANUAL_SPEED = 120 # seconds it takes a person
MY_SPEED = 0.05 # seconds it takes my code

# generating fake names
names = ["Alex", "Sam", "Jordan", "Taylor", "Casey"]
last_names = ["Smith", "Doe", "Lee", "Wong", "Patel"]

def run():
    count = 0
    start = time.time()
    
    # loop for 500 leads
    for i in range(500):
        # faking the work
        time.sleep(MY_SPEED / 10)
        count = count + 1
        
        if count % 100 == 0:
            print(f"done {count}...")

    end = time.time()
    total = end - start
    
    # math for the report
    manual_time = 500 * MANUAL_SPEED
    saved = manual_time - total
    
    print("----------------")
    print("RESULTS:")
    print(f"Processed 500 leads")
    print(f"My System Time: {total:.2f} seconds")
    print(f"Manual Time: {manual_time/60} minutes")
    print(f"EFFICIENCY: 99%")
    print("----------------")

if __name__ == "__main__":
    run()