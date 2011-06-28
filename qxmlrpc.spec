Name:           qxmlrpc
Summary:        qxmlrpc
Version:        1
Release:        2
License:        GPLv3
Group:          System/Libraries
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  qt4-devel

%files
%defattr(0755,root,root)
%_libdir/*.a

#--------------------------------------------------------------------

%description
qxmlrpc

%prep
%setup -q

%build
%qmake_qt4
%make 

%install
mkdir -p %buildroot%{_libdir}
cp *.a %buildroot%{_libdir}/

