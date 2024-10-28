#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v20
# autospec commit: f35655a
#
Name     : WALinuxAgent
Version  : 2.11.1.12
Release  : 105
URL      : https://github.com/Azure/WALinuxAgent/archive/v2.11.1.12/WALinuxAgent-2.11.1.12.tar.gz
Source0  : https://github.com/Azure/WALinuxAgent/archive/v2.11.1.12/WALinuxAgent-2.11.1.12.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: WALinuxAgent-autostart = %{version}-%{release}
Requires: WALinuxAgent-license = %{version}-%{release}
Requires: WALinuxAgent-python = %{version}-%{release}
Requires: WALinuxAgent-python3 = %{version}-%{release}
Requires: WALinuxAgent-services = %{version}-%{release}
Requires: pypi(distro)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(distro)
BuildRequires : pypi(pyasn1)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-waagent-error-caused-in-ClearLinuxDeprovisionHan.patch

%description
# Microsoft Azure Linux Agent
## Linux distributions support
Our daily automation tests most of the [Linux distributions supported by Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/endorsed-distros); the Agent can be
used on other distributions as well, but development, testing and support for those are done by the open source community.

%package autostart
Summary: autostart components for the WALinuxAgent package.
Group: Default

%description autostart
autostart components for the WALinuxAgent package.


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
Requires: pypi(distro)
Requires: pypi(pyasn1)

%description python3
python3 components for the WALinuxAgent package.


%package services
Summary: services components for the WALinuxAgent package.
Group: Systemd services
Requires: systemd

%description services
services components for the WALinuxAgent package.


%prep
%setup -q -n WALinuxAgent-2.11.1.12
cd %{_builddir}/WALinuxAgent-2.11.1.12
%patch -P 1 -p1
pushd ..
cp -a WALinuxAgent-2.11.1.12 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727795452
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/WALinuxAgent
cp %{_builddir}/WALinuxAgent-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/WALinuxAgent/861181924d993ee58a17a2c3c3a3faecf895849c || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## Remove excluded files
rm -f %{buildroot}*/usr/bin/waagent2.0
rm -f %{buildroot}*/usr/sbin/waagent
rm -f %{buildroot}*/usr/sbin/waagent2.0
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../waagent.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/waagent.service
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/waagent.service

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/WALinuxAgent/861181924d993ee58a17a2c3c3a3faecf895849c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/waagent.service
