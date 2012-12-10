%define		pre	beta2

Summary:	Powerfull and flexible parametric equalizer
Name:		lv2-eq10q
Version:	2
Release:	2
License:	GPL v3
Group:		Applications/Sound
Source0:	http://download.sourceforge.net/project/eq10q/eq10q-%{version}-%{pre}.tar.gz
# Source0-md5:	a5a6eca6b360201c67e9240673079f4f
URL:		http://eq10q.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	gtkmm-devel
BuildRequires:	lv2-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EQ10Q is an audio plugin over the LV2 standard (http://lv2plug.in)
implementing a powerfull and flexible parametric equalizer.
EQ10Q equalizer plugin includes parametric equalization with diferent
filter types like peaking, HPF, LPF, Shelving and Notch with IIR
algorithms and a nice GUI displaying the equalization curve.

%prep
%setup -qn eq10q-%{version}-%{pre}

# cleanups svn trash
find . -type d -name .svn | xargs rm -rf

# in rpmcflags we trust
%{__sed} -i "s/-O3//" CMakeLists.txt

# fix strange installation dir
%{__sed} -i "s|/usr/local/lib/lv2|%{_libdir}/lv2|g" CMakeLists.txt

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/sapistaEQv2.lv2
%dir %{_libdir}/lv2/sapistaEQv2.lv2/gui
%attr(755,root,root) %{_libdir}/lv2/sapistaEQv2.lv2/*.so
%attr(755,root,root) %{_libdir}/lv2/sapistaEQv2.lv2/gui/*.so
%{_libdir}/lv2/sapistaEQv2.lv2/*.ttl
%{_libdir}/lv2/sapistaEQv2.lv2/gui/combopix
%{_libdir}/lv2/sapistaEQv2.lv2/gui/icons
%{_libdir}/lv2/sapistaEQv2.lv2/gui/knobs

