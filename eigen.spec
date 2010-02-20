
Summary:	template library for linear algebra
Name:		eigen
Version:	2.91.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://bitbucket.org/eigen/eigen/get/default.tar.bz2
# Source0-md5:	397a5555a2c0d200cfad32746368ceba
URL:		http://eigen.tuxfamily.org/
BuildRequires:	cmake >= 2.6.2
Obsoletes:	%{name}-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eigen is a C++ template library for linear algebra: vectors, matrices,
and related algorithms. It is:

- Versatile. (See modules and tutorial). Eigen handles, without code
  duplication, and in a completely integrated way: o both fixed-size and
  dynamic-size matrices and vectors. o both dense and sparse (the latter
  is still experimental) matrices and vectors. o both plain
  matrices/vectors and abstract expressions. o both column-major (the
  default) and row-major matrix storage. o both basic matrix/vector
  manipulation and many more advanced, specialized modules providing
  algorithms for linear algebra, geometry, quaternions, or advanced
  array manipulation.
- Fast. (See benchmark). o Expression templates allow to intelligently
  remove temporaries and enable lazy evaluation, when that is
  appropriate -- Eigen takes care of this automatically and handles
  aliasing too in most cases. o Explicit vectorization is performed for
  the SSE (2 and later) and AltiVec instruction sets, with graceful
  fallback to non-vectorized code. Expression templates allow to perform
  these optimizations globally for whole expressions. o With fixed-size
  objects, dynamic memory allocation is avoided, and the loops are
  unrolled when that makes sense. o For large matrices, special
  attention is paid to cache-friendliness.
- Elegant. (See API showcase). The API is extremely clean and
  expressive, thanks to expression templates. Implementing an algorithm
  on top of Eigen feels like just copying pseudocode. You can use
  complex expressions and still rely on Eigen to produce optimized code:
  there is no need for you to manually decompose expressions into small
  steps.
- Compiler-friendy. Eigen has very reasonable compilation times at
  least with GCC, compared to other C++ libraries based on expression
  templates and heavy metaprogramming. Eigen is also standard C++ and
  supports various compilers.

%prep
%setup -q -n %{name}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_CXX_COMPILER_WORKS=1 \
	-DCMAKE_CXX_COMPILER="%{__cc}" \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_pkgconfigdir}
cp build/eigen3.pc $RPM_BUILD_ROOT/%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_includedir}/eigen3
%{_pkgconfigdir}/eigen3.pc
