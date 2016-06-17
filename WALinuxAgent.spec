Name     : WALinuxAgent
Version  : 2.1.4
Release  : 6
URL      : https://github.com/Azure/WALinuxAgent/archive/v2.1.4.tar.gz
Source0  : https://github.com/Azure/WALinuxAgent/archive/v2.1.4.tar.gz
Source1  : waagent.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools
Patch1: 0001-Add-Clear-Linux-distro-support.patch

%description
The preferred method of installing the Azure Linux Agent for
CentOS and other RPM-based distributions is to use the RPM packaging.
Platform images in the Azure Gallery will already include the agent
package. This guide is primarily for individuals who would like to
build their own custom packages.

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
Provides: walinuxagent-python

%description python
python components for the WALinuxAgent package.

%prep
%setup -q -n WALinuxAgent-2.1.4
%patch1 -p1

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --lnx-distro=clearlinux
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/waagent.service
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../waagent.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/waagent.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/waagent
%exclude /usr/bin/waagent2.0

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/waagent.service
/usr/lib/systemd/system/multi-user.target.wants/waagent.service
/usr/share/defaults/waagent/waagent.conf

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
