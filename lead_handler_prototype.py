import json
import datetime

# Vertex Automation: Lead Handling Logic v1.0
# Purpose: Normalizes unstructured realtor data into CRM-ready JSON

def process_lead(name, email, property_interest, budget):
    """
    Simulates the intake of a raw lead and timestamps it for the brokerage.
    """
    # 1. Generate a timestamp for the "Speed-to-Lead" metric
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. Structure the data (The "JSON" part)
    lead_packet = {
        "status": "NEW_INTAKE",
        "source": "Vertex_Web_Form",
        "timestamp": timestamp,
        "client_data": {
            "name": name,
            "contact": email,
            "target_property": property_interest,
            "budget_range": budget
        },
        "routing": "High_Priority_Queue"
    }
    
    # 3. "Log" the action (Simulating a database save)
    print(f"[VERTEX SYSTEM] Processing lead for {name} at {timestamp}...")
    return json.dumps(lead_packet, indent=4)

# Test the system (This runs when you open the file)
if __name__ == "__main__":
    test_result = process_lead("Test Client", "client@gmail.com", "123 Bayview Ave", "$1.5M")
    print("System Output:")
    print(test_result)
