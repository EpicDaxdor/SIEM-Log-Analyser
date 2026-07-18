🛡 SIEM Log Analyser

Overview

# SIEM Log Analyser

A Python-based Security Information and Event Management (SIEM) log analyser built to simulate common Security Operations Centre (SOC) tasks.

This project was created while teaching myself Python and cybersecurity. Each version introduces new concepts, gradually improving both the application and my programming skills.


Why I Built This Project

I currently work on an IT Service Desk and am working towards a career in Cyber Security, with the goal of becoming a SOC Analyst or Blue Team professional. Rather than following tutorials alone, I wanted to build a real project that would allow me to:

    - Learn Python through practical experience. 
    - Understand how security analysts interact with log data. 
    - Learn software development practices using Git and GitHub. 
    - Build a portfolio project that demonstrates continuous learning and problem-solving. 

Every feature in this project has been researched, designed and implemented as part of my learning journey.


Current Features
    - Read and analyse log files. 
    - Count total log entries. 
    - Summarise INFO, WARNING and ERROR events. 
    - Detect failed login attempts. 
    - Search log files for user-defined keywords. 
    - Detect known suspicious IP addresses using a predefined threat list. 
    - Interactive command-line menu. 
    - Timestamp each analysis report.
    
Technologies Used
    - Python 
    - Git 
    - GitHub 
    - Regular Expressions (re) 
    - File Handling 
    - Command Line Interface (CLI)

Screenshots

<img width="814" height="515" alt="suspicious_IP screenshot" src="https://github.com/user-attachments/assets/5d949b13-ec50-4258-88ab-a1daabc00c94" />
<img width="362" height="128" alt="security_summary screenshot" src="https://github.com/user-attachments/assets/6cd22608-d26b-470a-9ae5-3159f9f4c08a" />
<img width="357" height="228" alt="event_summary screenshot" src="https://github.com/user-attachments/assets/e4a34103-ac29-41c7-9148-4f97879b319c" />
<img width="381" height="312" alt="Main_menu Screenshot" src="https://github.com/user-attachments/assets/e00944ae-1b87-4246-b51c-8b2d0cf2286d" />



Roadmap
Version 0.4
    -  Added GeoIP to the IP detection feature
    -  Updated IP list with real world blacklisted IP addresses       

Version 0.3
    -  Added suspicious IP detection. 
    -  Introduced regular expressions. 
    -  Added modular threat list. 
Version 0.2
    -  Added an interactive menu. 
    -  Refactored code into reusable functions. 
Version 0.1
    -  Built the initial log analyser. 
    -  Added event summaries. 
    -  Added keyword searching. 
    -  Improved report formatting. 
    -  Added scan timestamps.
    

Future Development
Planned features include:
    - Detect repeated failed login attempts from the same IP. 
    - Parse multiple log formats. 
    - Export reports to CSV. 
    - Improve report formatting. 
    - Add configurable threat intelligence lists. 
    - Refactor the project into a more modular architecture. 
    - Improve error handling and validation.

How to install
    - git clone ...
    - cd ...
    - pip install -r requirements.txt
    - python main.py
