import pd
import json
import argparse
import csv

contact_method_types = {
	"email_contact_method": "Email", 
	"phone_contact_method": "Phone", 
	"push_notification_contact_method": "Push", 
	"sms_contact_method": "SMS"
}

parser = argparse.ArgumentParser()
parser.add_argument("pd_api_key", help="PagerDuty API key")
parser.add_argument("output_file", help="CSV file to write to")
args = parser.parse_args()

print("Getting Users... ", end="", flush=True)
users = pd.fetch_users(api_key=args.pd_api_key, params={"include[]": ["contact_methods", "notification_rules", "teams"]})
print(f"Got {len(users)}.")

csv_data = []
for user in users:
	teams = []
	for team in user['teams']:
		teams.append(team['name'])

	contacts = {
		"email_contact_method": 0, 
		"phone_contact_method": 0, 
		"push_notification_contact_method": 0, 
		"sms_contact_method": 0
	}
	for contact in user['contact_methods']:
		contacts[contact['type']] += 1

	rules = {
		"low": 0,
		"high": 0
	}
	for rule in user['notification_rules']:
		rules[rule['urgency']] += 1

	row = [user['email'], user['name'], ', '.join(teams)]
	row.extend(contacts.values())
	row.extend(rules.values())
	csv_data.append(row)

csv_headers = [
    "User Email",
    "User Name",
    "Team Names",
    "Emails",
    "Phone Numbers",
    "SMS Numbers",
    "Push Destinations",
    "Rules: Low",
    "Rules: High"
]

with open(args.output_file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(csv_headers)
    writer.writerows(csv_data)

print(f"Wrote {len(csv_data)} rows to {args.output_file}.")