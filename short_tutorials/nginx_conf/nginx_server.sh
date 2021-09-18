
# Script to host more than one website on nginx

sudo mkdir /var/www/html/demo-ad.example.com
sudo touch /var/www/html/demo-ad.example.com/index.html
sudo chmod 766 /var/www/html/demo-ad.example.com/index.html
sudo mkdir /var/www/html/demo-ad1.example.com
sudo touch /var/www/html/demo-ad1.example.com/index.html
sudo chmod 766 /var/www/html/demo-ad1.example.com/index.html
sudo echo "<html><body>ad on nginx</body></html>" > /var/www/html/demo-ad.example.com/index.html
sudo echo "<html><body>ad1 on nginx</body></html>" > /var/www/html/demo-ad1.example.com/index.html
sudo chown -R www-data:www-data /var/www/html/demo-ad.example.com
sudo chown -R www-data:www-data /var/www/html/demo-ad1.example.com
sudo rm /etc/nginx/sites-available/demo-ad.example.com.conf
sudo touch /etc/nginx/sites-available/demo-ad.example.com.conf
sudo tee -a /etc/nginx/sites-available/demo-ad.example.com.conf > /dev/null <<EOF
server {
        listen 80;
        listen [::]:80;
        root /var/www/html/demo-ad.example.com;
        index index.html index.htm;
        server_name demo-ad.example.com;
}
EOF
sudo rm /etc/nginx/sites-available/demo-ad1.example.com.conf
sudo touch /etc/nginx/sites-available/demo-ad1.example.com.conf
sudo tee -a /etc/nginx/sites-available/demo-ad1.example.com.conf > /dev/null <<EOF
server {
        listen 80;
        listen [::]:80;
        root /var/www/html/demo-ad1.example.com;
        index index.html index.htm;
        server_name demo-ad1.example.com;

}
EOF
sudo ln -s /etc/nginx/sites-available/demo-ad.example.com.conf /etc/nginx/sites-enabled
sudo ln -s /etc/nginx/sites-available/demo-ad1.example.com.conf /etc/nginx/sites-enabled

sudo nginx -t
sudo nginx -s reload
