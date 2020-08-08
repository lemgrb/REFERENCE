## Deploy to ec2

Pre: *.pem file (Private key)

1. On [AWS console](https://ap-southeast-1.console.aws.amazon.com/ec2/v2/home?region=ap-southeast-1#Instances:sort=instanceId) just click `Actions > Connect` for instance specific instructions :)
    - Also see: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html
2.`> Login as: ec2-user`
3. Upload .jar file via pscp or Winscp (GUI)
  > pscp -P 22 -i C:\Users\XXX\Downloads\kabtangan.ppk C:\Users\XXX\Desktop\full-stack\api\target\api-0.0.1-SNAPSHOT.jar ec2-user@XXX.compute.amazonaws.com:/home/ec2-user/api-0.0.1-SNAPSHOT.jar
4. Install jdk 11: `sudo amazon-linux-extras install java-openjdk11`
5. Listen 8080 TCP. See https://www.javacodegeeks.com/2019/10/deploy-spring-boot-application-aws-ec2-instance.html


## Install node
1. https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-up-node-on-ec2-instance.html
2. Deploy reactjs
  - https://medium.com/@balghazi/deploying-react-node-js-application-to-amazon-ec2-instance-a89140ab6aab
  
  
## Upload to s3 and enable static hosting

## Enable cors
- https://spring.io/guides/gs/rest-service-cors/

## View process using 8080
- `$ lsof -i :8080`
