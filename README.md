# PDhygiene

Scripts to show information about response health

## Installation:

* Clone this repo and `cd` to it
* Create a virtual environment with Python 3: `python3 -m venv venv`
* Activate the virtual environment: `. venv/bin/activate`
* Get the dependencies: `pip install -r requirements.txt`

## Usage:

### Show Escalation Policies where the same person is currently on call at multiple levels:

`python ./hygiene.py pd_api_key`

### Sample Output:

```
Getting Escalation policies... Got 21.

Escalation Policy Backend DBA: Malcolm Reynolds (martin+inara@pagerduty.com) is currently on call at multiple levels:
    Level 1: Mon Oct 28 00:00:00 2019 - Sat Nov  2 00:00:00 2019
    Level 3: Mon Oct 28 06:00:00 2019 - Sat Nov  2 06:00:00 2019

Escalation Policy Backend DBA: Inara Serra (martin+book@pagerduty.com) is currently on call at multiple levels:
    Level 2: Mon Oct 28 00:00:00 2019 - Sat Nov  2 00:00:00 2019
    Level 3: Always on call
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
