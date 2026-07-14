from datetime import datetime
import re
from suspicious_ips import suspicious_ips
import geoip2.database

reader = geoip2.database.Reader("GeoLite2-City.mmdb")

print("SIEM and Log Management \n")

print ("===============================================\n")
print ("            SIEM ANALYSER REPORT\n")
print ("===============================================\n")

Error_count = 0
Warning_count = 0
Info_count = 0
Failed_login_attempts = 0
Multiple_failed_login_attempts = 0
line_count = 0


def geo_lookup(ip):
    try:
        response = reader.city(ip)

        country = response.country.name
        city = response.city.name
        iso = response.country.iso_code
        lat = response.location.latitude
        lon = response.location.longitude

        print(f"\nGeo‑IP Lookup for {ip}")
        print(f"Country: {country} ({iso})")
        print(f"City: {city}")
        print(f"Latitude: {lat}, Longitude: {lon}")

    except Exception as e:
        print(f"Geo‑IP lookup failed for {ip}: {e}")


def main_menu():
        while True:
                print("\n====== Main Menu =======\n")
                print("1. Search logs")
                print("2. Event Summary")
                print("3. Security Summary")
                print("4. view suspicious ips")
                print("5. Exit\n")


                choice = input("Choose an option ? ")

                if choice == "1":
                        Search_logs()
                elif choice == "2":
                        Event_summary()
                elif choice == "3":
                        Security_events()
                elif choice == "4":
                        view_suspicious_ips()
                elif choice == "5":
                        print("Goodbye")
                        break
                else:
                        print("Invalid Choice, Try again!")     


def Search_logs():
        print("\n------------ SEARCH RESULTS ------------------\n")

        with open("sample_log.txt", 'r') as sample_log:
            search_word = input("What would you like to search for ? ")
            for line in sample_log:
                if search_word.lower() in line.lower():
                        print(line)
        input("\nPress Enter to go back to the menu...")
                    

def Event_summary():
    print("\n-------------- EVENT SUMMARY -----------------\n")

    global Error_count, Warning_count, Info_count
    global Failed_login_attempts, Multiple_failed_login_attempts, line_count

    
    Error_count = 0
    Warning_count = 0
    Info_count = 0
    Failed_login_attempts = 0
    Multiple_failed_login_attempts = 0
    line_count = 0

    with open("sample_log.txt", 'r') as sample_log:
        for line in sample_log:
            if "ERROR" in line:
                Error_count += 1
            if "WARNING" in line:
                Warning_count += 1
            if "INFO" in line:
                Info_count += 1
            if "Failed login attempt" in line:
                Failed_login_attempts += 1
            if "Multiple failed login attempts" in line:
                Multiple_failed_login_attempts += 1
            line_count += 1

    print("LOG FILE NAME: sample_log.txt")
    print("LOG SCAN TIME:", datetime.now(), "\n")
    print("TOTAL LOG ENTRIES:", line_count, "\n")
    print("ERROR EVENTS FOUND:", Error_count)
    print("WARNING EVENTS FOUND:", Warning_count)
    print("INFO EVENTS FOUND:", Info_count)
    input("\nPress Enter to go back to the menu...")


def Security_events():

        print("\n------------ SECURITY EVENT SUMMARY-----------\n")

        print("FAILED LOGIN ATTEMPTS:" , Failed_login_attempts)
        print("MULTIPLE FAILED LOGIN ATTEMPTS:" , Multiple_failed_login_attempts)
        input("\nPress Enter to go back to the menu...")

def view_suspicious_ips(): 

    print("\n------------ SUSPICIOUS IP CHECK -------------\n")


    ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
    suspicious_count = 0

    with open("sample_log.txt", "r") as sample_log:
        for line in sample_log:
            match = ip_pattern.search(line)
            if match:
                ip = match.group()
                if ip in suspicious_ips or "Failed login attempt" in line:
                    print("Suspicious IP detected:", ip, "→", line.strip())
                    geo_lookup(ip)
                    suspicious_count += 1

    print("\nTotal suspicious IP events:", suspicious_count)
    input("\nPress Enter to go back to the menu...")

main_menu()

print("================================================")