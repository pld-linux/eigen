%define		_rc	rc1
Summary:	template library for linear algebra
Name:		eigen
Version:	2.0
Release:	0.%{_rc}.1
License:	GPL v2
Group:		Libraries
Source0:	http://download.tuxfamily.org/eigen/%{name}-%{version}-%{_rc}.tar.bz2
# Source0-md5:	4bfeb40641017bc93df024a20c0d0807
URL:		http://eigen.tuxfamily.org/index.php?title=Main_Page
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eigen is a lightweight C++ template library for vector and matrix
math, a.k.a. linear algebra.

%prep
%setup -q -n %{name}2

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_includedir}/eigen2
