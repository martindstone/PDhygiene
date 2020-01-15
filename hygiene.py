#!/usr/bin/env python

import pd
import json
import argparse
from dateutil.parser import parse
from tzlocal import get_localzone
from datetime import datetime, timedelta, timezone

parser = argparse.ArgumentParser()
parser.add_argument("pd_api_key", help="PagerDuty API key")
args = parser.parse_args()

print("Getting Escalation policies... ", end="", flush=True)
escalation_policies = pd.fetch_escalation_policies(api_key=args.pd_api_key, params={"include[]": ["targets", "current_oncall"]})
print(f"Got {len(escalation_policies)}.\n\n")

for ep in escalation_policies:
	targets = {}

	findings = False
	if len(ep['escalation_rules']) < 2:
		findings =True
		print(f"Escalation Policy {ep['summary']} ({ep['html_url']}) has only {len(ep['escalation_rules'])} rule.")

	for oncall in ep["on_call"]:
		email = oncall['user']['email']
		if email not in targets:
			targets[email] = []
		targets[email].append(oncall)
	for email, oncalls in targets.items():
		if len(oncalls) > 1:
			findings = True
			print(f"Escalation Policy {ep['summary']} ({ep['html_url']}):\n    {oncall['user']['name']} ({email}) is currently on call at multiple levels:")
			for oncall in oncalls:
				timestr = ''
				if oncall['start'] == None and oncall['end'] == None:
					timestr = "Always on call"
				else:
					start = (parse(oncall['start'])).astimezone(get_localzone())
					end = (parse(oncall['end'])).astimezone(get_localzone())
					timestr = f"{start.strftime('%c')} - {end.strftime('%c')}"
				print(f"        Level {oncall['level']}: {timestr}")

print("\n\nGetting Schedules... ", end="", flush=True)
schedules = pd.fetch_schedules(api_key=args.pd_api_key)
print(f"Got {len(schedules)}.\n\n")
since = datetime.now(timezone.utc).replace(microsecond=0)
until = (datetime.now(timezone.utc) + timedelta(days=14)).replace(microsecond=0)
for s in schedules:
	s_full = pd.request(api_key=args.pd_api_key, endpoint=f"/schedules/{s['id']}", 
						params={"since": since.isoformat(), "until": until.isoformat()})['schedule']
	coverage = s_full['final_schedule']['rendered_coverage_percentage']
	if coverage < 100.0:
		print(f"Schedule {s_full['summary']} ({s_full['html_url']}) has only {coverage}% coverage")
		if coverage > 0.0:
			print("    Gaps:")
			entries = s_full['final_schedule']['rendered_schedule_entries']
			if parse(entries[0]['start']) > since:
				gap_start = since.astimezone(get_localzone())
				gap_end = parse(entries[0]['start']).astimezone(get_localzone())
				print(f"        {gap_start.strftime('%c')} - {gap_end.strftime('%c')}")
			for i in range(len(entries)-1):
				if entries[i]['end'] < entries[i+1]['start']:
					gap_start = parse(entries[i]['end']).astimezone(get_localzone())
					gap_end = parse(entries[i+1]['start']).astimezone(get_localzone())
					print(f"        {gap_start.strftime('%c')} - {gap_end.strftime('%c')}")
			if parse(entries[-1]['end']) < until:
				gap_start = parse(entries[-1]['end']).astimezone(get_localzone())
				gap_end = until.astimezone(get_localzone())
				print(f"        {gap_start.strftime('%c')} - {gap_end.strftime('%c')}")
