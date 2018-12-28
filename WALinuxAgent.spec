#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WALinuxAgent
Version  : 2.2.31
Release  : 67
URL      : https://github.com/Azure/WALinuxAgent/archive/v2.2.31.tar.gz
Source0  : https://github.com/Azure/WALinuxAgent/archive/v2.2.31.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: WALinuxAgent-bin
Requires: WALinuxAgent-python3
Requires: WALinuxAgent-autostart
Requires: WALinuxAgent-config
Requires: WALinuxAgent-data
Requires: WALinuxAgent-license
Requires: WALinuxAgent-python
Requires: distro
BuildRequires : buildreq-distutils3
BuildRequires : distro-python3
Patch1: 0001-Allow-Clear-Linux-detection-in-python2-and-python3.patch

%description
# Microsoft Azure Linux Agent
## Master branch status
Each badge below represents our basic validation tests for an image, which are executed several times each day. These include provisioning, user account, disk, extension and networking scenarios.

%package autostart
Summary: autostart components for the WALinuxAgent package.
Group: Default

%description autostart
autostart components for the WALinuxAgent package.


%package bin
Summary: bin components for the WALinuxAgent package.
Group: Binaries
Requires: WALinuxAgent-data = %{version}-%{release}
Requires: WALinuxAgent-config = %{version}-%{release}
Requires: WALinuxAgent-license = %{version}-%{release}

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


%package license
Summary: license components for the WALinuxAgent package.
Group: Default

%description license
license components for the WALinuxAgent package.


%package python
Summary: python components for the WALinuxAgent package.
Group: Default
Requires: WALinuxAgent-python3 = %{version}-%{release}
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
%setup -q -n WALinuxAgent-2.2.31
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1537800680
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/WALinuxAgent
cp LICENSE.txt %{buildroot}/usr/share/doc/WALinuxAgent/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../waagent.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/waagent.service
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/waagent.service

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/waagent2.0
/usr/bin/waagent

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/waagent.service
/usr/lib/systemd/system/waagent.service

%files data
%defattr(-,root,root,-)
/usr/share/defaults/waagent/waagent.conf

%files license
%defattr(-,root,root,-)
/usr/share/doc/WALinuxAgent/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
