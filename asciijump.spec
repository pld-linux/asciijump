# $Id: asciijump.spec,v 1.7 2003-03-17 15:59:50 adamg Exp $
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
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/games/asciijump

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README-pl
%attr(2750,root,games) %{_bindir}/asciijump
%attr(775,root,games) %{_var}/games/asciijump
%{_datadir}/asciijump
%{_mandir}/man6/asciijump.6.gz
%{_applnkdir}/Games/Arcade/asciijump.desktop
%{_pixmapsdir}/asciijump.png
