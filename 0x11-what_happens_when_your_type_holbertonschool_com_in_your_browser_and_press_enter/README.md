What happens when you type holbertonschool.com in your browser and press Enter
Daniel Urrego
Daniel Urrego

Just now·3 min read




Since I was a child and I used internet explorer. I used to type by myself the full protocol + the subdomain + the domain without anyidea whats going on. Fortunately today we are going to understand what happens when you type any web address in your browser and press Enter, in this case Holberton.
To understand the full package, we are going to start for the domain, for that we need to understand what does mean DNS, so the Domain Name System as know as DNS is the alphabetic translation of an IP address everything in internet is connected through an IP an IP is an unique number which function is identify what device is sending or receiving a request.
In this case as human are bad to remember long number then the DNS provide us the chance to translate long numbers into domain names, for that when we type the domain holberton.com our internal pc tries to find in the DNS record, if the record is not there then the browser as to the ISP to look up into the DNS record and if not find it then the request goes straight to the root domain server.

Once the communication is done and the device find the correct ip then the communication that is used in this case is the TCP/IP.
“The Internet protocol suite provides end-to-end data communication specifying how data should be packetized, addressed, transmitted, routed, and received”
This communication is only established when the firewall allows the traffic. Firewall are a security measure to block devices with malicious attacks, firewall are like police with a serie of paremethers that we can modify. But be careful in case you let allow everything that means that you are vulnerable to cyber-attacks.

HTTPS/SSL is a certificate where we can guaranty that communication between the server and the device is cifrated that means that nobody can get access to the information and in case that somebody can access to the information that person will not able to understand anything due that the information is cifrated therefore only the device who made the request and the server who send the request are able to see the content of the information due that they are the only devices with the private key to unpackage the cifrate code.
Some websites that have several traffic they have to implement a load balancer, the load balancer is the first point of contact between the device and the server and the main task is balace the traffic to the servers trhough an algorith the idea is guarantee that all the server are working with the same demand.
If the website has a dynamic content then the web server should redirect the request to the application server, the application server is the software that constantly are listening for dynamic request that needs an answer provided for an specific software.
A web server is designed — and often optimized — to serve webpages. Therefore, it may not have the resources to run demanding web applications. An application server provides the processing power and memory to run these applications in real-time. It also provides the environment to run specific applications.
https://techterms.com/definition/application_server
Most of these requests need a database,therefore is important to have a dataserver where the application server constantly are request information as querys. Those dataserver need to be setup. Its common have 2 or more servers one as Master and the others as slave, with that we can guaranty that the information always going to be syncronized.