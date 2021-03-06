#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-keyczar
Version  : 0.716
Release  : 14
URL      : http://pypi.debian.net/python-keyczar/python-keyczar-0.716.tar.gz
Source0  : http://pypi.debian.net/python-keyczar/python-keyczar-0.716.tar.gz
Summary  : Toolkit for safe and simple cryptography
Group    : Development/Tools
License  : Apache-2.0
Requires: python-keyczar-bin
Requires: python-keyczar-python3
Requires: python-keyczar-python
Requires: pyasn1
Requires: pycrypto
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyasn1
BuildRequires : pyasn1-python
BuildRequires : pycrypto
BuildRequires : python-dev
BuildRequires : python-keyczar
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Keyczar is an open source cryptographic toolkit designed to make it easier and safer for developers to use cryptography in their applications. Keyczar supports authentication and encryption with both symmetric and asymmetric keys. Some features of Keyczar include:

%package bin
Summary: bin components for the python-keyczar package.
Group: Binaries

%description bin
bin components for the python-keyczar package.


%package python
Summary: python components for the python-keyczar package.
Group: Default
Requires: python-keyczar-python3

%description python
python components for the python-keyczar package.


%package python3
Summary: python3 components for the python-keyczar package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-keyczar package.


%prep
%setup -q -n python-keyczar-0.716

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517697235
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd tests/keyczar_tests ; python2 alltests.py || : ; popd
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keyczart

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
