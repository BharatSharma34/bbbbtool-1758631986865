import json
import inspect

# Add your tool logic here
def example_function(input_data):
    """
    Replace this with your actual tool function.
    This function will be automatically called by the Lambda handler.
    """
    return {"message": "Hello from bbbbtool!", "input": input_data}

def lambda_handler(event, context):
    try:
        body = event.get("body")
        if isinstance(body, str):
            body = json.loads(body)

        # Find all callable functions except lambda_handler
        funcs = [v for k, v in globals().items() if callable(v) and k != 'lambda_handler']

        if not funcs:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "No callable function found"})
            }

        # Use the last defined function
        func = funcs[-1]
        sig = inspect.signature(func)
        args = {k: body[k] for k in sig.parameters if k in body}

        result = func(**args)
        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }