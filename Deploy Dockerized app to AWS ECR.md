
```shell
docker build . -t devqe/node-web-app:latest
docker run -p 49160:8080 -d devqe/node-web-app:latest

# Login to ECR
aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 311965462692.dkr.ecr.ap-southeast-1.amazonaws.com

# Tag the version
docker tag devqe/node-web-app:latest 311965462692.dkr.ecr.ap-southeast-1.amazonaws.com/node:latest

# Upload 
docker push 311965462692.dkr.ecr.ap-southeast-1.amazonaws.com/node:latest
```


```shell
access key id: AKIAURIUXGCSGF4IODSU
secret key: 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
```

Docker image uri: `311965462692.dkr.ecr.ap-southeast-1.amazonaws.com/node:latest`
