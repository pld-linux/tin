#
#   You can build tin with:
# --define 'domain_name your.domain'
# --define 'default_server default.nntp.server'
#
Summary:	tin News Reader
Summary(de.UTF-8):	tin News-Reader
Summary(fr.UTF-8):	Lecteur de news tin
Summary(pl.UTF-8):	tin - czytnik newsów
Summary(ru.UTF-8):	tin - программа для чтения телеконференций Usenet
Summary(tr.UTF-8):	Haber okuyucu
Summary(uk.UTF-8):	tin - програма для читання телеконференцій Usenet
Name:		tin
Version:	1.9.4
Release:	4
Epoch:		5
License:	distributable
Group:		Applications/News
Source0:	ftp://ftp.tin.org/pub/news/clients/tin/v1.9/%{name}-%{version}.tar.gz
# Source0-md5:	21b02faf65bb523ce1ee58d4dfbc77fa
Source1:	%{name}.desktop
Source2:	%{name}.attributes
Patch0:		%{name}-enable_coloring.patch
Patch1:		%{name}-ncurses.patch
Patch2:		%{name}-range.patch
Patch3:		%{name}-charset.patch
URL:		http://www.tin.org/
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pcre-devel
BuildRequires:	uudeview-devel
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

%description -l de.UTF-8
Tin ist ein Vollbild-Newsreader. Das Programm kann entweder lokal
(z.B. usr/spool/news) oder entfernt (Option 'rtin' bzw. 'tin -r') über
einen NNTP-Server (Network News Transport Protocol) eingesetzt werden.

%description -l fr.UTF-8
Tin est un lecteur de news plein écran facile à utiliser. Il peut lire
des articles localement (i.e. /usr/spool/news) ou à distance ('rtin'
ou 'tin -r') via un serveur NNTP (Network News Transport Protocol).

%description -l pl.UTF-8
Tin jest pełnoekranowym czytnikiem newsów. Umożliwia czytanie zarówno
z lokalnych zasobów (np. z katalogu /var/spool/news jak i ze zdalnych
(uruchamiając 'rtin' lub 'tin -r') serwerów NNTP (Network News
Transport Protocol).

%description -l ru.UTF-8
Tin - это простая в использовании полноэкранная программа для чтения
телеконференций Usenet. Она может читать телеконференции с локальной
(т.е. /var/spool/news) или удаленной (rtin или опция tin -r) по NNTP
(Network News Transport Protocol).

%description -l tr.UTF-8
Tin, metin ekranda çalışan kolay kullanılır bir USENET haber
okuyucusudur. Haberleri yerel olarak (/usr/spool/news), ya da bir NNTP
sunucusu aracılığıyla uzaktan ('rtin' ya da 'tin -r' seçeneği ile)
okuyabilir.

%description -l uk.UTF-8
Tin - це проста у використанні повноекранна програма для читання
телеконференцій Usenet. Вона дозволяє читати телеконференції як з
локальної машини (тобто /var/spool/news) так і з віддаленої (rtin або
опція tin -r) по NNTP (Network News Transport Protocol).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
LDFLAGS="%{rpmldflags}"
%configure2_13 \
	--disable-debug \
	--enable-color \
	--enable-curses \
	--enable-ipv6 \
	--enable-nls \
	--with-gpg=%{_bindir}/gpg \
	--with-ispell=%{_bindir}/ispell \
	--with-mailer=/usr/lib/sendmail \
	--with-metamail=%{_bindir}/metamail \
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

# file conflict mmdf between mutt and tin
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/mmdf.5*

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
%{_desktopdir}/*.desktop
