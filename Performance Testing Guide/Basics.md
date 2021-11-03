## Proxies
1. You may record the requests using Proxies. JMeter for example has "[Test Script Record](http://jmeter.apache.org/usermanual/jmeter_proxy_step_by_step.html))" and [Postman](https://learning.postman.com/docs/sending-requests/capturing-request-data/proxy/) too

## Authentication methods
+ HTTP Basic Authentication
+ HTTP Digest Authentication
+ Session-based Auth
+ Token-Based Authentication
+ One Time Passwords
+ OAuth and OpenID

See this [article]([https://testdriven.io/blog/web-authentication-methods/](https://testdriven.io/blog/web-authentication-methods/)) by testdriven.io

## Distributed testing
Consider:
1. How many user can CPU handle
2. Is there a firewall that limits request
3. Virtual user limit
4. SPAM Guard
5. Single point of entry
6. Protected against DDOS?

### Architecture
`Master -> Server (x N) -> Application under load`
- Servers sends results to master
- All JMeter version should be the same
- All should be the same logical network
- You may host on AWS

### On EC2
+ Run jmeter first on master then servers

Master:

```bash
$ sudo apt update 
$ sudo apt install openjdk-8-jre-headless # check jmeter docs if compatible
$ mkdir jmeter
$ cd jmeter
$ wget https://...apache-jmeter-5.3.tgz
$ tar -xzf apache-jmeter-5.3.tgz
$ ls
$ cd apache-jmeter-5.3/bin
$ sh create-rmi-keystore.sh # -> rmi_keystore.jks
$ # Transfer the files to different server e.g. use sftp cyberduck.io
$ ifconfig # Check public ip and use that to connect from sftp client
$ # Upload the .jmx file
$ # n: non-gui, t: file
$ sh jmeter.sh -n -t sample.jmx -Jserver.rmi.ssl.keystore.file=rmi_keystore.jks -l home/users/linux/jmeter/apache-jmeter-5.0/bin/report.jtl -R18.132.0.1,18.132.0.2
```

Node server instance x N:

```bash
$ sudo apt update
$ sudo apt install openjdk-8-jre-headless
$ mkdir jmeter
$ cd jmeter
$ wget https://...apache-jmeter-5.3.tgz
$ tar -xzf apache-jmeter-5.3.tgz
$ # Transfer rmi_keystore.jks to /bin on this machine using SFTP client
$ sh jmeter-server -Jserver.rmi.ssl.keystore.file=rmi_keystore.jks
```

Resource:
+ [Advanced JMeter](https://www.linkedin.com/learning/advanced-jmeter) 1h only
+ [JMeter Cookbook | Packt (packtpub.com)](https://www.packtpub.com/product/jmeter-cookbook/9781783988280)