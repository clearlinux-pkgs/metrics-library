#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
Name     : metrics-library
Version  : 1.0.198
Release  : 2
URL      : https://github.com/intel/metrics-library/archive/metrics-library-1.0.198/metrics-library-1.0.198.tar.gz
Source0  : https://github.com/intel/metrics-library/archive/metrics-library-1.0.198/metrics-library-1.0.198.tar.gz
Summary  : Metrics Library for Intel(R) Metrics Discovery API
Group    : Development/Tools
License  : MIT
Requires: metrics-library-lib = %{version}-%{release}
Requires: metrics-library-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkgconfig(libdrm)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Intel(R) Metrics Library for MDAPI
## Introduction
This software is a user mode driver helper library that provides access to GPU performance counters.

%package dev
Summary: dev components for the metrics-library package.
Group: Development
Requires: metrics-library-lib = %{version}-%{release}
Provides: metrics-library-devel = %{version}-%{release}
Requires: metrics-library = %{version}-%{release}

%description dev
dev components for the metrics-library package.


%package lib
Summary: lib components for the metrics-library package.
Group: Libraries
Requires: metrics-library-license = %{version}-%{release}

%description lib
lib components for the metrics-library package.


%package license
Summary: license components for the metrics-library package.
Group: Default

%description license
license components for the metrics-library package.


%prep
%setup -q -n metrics-library-metrics-library-1.0.198
cd %{_builddir}/metrics-library-metrics-library-1.0.198

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1749654393
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DCMAKE_BUILD_TYPE=Release  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1749654393
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/metrics-library
cp %{_builddir}/metrics-library-metrics-library-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/metrics-library/d39b22518623f5cfcbca01d6697c60308bc0d68d || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/metrics_library_api_1_0.h
/usr/lib64/libigdml.so
/usr/lib64/libigdml64.so
/usr/lib64/pkgconfig/libigdml.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libigdml.so.1
/usr/lib64/libigdml.so.1.0.198

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/metrics-library/d39b22518623f5cfcbca01d6697c60308bc0d68d
