import os

def save_data(date, aqi, category):
    f = open("campus_aqi.txt", "a")
    line_to_save = str(date) + "," + str(aqi) + "," + category + "\n"
    f.write(line_to_save)
    f.close()

def read_data():
    my_list = []
    
    if os.path.exists("campus_aqi.txt"):
        f = open("campus_aqi.txt", "r")
        lines = f.readlines()
        f.close()
        
        for line in lines:
            clean_line = line.strip()
            parts = clean_line.split(",")
            
            if len(parts) == 3:
                record = {
                    "date": parts[0],
                    "aqi": int(parts[1]),
                    "category": parts[2]
                }
                my_list.append(record)
                
    return my_list