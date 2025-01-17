%define _disable_ld_no_undefined 1

Summary:	X.org driver for generic S3 Cards
Name:		x11-driver-video-s3
Version:	0.7.0
Release:	3
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-s3-%{version}.tar.bz2
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-s3 is the X.org driver for generic S3 Cards.

%prep
%autosetup -n xf86-video-s3-%{version} -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/s3_drv.so
%{_mandir}/man4/s3.*

