# $Id: asciijump.spec,v 1.19 2003-12-18 22:00:49 undefine Exp $
%define _ver	1.0.2beta
Summary:	(a)sci(i)jump game
Summary(pl):	Skoki narciarskie w ascii
Name:		asciijump
Version:	1.0.2
Release:	0.beta.1
License:	GPL
Group:		Applications/Games
Vendor:		Grzegorz Moskal <g.moskal@opengroup.org>
Source0:	http://otak.k-k.pl/asciijump/tgz/%{name}-%{_ver}.tar.gz
# Source0-md5:	199228bbfb4a16914913fe594b775a6d
URL:		http://asciijump.prv.pl/
BuildRequires:	autoconf
BuildRequires:	conflib-devel
BuildRequires:	ctags
BuildRequires:	slang-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ski jumping in text mode.

%description -l pl
Skoki narciarskie w trybie tekstowym.

%prep
%setup -q -n asciijump-%{_ver}

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README-pl
%attr(2755,root,games) %{_bindir}/asciijump
%attr(2755,root,games) %{_bindir}/aj-server
%attr(775,root,games) %{_var}/games/asciijump
%{_datadir}/asciijump
%{_mandir}/man6/asciijump.6*
%{_desktopdir}/asciijump.desktop
%{_pixmapsdir}/asciijump.png
