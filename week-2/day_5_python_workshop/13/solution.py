def main(input_str):
    names = [name.strip() for name in input_str.split(',')]
    
    def get_email(name):
        # Removing non-alpha characters except spaces
        cleaned_name = ''.join([char if char.isalpha() or char.isspace() else '' for char in name])
        parts = cleaned_name.split()
        email = f"{parts[0]}.{parts[-1]}"
        return email.lower()

    created_emails = set()
    result = []
    
    for name in names:
        base_email = get_email(name)
        full_email = f"{base_email}@company.com"
        
        counter = 1
        while full_email in created_emails:
            counter += 1
            full_email = f"{base_email}{counter}@company.com"
        
        created_emails.add(full_email)
        result.append((name, full_email))
            
    return result