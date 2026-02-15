# Vertex Automation: Lead Handling Script (Prototype v1.0)
# Purpose: Researching data flow from web-forms to CRM API

def process_lead(name, interest_type):
    """
    Standardizes lead data for Richmond Hill real estate analysis.
    """
    print(f"Vertex System: Analyzing lead for {name}...")
    
    lead_data = {
        "entity": name,
        "type": interest_type,
        "status": "RESEARCH_LOGGED",
        "lab_id": "ST-ROB-10"
    }
    
    return lead_data

# Run mock analysis
if __name__ == "__main__":
    test_lead = process_lead("Sample Client", "Residential Purchase")
    print(f"Data Normalized: {test_lead}")
