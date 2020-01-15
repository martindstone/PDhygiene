# PDhygiene

Scripts to show information about response health

## Installation:

* Clone this repo and `cd` to it
* Create a virtual environment with Python 3: `python3 -m venv venv`
* Activate the virtual environment: `. venv/bin/activate`
* Get the dependencies: `pip install -r requirements.txt`

## Usage:

### Show Escalation Policies where the same person is currently on call at multiple levels,
### and show Schedules with coverage gaps:

`python ./hygiene.py pd_api_key`

### Sample Output:

```
Getting Escalation policies... Got 21.

Escalation Policy Backend DBA (https://example.pagerduty.com/escalation_policies/PXXXXXX):
    Jayne Cobb (martin+inara@pagerduty.com) is currently on call at multiple levels:
        Level 2: Mon Jan 13 00:00:00 2020 - Sat Jan 18 00:00:00 2020
        Level 3: Mon Jan 13 00:00:00 2020 - Sat Jan 18 00:00:00 2020
Escalation Policy Backend DevOps (https://example.pagerduty.com/escalation_policies/PXXXXXX):
    Malcolm Reynolds (martin+jayne@pagerduty.com) is currently on call at multiple levels:
        Level 1: Tue Jan 14 09:00:00 2020 - Wed Jan 15 09:00:00 2020
        Level 3: Tue Jan 14 09:00:00 2020 - Wed Jan 15 09:00:00 2020
Escalation Policy Backend DevOps (https://example.pagerduty.com/escalation_policies/PXXXXXX):
    Jayne Cobb (martin+book@pagerduty.com) is currently on call at multiple levels:
        Level 2: Tue Jan 14 09:00:00 2020 - Wed Jan 15 09:00:00 2020
        Level 3: Tue Jan 14 09:00:00 2020 - Wed Jan 15 09:00:00 2020
Escalation Policy Event Sender (https://example.pagerduty.com/escalation_policies/PXXXXXX) has only 1 rule.
Escalation Policy SN:Database (https://example.pagerduty.com/escalation_policies/PXXXXXX) has only 1 rule.
Escalation Policy Unusual EP (https://example.pagerduty.com/escalation_policies/PXXXXXX) has only 1 rule.


Getting Schedules... Got 19.


Schedule SN-CAB Approval (https://example.pagerduty.com/schedules/PXXXXXX) has only 0.0% coverage
Schedule SN-Capacity Mgmt (https://example.pagerduty.com/schedules/PXXXXXX) has only 0.0% coverage
Schedule SN-Change Management (https://example.pagerduty.com/schedules/PXXXXXX) has only 0.0% coverage
Schedule Sparse - Inara (https://example.pagerduty.com/schedules/PXXXXXX) has only 37.5% coverage
    Gaps:
        Tue Jan 14 22:53:35 2020 - Wed Jan 15 04:00:00 2020
        Wed Jan 15 13:00:00 2020 - Thu Jan 16 04:00:00 2020
        Thu Jan 16 13:00:00 2020 - Fri Jan 17 04:00:00 2020
        Fri Jan 17 13:00:00 2020 - Sat Jan 18 04:00:00 2020
        Sat Jan 18 13:00:00 2020 - Sun Jan 19 04:00:00 2020
        Sun Jan 19 13:00:00 2020 - Mon Jan 20 04:00:00 2020
        Mon Jan 20 13:00:00 2020 - Tue Jan 21 04:00:00 2020
        Tue Jan 21 13:00:00 2020 - Wed Jan 22 04:00:00 2020
        Wed Jan 22 13:00:00 2020 - Thu Jan 23 04:00:00 2020
        Thu Jan 23 13:00:00 2020 - Fri Jan 24 04:00:00 2020
        Fri Jan 24 13:00:00 2020 - Sat Jan 25 04:00:00 2020
        Sat Jan 25 13:00:00 2020 - Sun Jan 26 04:00:00 2020
        Sun Jan 26 13:00:00 2020 - Mon Jan 27 04:00:00 2020
        Mon Jan 27 13:00:00 2020 - Tue Jan 28 04:00:00 2020
        Tue Jan 28 13:00:00 2020 - Tue Jan 28 22:53:35 2020
Schedule Sparse - Jayne (https://example.pagerduty.com/schedules/PXXXXXX) has only 33.3% coverage
    Gaps:
        Tue Jan 14 22:53:35 2020 - Wed Jan 15 09:00:00 2020
        Wed Jan 15 17:00:00 2020 - Thu Jan 16 09:00:00 2020
        Thu Jan 16 17:00:00 2020 - Fri Jan 17 09:00:00 2020
        Fri Jan 17 17:00:00 2020 - Sat Jan 18 09:00:00 2020
        Sat Jan 18 17:00:00 2020 - Sun Jan 19 09:00:00 2020
        Sun Jan 19 17:00:00 2020 - Mon Jan 20 09:00:00 2020
        Mon Jan 20 17:00:00 2020 - Tue Jan 21 09:00:00 2020
        Tue Jan 21 17:00:00 2020 - Wed Jan 22 09:00:00 2020
        Wed Jan 22 17:00:00 2020 - Thu Jan 23 09:00:00 2020
        Thu Jan 23 17:00:00 2020 - Fri Jan 24 09:00:00 2020
        Fri Jan 24 17:00:00 2020 - Sat Jan 25 09:00:00 2020
        Sat Jan 25 17:00:00 2020 - Sun Jan 26 09:00:00 2020
        Sun Jan 26 17:00:00 2020 - Mon Jan 27 09:00:00 2020
        Mon Jan 27 17:00:00 2020 - Tue Jan 28 09:00:00 2020
        Tue Jan 28 17:00:00 2020 - Tue Jan 28 22:53:35 2020

```

## Usage:

### Make a CSV file with counts of contact methods by type and notification rules by urgency:

`python ./contact_methods.py pd_api_key my_csv_file.csv`

### Sample Output:

| User Email                    | User Name                | Team Names                                                                                               | Emails | Phone Numbers | SMS Numbers | Push Destinations | Rules: Low | Rules: High |
| ----------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------- | ------ | ------------- | ----------- | ----------------- | ---------- | ----------- |
| marketingevents@pagerduty.com | Abel Marshall            | Operations, Helpdesk, Security, Customer Experience, Major All Hands, Support, Engineering, Service Desk | 2      | 2             | 4           | 1                 | 1          | 9           |
| adela.cervantsz@example.com   | Adela Cervantsz          | Operations, Security, Customer Experience, Engineering                                                   | 1      | 0             | 0           | 0                 | 1          | 1           |
| aileen.mottern@example.com    | Aileen Mottern           | Operations, Helpdesk, Security, Engineering, DevOps - Tools, Service Desk                                | 1      | 0             | 0           | 0                 | 1          | 1           |
| alejandra.prenatt@example.com | Alejandra Prenatt        | Operations, Helpdesk, Security, Major All Hands                                                          | 1      | 0             | 0           | 0                 | 1          | 1           |
| alene.rabeck@example.com      | Alene Rabeck             | Operations, Helpdesk, Security, Customer Experience, Major All Hands, Engineering                        | 1      | 0             | 0           | 0                 | 1          | 1           |
| alfonso.griglen@example.com   | Alfonso Griglen          | Security, Major All Hands, Engineering                                                                   | 1      | 0             | 0           | 1                 | 1          | 2           |
|                               |
