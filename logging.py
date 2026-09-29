import datetime
import validation
import storage

def get_category(aqi):
    if aqi >= 0 and aqi <= 50:
        return "Good"
    elif aqi >= 51 and aqi <= 100:
        return "Satisfactory"
    elif aqi >= 101 and aqi <= 200:
        return "Moderate"
    elif aqi >= 201 and aqi <= 300:
        return "Poor"
    elif aqi >= 301 and aqi <= 400:
        return "Very Poor"
    elif aqi > 400:
        return "Severe"
    else:
        return "Unknown"

def log_aqi():
    print("\n--- Log AQI ---")
    today_date = datetime.date.today()
    
    aqi_val = validation.get_valid_aqi()
    cat = get_category(aqi_val)
    
    storage.save_data(today_date, aqi_val, cat)
    print("Done! Data saved successfully.")