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
