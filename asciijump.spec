# $Id: asciijump.spec,v 1.1 2003-02-28 10:48:51 misto Exp $
Summary:	(a)sci(i)jump game.
Name:		asciijump
Version:	0.0.2
Vendor:		Grzegorz Moskal <g.moskal@opengroup.org>
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	conflib-devel
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ski jumping in text mode.

%description -l pl
Skoki narciarskie w trybie tekstowym.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README-pl
%attr(755,root,root) %{_bindir}/asciijump
%{_datadir}/asciijump
%{_applnkdir}/Games/Arcade/asciijump.desktop
%{_pixmapsdir}/asciijump.png
