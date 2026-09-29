import storage

def get_advisory(category):
    if category == "Good":
        return "Normal outdoor campus activities and sports permitted."
    elif category == "Satisfactory":
        return "Safe for most. Asthmatic students should carry inhalers."
    elif category == "Moderate":
        return "Sensitive students should avoid heavy physical exertion outside."
    elif category == "Poor":
        return "Cancel prolonged outdoor physical training and NCC drills."
    elif category == "Very Poor":
        return "Mandate N95 masks for outdoor campus movement."
    elif category == "Severe":
        return "Suspend all outdoor sports. All students must remain indoors."
    else:
        return "No advisory available for this category."

def check_current():
    print("\n--- Latest Campus Advisory ---")
    all_records = storage.read_data()
    
    if len(all_records) == 0:
        print("No data found! Please enter AQI first.")
    else:
        last_record = all_records[-1] 
        advice = get_advisory(last_record['category'])
        
        print("Date:", last_record['date'])
        print("AQI Level:", last_record['aqi'])
        print("Category:", last_record['category'])
        print("Notice:", advice)

def view_history():
    print("\n--- AQI History ---")
    all_records = storage.read_data()
    
    if len(all_records) == 0:
        print("Text file is empty.")
    else:
        for item in all_records:
            print("Date:", item['date'], " | AQI:", item['aqi'], " | Status:", item['category'])