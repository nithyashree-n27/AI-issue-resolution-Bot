# 🤖 AI Issue Resolution Bot (AWS + MS Teams)

An AI-powered automated issue-resolution bot built using **AWS Q, Lambda, S3, Confluence**, and integrated with **Microsoft Teams**.  
The bot reduces response time, improves accuracy, and provides instant answers such as **order tracking information** and **automated solutions for common problems**.

---

##  Project Overview

This project was developed during my internship to automate repetitive support tasks and improve operational efficiency.

### ✔ Key Objectives
- Reduce manual effort in resolving repeated issues  
- Enable instant access to troubleshooting steps stored in Confluence  
- Provide fast and accurate responses through MS Teams  
- Use AWS Q to interpret queries and fetch relevant solutions  

---

##  Architecture Overview

The system uses AWS-managed AI + serverless components:

User (MS Teams)
↓
Microsoft Bot Framework
↓
AWS API Gateway
↓
AWS Lambda (Core logic)
↓
┌───────────────┬────────────────────────────┐
│ AWS Q │ S3 Knowledge Store │
│ (AI Search) │ (Order Data / Issue Files) │
└───────────────┴────────────────────────────┘
↓
Confluence Knowledge Base
---

## 🛠️ Tech Stack

### **AWS Services**
- AWS Q (AI assistant for knowledge search)
- AWS Lambda
- Amazon S3
- API Gateway
- IAM Roles & Policies

### **Other Tools**
- Confluence (knowledge documents)
- Microsoft Teams (chat interface)
- JSON-based knowledge objects

---

##  Features

###  **AI-Powered Query Handling**
- Bot understands user queries using AWS Q  
- Searches Confluence pages automatically  
- Returns accurate troubleshooting steps  

###  **Order Tracking**
- Reads order data from S3  
- Returns order status instantly  

###  **Issue Resolution**
- Provides solutions for frequently occurring tech/operations issues  

###  **MS Teams Interface**
- Complete chatbot experience  
- Instant responses with zero human intervention  

---

##  Screenshots

> Add your screenshots inside a `screenshots/` folder in the repo and update the image names below.

### **Architecture**
![Architecture Diagram](architecture/architecture.png)

### **Bot in MS Teams**
![Bot UI Sample](screenshots/bot-ui.png)

### **Order Tracking Response**
![Order Tracking](screenshots/order-tracking.png)

---

## 📁 Project Structure

AI-issue-resolution-Bot/
│
├── README.md
├── architecture/
│ └── architecture.png
├── screenshots/
│ └── bot-ui.png
│ └── order-tracking.png
├── lambda/
│ └── sample-lambda.py
└── docs/
└── project-report.pdf

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


📊 Results & Impact

 Significantly reduced issue response time

 Automated solutions for repeated problems

 Reduced manual workload of support teams

 Improved accuracy & consistency in responses

 Easy accessibility through MS Teams


👩‍💻 My Contribution

Designed AWS architecture for the bot

Connected AWS Q with Confluence knowledge pages

Built Lambda logic for issue resolution & order lookup

Integrated bot with MS Teams using API Gateway

Created flow diagrams, workflows, and testing reports

