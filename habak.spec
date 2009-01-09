Summary:	"Ha" Background - setting of window manager background image
Summary(pl.UTF-8):	"Ha" Background - program do ustawiania tła zarządcy okien
Name:		habak
Version:	0.2.5
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://download.gna.org/fvwm-crystal/habak/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bee5c394989367f7a4c5cb9ec99d307c
URL:		http://fvwm-crystal.org/
Patch0:		%{name}-Makefile.patch
BuildRequires:	imlib2-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel
Provides:       WallpaperChanger
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Habak sets window manager background image. Habak uses layered model.
Lowest layer is completely black screen. On this screen you can put
other objects called habaks. There are 3 kinds of habaks: images,
fonts and internals. Wallpaper is made by combining one or more
habaks. Order of defining habaks in command line is also order of
putting it on stack, so habak which is last on the command line is
drawn over all previous habaks.

%description -l pl.UTF-8
Habak jest programem do ustawiania tła zarządcy okien. Habak używa
modelu warstwowego. Najniższą warstwą jest po prostu całkiem czarny
ekran. Na tym ekranie można układać inne obiekty, zwane habakami.
Habaki dzielone są na 3 rodzaje: pliki graficzne (images), fonty i
"obiekty wbudowane" (internals). Gotową tapetę tworzy się nakładając
na czarny pulpit jeden lub więcej habaków dowolnego typu. Kolejność
występowania habaków w linii poleceń jest zarazem kolejnością
nakładania ich na pulpit, czyli habak który występuje ostatni zostanie
narysowany nad "wcześniejszymi" habakami.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I/usr/X11R6/include -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install habak $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/habak
