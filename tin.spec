Summary:	tin News Reader
Summary(de):	tin News-Reader
Summary(fr):	Lecteur de news tin
Summary(pl):	tin - czytnik newsów
Summary(tr):	Haber okuyucu
Name:		tin
Version:	1.5.6
Release:	1
Serial:		2
Copyright:	distributable
Group:		Applications/News
Group(pl):	Aplikacje/News
Source0:	ftp://ftp.tin.org/pub/news/clients/tin/unstable/%{name}-%{version}.tar.bz2
Patch0:		tin-enable_coloring.patch
Patch1:		tin-with_system_pcre.patch
URL:		http://www.tin.org/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pcre-devel
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
ou 'tin
- -r') via un serveur NNTP (Network News Transport Protocol).

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

%build
CPPFLAGS="-DINET6"
LDFLAGS="-s"
CFLAGS="-I/usr/include/ncurses $RPM_OPT_FLAGS"
export CPPFLAGS LDFLAGS CFLAGS
%configure \
	--enable-color \
	--with-ncurses \
	--with-nov-dir=/var/spool/news \
	--with-spooldir=/var/spool/news \
	--enable-locale \
	--disable-debug

%{__make} -C src

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc,%{_bindir},%{_mandir}/man1}

install src/tin $RPM_BUILD_ROOT%{_bindir}
ln -sf tin $RPM_BUILD_ROOT%{_bindir}/rtin

install doc/tin.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/tin.defaults $RPM_BUILD_ROOT%{_sysconfdir}

echo ".so tin.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rtin.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	{README,MANIFEST,doc/{CHANGES,TODO,DEBUG_REFS,WHATSNEW,*.txt}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,MANIFEST,doc/{CHANGES,TODO,DEBUG_REFS,WHATSNEW,*.txt}}.gz
%verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/tin.defaults
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
