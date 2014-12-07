%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define debug_package %{nil}

Summary:	Full Qt4 based implementation of XML-RPC protocol
Name:		qxmlrpc
Version:	1
Release:	12
License:	GPLv3+
Group:		System/Libraries
Url:		https://code.google.com/p/qxmlrpc/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		qxmlrpc-1-shared.patch
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtNetwork)
BuildRequires:	pkgconfig(QtXml)

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
%apply_patches

%build
%qmake_qt4 xmlrpc.pro -config static -o Makefile.static
%qmake_qt4 xmlrpc.pro -config shared -o Makefile.shared

%make -f Makefile.static CFLAGS="%{optflags}"
make clean -f Makefile.static
%make -f Makefile.shared

%install
mkdir -p %{buildroot}%{_libdir}
cp -a libqxmlrpc.a %{buildroot}%{_libdir}/
cp -a libqxmlrpc.so* %{buildroot}%{_libdir}/

mkdir -p %{buildroot}%{_includedir}/%{name}/
cp *.h %{buildroot}%{_includedir}/%{name}/

