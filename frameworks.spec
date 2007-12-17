%define name	frameworks
%define version	0.3.6
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Stop-motion animation tool
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://www.polycrystal.org/software/frameworks.html
License:	GPL
Group:		Video
BuildRequires:	pkgconfig gtk2-devel libglade2.0-devel

%description
Frameworks is designed to capture frames of stop-motion animation (claymation)
in PNG format. Using other software, these frames may be assembled into a
video. Frameworks is designed to work easily with the GIMP Animation Plugin
(GAP).

%prep
%setup -q

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="video_section.png" needs="x11" title="FrameWorks" longtitle="Stop-motion animation tool" section="Multimedia/Video"
EOF

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_menudir}/%name
%{_datadir}/*.glade

