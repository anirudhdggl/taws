# Using nginx To Host Multiple Site

_This tutorial covers how you can use nginx to host multiple website from a single ubuntu server_

### Step 1: SSH into the server

If not already created or provisioned, you can create a new ubuntu server (using EC2 or any other cloud service). The SSH into the instance

### Step 2: Prepare the script

Copy the nginx_server.sh file and pase it in a code editor (like VS Code).

Replace all instances all demo-ad.example.com and demo-ad1.example.com with your two websites. You can create more than two websites as well, but this script supports only two websites.

Add more sections to the script if required

### Step 3: Run the script

Once the script is ready and you are SSHed in to the server, either copy pase the commands and run manually or send the entire file to server using scp and execute it.

It will automatically do all the configurations for you.

### Step 4: The DNS

Once everything is configured on the server side, you can point your DNS records to that serer, maybe using ELB's CNAME or the server's public IP

_Feel free to create a PR and contribute to the script if you find something could be enhanced_
