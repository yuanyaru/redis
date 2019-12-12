#!/usr/bin/bash

# CentOS7 yum库中ruby的版本支持到 2.0.0，但是gem安装redis需要最低是2.3.0，采用rvm来更新ruby
# 安装curl
yum -y install curl

# 安装rvm
gpg2 --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3
curl -L get.rvm.io | bash -s stable
source /etc/profile.d/rvm.sh
rvm list known
rvm install 2.3.3

# 修改 rvm下载 ruby的源，到 Ruby China 的镜像
gem sources --add https://gems.ruby-china.com/ --remove https://rubygems.org/

# 查看rvm库中已知的ruby版本
rvm list known

# 安装一个ruby版本
rvm install 2.3.3

# 使用一个ruby版本
rvm use 2.3.3

# 设置默认版本
rvm use 2.3.3 --default

# 卸载一个已知版本
# rvm remove 2.0.0

# 查看ruby版本
ruby --version