# $Id: asciijump.spec,v 1.6 2003-03-17 14:14:13 adamg Exp $
Summary:	(a)sci(i)jump game
Summary(pl):	Skoki narciarskie w ascii
Name:		asciijump
Version:	0.0.6
Release:	1
License:	GPL
Group:		Applications/Games
Vendor:		Grzegorz Moskal <g.moskal@opengroup.org>
Source0:	http://otak.k-k.pl/asciijump/%{name}-%{version}.tar.gz
URL:		http://asciijump.prv.pl/
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
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README-pl
%attr(755,root,root) %{_bindir}/asciijump
%{_datadir}/asciijump
%{_applnkdir}/Games/Arcade/asciijump.desktop
%{_pixmapsdir}/asciijump.png
