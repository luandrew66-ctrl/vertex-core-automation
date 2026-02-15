import json
import datetime

# lead handler for vertex
# feb 2026
# basically just takes the info and puts it in a json format

def process(name, email, type, budget):
    # getting the current time
    x = datetime.datetime.now()
    timestamp = x.strftime("%Y-%m-%d %H:%M:%S")

    # making the packet
    # TODO: add phone number later??
    data = {
        "status": "NEW",
        "time": timestamp,
        "client": name,
        "email": email,
        "info": {
            "type": type,
            "budget": budget
        },
        "source": "web_form"
    }

    # print("check") 
    
    # returning it as text
    return json.dumps(data, indent=2)

# testing
if __name__ == "__main__":
    print("running test...")
    test = process("John Doe", "john@gmail.com", "House", "1.2m")
    print(test)