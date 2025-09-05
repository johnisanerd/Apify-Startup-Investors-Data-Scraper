"""
Fetch Startup Investors: A Quick Start Example
Scrape the US Startup Investors:  get transactions from both the House and the Senate.
See more at https://apify.com/johnvc/apify-startup-investors-data-scraper?fpr=9n7kx3

This script demonstrates how to use the Startup Investors Scraper Actor
to search Startup Investors and retrieve structured search results.

https://docs.apify.com/api/client/python/docs/overview/introduction


"""

import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input.  In this case we are going to search for Startup Investors in the United States.
run_input = {
    "Firm_Types": ["Venture Capital Investor"],
    "Focus_Areas": ["Artificial Intelligence"],
    "Investment_Stages": [
        "Seed",
        "Series A",
    ],
    "Countries": ["United States"],
    "Keyword": None,
    "Max_Results": 100,
    "Order_By": "created_at",
    "Order_Direction": "desc",
}

# Run the Actor and wait for it to finish
run = client.actor("SVdYzqKOwfJT7shHd").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)