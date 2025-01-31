import re
import json

with open('data_log.txt', 'r') as file:
    data = file.readlines()

# 1. Extract All IP Addresses
regex = r'\b(\d[0-9]{1,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3}\.\d[0-9]{0,3})\b'
ip_addresses = re.findall(regex, "\n".join(data))
unique_ip_addresses = sorted(set(ip_addresses))

for ip in unique_ip_addresses:
    print(ip)


# 2. Extract User Actions
pattern= r'INFO: User (\w+) (performed action .*? on record \d+|created a new record|logged (?:in|out))'
user_actions={}
for line in data:
        match= re.search(pattern, line)
        if match:
                username, action= match.groups()
                user_actions.setdefault(username, set()).add(action)
               
user_actions={user: list(actions) for user, actions in user_actions.items()}
print(user_actions)


# 3. Validate and Extract Email Addresses
email_pattern= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,5}\b'
emails= re.findall(email_pattern, "\n".join(data))
print(emails)


# 4. Extract Phone Numbers
phone_pattern= r'\b\d{3}-\d{3}-\d{4}\b'
phones= re.findall(phone_pattern, "n".join(data))
print(phones)


# 5. Extract All URLs
url_pattern= r'https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9./?=&%-]*)?'
urls= set(re.findall(url_pattern, "\n".join(data)))
print(urls)


# 6. Classify Log Levels
log_severity= {'INFO': 0, 'WARNING': 1, 'ERROR': 2, 'CRITICAL': 3}
for line in data:
    for severity in log_severity.keys():
        if f"{severity}" in line:
            log_severity[severity] +=1
print(log_severity)


# 7. Extract Timestamps
timestamps_pattern = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]'
timestamps = sorted(re.findall(timestamps_pattern, "\n".join(data)))
print(timestamps)


# 8. Mask Sensitive Information
masked_data = "\n".join(data)
masked_data  = re.sub(regex, "***.***.***.***", masked_data)
masked_data = re.sub(phone_pattern, "XXX-XXX-XXXX", masked_data)
masked_data  = re.sub(email_pattern, "hidden@example.com", masked_data)

with open('masked_data_log.txt', 'w') as f:
     f.write(masked_data )


# 9. Validate Error Codes
error_code_pattern = r'\bDB_ERR_\d{4}\b'
error_code = sorted(set(re.findall(error_code_pattern, "\n".join(data))))
print(error_code)


# 10. Parse Log into Structured Format'
log_entries = []
log_entry_pattern = r'\[(.*?)\] (\w+): (.*)'
for line in data:
    match = re.match(log_entry_pattern, line)
    if match:
         timestamp, severity, message = match.groups()
         log_entries.append({"timestamp": timestamp, "level": severity, "message": message})
with open("parsed_log.json", 'w') as json_file:
    json.dump(log_entries, json_file, indent = 4)