To replicate the Python `boto3.Session` setup in Node.js, you can use the AWS SDK for JavaScript (`aws-sdk` or the newer `@aws-sdk/client-*` modules). Here's how to do it using the legacy `aws-sdk` package:

### Node.js Equivalent Using `aws-sdk`

```javascript
const AWS = require('aws-sdk');

const AWS_ACCESS_KEY = 'your-access-key';
const AWS_SECRET_KEY = 'your-secret-key';
const AWS_REGION = 'your-region';

const session = new AWS.Config({
  accessKeyId: AWS_ACCESS_KEY,
  secretAccessKey: AWS_SECRET_KEY,
  region: AWS_REGION
});
```

### Node.js Equivalent Using Modular `@aws-sdk/client-*`

If you're using the newer modular SDK (recommended for tree-shaking and performance):

```javascript
const { S3Client } = require('@aws-sdk/client-s3');

const AWS_ACCESS_KEY = 'your-access-key';
const AWS_SECRET_KEY = 'your-secret-key';
const AWS_REGION = 'your-region';

const client = new S3Client({
  region: AWS_REGION,
  credentials: {
    accessKeyId: AWS_ACCESS_KEY,
    secretAccessKey: AWS_SECRET_KEY
  }
});
```

> Replace `S3Client` with the appropriate service client (e.g., `DynamoDBClient`, `EC2Client`) depending on what you're using the session for.