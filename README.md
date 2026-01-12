# Log Analyzer v2 (Regex Edition)

A simple console program that analyzes a log file using regular expressions and prints useful statistics.

This is the second version of the project, focused on regex-based parsing and handling malformed log lines.

## Features
- Counts total number of log lines
- Parses valid log entries using regular expressions
- Counts message types (INFO, WARNING, ERROR)
- Detects and skips malformed log lines
- Finds the most common message type
- Prints all ERROR messages with date and message

## Log format
Each valid log line must follow this format:
```
TYPE YYYY-MM-DD message...
```
Example:
```
ERROR 2026-01-09 Disk is full
INFO 2026-01-09 User logged in
WARNING 2026-01-10 Low memory
```
Invalid lines are safely skipped and counted.

## How to run
1. Put your log file into the `text_files/` directory as `log.txt`
2. Run the script:

```python log_analyzer_v2.py``` # or python3, depending on your system

## Technologies used
- Python
- Regular Expressions (`re`)
- File I/O
- Dictionaries and lists
- Basic text processing

## Purpose
This project was built to practice:
- parsing text files with regular expressions
- extracting structured data from logs
- handling invalid input gracefully
- building small but complete Python scripts
