with open("creds.log") as f:
    entries = f.readlines()

print(f"{'Timestamp':<25} | {'IP':<15} | {'Username':<12} | {'Password'}")
print("-" * 70)
for line in entries:
    parts = line.strip().split('|')
    try:
        timestamp = parts[0].strip()
        ip = parts[1].split(':')[1].strip()
        user = parts[3].split(':')[1].strip()
        pwd = parts[4].split(':')[1].strip()
        print(f"{timestamp:<25} | {ip:<15} | {user:<12} | {pwd}")
    except IndexError:
        continue
