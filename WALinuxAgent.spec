#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WALinuxAgent
Version  : 2.1.5
Release  : 19
URL      : https://github.com/Azure/WALinuxAgent/archive/v2.1.5.tar.gz
Source0  : https://github.com/Azure/WALinuxAgent/archive/v2.1.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: WALinuxAgent-bin
Requires: WALinuxAgent-python
Requires: WALinuxAgent-config
Requires: WALinuxAgent-data
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools
Patch1: 0001-Add-Clear-Linux-distro-support.patch
Patch2: 0002-Update-resource-disk-handling-for-new-sfdisk.patch
Patch3: 0003-Make-the-majority-of-the-codebase-PEP8-compliant.patch

%description
The preferred method of installing the Azure Linux Agent for
CentOS and other RPM-based distributions is to use the RPM packaging.
Platform images in the Azure Gallery will already include the agent
package. This guide is primarily for individuals who would like to
build their own custom packages.

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
%setup -q -n WALinuxAgent-2.1.5
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export LANG=C
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../waagent.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/waagent.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/waagent2.0
/usr/bin/waagent

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/waagent.service
/usr/lib/systemd/system/waagent.service

%files data
%defattr(-,root,root,-)
/usr/share/defaults/waagent/waagent.conf

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
