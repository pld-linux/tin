%define date 981225
Summary:     tin News Reader
Summary(de): tin News-Reader
Summary(fr): Lecteur de news tin.
Summary(pl): tin - czytnik newsów
Summary(tr): Haber okuyucu
Name:        tin
Version:     1.4pre%{date}
Release:     1
Serial:      104%{date}
Copyright:   distributable
Group:       Applications/News
Source:      ftp://ftp.tin.org/pub/news/clients/tin/current/tinpre-1.4-%{date}.tar.bz2
URL:         http://www.tin.org/
BuildRoot:   /tmp/%{name}-%{version}-root

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
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure --prefix=/usr \
	--enable-color \
	--with-ncurses \
	--with-nov-dir=/var/spool/news \
	--with-spooldir=/var/spool/news \
	--enable-locale \
	--disable-debug

(cd src; make)

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc,usr/{bin,man/man1}}

install -s src/tin $RPM_BUILD_ROOT/usr/bin
ln -sf tin $RPM_BUILD_ROOT/usr/bin/rtin

install doc/tin.1 $RPM_BUILD_ROOT/usr/man/man1
install doc/tin.defaults $RPM_BUILD_ROOT/etc

echo ".so tin.1" > $RPM_BUILD_ROOT/usr/man/man1/rtin.1

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README MANIFEST doc/{CHANGES,TODO,DEBUG_REFS,WHATSNEW,*.txt}
%verify(not md5 mtime size) %config(noreplace) /etc/tin.defaults
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Sun Dec 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4pre981225-1]
- added gzipping man pages,
- added using LDFLAGS="-s" to ./configure enviroment.

* Thu Jul 30 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4pre980730-1]
- fixed %verify (not size) on /etc/tin.defaults,
- changed passing $RPM_OPT_FLAGS contents,
- added translation for de, fr, tr (from orginam RH 5.1 spec),
- added pl translation,
- locale support added (counfigure is now called with --enalbe-locale),
- added ULR,
- changet Source URL to ftp.tin.org.

* Mon Jun  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4pre980514-2]
- built against ncurses 4.2 (for RH 5.1).

* Fri May 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4pre980514-1]
- added Serial field which will be calculated as: <major_ver> * 10^9 +
  <minor_ver> + 10^7 + <date>. Current for 1.4pre980514 is
  104980514. <date> = 999999 is reserved for finan version.
  Serial number is added because previouse version released in regular
  distribution have version 1.22 (real version is 1.2pl2)
  This allow slight upgrade to 1.4pre from 1.22,
- added -q %setup parameter,
- added %%{date} macro,
- added using %%{name} macro in Buildroot,
- added %clean section,
- added /etc/tin.defaults %config file,
- tin now is builded from tar.bz2 file,
- added %defattr and %attr macro in %files (require rpm >= 2.4.109).

* Mon Mar 30 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4pre980226-1]
- added CFLAGS="$RPM_OPT_FLAGS" as a make parameter,
- removed Packager field (if you want recompile and redisstrubute this stuff    
  put this field in your own ~/.rpmrc).

* Wed Jan 14 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4pre980105]
- added rtin(1) man page,
- rtin now it is sym link to tin,
- added --disable-debug to configure parameters.
 
* Tue Nov  4 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.4pre971102]
- added %%{PACKAGE_VERSION} in Buildroot,
- added all doc/*.txt docs.

* Fri Sep 12 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.3beta970911]
- changed %attr in %doc,

* Fri Aug 22 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- added %descripion.

* Mon Jul 21 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- added %attr to all %doc (allows build package from non root account),

* Fri Jul 18 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- added macro %version,
- added macros %attr in files,

* Mon Jun 16 1997 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- changed nov-dir and spooldir (configure) to /var/spool/news,
- added Prefix field (packake now is relocatable),
- changed %install section.
