# Extract emails from text problem
import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)

# Example usage
text = "Please contact us at support@example.com or sales@example.org for more information."
emails = extract_emails(text)
print("Extracted emails:", emails)  # Output: Extracted emails: ['support@example.com', 'sales@example.org']