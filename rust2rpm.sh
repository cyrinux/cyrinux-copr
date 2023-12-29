#!/bin/sh -x

dnf -y install rust2rpm-helper git
rust2rpm -V -s $1
