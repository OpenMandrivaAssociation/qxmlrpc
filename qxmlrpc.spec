%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define debug_package %{nil}

Summary:	Full Qt4 based implementation of XML-RPC protocol
Name:		qxmlrpc
Version:	1
Release:	6
License:	GPLv3+
Group:		System/Libraries
Source0:	%{name}-%{version}.tar.bz2
Patch0:		qxmlrpc-1-shared.patch
BuildRequires:	qt4-devel

%description
Full Qt4 based implementation of XML-RPC protocol.

%package -n %{libname}
Summary:	Full Qt4 based implementation of XML-RPC protocol
Group:		System/Libraries

%description -n %{libname}
Full Qt4 based implementation of XML-RPC protocol.

%files -n %{libname}
%{_libdir}/libqxmlrpc.so.%{major}*

%package -n %{devname}
Summary:	Develompent stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name} < 1-5
Obsoletes:	%{name}-devel < 1-5

%description -n %{devname}
Files needed to build applications based on %{name}.

%files -n %{devname}
%{_libdir}/libqxmlrpc.so
%{_libdir}/libqxmlrpc.a
%{_includedir}/%{name}

%prep
%setup -q
%patch0 -p1

%build
%qmake_qt4 xmlrpc.pro -config static -o Makefile.static
%qmake_qt4 xmlrpc.pro -config shared -o Makefile.shared

%make -f Makefile.static CFLAGS="%{optflags}"
make clean -f Makefile.static
%make -f Makefile.shared

%install
mkdir -p %{buildroot}%{_libdir}
cp libqxmlrpc.a %{buildroot}%{_libdir}/
cp libqxmlrpc.so.%{major}.0.0 %{buildroot}%{_libdir}/

pushd %{buildroot}%{_libdir}
ln -s libqxmlrpc.so.%{major}.0.0 libqxmlrpc.so.%{major}.0
ln -s libqxmlrpc.so.%{major}.0 libqxmlrpc.so.%{major}
ln -s libqxmlrpc.so.%{major} libqxmlrpc.so
popd

mkdir -p %{buildroot}%{_includedir}/%{name}/
cp *.h %{buildroot}%{_includedir}/%{name}/

%changelog
* Thu Sep 06 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1-5
- Completely recreate package according to Mandriva policy

* Fri Jul 13 2012 Sergey A. Sokolov <sokol@mtik.ru> 1-4
- devel package

* Tue Jun 28 2011 Alex Burmashev <burmashev@mandriva.org> 1-2
+ Revision: 687644
- spec fix
- small spec fix
- import qxmlrpc
