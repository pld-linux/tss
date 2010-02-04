Summary:	TSS - A Terminal ScreenSaver
Summary(pl.UTF-8):	TSS - Terminal ScreenSaver
Name:		tss
Version:	0.8.2
Release:	1
License:	GPL v2
Group:		Applications/Terminal
Source0:	http://www.pulia.nu/tss/src/%{name}-%{version}.tar.gz
# Source0-md5:	e4223283dd2d7cf564fb81b940c0bdc8
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-asciidir.patch
URL:		http://www.asty.org/cmatrix/
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Terminal ScreenSaver (or tss for short) is an attempt to clone and
enhance FreeBSD's daemon saver.

%description -l pl.UTF-8
Terminal ScreenSaver (w skrócie tss) jest próbą odtworzenia, oraz
ulepszenia daemon saver z FreeBSD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir},%{_bindir}}
install %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a tss_art $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ART_CREDITS README Changelog
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/tss
