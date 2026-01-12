import re

LOG_PATH = "text_files/log.txt"

PATTERN = re.compile(r"^(ERROR|INFO|WARNING) (\d{4}-\d{2}-\d{2}) (.+)$")

type_counts = {}
error_lines = []

total_lines = 0
parsed_lines = 0
skipped_lines = 0

try:
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue

            total_lines += 1

            m = PATTERN.search(line)
            if not m:
                skipped_lines += 1
                continue

            parsed_lines += 1

            msg_type = m.group(1)
            date = m.group(2)
            message = m.group(3)

            type_counts[msg_type] = type_counts.get(msg_type, 0) + 1

            if msg_type == "ERROR":
                error_lines.append((date, message))

except FileNotFoundError:
    print(f"File not found: {LOG_PATH}")
    raise SystemExit(1)

print(f"Total lines: {total_lines}")
print(f"Parsed lines: {parsed_lines}")
print(f"Skipped lines: {skipped_lines}\n")

if type_counts:
    for msg_type, count in type_counts.items():
        print(f"{msg_type}: {count}")

    most_common = max(type_counts, key=type_counts.get)
    print(f"\nMost common type: {most_common} ({type_counts[most_common]} times)")
else:
    print("No message types found (no valid log lines).")

print("\nERRORS:")
if error_lines:
    for date, message in error_lines:
        print(f"{date} | {message}")
else:
    print("No ERROR lines found.")




