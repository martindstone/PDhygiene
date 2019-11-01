#!/usr/bin/env python

import pd
import json
import argparse
from dateutil.parser import parse
from tzlocal import get_localzone

parser = argparse.ArgumentParser()
parser.add_argument("pd_api_key", help="PagerDuty API key")
args = parser.parse_args()

print("Getting Escalation policies... ", end="", flush=True)
escalation_policies = pd.fetch_escalation_policies(api_key=args.pd_api_key, params={"include[]": ["targets", "current_oncall"]})
print(f"Got {len(escalation_policies)}.")

for ep in escalation_policies:
	targets = {}
	for oncall in ep["on_call"]:
		email = oncall['user']['email']
		if email not in targets:
			targets[email] = []
		targets[email].append(oncall)
	for email, oncalls in targets.items():
		if len(oncalls) > 1:
			print(f"\nEscalation Policy {ep['summary']}: {oncall['user']['name']} ({email}) is currently on call at multiple levels:")
			for oncall in oncalls:
				timestr = ''
				if oncall['start'] == None and oncall['end'] == None:
					timestr = "Always on call"
				else:
					start = (parse(oncall['start'])).astimezone(get_localzone())
					end = (parse(oncall['end'])).astimezone(get_localzone())
					timestr = f"{start.strftime('%c')} - {end.strftime('%c')}"
				print(f"    Level {oncall['level']}: {timestr}")
