"""
Example: call the Startup Investors API Apify Actor from Python.

Get a free Apify API key at: https://apify.com?fpr=9n7kx3
Set it in a .env file (see .env.example) or export APIFY_API_TOKEN.

The Actor searches a curated database of investor firms (venture capital,
angel, accelerator, private equity, family office, and more). This example
keeps Max_Results small and leaves contacts off so the first run is cheap:
each firm returned is billed, and enabling contacts adds a per-contact fee.
"""

import os

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
if not APIFY_API_TOKEN:
    raise SystemExit(
        "APIFY_API_TOKEN is not set. Copy .env.example to .env and add your key, "
        "or run: export APIFY_API_TOKEN=your_api_key_here"
    )

client = ApifyClient(APIFY_API_TOKEN)

# Inputs are kept small so the first run is inexpensive: a narrow keyword,
# only 3 firms, and contacts off (each firm is billed; contacts cost extra).
run_input = {
    "Firm_Types": ["Venture Capital Investor"],
    "Keyword": "Sequoia",
    "Max_Results": 3,
    "Order_By": "firm_name",
    "Order_Direction": "asc",
    "Include_Contacts": False,  # set True to also pull investor contacts (billed per contact)
}

print(f"Searching investor firms for keyword: {run_input['Keyword']}")
run = client.actor("johnvc/startup-investors-data-scraper").call(run_input=run_input)

if run is None:
    raise SystemExit("The Actor run did not start. Check your API token and inputs.")

items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"\nReturned {len(items)} investor firms.\n")

for i, firm in enumerate(items, start=1):
    name = firm.get("firm_name", "")
    ftype = firm.get("firm_type_id", "")
    location = ", ".join(p for p in (firm.get("firm_city"), firm.get("firm_state"), firm.get("firm_country")) if p)
    website = firm.get("firm_website", "")
    stages = ", ".join(firm.get("firm_stages") or [])
    focus = ", ".join(firm.get("firm_focus") or [])

    print(f"{i}. {name} ({ftype})")
    print(f"   Location: {location}")
    print(f"   Website:  {website}")
    if stages:
        print(f"   Stages:   {stages}")
    if focus:
        print(f"   Focus:    {focus}")

    # When Include_Contacts is True, each firm also has an investor_contacts list.
    contacts = firm.get("investor_contacts") or []
    if contacts:
        print(f"   Contacts: {len(contacts)} (name, title, email when available, LinkedIn)")
    print()
