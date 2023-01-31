## Node Web Service
1. Install [nvm](https://nvm.sh)
2. Install node via nvm
3. Create empty repo on github and clone
4. echo "# motornako" >> README.md
5. git init
6. git add README.md
7. git commit -m "first commit"
8. git branch -M main
9. git remote add origin git@github.com:lemgrb/motornako.git
10. git push -u origin main
11. `npm init`
12. `npm i express dotenv body-parser morgan nodemon cors method-override lodash`
15. Install mongodb
16. Install [mongoose](https://mongoosejs.com) `npm i mongoose`
17. Install babel `npm i --save-dev @babel/core @babel/cli @babel/node @babel/preset-env`
20. Setup `.babelrc`
21. Install testing dependencies: `npm i --save-dev jest supertest cross-env`
22. Install jsonwebtoken : `npm i jsonwebtoken bcrypt`
23. Implement GET, POST, PUT, DELETE endpoints.

.babelrc
```json
{
	"presets": [
		"@babel/preset-env"
	]
}
```


## Dockerize

1. `touch Dockerfile`

Dockerfile
```dockerfile
FROM node:18

# Create app directory
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm ci --only=production
COPY . .

# Tell the port number the container should expose (port 3000 of the container)
EXPOSE 3030

CMD ["node","index.js"]
```

.dockerignore
```dockerignore
node_modules
npm-debug.log
```

2. `docker build -t motornako .` where repo=motornako and tag=latest
3. `docker images`
4. `docker run -d --publish 80:3030 motornako`
5. Check container_id: `docker ps`
6. `docker logs <container_id>`
7. Enter the container: `docker exec -it <container id> /bin/bash`
8. `docker kill <container_id>`

## Deploy to AWS ECR on EC2

1. Create IAM user using this [policy](https://gist.github.com/awssimplified/da49577fa48128e1da992dd6ec21085c)
	1. Access Key ID: `xx`
	2. Secret key: `xxxx`
2. In terminal, `aws configure`
3. Log in to ECR `aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin ACCT.dkr.ecr.ap-southeast-1.amazonaws.com`
4. Create ECR repo on aws
5. Tag the version `docker tag motornako:latest ACCT.dkr.ecr.ap-southeast-1.amazonaws.com/motornako:latest`
	1. Push `docker push ACCT.dkr.ecr.ap-southeast-1.amazonaws.com/motornako:latest`
6. Copy image uri: `ACCT.dkr.ecr.ap-southeast-1.amazonaws.com/motornako:latest`
7. Copy image uri: `ACCT.dkr.ecr.ap-southeast-1.amazonaws.com/motornako:latest`
8. Go to Amazon ECS
9. Create Cluster
10. Select EC2 Linux + Networking
11. Configure cluster
	1. Name: motornakoCluster
	2. On demand provisioning
	3. t3a.micro
	4. Under networking, use default VPC
	5. Choose first subnet
	6. Auto-assign public IP: Enabled
	7. Security group: Default
	8. Container instance IAM Role: Create new role
	9. Click `Create` button
12. Click 'Task Definitions'
	1. Create new task definition
	2. Launch type: EC2
	3. Task definition name: motornakoTask
	4. Task role: None
	5. Network mode: default
	6. Task memory: 512mb
	7. CPU: 1 vcpu
	8. Click `Add container`
		9. Container name: motornakoContainer
		10. Image: `ACCT.dkr.ecr.ap-southeast-1.amazonaws.com/motornako:latest`
		11. Port mapping: `80:3030`
	9. Click `Create`
13. Go back to 'Cluster'
	1. Go to Task
	2. Run new task
	3. Launch type: EC2
	4. Task definition: motornakoTask
	5. Cluster: motornakoCluster
	6. Number of task: 1
	7. Click `Run task`
14. Go to EC2
	1. Go to Security Group
	2. Edit inbound rule
	3. Allow port 80 from all ipv4/ipv6 addresses

## Testing

### Unit testing

Guide: https://www.freecodecamp.org/news/how-to-test-in-express-and-mongoose-apps/


### Integration testing


## TODO
1. Put secrets in environment variables: See https://docs.aws.amazon.com/AmazonECS/latest/developerguide/taskdef-envfiles.html
2. Unit testing: mocha, chai, jest
	1. Preconditions
	2. Extenal data
	3. Database Assertions
	4. API Assertions
3. Integration testing: cypress (ui), gauge
4. "Where are the promises?"
5. Disable logs in production
	1. TEST/PROD environment
2. JWT
3. OWASP
4. Setup https esp. sending pssword over HTTPS / SSL!
5. config FILE for switching environments
6. Search and filters!
7. How to call other services?


### MongoDB

+ Show databases `show dbs`
+ Use and create db `use <dbname>`
+ Create collection `db.createCollection('motor')``
+ `show collections`
+ Insert document to collection: `db.motor.insertOne({slug:'honda-click-150i',name:'Honda Click 150i',ddisplacement:'150cc'})`
+ Show all documents in a collection: `db.motor.find()` or `db.getCollection("motor").find({})`

#### Kata
1. `npm i mongoose`



### What i do not know
1. Async await vs promise
2. async? vs sync?
3. Di ko ka relate aning "Eventing"