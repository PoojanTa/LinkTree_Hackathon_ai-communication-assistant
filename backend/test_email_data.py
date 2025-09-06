# Test script for analyzing support email dataset
import pandas as pd

# Load the sample data
csv_path = '../sample_data/68b1acd44f393_Sample_Support_Emails_Dataset.csv'
df = pd.read_csv(csv_path)

# Simple analysis: Count emails per sender and most common subject
sender_counts = df['sender'].value_counts()
common_subject = df['subject'].value_counts().idxmax()

print('Email counts by sender:')
print(sender_counts)
print('\nMost common subject:')
print(common_subject)

# Example: Find all emails about login issues
login_emails = df[df['body'].str.contains('log into my account', case=False)]
print('\nEmails about login issues:')
print(login_emails[['sender', 'subject', 'sent_date']])
