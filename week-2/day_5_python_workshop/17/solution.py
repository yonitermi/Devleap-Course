import re

def main(txt):
    # Use regular expression to find emails
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, txt)

    # De-duplicate emails (retain case of the first instance found)
    seen = set()
    unique_emails = []
    for email in emails:
        lowercase_email = email.lower()
        if lowercase_email not in seen:
            seen.add(lowercase_email)
            unique_emails.append(email)

    # Sort emails by domain and then by name
    unique_emails.sort(key=lambda x: (x.split('@')[1], x.split('@')[0]))

    return unique_emails