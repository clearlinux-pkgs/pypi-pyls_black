#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyls_black
Version  : 0.4.7
Release  : 23
URL      : https://files.pythonhosted.org/packages/5b/be/3295df9635f7059e1229a3d6770284306dd295ea653fba5ce5b278af3d79/pyls-black-0.4.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/5b/be/3295df9635f7059e1229a3d6770284306dd295ea653fba5ce5b278af3d79/pyls-black-0.4.7.tar.gz
Summary  : Black plugin for the Python Language Server
Group    : Development/Tools
License  : MIT
Requires: pypi-pyls_black-license = %{version}-%{release}
Requires: pypi-pyls_black-python = %{version}-%{release}
Requires: pypi-pyls_black-python3 = %{version}-%{release}
Requires: pypi(black)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(black)
BuildRequires : pypi(python_language_server)
BuildRequires : pypi(toml)

%description
# pyls-black
[![PyPI](https://img.shields.io/pypi/v/pyls-black.svg)](https://pypi.org/project/pyls-black/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

%package license
Summary: license components for the pypi-pyls_black package.
Group: Default

%description license
license components for the pypi-pyls_black package.


%package python
Summary: python components for the pypi-pyls_black package.
Group: Default
Requires: pypi-pyls_black-python3 = %{version}-%{release}

%description python
python components for the pypi-pyls_black package.


%package python3
Summary: python3 components for the pypi-pyls_black package.
Group: Default
Requires: python3-core
Provides: pypi(pyls_black)
Requires: pypi(black)
Requires: pypi(python_language_server)
Requires: pypi(toml)

%description python3
python3 components for the pypi-pyls_black package.


%prep
%setup -q -n pyls-black-0.4.7
cd %{_builddir}/pyls-black-0.4.7
pushd ..
cp -a pyls-black-0.4.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656398602
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyls_black
cp %{_builddir}/pyls-black-0.4.7/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pyls_black/7532b3851d1e9508f34ad6b7078cf6389b0d5cf8
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyls_black/7532b3851d1e9508f34ad6b7078cf6389b0d5cf8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
