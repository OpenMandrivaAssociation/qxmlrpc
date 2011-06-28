%define name    qxmlrpc
%define version 1
%define release 0
%define buildroot %{_tmppath}/%{name}-buildroot

BuildRoot:      %{buildroot}
Summary:        qxmlrpc
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL-3
Group:          Network
Source0:        %{name}-%{version}.tar.bz2

%description
qxmlrpc
%prep
%setup -q
%build
qmake
make 
%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/
cp *.a $RPM_BUILD_ROOT%{_libdir}/
%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(0755,root,root)
%_libdir
