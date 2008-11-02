Summary:	template library for linear algebra
Name:		eigen
Version:	1.0.5
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://download.tuxfamily.org/eigen/%{name}-%{version}.tar.gz
# Source0-md5:	960d7e5fb6542270eae4d53ca99b607c
URL:		http://eigen.tuxfamily.org/index.php?title=Main_Page
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eigen is a lightweight C++ template library for vector and matrix
math, a.k.a. linear algebra.

%prep
%setup -q -n %{name}

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
%doc LICENSE TODO README
%dir %{_includedir}/eigen
%{_includedir}/eigen/*.h
