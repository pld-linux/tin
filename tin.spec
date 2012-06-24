Summary:	tin News Reader
Summary(de):	tin News-Reader
Summary(fr):	Lecteur de news tin
Summary(pl):	tin - czytnik news�w
Summary(tr):	Haber okuyucu
Name:		tin
Version:	1.5.12
Release:	2
Epoch:		3
License:	distributable
Group:		Applications/News
Source0:	ftp://ftp.tin.org/pub/news/clients/tin/1.5/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-enable_coloring.patch
Patch1:		%{name}-ncurses.patch
Patch2:		%{name}-range.patch
Patch3:		%{name}-charset.patch
URL:		http://www.tin.org/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pcre-devel
BuildRequires:	metamail
Requires:	urlview
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
(z.B. usr/spool/news) oder entfernt (Option 'rtin' bzw. 'tin -r') �ber
einen NNTP-Server (Network News Transport Protocol) eingesetzt werden.

%description -l fr
Tin est un lecteur de news plein �cran facile � utiliser. Il peut lire
des articles localement (i.e. /usr/spool/news) ou � distance ('rtin'
ou 'tin -r') via un serveur NNTP (Network News Transport Protocol).

%description -l pl
Tin jest pe�noekranowym czytnikiem news�w. Umo�liwia czytanie zar�wno
z lokalnych zasob�w (np. z katalogu /var/spool/news jak i ze zdalnych
(uruchamiaj�c 'rtin' lub 'tin -r') serwer�w NNTP (Network News
Transport Protocol).

%description -l tr
Tin, metin ekranda �al��an kolay kullan�l�r bir USENET haber
okuyucusudur. Haberleri yerel olarak (/usr/spool/news), ya da bir NNTP
sunucusu arac�l���yla uzaktan ('rtin' ya da 'tin -r' se�ene�i ile)
okuyabilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
LDFLAGS="%{rpmldflags} -lpcre"
%configure2_13 \
	--enable-nls \
	--enable-color \
	--disable-mime-strict-charset \
	--with-pcre \
	--with-ncurses \
	--with-nov-dir=%{_var}/spool/news \
	--with-spooldir=%{_var}/spool/news \
	--disable-locale \
	--with-gpg=%{_bindir}/gpg \
	--with-mailer=%{_libdir}/sendmail \
	--enable-ipv6 \
	--disable-debug

%{__make} -C src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,etc/tin,%{_bindir},%{_mandir}/man1,%{_mandir}/man5,%{_applnkdir}/Network/News}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__install} doc/tin.defaults $RPM_BUILD_ROOT%{_sysconfdir}/tin
echo ".so tin.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rtin.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/News

rm -f $RPM_BUILD_ROOT%{_bindir}/url_handler.sh

%find_lang %{name}

gzip -9nf README MANIFEST doc/{CHANGES,TODO,DEBUG_REFS,WHATSNEW,*.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/tin/tin.defaults
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
%{_applnkdir}/Network/News/*
