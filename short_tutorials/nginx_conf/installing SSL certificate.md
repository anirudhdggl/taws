# Installing SSL Certificate For Your Website

Most of the time we need to buy an SSL certificate if we have a managed hosting, or if using cloud like AWS use some services like ALB which support those certificates.

These things come with associated costs.

One way to tackle this is by using openssl to create self signed certificates. But with these, most browsers show a warning which is not good for your website's reputation.

To overcome this, we will be using let's encrypt's SSL certificate.

Install the letsencrypt utility on your server using the following command
```
sudo apt-get install letsencrypt -y
```
Then create a new certificate using the following command
```
sudo certbot certonly --standalone --agree-tos --preferred-challenges http -d example.com
```
Once the certificate is generated, we need to make relevant changes in nginx configuration. We will use certbot to that automatically for us
```
sudo apt-get install python3-certbot-nginx -y
```
The above command will install certbot for nginx. We can now run this command to make the changes
```
sudo certbot --nginx --agree-tos --preferred-challenges http -d example.com
```
Reload the nginx configurations and your website will be up with an SSL certificate
```
sudo nginx -s reload
```
