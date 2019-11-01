# PDhygiene

Show Escalation Policies where the same person is currently on call at multiple levels

## Installation:

* Clone this repo and `cd` to it
* Create a virtual environment with Python 3: `python3 -m venv venv`
* Activate the virtual environment: `. venv/bin/activate`
* Get the dependencies: `pip install -r requirements.txt`

## Usage:

`python ./hygiene.py pd_api_key`

## Sample Output:

```
Getting Escalation policies... Got 21.

Escalation Policy Backend DBA: Malcolm Reynolds (martin+inara@pagerduty.com) is currently on call at multiple levels:
    Level 1: Mon Oct 28 00:00:00 2019 - Sat Nov  2 00:00:00 2019
    Level 3: Mon Oct 28 06:00:00 2019 - Sat Nov  2 06:00:00 2019

Escalation Policy Backend DBA: Inara Serra (martin+book@pagerduty.com) is currently on call at multiple levels:
    Level 2: Mon Oct 28 00:00:00 2019 - Sat Nov  2 00:00:00 2019
    Level 3: Always on call
```
