Summary:	tin News Reader
Summary(de):	tin News-Reader
Summary(fr):	Lecteur de news tin
Summary(pl):	tin - czytnik newsów
Summary(tr):	Haber okuyucu
Name:		tin
Version:	1.5.9
Release:	3
Epoch:		3
License:	Distributable
Group:		Applications/News
Group(de):	Applikationen/News
Group(pl):	Aplikacje/News
Source0:	ftp://ftp.tin.org/pub/news/clients/tin/unstable/snapshots/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-enable_coloring.patch
Patch1:		%{name}-with_system_pcre.patch
Patch2:		%{name}-ncurses.patch
Patch3:		%{name}-range.patch
URL:		http://www.tin.org/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pcre-devel
BuildRequires:	metamail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tin is a full-screen easy to use Netnews reader. It can read news
locally (i.e., /var/spool/news) or remotely (rtin or tin -r option)
via a NNTP (Network News Transport Protocol) server. It will
automatically utilize NOV (News OVerview) style index files if
available locally or via the NNTP XOVER command.

Tin has four separate levels of operation: Group selection level,
Group level, Thread level and Article level. Use the 'h' (help)
command to view a list of the commands available at a particular
level.

%description -l de
Tin ist ein Vollbild-Newsreader. Das Programm kann entweder lokal
(z.B. usr/spool/news) oder entfernt (Option 'rtin' bzw. 'tin -r') über
einen NNTP-Server (Network News Transport Protocol) eingesetzt werden.

%description -l fr
Tin est un lecteur de news plein écran facile à utiliser. Il peut lire
des articles localement (i.e. /usr/spool/news) ou à distance ('rtin'
ou 'tin -r') via un serveur NNTP (Network News Transport Protocol).

%description -l pl
Tin jest pe³noekranowym czytnikiem newsów. Umo¿liwia czytanie zarówno
z lokalnych zasobów (np. z katalogu /var/spool/news jak i ze zdalnych
(uruchamiaj±c 'rtin' lub 'tin -r') serwerów NNTP (Network News
Transport Protocol).

%description -l tr
Tin, metin ekranda çalýþan kolay kullanýlýr bir USENET haber
okuyucusudur. Haberleri yerel olarak (/usr/spool/news), ya da bir NNTP
sunucusu aracýlýðýyla uzaktan ('rtin' ya da 'tin -r' seçeneði ile)
okuyabilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure \
	--enable-nls \
	--enable-color \
	--with-ncurses \
	--with-nov-dir=%{_var}/spool/news \
	--with-spooldir=%{_var}/spool/news \
	--enable-locale \
	--with-gpg=%{_bindir}/gpg \
	--with-mailer=%{_sbindir}/sendmail \
	--enable-ipv6 \
	--disable-debug

%{__make} -C src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,%{_bindir},%{_mandir}/man1,%{_applnkdir}/Network/News}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__install} doc/tin.defaults $RPM_BUILD_ROOT%{_sysconfdir}
echo ".so tin.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rtin.1

%{__install} %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/New

%find_lang %{name}

gzip -9nf README MANIFEST doc/{CHANGES,TODO,DEBUG_REFS,WHATSNEW,*.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/tin.defaults
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%{_applnkdir}/Network/New/*
