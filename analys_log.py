# Run with: python3 analyze_logs.py

with open("creds.log") as f:
    entries = f.readlines()

print(f"{'Timestamp':<25} | {'IP':<15} | {'Location':<20} | {'Username':<12} | {'Password'}")
print("-" * 90)
for line in entries:
    parts = line.strip().split('|')
    try:
        timestamp = parts[0].strip()
        ip_info = parts[1].split(':')[1].strip()
        location = ip_info[ip_info.find('(')+1:ip_info.find(')')]
        user = parts[3].split(':')[1].strip()
        pwd = parts[4].split(':')[1].strip()
        print(f"{timestamp:<25} | {ip_info.split()[0]:<15} | {location:<20} | {user:<12} | {pwd}")
    except IndexError:
        continue
