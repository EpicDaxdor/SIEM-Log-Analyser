SIEM Log Analyser
Overview

The SIEM Log Analyser is a Python project designed to analyse security log files and present key information in a clear, readable format. The aim is to replicate some of the core tasks performed by Security Operations Centre (SOC) analysts, such as identifying errors, summarising events, searching logs, and highlighting suspicious activity.
This project is being developed incrementally as I learn Python, with each new feature introducing new programming concepts and improving the overall application.


Why I Built This Project

I currently work on an IT Service Desk and am working towards a career in Cyber Security, with the goal of becoming a SOC Analyst or Blue Team professional.
Rather than following tutorials alone, I wanted to build a real project that would allow me to:
    • Learn Python through practical experience. 
    • Understand how security analysts interact with log data. 
    • Learn software development practices using Git and GitHub. 
    • Build a portfolio project that demonstrates continuous learning and problem-solving. 
Every feature in this project has been researched, designed and implemented as part of my learning journey.


Current Features
    • Read and analyse log files. 
    • Count total log entries. 
    • Summarise INFO, WARNING and ERROR events. 
    • Detect failed login attempts. 
    • Search log files for user-defined keywords. 
    • Detect known suspicious IP addresses using a predefined threat list. 
    • Interactive command-line menu. 
    • Timestamp each analysis report.
    
Technologies Used
    • Python 
    • Git 
    • GitHub 
    • Regular Expressions (re) 
    • File Handling 
    • Command Line Interface (CLI)

Roadmap

Version 0.3
    • ✅ Added suspicious IP detection. 
    • ✅ Introduced regular expressions. 
    • ✅ Added modular threat list. 
Version 0.2
    • ✅ Added an interactive menu. 
    • ✅ Refactored code into reusable functions. 
Version 0.1
    • ✅ Built the initial log analyser. 
    • ✅ Added event summaries. 
    • ✅ Added keyword searching. 
    • ✅ Improved report formatting. 
    • ✅ Added scan timestamps.
    
Future Development

Planned features include:
    • Detect repeated failed login attempts from the same IP. 
    • Parse multiple log formats. 
    • Export reports to CSV. 
    • Improve report formatting. 
    • Add configurable threat intelligence lists. 
    • Refactor the project into a more modular architecture. 
    • Improve error handling and validation.
