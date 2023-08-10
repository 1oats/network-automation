# Network Scenario

Summary: In this project, I use python to create VLANs across the four access layer switches in Access Closet 1. I then use ansible to automate the creation of user accounts on all device types in the diagram.

---

- SunMSP is a third-party IT installation vendor that partners with and supports networking infrastructures for school districts. SunMSP recently won one of the largest bids in the company’s history to upgrade and maintain the networking equipment for the School District. In past deployments, SunMSP often missed promised delivery dates due to last-minute changes or patches that needed to be made to customers’ devices. The company needs to change its deployment process with the upcoming School District project. 

- You are a new network engineer for SunMSP who was hired to help accelerate the deployment of networking devices into customer environments. The company’s current process to configure new networking switches and routers entails logging into each device manually. Since large-scale deployments could take over a year to roll out into an environment, any configuration changes would take multiple days to push out into the different buildings within the environment. 

- The School District has 20 buildings with 100 closets split between each of the buildings. Each building has several core switches, and the rest are access layer switches. Each access layer switch is uplinked via trunk port to the core through a 10 gigabit Ethernet fiber port.  
You have been asked to create a proof of concept using Python to automate the VLAN configuration within Access Closet 1 that is in the N-CoreA-01 building. <br><br>

Part 1:
Create a separate VLAN for each of the four access layer switches in Access Closet 1 and configure all devices in the “Local” project in the Assessment Lab appropriately.  

1.	User_Network
2.	ACCT_Network
3.	MGMT_Network
4.	IT_Network
<br>
Part 2:
You have been asked to use Ansible to automate the creation of user accounts for the each of the devices in Access Closet 1. Be sure your automated solution uses the user name, password, and access levels listed below:

- Switches: 
  - User name: Local-Admin
  - Password: XXXXXX
  - Access Level: Read/Write (or device equivalent)

- Four Windows desktops on User_Network:
  - User name: DesktopUser1, DesktopUser2, DesktopUser3, DesktopUser4
  - Password: XXXXXX
  - Access Level: Local Admin

- Test boxes on ACCT_Network and MGMT_Network:
  - User name: TestUser1 (ACCT_Network) and TestUser2 (MGMT_Network)
  - Password: XXXXXX
  - Access Level: Local Admin
 

<img src="Access Closet 1 in the N-CoreA-01 (10.10.1.1) network.jpg" alt="Access Closet" width="700" />
<br>
<img src="School District Network Diagram.png" alt="School Network" width="700" />



