Name: x11-driver-video-s3
Version: 0.5.0
Release: %mkrel 3
Summary: The X.org driver for generic S3 Cards
Group: Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-s3  xorg/drivers/xf86-video-s3
# cd xorg/drivers/xf86-video/s3
# git-archive --format=tar --prefix=xf86-video-s3-0.5.0/ xf86-video-s3-0.5.0 | bzip2 -9 > xf86-video-s3-0.5.0.tar.bz2
########################################################################
Source0: xf86-video-s3-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-s3-0.5.0..origin/mandriva+gpl
Patch1: 0001-renamed-.cvsignore-.gitignore.patch
Patch2: 0002-Was-previously-done-in-monolith-Imakefile-as.patch
Patch3: 0003-Define-VERSION-using-PACKAGE_VERSION.patch
Patch4: 0004-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for generic S3 Cards

%prep
%setup -q -n xf86-video-s3-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/s3_drv.so
