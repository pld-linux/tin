%define date 19990927
Summary:	tin News Reader
Summary(de):	tin News-Reader
Summary(fr):	Lecteur de news tin.
Summary(pl):	tin - czytnik newsów
Summary(tr):	Haber okuyucu
Name:		tin
Version:	1.4pre%{date}
Release:	1
Serial:		1
Copyright:	distributable
Group:		Applications/News
Group(pl):	Aplikacje/News
Source:		ftp://ftp.tin.org/pub/news/clients/tin/current/tinpre-1.4-%{date}.tar.bz2
URL:		http://www.tin.org/
BuildRequires:	ncurses-devel
Requires:	ncurses => 4.2-12
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Tin is a full-screen easy to use Netnews reader. It can read news locally
(i.e., /var/spool/news) or remotely (rtin or tin -r option) via a NNTP
(Network News Transport Protocol) server. It will automatically utilize NOV
(News OVerview) style index files if available locally or via the NNTP XOVER
command.
                                                                                
Tin has four separate levels of operation: Group selection level, Group
level, Thread level and Article level. Use the 'h' (help) command to view a
list of the commands available at a particular level.

%description -l de
Tin ist ein Vollbild-Newsreader. Das Programm kann entweder lokal (z.B.
usr/spool/news) oder entfernt (Option 'rtin' bzw. 'tin -r') über einen
NNTP-Server (Network News Transport Protocol) eingesetzt werden.

%description -l fr
Tin est un lecteur de news plein écran facile à utiliser. Il peut lire des
articles localement (i.e. /usr/spool/news) ou à distance ('rtin' ou 'tin -r')
via un serveur NNTP (Network News Transport Protocol).

%description -l pl
Tin jest pe³noekranowym czytnikiem newsów. Umo¿liwia czytanie zarówno z
lokalnych zasobów (np. z katalogu /var/spool/news jak i ze zdalnych
(uruchamiaj±c 'rtin' lub 'tin -r') serwerów NNTP (Network News Transport
Protocol).

%description -l tr
Tin, metin ekranda çalýþan kolay kullanýlýr bir USENET haber okuyucusudur.
Haberleri yerel olarak (/usr/spool/news), ya da bir NNTP sunucusu
aracýlýðýyla uzaktan ('rtin' ya da 'tin -r' seçeneði ile) okuyabilir.

%prep
%setup -q -n tin-%{date}

%build
%configure \
	--enable-color \
	--with-ncurses \
	--with-nov-dir=/var/spool/news \
	--with-spooldir=/var/spool/news \
	--enable-locale \
	--disable-debug

(cd src; make)

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc,%{_bindir},%{_mandir}/man1}

install -s src/tin $RPM_BUILD_ROOT%{_bindir}
ln -sf tin $RPM_BUILD_ROOT%{_bindir}/rtin

install doc/tin.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/tin.defaults $RPM_BUILD_ROOT/etc

echo ".so tin.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rtin.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	{README,MANIFEST,doc/{CHANGES,TODO,DEBUG_REFS,WHATSNEW,*.txt}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,MANIFEST,doc/{CHANGES,TODO,DEBUG_REFS,WHATSNEW,*.txt}}.gz
%verify(not md5 mtime size) %config(noreplace) /etc/tin.defaults
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
