#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WALinuxAgent
Version  : 2.2.5
Release  : 30
URL      : https://github.com/Azure/WALinuxAgent/archive/v2.2.5.tar.gz
Source0  : https://github.com/Azure/WALinuxAgent/archive/v2.2.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: WALinuxAgent-bin
Requires: WALinuxAgent-python
Requires: WALinuxAgent-autostart
Requires: WALinuxAgent-config
Requires: WALinuxAgent-data
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
### INTRODUCTION
The Microsoft Azure Linux Agent (waagent) manages Linux & FreeBSD provisioning,
and VM interaction with the Azure Fabric Controller. It provides the following
functionality for Linux and FreeBSD IaaS deployments:

%package autostart
Summary: autostart components for the WALinuxAgent package.
Group: Default

%description autostart
autostart components for the WALinuxAgent package.


%package bin
Summary: bin components for the WALinuxAgent package.
Group: Binaries
Requires: WALinuxAgent-data
Requires: WALinuxAgent-config

%description bin
bin components for the WALinuxAgent package.


%package config
Summary: config components for the WALinuxAgent package.
Group: Default

%description config
config components for the WALinuxAgent package.


%package data
Summary: data components for the WALinuxAgent package.
Group: Data

%description data
data components for the WALinuxAgent package.


%package python
Summary: python components for the WALinuxAgent package.
Group: Default
Provides: walinuxagent-python

%description python
python components for the WALinuxAgent package.


%prep
%setup -q -n WALinuxAgent-2.2.5

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489128688
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489128688
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../waagent.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/waagent.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/waagent.service

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/waagent2.0
%exclude /usr/sbin/waagent
%exclude /usr/sbin/waagent2.0
/usr/bin/waagent

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/waagent.service
/usr/lib/systemd/system/waagent.service

%files data
%defattr(-,root,root,-)
/usr/share/defaults/waagent/waagent.conf

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
