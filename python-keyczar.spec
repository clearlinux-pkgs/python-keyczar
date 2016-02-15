#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-keyczar
Version  : 0.715
Release  : 6
URL      : https://pypi.python.org/packages/source/p/python-keyczar/python-keyczar-0.715.tar.gz
Source0  : https://pypi.python.org/packages/source/p/python-keyczar/python-keyczar-0.715.tar.gz
Summary  : Toolkit for safe and simple cryptography
Group    : Development/Tools
License  : Apache-2.0
Requires: python-keyczar-bin
Requires: python-keyczar-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyasn1-python
BuildRequires : pycrypto
BuildRequires : python-dev
BuildRequires : python-keyczar
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

%description python
python components for the python-keyczar package.


%prep
%setup -q -n python-keyczar-0.715

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd tests/keyczar_tests ; python alltests.py ; popd
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keyczart

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
