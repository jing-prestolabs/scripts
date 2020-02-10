#!/bin/bash

yum -y install wget
wget https://copr.fedorainfracloud.org/coprs/vbatts/bazel/repo/epel-7/vbatts-bazel-epel-7.repo -P /etc/yum.repos.d
yum -y install bazel 
