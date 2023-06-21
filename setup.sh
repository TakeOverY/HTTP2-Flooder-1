#!/bin/bash

# Hàm hiệu ứng tải
spinner()
{
    local pid=$!
    local delay=0.1
    local spinstr='|/-\'
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " [%c]  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
}

# Hàm hiển thị thông báo cài đặt hoàn tất
loading_message()
{
    printf "\nĐã cài đặt hoàn tất\n"
}

# Kiểm tra hệ điều hành là CentOS hay Ubuntu
if [[ -f /etc/centos-release ]]; then
    echo "Hệ điều hành: CentOS"
    # Cài đặt các gói phụ thuộc cho CentOS
    yum install nodejs -y
    yum install python3-pip -y
    yum install npm -y
elif [[ -f /etc/lsb-release ]]; then
    echo "Hệ điều hành: Ubuntu"
    # Cài đặt các gói phụ thuộc cho Ubuntu
    apt install nodejs -y
    apt install python3-pip -y
    apt install npm -y
else
    echo "Không thể xác định hệ điều hành."
    exit 1
fi

# Cài đặt các gói phụ thuộc chung
pip3 install pystyle

# Tải mã nguồn và cài đặt các gói phụ thuộc khác
cd /root/HTTP2-Flooder
npm i http http2 crypto tls &
spinner

# Hiển thị thông báo cài đặt hoàn tất
loading_message

# Đợi 3 giây
sleep 3

# Mở file TLS.py
python3 TLS.py
