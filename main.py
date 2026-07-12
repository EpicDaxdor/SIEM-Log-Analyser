from datetime import datetime

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

print("LOG FILE NAME: sample_log.txt")
print("LOG SCAN TIME: ", datetime.now())

print("\n-------------- EVENT SUMMARY -----------------\n")


sample_log = open("sample_log.txt", 'r')
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
                Multiple_failed_login_attempts +=1
        line_count += 1

       

print ("TOTAL LOG ENTRIES: ", line_count, "\n")

print("ERROR EVENTS FOUND:" , Error_count)
print("WARNING EVENTS FOUND:" , Warning_count)
print("INFO EVENTS FOUND:" , Info_count)

print("\n------------ SECURITY EVENT SUMMARY-----------\n")

print("FAILED LOGIN ATTEMPTS:" , Failed_login_attempts)
print("MULTIPLE FAILED LOGIN ATTEMPTS:" , Multiple_failed_login_attempts)

print("\n------------ SEARCH RESULTS ------------------\n")

sample_log = open("sample_log.txt", 'r')
search_word = input("What would you like to search for ? \n")
for line in sample_log:
        if search_word.lower() in line.lower():
                print(line)


sample_log.close()

print("================================================")