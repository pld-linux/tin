#
#   You can build tin with:
# --define 'domain_name your.domain'
# --define 'default_server default.nntp.server'
#
Summary:	tin News Reader
Summary(de):	tin News-Reader
Summary(fr):	Lecteur de news tin
Summary(pl):	tin - czytnik news�w
Summary(ru):	tin - ��������� ��� ������ ��������������� Usenet
Summary(tr):	Haber okuyucu
Summary(uk):	tin - �������� ��� ������� ������������æ� Usenet
Name:		tin
Version:	1.8.1
Release:	1
Epoch:		5
License:	distributable
Group:		Applications/News
Source0:	ftp://ftp.tin.org/pub/news/clients/tin/v1.8/%{name}-%{version}.tar.bz2
# Source0-md5:	efeecdf72683213d9e705c28de87ea2e
Source1:	%{name}.desktop
Source2:	%{name}.attributes
Patch0:		%{name}-enable_coloring.patch
Patch1:		%{name}-ncurses.patch
Patch2:		%{name}-range.patch
Patch3:		%{name}-charset.patch
URL:		http://www.tin.org/
BuildRequires:	bison
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pcre-devel
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

%description -l ru
Tin - ��� ������� � ������������� ������������� ��������� ��� ������
��������������� Usenet. ��� ����� ������ ��������������� � ���������
(�.�. /var/spool/news) ��� ��������� (rtin ��� ����� tin -r) �� NNTP
(Network News Transport Protocol).

%description -l tr
Tin, metin ekranda �al��an kolay kullan�l�r bir USENET haber
okuyucusudur. Haberleri yerel olarak (/usr/spool/news), ya da bir NNTP
sunucusu arac�l���yla uzaktan ('rtin' ya da 'tin -r' se�ene�i ile)
okuyabilir.

%description -l uk
Tin - �� ������ � ����������Φ ������������ �������� ��� �������
������������æ� Usenet. ���� ������Ѥ ������ ������������æ� �� �
�������ϧ ������ (����� /var/spool/news) ��� � � צ������ϧ (rtin ���
��æ� tin -r) �� NNTP (Network News Transport Protocol).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
LDFLAGS="%{rpmldflags} -lpcre"
%configure2_13 \
	--disable-debug \
	--disable-locale \
	--disable-mime-strict-charset \
	--enable-color \
	--enable-curses \
	--enable-ipv6 \
	--enable-nls \
	--with-gpg=/usr/bin/gpg \
	--with-ispell=/usr/bin/ispell \
	--with-mailer=/usr/lib/sendmail \
	--with-metamail=/usr/bin/metamail \
	--with-ncurses \
	--with-nov-dir=%{_var}/spool/news \
	--with-pcre \
	--with-screen=ncurses \
	--with-spooldir=%{_var}/spool/news \
	%{?domain_name:--with-domain-name=%{domain_name}} \
	%{?default_server:--with-nntp-default-server=%{default_server}}

%{__make} -C src

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,etc/tin,%{_bindir},%{_mandir}/man1,%{_mandir}/man5,%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install doc/tin.defaults $RPM_BUILD_ROOT%{_sysconfdir}/tin/tinrc
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/tin/attributes
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/rtin.1
echo ".so tin.1" > $RPM_BUILD_ROOT%{_mandir}/man1/rtin.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -f $RPM_BUILD_ROOT%{_bindir}/url_handler.sh

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README MANIFEST doc/{CHANGES,TODO,DEBUG_REFS,WHATSNEW,*.txt}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/tinrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/attributes
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/tin.5*
%{_mandir}/man5/mmdf*
%{_desktopdir}/*
