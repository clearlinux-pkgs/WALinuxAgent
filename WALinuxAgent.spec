#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WALinuxAgent
Version  : 2.2.25
Release  : 55
URL      : https://github.com/Azure/WALinuxAgent/archive/v2.2.25.tar.gz
Source0  : https://github.com/Azure/WALinuxAgent/archive/v2.2.25.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: WALinuxAgent-python3
Requires: WALinuxAgent-autostart
Requires: WALinuxAgent-config
Requires: WALinuxAgent-bin
Requires: WALinuxAgent-python
Requires: distro
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
### INTRODUCTION
The Microsoft Azure Linux Agent (waagent) manages Linux & BSD provisioning,
and VM interaction with the Azure Fabric Controller. It provides the following
functionality for Linux and BSD IaaS deployments:

%package autostart
Summary: autostart components for the WALinuxAgent package.
Group: Default

%description autostart
autostart components for the WALinuxAgent package.


%package bin
Summary: bin components for the WALinuxAgent package.
Group: Binaries
Requires: WALinuxAgent-config

%description bin
bin components for the WALinuxAgent package.


%package config
Summary: config components for the WALinuxAgent package.
Group: Default

%description config
config components for the WALinuxAgent package.


%package python
Summary: python components for the WALinuxAgent package.
Group: Default
Requires: WALinuxAgent-python3
Provides: walinuxagent-python

%description python
python components for the WALinuxAgent package.


%package python3
Summary: python3 components for the WALinuxAgent package.
Group: Default
Requires: python3-core

%description python3
python3 components for the WALinuxAgent package.


%prep
%setup -q -n WALinuxAgent-2.2.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526505933
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
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
%exclude /usr/sbin/waagent
%exclude /usr/sbin/waagent2.0

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/waagent.service

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
