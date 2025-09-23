# bbbbtool - Lambda Tool

testing new tool

## Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/BharatSharma34/bbbbtool-1758631986865.git
   cd bbbbtool-1758631986865
   ```

2. Add your AWS credentials to GitHub Secrets:
   - Go to Settings → Secrets and variables → Actions
   - Add: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
   - Optionally add: `TOOL_SECRET` for additional security

3. Edit `lambda_function.py` with your tool logic

4. Update `requirements.txt` if you need additional Python packages

5. Push to main branch to auto-deploy to AWS Lambda

## Files

- `lambda_function.py` - Your tool's main code
- `requirements.txt` - Python dependencies
- `.github/workflows/deploy.yml` - Auto-deployment workflow
- `README.md` - This file

## How to Use Your Tool

Once deployed, your Lambda function will be available at:
**Function Name:** `bbbbtool-1758631986865`

### Testing Your Tool

You can test your deployed function using AWS CLI:
```bash
aws lambda invoke \
  --function-name bbbbtool-1758631986865 \
  --payload '{"body": "{\"input_data\": \"test\"}"}' \
  response.json
```

### Adding Your Tool Logic

Replace the `example_function` in `lambda_function.py` with your actual tool code. The Lambda handler will automatically:

1. Parse the incoming request body
2. Find your function
3. Match parameters from the request to your function arguments
4. Call your function and return the result

## Deployment

Every push to the `main` branch automatically:
1. Installs dependencies from `requirements.txt`
2. Packages your code
3. Deploys to AWS Lambda
4. Updates the existing function or creates a new one

## Tool Details

- **Secret Key:** sk-nzdteflcf-mfwk1yp2
- **Created:** 2025-09-23T12:53:08.359Z
- **Runtime:** Python 3.11
- **Timeout:** 60 seconds
- **Memory:** 128 MB

## Support

For issues or questions about this tool, please contact the development team.
