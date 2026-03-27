# AI Issue Resolution Bot

A shipped, production-deployed bot that resolves support issues 
automatically — cutting response latency by 50% and eliminating 
manual triage for repeated problems.

Built during my internship at Titan Company Limited (TATA) using 
AWS Q, Lambda, S3, API Gateway, and Microsoft Teams.

---

##  The Problem

Support teams were spending hours manually triaging the same 
repeated issues — order tracking queries, common troubleshooting 
steps, access problems. Every response required a human. 
Response times were slow and inconsistent.

## What I Built

An end-to-end AI bot that plugs into MS Teams, understands 
natural language queries, searches a Confluence knowledge base 
automatically, and returns accurate solutions instantly — 
with zero human intervention.

Key results:
- 50% reduction in issue response latency
- Automated resolution for the top recurring support categories
- Consistent, accurate output across all queries — no human QA needed
 
---

##  How It Works

User sends a message in MS Teams
→ Microsoft Bot Framework routes it to API Gateway
→ AWS Lambda runs the core classification and routing logic
→ AWS Q searches the Confluence knowledge base
→ S3 handles order data lookups
→ Response returned to user in under 3 seconds

The prompt logic behind AWS Q was designed to handle ambiguous 
queries — edge cases that don't fit neatly into one category 
get flagged separately rather than forced into a wrong bucket. 
This was the core iteration challenge: getting consistent, 
high-quality output across messy real-world inputs.
The system uses AWS-managed AI + serverless components:

---

## Tech Stack

- AWS Q — AI-powered knowledge search
- AWS Lambda — core classification and routing logic
- Amazon S3 — order data and knowledge store
- API Gateway — request handling
- Microsoft Teams + Bot Framework — user interface
- Confluence — knowledge base

---

## What I Owned

- Designed the full AWS architecture
- Built and iterated the prompt logic for consistent output quality
- Connected AWS Q with Confluence knowledge pages
- Built Lambda functions for issue resolution and order tracking
- Integrated the bot with MS Teams via API Gateway
- Tested across edge cases until output quality met production standard
  
---

## Repo Structure

architecture/   — system diagrams
screenshot/     — bot in action
lambda.txt      — core Lambda logic

---

##  Sample Lambda Code (for demonstration)

```python
import json
import boto3

s3 = boto3.client("s3")

def lambda_handler(event, context):
    query = event.get("query")
    order_id = event.get("order_id")

    if order_id:
        response = s3.get_object(Bucket="sample-bucket", Key=f"orders/{order_id}.json")
        data = json.loads(response["Body"].read())

        return {
            "statusCode": 200,
            "body": {
                "order_id": order_id,
                "status": data.get("status"),
                "customer": data.get("customer")
            }
        }

    return {
        "statusCode": 200,
        "body": "AI bot processed your query successfully."
    }
)
```
