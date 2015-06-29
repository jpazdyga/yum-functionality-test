#!/bin/bash

isinstalled()
{
	if [ -r /tmp/yumtestpkg-0.0.1.tmp ];
	then
		#echo "installed"
		ii=1
	else
		#echo "not installed"
		ii=0
	fi
}

pkginstall()
{
	/usr/bin/yum -q -d0 -e0 -y install yumtestpkg &> /dev/null
}

pkgremove()
{
	/usr/bin/yum -q -d0 -e0 -y remove yumtestpkg &> /dev/null
}

check()
{
	isinstalled
	if [ $ii -eq 1 ];
	then
		now=`date +%s`
		stamp=`cat /tmp/yumtestpkg-0.0.1.tmp | grep -v yumtestpkg`
		diff=`expr $now - $stamp`
		if [ $diff -gt 300 ];
		then
			echo "Test failed. Old install time found."
		elif [ $diff -le 300 ];
		then
			echo "yumtestpkg was installed $diff secs ago. That's good."
		else
			echo "Some other error occured. Exiting."
			return 1
		fi
	else
		echo "yumtestpkg wasn't installed. Something's wrong with yum install."
		exit 1
	fi
}

isinstalled
if [ $ii -eq 0 ];
then
	pkginstall
	check
	pkgremove
else
	echo "Package already installed."
	pkgremove
	pkginstall
	check
	pkgremove
fi
