Summary:       Package to test yum installing capability.
Name:          yumtestpkg
Version:       0.0.1
Release:       1
Group:         System Environment/Libraries
License:       GPL
URL:           http://labs.ft.com
Source0:       yumtestpkg-0.0.1-1.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Package to test yum installing capability.

%prep
echo "PREP:"
pwd
tar -xvf %{SOURCE0}
#cd ad_sshkey-0.0.1-1.x86_64
cd %{name}-%{version}-%{release}
ls

%build
echo "BUILD:"
pwd
cd %{name}-%{version}-%{release}
#cp ./ad_sshkeys.conf $RPM_BUILD_ROOT/
#cp ./ad_sshkeys_update.sh $RPM_BUILD_ROOT/
#cp ./ldap_expiry_warning.sh $RPM_BUILD_ROOT/
#cp ./ssh-key-from-ldap $RPM_BUILD_ROOT/

%install
pwd
cd %{name}-%{version}-%{release}
mkdir -p $RPM_BUILD_ROOT/tmp
cp ./yumtestpkg-0.0.1.tmp $RPM_BUILD_ROOT/tmp/yumtestpkg-0.0.1.tmp

%post
date +%s >> $RPM_BUILD_ROOT/tmp/yumtestpkg-0.0.1.tmp

%files
%defattr(-,root,root,-)
%{_localtmpdir}/*

%changelog
* Thu Nov 13 2014 Jakub Pazdyga <jakub.pazdyga@ft.com> - 0.0.1-1
- Initial release, just creates a file in /tmp
