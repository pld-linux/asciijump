# $Id: asciijump.spec,v 1.13 2003-07-07 04:23:49 blues Exp $
%define _ver	1.0.1beta
Summary:	(a)sci(i)jump game
Summary(pl):	Skoki narciarskie w ascii
Name:		asciijump
Version:	1.0.1
Release:	0.beta
License:	GPL
Group:		Applications/Games
Vendor:		Grzegorz Moskal <g.moskal@opengroup.org>
# Source0-md5:	d566ac2b38c03d4cf726e49e5fe7eb21
Source0:	http://otak.k-k.pl/asciijump/tgz/%{name}-%{_ver}.tar.gz
URL:		http://asciijump.prv.pl/
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
install -d $RPM_BUILD_ROOT/var/games/asciijump
# get rid of those subversion related directories
# FixMe: replace with find?
# find . -type d -name '\.svn' -exec rm -rf {} \;
rm -rf hills/.svn gfx/.svn
for i in gfx/*; do 
	rm -rf $i/.svn
done
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README-pl
%attr(2750,root,games) %{_bindir}/asciijump
%attr(2750,root,games) %{_bindir}/aj-server
%attr(775,root,games) %{_var}/games/asciijump
%{_datadir}/asciijump
%{_mandir}/man6/asciijump.6*
%{_applnkdir}/Games/Arcade/asciijump.desktop
%{_pixmapsdir}/asciijump.png
