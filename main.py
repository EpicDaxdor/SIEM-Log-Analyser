print("SIEM and Log Management \n")

print ("============= SIEM REPORT ===============\n")

Error_count = 0
Warning_count = 0
Info_count = 0
Failed_login_attempts = 0
Multiple_failed_login_attempts = 0


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

print("ERRORS FOUND:" , Error_count)
print("WARNINGS FOUND:" , Warning_count)
print("INFO FOUND:" , Info_count)
print("FAILED LOGIN ATTEMPTS:" , Failed_login_attempts)
print("MULTIPLE FAILED LOGIN ATTEMPTS:" , Multiple_failed_login_attempts)

sample_log = open("sample_log.txt", 'r')
search_word = input("What would you like to search for ? ")
for line in sample_log:
        if search_word.lower() in line.lower():
                print(line)


sample_log.close()

print("==========================================")