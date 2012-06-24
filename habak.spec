Summary:	"Ha" Background - setting of window manager background image
Summary(pl):	"Ha" Background - program do ustawiania t�a zarz�dcy okien
Name:		habak
Version:	0.2.4
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://lubuska.zapto.org/~hoppke/yellow_brown/%{name}-%{version}.tar.bz2
# Source0-md5:	d3d514780588500a27f326f3a5c14511
URL:		http://lubuska.zapto.org/~hoppke/yellow_brown/
BuildRequires:	imlib2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Habak sets window manager background image. Habak uses layered model.
Lowest layer is completely black screen. On this screen you can put
other objects called habaks. There are 3 kinds of habaks: images,
fonts and internals. Wallpaper is made by combining one or more
habaks. Order of defining habaks in command line is also order of
putting it on stack, so habak which is last on the command line is
drawn over all previous habaks.

%description -l pl
Habak jest programem do ustawiania t�a zarz�dcy okien. Habak u�ywa
modelu warstwowego. Najni�sz� warstw� jest po prostu ca�kiem czarny
ekran. Na tym ekranie mo�na uk�ada� inne obiekty, zwane habakami.
Habaki dzielone s� na 3 rodzaje: pliki graficzne (images), fonty i
"obiekty wbudowane" (internals). Gotow� tapet� tworzy si� nak�adaj�c
na czarny pulpit jeden lub wi�cej habak�w dowolnego typu. Kolejno��
wyst�powania habak�w w linii polece� jest zarazem kolejno�ci�
nak�adania ich na pulpit, czyli habak kt�ry wyst�puje ostatni zostanie
narysowany nad "wcze�niejszymi" habakami.

%prep
%setup -q

%build
%{__make} \
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
%attr(755,root,root) %{_bindir}/*
