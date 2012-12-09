Name: x11-driver-video-s3
Version: 0.6.5
Release: 2
Summary: X.org driver for generic S3 Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-s3-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-s3 is the X.org driver for generic S3 Cards.

%prep
%setup -qn xf86-video-s3-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/s3_drv.so
%{_mandir}/man4/s3.*



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.5-1
+ Revision: 810703
- version update 0.6.5

* Tue May 15 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.4-1
+ Revision: 798907
- version update 0.6.3

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.6.3-8
+ Revision: 787267
- Rebuild for x11-server 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.6.3-7
+ Revision: 748450
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.3-6
+ Revision: 703685
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.6.3-5
+ Revision: 683583
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.3-4
+ Revision: 671164
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 0.6.3-3mdv2011.0
+ Revision: 595724
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 0.6.3-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 0.6.3-1mdv2010.0
+ Revision: 407721
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 0.6.2-1mdv2010.0
+ Revision: 391891
- update to new version 0.6.2

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.1-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Tue Dec 23 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 0.6.1-1mdv2009.1
+ Revision: 317849
- New version 0.6.1

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.0-3mdv2009.1
+ Revision: 308173
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-2mdv2009.0
+ Revision: 265926
- rebuild early 2009.0 package (before pixel changes)
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.6.0-1mdv2009.0
+ Revision: 194165
- Update to version 0.6.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.5.0-5mdv2008.1
+ Revision: 165589
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.5.0-4mdv2008.1
+ Revision: 156616
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 0.5.0-3mdv2008.1
+ Revision: 154830
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Update to use existing tag xf86-video-s3-0.5.0 and generate patches from
  that point.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 16 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.5.0-2mdv2008.1
+ Revision: 99043
- minor spec cleanup
- build against new xserver (1.4)

* Mon Jun 04 2007 Thierry Vignaud <tv@mandriva.org> 0.5.0-1mdv2008.0
+ Revision: 35125
- new release

