%define name	frameworks
%define version	0.3.6
%define release %mkrel 5

Name: 	 	%{name}
Summary: 	Stop-motion animation tool
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://www.polycrystal.org/software/frameworks.html
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=video_section
Name=FrameWorks
Comment=Stop-motion animation tool
Categories=AudioVideo;
EOF

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_datadir}/*.glade

