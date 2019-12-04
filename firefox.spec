# TODO:
# - consider --enable-libproxy
# - do something with *.rdf file, there if file conflict with other lang packages
#
# Conditional build:
%bcond_with	tests		# enable tests (whatever they check)
%bcond_without	kerberos	# disable krb5 support
%bcond_without	official	# official Firefox branding
%bcond_with	lto		# build with link time optimization
%bcond_with	pgo		# PGO-enabled build (requires working $DISPLAY == :100)
%bcond_without	geckodriver	# WebDriver
%bcond_without	gold		# use default linker instead of gold
# - disabled shared_js - https://bugzilla.mozilla.org/show_bug.cgi?id=1039964
%bcond_with	shared_js	# shared libmozjs library [broken]
%bcond_without	system_icu	# build without system ICU
%bcond_with	system_cairo	# build with system cairo (not supported in 60.0)
%bcond_with	system_libvpx	# build with system libvpx (67.0 does not build with libvpx 1.8)
%bcond_without	clang		# build using Clang/LLVM
%bcond_with	legacy_exts	# build with legacy extensions support

%if %{with lto}
%define		with_clang	1
%undefine	with_gold
%endif

# On updating version, grab CVE links from:
# https://www.mozilla.org/security/known-vulnerabilities/firefox.html
# Release Notes:
# https://developer.mozilla.org/en-US/Firefox/Releases
# UPDATING TRANSLATIONS:
%if 0
rm -vf *.xpi
../builder -g firefox-languages.spec
V=53.0
U=http://releases.mozilla.org/pub/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

# The actual sqlite version (see RHBZ#480989):
%define		sqlite_build_version %(pkg-config --silence-errors --modversion sqlite3 2>/dev/null || echo ERROR)

%define		nspr_ver	4.23
%define		nss_ver		3.47.1

Summary:	Firefox web browser
Summary(hu.UTF-8):	Firefox web böngésző
Summary(pl.UTF-8):	Firefox - przeglądarka WWW
Name:		firefox
Version:	71.0
Release:	1
License:	MPL v2.0
Group:		X11/Applications/Networking
Source0:	http://releases.mozilla.org/pub/firefox/releases/%{version}/source/firefox-%{version}.source.tar.xz
# Source0-md5:	a611a03c08703c665f5216e227a0adce
Source3:	%{name}.desktop
Source4:	%{name}.sh
Source5:	vendor.js
Source6:	vendor-ac.js
Source100:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source100-md5:	3a0eb1c100f25573cfb7c32e4c4bf368
Source101:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source101-md5:	add5955d3640833dd495accdd42f5203
Source102:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source102-md5:	826e03e0ae75ae6fa7b48299ccab211b
Source103:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source103-md5:	0e69ecfe438ff0a626cf28581bcdf6ec
Source104:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source104-md5:	f4e839635f6b7678794d5a5083781f13
Source105:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source105-md5:	3b7f958ae6f5a3c1b3e2f44f2910e93a
Source106:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source106-md5:	7d855fbd637a6d43195c19a23206206c
Source107:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source107-md5:	d71d94226db91e2f5e5e5f00d74782e4
Source108:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bn.xpi
# Source108-md5:	d546ff654c19b3ab9c5bb57389965543
Source109:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source109-md5:	bc733448f7949a132bdfb899ba83cd41
Source110:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source110-md5:	352f12543202b0618d7c5aadedc1361e
Source111:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source111-md5:	bbe841a0329f8d58b057c57f32fe0324
Source112:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cak.xpi
# Source112-md5:	05be735533fb22b017771a046998f40a
Source113:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source113-md5:	3180cf3a5484573e8f6cdc38496b94bc
Source114:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source114-md5:	77e8d8c06deb116f17d57a88652b1194
Source115:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source115-md5:	9b0f7242428b4c915322f087702c2ac3
Source116:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source116-md5:	2362593eba69e14535986b7b82d5869c
Source117:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source117-md5:	2fac4ae4fe9eb5e7da867d56b365f5b2
Source118:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source118-md5:	d33df26a4f8ce836cef22ead5d1fb949
Source119:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-CA.xpi
# Source119-md5:	9014858ac9a79d2acc4a47e223ca154d
Source120:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source120-md5:	0000bdfea996f6b0ec69014f0b3ee6c2
Source121:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source121-md5:	b5ff5a33465e4ee5838baa33a238e3d5
Source122:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source122-md5:	875c4b70de5c0ce302f126c188aa2276
Source123:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source123-md5:	b971e5611d300e8cc1b0ba9b8f64e676
Source124:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source124-md5:	c84a49d90e7877f38d29df322b6ad915
Source125:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source125-md5:	c84df0f60045954b571b476265807a9e
Source126:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source126-md5:	06f5ae27c57776e5322aefd1384f94b3
Source127:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source127-md5:	79dd85f9241feaae08c6146ad9fb188e
Source128:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source128-md5:	d8af61a6d314e3164ce94e6a7e973171
Source129:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source129-md5:	9ba984cec80a01214d72f2191573e925
Source130:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source130-md5:	54e836c6b7ccd4eb1c5e9f52240671a5
Source131:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source131-md5:	1db7653b53296099c6b154e3303fdd93
Source132:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source132-md5:	dc847990362e83197a5979358149e17e
Source133:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source133-md5:	1898dc42b8302e282cef4dff3fdb3260
Source134:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source134-md5:	3e4fa2896a0e71d661f0135226f2a16e
Source135:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source135-md5:	cc726cc4b6d4b236b631e65d260567f0
Source136:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source136-md5:	7f9e5f3e8f86886b1c593c4ff558f4ed
Source137:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gn.xpi
# Source137-md5:	481c516386bd06c7062cceef1da53668
Source138:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source138-md5:	fc23bb1fc1855cf14d97de394c09a960
Source139:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source139-md5:	9338a9bbe52972f64c9828a3a7917e90
Source140:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source140-md5:	7bbf0569b65fe6a27975d78ebb5f80d4
Source141:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source141-md5:	a12ee8583bafed2aee59bc8a9a63f0b8
Source142:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source142-md5:	49b02390efb1acc9a2e5f7d4e902f616
Source143:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source143-md5:	b18d4eaf32b37f12c1a8cc161a8bb62b
Source144:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source144-md5:	0738f9351ad55be53a949628f38d61a3
Source145:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ia.xpi
# Source145-md5:	cd6984797ebe9f28c7d717ea7287faca
Source146:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source146-md5:	e83da120066cbfbe1fe1fcefca6fd287
Source147:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source147-md5:	b917f17c1266f57976588ed31a735b78
Source148:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source148-md5:	f1c60cbd73258fc95e367edcb34c82e8
Source149:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source149-md5:	b139d6d8b12f2e8c86cdeb1437e1aabd
Source150:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ka.xpi
# Source150-md5:	a4255462d1227a2a21175d9c9a6af16d
Source151:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/kab.xpi
# Source151-md5:	777dd231601c58de318787a6fd81e076
Source152:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source152-md5:	5bd163b1d909454ec5df9099d2323cc3
Source153:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source153-md5:	d2167dc9fc0a3998e09f0ddd98ef0739
Source154:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source154-md5:	aedafe2cc39ab5942c54af13ff21e272
Source155:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source155-md5:	978ba791a5357bf94fda7de30f052596
Source156:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source156-md5:	954c14e47125d1359ef9a9e3c1248702
Source157:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source157-md5:	cc904c9db5920c5f206e992c114ec953
Source158:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source158-md5:	8e37bc96fa0121c4710e70f6b9e7b548
Source159:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source159-md5:	70844767890e92e7430bd7f9f446177f
Source160:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source160-md5:	ae596c803c8971f599fd38cc4fffa7e8
Source161:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source161-md5:	12695ae755908111f2ad0b79c5c8ee57
Source162:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/my.xpi
# Source162-md5:	0b6009cf698a41b1a68e72e59fecda94
Source163:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source163-md5:	1dc4a0ef82dda5ad7ab634b8d58fc04b
Source164:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ne-NP.xpi
# Source164-md5:	9e98ec02e03b52572e913bd7d8f4c270
Source165:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source165-md5:	33c303f19f654d3d1bdc0cc9e72cf449
Source166:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source166-md5:	f94e54a245681253267d5ca4edb79f45
Source167:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/oc.xpi
# Source167-md5:	839d168dc33df87a0ef4a31fe42ceffe
Source168:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source168-md5:	137dd62c1eec82edf1dba0a2eeadd771
Source169:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source169-md5:	1108509a005600739951a3f893a15a37
Source170:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source170-md5:	2c54f307918ced2bcc4658e35aeb916c
Source171:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source171-md5:	d0ebe33f13ca29de2c88d498a58002d6
Source172:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source172-md5:	88f57f1fbbb42cdc252c39f3249a1b7e
Source173:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source173-md5:	48406ff729d5c21d593002dfda41b34e
Source174:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source174-md5:	2c2a9a5f1f6bef464b943a0a493f3d05
Source175:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source175-md5:	277d02425cf45fad6036a9899dc9d10e
Source176:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source176-md5:	32eeeea2dbc94ec0df343018d65b0733
Source177:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source177-md5:	ea9cd6229b8ce3653b74c11bccc3cf97
Source178:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source178-md5:	dda675eecd3b79ee661e63e0dcaa8a9f
Source179:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source179-md5:	9e1f9acab3900599b7eaf9685b113c15
Source180:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source180-md5:	1a13f704accdd54bf619e2637b722fda
Source181:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source181-md5:	11b5facc6c138f9b24e4c63f5c4163eb
Source182:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source182-md5:	1b527bffc5300fbeb481fc5db5f27d80
Source183:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source183-md5:	0a267ae58cabd4f12c62ae15e70e221f
Source184:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source184-md5:	b19c9378687b7bdcd18a97072db19afd
Source185:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source185-md5:	5ac0471a1eed9685fd73dee74235d669
Source186:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source186-md5:	6ba4a7dfdac71cd83cd40a671deb9b6a
Source187:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ur.xpi
# Source187-md5:	9f7f4ef2e55ac76cd910e53d85a4489f
Source188:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/uz.xpi
# Source188-md5:	4d6191e19aa6668b7411ede6d81714e6
Source189:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source189-md5:	58f5632cdbf149c414dcdb7f4597e889
Source190:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source190-md5:	6bcbfadfa3aeb0d2859e9e3a2ecda01b
Source191:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source191-md5:	40da1fce07715721fafb67d9f1498ded
Source192:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source192-md5:	2d2f678eaf77460c841782aae12fcebc

Patch4:		%{name}-prefs.patch
Patch5:		%{name}-pld-bookmarks.patch
Patch6:		%{name}-no-subshell.patch
Patch7:		%{name}-middle_click_paste.patch
Patch8:		%{name}-system-virtualenv.patch
Patch9:		%{name}-Disable-Firefox-Health-Report.patch
Patch10:	system-cairo.patch
URL:		https://www.mozilla.org/firefox/
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf2_13
BuildRequires:	automake
%{?with_gold:BuildRequires:	binutils >= 3:2.20.51.0.7}
BuildRequires:	bzip2-devel
%{?with_system_cairo:BuildRequires:	cairo-devel >= 1.10.2-5}
BuildRequires:	cargo >= 1.32.0
%{?with_clang:BuildRequires:	clang}
BuildRequires:	clang-devel >= 3.9.0
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	fontconfig-devel >= 1:2.7.0
BuildRequires:	freetype-devel >= 1:2.1.8
%{!?with_clang:BuildRequires:	gcc-c++ >= 6:4.4}
BuildRequires:	glib2-devel >= 1:2.22
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk+3-devel >= 3.4.0
%{?with_kerberos:BuildRequires:	heimdal-devel >= 0.7.1}
BuildRequires:	libIDL-devel >= 0.8.0
BuildRequires:	libatomic-devel
# DECnet (dnprogs.spec), not dummy net (libdnet.spec)
#BuildRequires:	libdnet-devel
BuildRequires:	libevent-devel >= 1.4.7
# standalone libffi 3.0.9 or gcc's from 4.5(?)+
BuildRequires:	libffi-devel >= 6:3.0.9
%{?with_system_icu:BuildRequires:	libicu-devel >= 63.1}
# requires libjpeg-turbo implementing at least libjpeg 6b API
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng(APNG)-devel >= 0.10
BuildRequires:	libpng-devel >= 2:1.6.35
BuildRequires:	libstdc++-devel >= 6:4.4
BuildRequires:	libxcb-devel
%{?with_system_libvpx:BuildRequires:	libvpx-devel >= 1.7.0}
BuildRequires:	libwebp-devel >= 1.0.2
%{?with_clang:BuildRequires:	lld}
BuildRequires:	llvm-devel >= 3.9.0
# or --disable-nodejs ?
BuildRequires:	nodejs >= 8.11
BuildRequires:	nspr-devel >= 1:%{nspr_ver}
BuildRequires:	nss-devel >= 1:%{nss_ver}
BuildRequires:	pango-devel >= 1:1.22.0
BuildRequires:	pixman-devel >= 0.19.2
BuildRequires:	perl-modules >= 5.004
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	pkgconfig(libffi) >= 3.0.9
BuildRequires:	pulseaudio-devel
BuildRequires:	python-modules >= 1:2.5
%{?with_pgo:BuildRequires:	python-modules-sqlite}
BuildRequires:	python-simplejson
BuildRequires:	python-virtualenv >= 15
BuildRequires:	readline-devel
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	rust >= 1.32.0
BuildRequires:	rust-cbindgen >= 0.9.0
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3.29.0
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXt-devel
%{?with_pgo:BuildRequires:	xorg-xserver-Xvfb}
%ifarch %{x8664}
BuildRequires:	yasm >= 1.0.1
%endif
BuildRequires:	unzip
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.2.3
BuildConflicts:	%{name}-devel < %{version}
Requires(post):	mktemp >= 1.5-18
Requires:	browser-plugins >= 2.0
%{?with_system_cairo:Requires:	cairo >= 1.10.2-5}
Requires:	dbus-glib >= 0.60
Requires:	desktop-file-utils
Requires:	fontconfig-libs >= 1:2.7.0
Requires:	glib2 >= 1:2.22
Requires:	gtk+2 >= 2:2.18.0
Requires:	gtk+3 >= 3.4.0
Requires:	hicolor-icon-theme
Requires:	libjpeg-turbo
Requires:	libpng >= 2:1.6.35
Requires:	libpng(APNG) >= 0.10
%{?with_system_libvpx:Requires:	libvpx >= 1.7.0}
Requires:	myspell-common
Requires:	nspr >= 1:%{nspr_ver}
Requires:	nss >= 1:%{nss_ver}
Requires:	pango >= 1:1.22.0
Requires:	pixman >= 0.19.2
Requires:	sqlite3 >= %{sqlite_build_version}
Requires:	startup-notification >= 0.8
Provides:	xulrunner-libs = 2:%{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	firefox-devel
Obsoletes:	firefox-lang-as < 68.0-1
Obsoletes:	firefox-lang-en_ZA < 68.0-1
Obsoletes:	firefox-lang-mai < 68.0-1
Obsoletes:	firefox-lang-ml < 68.0-1
Obsoletes:	firefox-lang-or < 68.0-1
Obsoletes:	firefox-libs
Obsoletes:	iceweasel
Obsoletes:	iceweasel-libs
Obsoletes:	mozilla-firebird
Obsoletes:	mozilla-firefox
Obsoletes:	mozilla-firefox-lang-en < 2.0.0.8-3
Obsoletes:	mozilla-firefox-libs
Obsoletes:	xulrunner
Obsoletes:	xulrunner-gnome
Obsoletes:	xulrunner-libs < 42
Conflicts:	firefox-lang-resources < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_cpp		-D_FORTIFY_SOURCE=[0-9]+

%if %{with clang}
%define		filterout		-fvar-tracking-assignments
%else
%define		filterout		-Werror=format-security
%endif

# don't satisfy other packages
%define		_noautoprovfiles	%{_libdir}/%{name}

# and as we don't provide them, don't require either
%define		_noautoreq	liblgpllibs.so libmozavcodec.so libmozavutil.so libmozgtk.so libmozjs.so libmozsandbox.so libmozwayland.so libxul.so

# 67.0 libxul.so: debugedit: canonicalization unexpectedly shrank by one character
%define		_enable_debug_packages	0

%description
Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%description -l hu.UTF-8
Firefox egy nyílt forrású webböngésző, hatékonyságra és
hordozhatóságra tervezve.

%description -l pl.UTF-8
Firefox jest przeglądarką WWW rozpowszechnianą zgodnie z ideami
ruchu otwartego oprogramowania oraz tworzoną z myślą o zgodności ze
standardami, wydajnością i przenośnością.

%package -n gmp-api
Summary:	GeckoMediaPlugins API header files
Summary(pl.UTF-8):	Pliki nagłówkowe API GeckoMediaPlugins
Group:		Development/Libraries
URL:		https://wiki.mozilla.org/GeckoMediaPlugins
# actually C++ compiler; STL is not even used
Requires:	libstdc++-devel

%description -n gmp-api
GeckoMediaPlugins API header files.

%description -n gmp-api -l pl.UTF-8
Pliki nagłówkowe API GeckoMediaPlugins.

%package lang-ach
Summary:	Acoli resources for Firefox
Summary(pl.UTF-8):	Pliki językowe aczoli dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ach
Obsoletes:	mozilla-firefox-lang-ach
BuildArch:	noarch

%description lang-ach
Acoli resources for Firefox.

%description lang-ach -l pl.UTF-8
Pliki językowe aczoli dla Firefoksa.

%package lang-af
Summary:	Afrikaans resources for Firefox
Summary(pl.UTF-8):	Afrykanerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-af
Obsoletes:	mozilla-firefox-lang-af
BuildArch:	noarch

%description lang-af
Afrikaans resources for Firefox.

%description lang-af -l pl.UTF-8
Afrykanerskie pliki językowe dla Firefoksa.

%package lang-an
Summary:	Aragonese resources for Firefox
Summary(pl.UTF-8):	Aragońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-an
Obsoletes:	mozilla-firefox-lang-an
BuildArch:	noarch

%description lang-an
Aragonese resources for Firefox.

%description lang-an -l pl.UTF-8
Aragońskie pliki językowe dla Firefoksa.

%package lang-ar
Summary:	Arabic resources for Firefox
Summary(pl.UTF-8):	Arabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ar
Obsoletes:	mozilla-firefox-lang-ar
BuildArch:	noarch

%description lang-ar
Arabic resources for Firefox.

%description lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Firefoksa.

%package lang-ast
Summary:	Asturian resources for Firefox
Summary(pl.UTF-8):	Asturyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ast
Obsoletes:	mozilla-firefox-lang-ast
BuildArch:	noarch

%description lang-ast
Asturian resources for Firefox.

%description lang-ast -l pl.UTF-8
Asturyjskie pliki językowe dla Firefoksa.

%package lang-az
Summary:	Azerbaijani resources for Firefox
Summary(pl.UTF-8):	Azerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-az
Obsoletes:	mozilla-firefox-lang-az
BuildArch:	noarch

%description lang-az
Azerbaijani resources for Firefox.

%description lang-az -l pl.UTF-8
Azerskie pliki językowe dla Firefoksa.

%package lang-be
Summary:	Belarusian resources for Firefox
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-be
Obsoletes:	mozilla-firefox-lang-be
BuildArch:	noarch

%description lang-be
Belarusian resources for Firefox.

%description lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Firefoksa.

%package lang-bg
Summary:	Bulgarian resources for Firefox
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-bg
Obsoletes:	mozilla-firefox-lang-bg
BuildArch:	noarch

%description lang-bg
Bulgarian resources for Firefox.

%description lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Firefoksa.

%package lang-bn
Summary:	Bengali (Bangladesh) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	firefox-lang-bn_IN
Obsoletes:	iceweasel-lang-bn
Obsoletes:	mozilla-firefox-lang-bn
BuildArch:	noarch

%description lang-bn
Bengali (Bangladesh) resources for Firefox.

%description lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu).

%package lang-bn_IN
Summary:	Bengali (India) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-bn_IN
Obsoletes:	mozilla-firefox-lang-bn_IN
BuildArch:	noarch

%description lang-bn_IN
Bengali (India) resources for Firefox.

%description lang-bn_IN -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Indii).

%package lang-br
Summary:	Breton resources for Firefox
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-br
Obsoletes:	mozilla-firefox-lang-br
BuildArch:	noarch

%description lang-br
Breton resources for Firefox.

%description lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Firefoksa.

%package lang-bs
Summary:	Bosnian resources for Firefox
Summary(pl.UTF-8):	Bośniackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-bs
Obsoletes:	mozilla-firefox-lang-bs
BuildArch:	noarch

%description lang-bs
Bosnian resources for Firefox.

%description lang-bs -l pl.UTF-8
Bośniackie pliki językowe dla Firefoksa.

%package lang-ca
Summary:	Catalan resources for Firefox
Summary(ca.UTF-8):	Recursos catalans per Firefox
Summary(es.UTF-8):	Recursos catalanes para Firefox
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.softcatala.org/projectes/mozilla/
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ca
Obsoletes:	mozilla-firefox-lang-ca
BuildArch:	noarch

%description lang-ca
Catalan resources for Firefox.

%description lang-ca -l ca.UTF-8
Recursos catalans per Firefox.

%description lang-ca -l es.UTF-8
Recursos catalanes para Firefox.

%description lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Firefoksa.

%package lang-cak
Summary:	Kaqchikel resources for Firefox
Summary(pl.UTF-8):	Pliki językowe kaqchikel dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-cak
Kaqchikel resources for Firefox.

%description lang-cak -l pl.UTF-8
Pliki językowe kaqchikel dla Firefoksa.

%package lang-cs
Summary:	Czech resources for Firefox
Summary(pl.UTF-8):	Czeskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-cs
Obsoletes:	mozilla-firefox-lang-cs
BuildArch:	noarch

%description lang-cs
Czech resources for Firefox.

%description lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Firefoksa.

%package lang-csb
Summary:	Kashubian resources for Firefox
Summary(pl.UTF-8):	Kaszubskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-csb
Obsoletes:	mozilla-firefox-lang-csb
BuildArch:	noarch

%description lang-csb
Kashubian resources for Firefox.

%description lang-csb -l pl.UTF-8
Kaszubskie pliki językowe dla Firefoksa.

%package lang-cy
Summary:	Welsh resources for Firefox
Summary(pl.UTF-8):	Walijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-cy
Obsoletes:	mozilla-firefox-lang-cy
BuildArch:	noarch

%description lang-cy
Welsh resources for Firefox.

%description lang-cy -l pl.UTF-8
Walijskie pliki językowe dla Firefoksa.

%package lang-da
Summary:	Danish resources for Firefox
Summary(pl.UTF-8):	Duńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-da
Obsoletes:	mozilla-firefox-lang-da
BuildArch:	noarch

%description lang-da
Danish resources for Firefox.

%description lang-da -l pl.UTF-8
Duńskie pliki językowe dla Firefoksa.

%package lang-de
Summary:	German resources for Firefox
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-de
Obsoletes:	mozilla-firefox-lang-de
BuildArch:	noarch

%description lang-de
German resources for Firefox.

%description lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Firefoksa.

%package lang-dsb
Summary:	Lower Sorbian resources for Firefox
Summary(pl.UTF-8):	Dolnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-dsb
Obsoletes:	mozilla-firefox-lang-dsb
BuildArch:	noarch

%description lang-dsb
Lower Sorbian resources for Firefox.

%description lang-dsb -l pl.UTF-8
Dolnołużyckie pliki językowe dla Firefoksa.

%package lang-el
Summary:	Greek resources for Firefox
Summary(pl.UTF-8):	Greckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-el
Obsoletes:	mozilla-firefox-lang-el
BuildArch:	noarch

%description lang-el
Greek resources for Firefox.

%description lang-el -l pl.UTF-8
Greckie pliki językowe dla Firefoksa.

%package lang-en_CA
Summary:	English (Canadian) resources for Firefox
Summary(pl.UTF-8):	Angielskie (kanadyjskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-en_CA
English (Canadian) resources for Firefox.

%description lang-en_CA -l pl.UTF-8
Angielskie (kanadyjskie) pliki językowe dla Firefoksa.

%package lang-en_GB
Summary:	English (British) resources for Firefox
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-en_GB
Obsoletes:	mozilla-firefox-lang-en_GB
BuildArch:	noarch

%description lang-en_GB
English (British) resources for Firefox.

%description lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Firefoksa.

%package lang-en_US
Summary:	English (American) resources for Firefox
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-en_US
Obsoletes:	mozilla-firefox-lang-en_US
BuildArch:	noarch

%description lang-en_US
English (American) resources for Firefox.

%description lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Firefoksa.

%package lang-eo
Summary:	Esperanto resources for Firefox
Summary(pl.UTF-8):	Pliki językowe esperanto dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-eo
Obsoletes:	mozilla-firefox-lang-eo
BuildArch:	noarch

%description lang-eo
Esperanto resources for Firefox.

%description lang-eo -l pl.UTF-8
Pliki językowe esperanto dla Firefoksa.

%package lang-es_AR
Summary:	Spanish (Andorra) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Andorra) per Firefox
Summary(es.UTF-8):	Recursos españoles (Andorra) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-es_AR
Obsoletes:	mozilla-firefox-lang-es_AR
BuildArch:	noarch

%description lang-es_AR
Spanish (Spain) resources for Firefox.

%description lang-es_AR -l ca.UTF-8
Recursos espanyols (Andorra) per Firefox.

%description lang-es_AR -l es.UTF-8
Recursos españoles (Andorra) para Firefox.

%description lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory).

%package lang-es_CL
Summary:	Spanish (Chile) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Xile) per Firefox
Summary(es.UTF-8):	Recursos españoles (Chile) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-es_CL
Obsoletes:	mozilla-firefox-lang-es_CL
BuildArch:	noarch

%description lang-es_CL
Spanish (Chile) resources for Firefox.

%description lang-es_CL -l ca.UTF-8
Recursos espanyols (Xile) per Firefox.

%description lang-es_CL -l es.UTF-8
Recursos españoles (Chile) para Firefox.

%description lang-es_CL -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile).

%package lang-es
Summary:	Spanish (Spain) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Espanya) per Firefox
Summary(es.UTF-8):	Recursos españoles (España) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-es
Obsoletes:	mozilla-firefox-lang-es
BuildArch:	noarch

%description lang-es
Spanish (Spain) resources for Firefox.

%description lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per Firefox.

%description lang-es -l es.UTF-8
Recursos españoles (España) para Firefox.

%description lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii).

%package lang-es_MX
Summary:	Spanish (Mexico) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Mèxic) per Firefox
Summary(es.UTF-8):	Recursos españoles (México) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-es_MX
Obsoletes:	mozilla-firefox-lang-es_MX
BuildArch:	noarch

%description lang-es_MX
Spanish (Mexico) resources for Firefox.

%description lang-es_MX -l ca.UTF-8
Recursos espanyols (Mèxic) per Firefox.

%description lang-es_MX -l es.UTF-8
Recursos españoles (México) para Firefox.

%description lang-es_MX -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku).

%package lang-et
Summary:	Estonian resources for Firefox
Summary(pl.UTF-8):	Estońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-et
Obsoletes:	mozilla-firefox-lang-et
BuildArch:	noarch

%description lang-et
Estonian resources for Firefox.

%description lang-et -l pl.UTF-8
Estońskie pliki językowe dla Firefoksa.

%package lang-eu
Summary:	Basque resources for Firefox
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-eu
Obsoletes:	mozilla-firefox-lang-eu
BuildArch:	noarch

%description lang-eu
Basque resources for Firefox.

%description lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Firefoksa.

%package lang-fa
Summary:	Persian resources for Firefox
Summary(pl.UTF-8):	Perskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-fa
Obsoletes:	mozilla-firefox-lang-fa
BuildArch:	noarch

%description lang-fa
Persian resources for Firefox.

%description lang-fa -l pl.UTF-8
Perskie pliki językowe dla Firefoksa.

%package lang-ff
Summary:	Fulah resources for Firefox
Summary(pl.UTF-8):	Pliki językowe fulani dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ff
Obsoletes:	mozilla-firefox-lang-ff
BuildArch:	noarch

%description lang-ff
Fulah resources for Firefox.

%description lang-ff -l pl.UTF-8
Pliki językowe fulani dla Firefoksa.

%package lang-fi
Summary:	Finnish resources for Firefox
Summary(pl.UTF-8):	Fińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-fi
Obsoletes:	mozilla-firefox-lang-fi
BuildArch:	noarch

%description lang-fi
Finnish resources for Firefox.

%description lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Firefoksa.

%package lang-fr
Summary:	French resources for Firefox
Summary(pl.UTF-8):	Francuskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-fr
Obsoletes:	mozilla-firefox-lang-fr
BuildArch:	noarch

%description lang-fr
French resources for Firefox.

%description lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Firefoksa.

%package lang-fy
Summary:	Frisian resources for Firefox
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-fy
Obsoletes:	mozilla-firefox-lang-fy
BuildArch:	noarch

%description lang-fy
Frisian resources for Firefox.

%description lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Firefoksa.

%package lang-ga
Summary:	Irish resources for Firefox
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ga
Obsoletes:	mozilla-firefox-lang-ga
BuildArch:	noarch

%description lang-ga
Irish resources for Firefox.

%description lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Firefoksa.

%package lang-gd
Summary:	Gaelic resources for Firefox
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-gd
Obsoletes:	mozilla-firefox-lang-gd
BuildArch:	noarch

%description lang-gd
Gaelic resources for Firefox.

%description lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Firefoksa.

%package lang-gl
Summary:	Galician resources for Firefox
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-gl
Obsoletes:	mozilla-firefox-lang-gl
BuildArch:	noarch

%description lang-gl
Galician resources for Firefox.

%description lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Firefoksa.

%package lang-gn
Summary:	Guarani resources for Firefox
Summary(pl.UTF-8):	Pliki językowe guarani dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-gn
Obsoletes:	mozilla-firefox-lang-gn
BuildArch:	noarch

%description lang-gn
Guarani resources for Firefox.

%description lang-gn -l pl.UTF-8
Pliki językowe guarani dla Firefoksa.

%package lang-gu
Summary:	Gujarati resources for Firefox
Summary(pl.UTF-8):	Pliki językowe gudźarati dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-gu
Obsoletes:	mozilla-firefox-lang-gu
BuildArch:	noarch

%description lang-gu
Gujarati resources for Firefox.

%description lang-gu -l pl.UTF-8
Pliki językowe gudźarati dla Firefoksa.

%package lang-he
Summary:	Hebrew resources for Firefox
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-he
Obsoletes:	mozilla-firefox-lang-he
BuildArch:	noarch

%description lang-he
Hebrew resources for Firefox.

%description lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Firefoksa.

%package lang-hi
Summary:	Hindi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe hindi dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-hi
Obsoletes:	mozilla-firefox-lang-hi
BuildArch:	noarch

%description lang-hi
Hindi resources for Firefox.

%description lang-hi -l pl.UTF-8
Pliki językowe hindi dla Firefoksa.

%package lang-hr
Summary:	Croatian resources for Firefox
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-hr
Obsoletes:	mozilla-firefox-lang-hr
BuildArch:	noarch

%description lang-hr
Croatian resources for Firefox.

%description lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Firefoksa.

%package lang-hsb
Summary:	Upper Sorbian resources for Firefox
Summary(pl.UTF-8):	Górnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-hsb
Obsoletes:	mozilla-firefox-lang-hsb
BuildArch:	noarch

%description lang-hsb
Upper Sorbian resources for Firefox.

%description lang-hsb -l pl.UTF-8
Górnołużyckie pliki językowe dla Firefoksa.

%package lang-hu
Summary:	Hungarian resources for Firefox
Summary(hu.UTF-8):	Magyar nyelv Firefox-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-hu
Obsoletes:	mozilla-firefox-lang-hu
BuildArch:	noarch

%description lang-hu
Hungarian resources for Firefox.

%description lang-hu -l hu.UTF-8
Magyar nyelv Firefox-hez.

%description lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Firefoksa.

%package lang-hy
Summary:	Armenian resources for Firefox
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-hy
Obsoletes:	mozilla-firefox-lang-hy
BuildArch:	noarch

%description lang-hy
Armenian resources for Firefox.

%description lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Firefoksa.

%package lang-ia
Summary:	Interlingua resources for Firefox
Summary(pl.UTF-8):	Pliki językowe interlingua dla Firefoksa
Group:		I18n
Requires:	%{name} >= %{version}
Provides:	%{name}-lang-resources = %{version}
BuildArch:	noarch

%description lang-ia
Interlingua resources for Firefox.

%description lang-ia -l pl.UTF-8
Pliki językowe interlingua dla Firefoksa.

%package lang-id
Summary:	Indonesian resources for Firefox
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-id
Obsoletes:	mozilla-firefox-lang-id
BuildArch:	noarch

%description lang-id
Indonesian resources for Firefox.

%description lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Firefoksa.

%package lang-is
Summary:	Icelandic resources for Firefox
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-is
Obsoletes:	mozilla-firefox-lang-is
BuildArch:	noarch

%description lang-is
Icelandic resources for Firefox.

%description lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Firefoksa.

%package lang-it
Summary:	Italian resources for Firefox
Summary(pl.UTF-8):	Włoskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-it
Obsoletes:	mozilla-firefox-lang-it
BuildArch:	noarch

%description lang-it
Italian resources for Firefox.

%description lang-it -l pl.UTF-8
Włoskie pliki językowe dla Firefoksa.

%package lang-ja
Summary:	Japanese resources for Firefox
Summary(pl.UTF-8):	Japońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ja
Obsoletes:	mozilla-firefox-lang-ja
BuildArch:	noarch

%description lang-ja
Japanese resources for Firefox.

%description lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Firefoksa.

%package lang-ka
Summary:	Georgian resources for Firefox
Summary(pl.UTF-8):	Gruzińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ka
Obsoletes:	mozilla-firefox-lang-ka
BuildArch:	noarch

%description lang-ka
Georgian resources for Firefox.

%description lang-ka -l pl.UTF-8
Gruzińskie pliki językowe dla Firefoksa.

%package lang-kab
Summary:	Kabyle resources for Firefox
Summary(pl.UTF-8):	Kabylskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-kab
Kabyle resources for Firefox.

%description lang-kab -l pl.UTF-8
Kabylskie pliki językowe dla Firefoksa.

%package lang-kk
Summary:	Kazakh resources for Firefox
Summary(pl.UTF-8):	Kazachskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-kk
Obsoletes:	mozilla-firefox-lang-kk
BuildArch:	noarch

%description lang-kk
Kazakh resources for Firefox.

%description lang-kk -l pl.UTF-8
Kazachskie pliki językowe dla Firefoksa.

%package lang-km
Summary:	Khmer resources for Firefox
Summary(pl.UTF-8):	Khmerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-km
Obsoletes:	mozilla-firefox-lang-km
BuildArch:	noarch

%description lang-km
Khmer resources for Firefox.

%description lang-km -l pl.UTF-8
Khmerskie pliki językowe dla Firefoksa.

%package lang-kn
Summary:	Kannada resources for Firefox
Summary(pl.UTF-8):	Pliki językowe kannada dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-kn
Obsoletes:	mozilla-firefox-lang-kn
BuildArch:	noarch

%description lang-kn
Kannada resources for Firefox.

%description lang-kn -l pl.UTF-8
Pliki językowe kannada dla Firefoksa.

%package lang-ko
Summary:	Korean resources for Firefox
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ko
Obsoletes:	mozilla-firefox-lang-ko
BuildArch:	noarch

%description lang-ko
Korean resources for Firefox.

%description lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Firefoksa.

%package lang-ku
Summary:	Kurdish resources for Firefox
Summary(pl.UTF-8):	Kurdyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ku
Obsoletes:	mozilla-firefox-lang-ku
BuildArch:	noarch

%description lang-ku
Kurdish resources for Firefox.

%description lang-ku -l pl.UTF-8
Kurdyjskie pliki językowe dla Firefoksa.

%package lang-lij
Summary:	Ligurian resources for Firefox
Summary(pl.UTF-8):	Liguryjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-lij
Obsoletes:	mozilla-firefox-lang-lij
BuildArch:	noarch

%description lang-lij
Ligurian resources for Firefox.

%description lang-lij -l pl.UTF-8
Liguryjskie pliki językowe dla Firefoksa.

%package lang-lt
Summary:	Lithuanian resources for Firefox
Summary(pl.UTF-8):	Litewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-lt
Obsoletes:	mozilla-firefox-lang-lt
BuildArch:	noarch

%description lang-lt
Lithuanian resources for Firefox.

%description lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Firefoksa.

%package lang-lv
Summary:	Latvian resources for Firefox
Summary(pl.UTF-8):	Łotewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-lv
Obsoletes:	mozilla-firefox-lang-lv
BuildArch:	noarch

%description lang-lv
Latvian resources for Firefox.

%description lang-lv -l pl.UTF-8
Łotewskie pliki językowe dla Firefoksa.

%package lang-mk
Summary:	Macedonian resources for Firefox
Summary(pl.UTF-8):	Macedońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-mk
Obsoletes:	mozilla-firefox-lang-mk
BuildArch:	noarch

%description lang-mk
Macedonian resources for Firefox.

%description lang-mk -l pl.UTF-8
Macedońskie pliki językowe dla Firefoksa.

%package lang-mr
Summary:	Marathi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe marathi dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-mr
Obsoletes:	mozilla-firefox-lang-mr
BuildArch:	noarch

%description lang-mr
Marathi resources for Firefox.

%description lang-mr -l pl.UTF-8
Pliki językowe marathi dla Firefoksa.

%package lang-ms
Summary:	Malay resources for Firefox
Summary(pl.UTF-8):	Malajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ms
Obsoletes:	mozilla-firefox-lang-ms
BuildArch:	noarch

%description lang-ms
Malay resources for Firefox.

%description lang-ms -l pl.UTF-8
Malajskie pliki językowe dla Firefoksa.

%package lang-my
Summary:	Burmese resources for Firefox
Summary(pl.UTF-8):	Birmańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-my
Burmese resources for Firefox.

%description lang-my -l pl.UTF-8
Birmańskie pliki językowe dla Firefoksa.

%package lang-nb
Summary:	Norwegian Bokmaal resources for Firefox
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-nb
Obsoletes:	mozilla-firefox-lang-nb
BuildArch:	noarch

%description lang-nb
Norwegian Bokmaal resources for Firefox.

%description lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Firefoksa.

%package lang-ne
Summary:	Nepali resources for Firefox
Summary(pl.UTF-8):	Nepalskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	%{name} >= %{version}
Provides:	%{name}-lang-resources = %{version}
BuildArch:	noarch

%description lang-ne
Nepali resources for Firefox.

%description lang-ne -l pl.UTF-8
Nepalskie pliki językowe dla Firefoksa.

%package lang-nl
Summary:	Dutch resources for Firefox
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-nl
Obsoletes:	mozilla-firefox-lang-nl
BuildArch:	noarch

%description lang-nl
Dutch resources for Firefox.

%description lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Firefoksa.

%package lang-nn
Summary:	Norwegian Nynorsk resources for Firefox
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-nn
Obsoletes:	mozilla-firefox-lang-nn
BuildArch:	noarch

%description lang-nn
Norwegian Nynorsk resources for Firefox.

%description lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Firefoksa.

%package lang-oc
Summary:	Occitan resources for Firefox
Summary(pl.UTF-8):	Oksytańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	%{name} >= %{version}
Provides:	%{name}-lang-resources = %{version}
BuildArch:	noarch

%description lang-oc
Occitan resources for Firefox.

%description lang-oc -l pl.UTF-8
Oksytańskie pliki językowe dla Firefoksa.

%package lang-pa
Summary:	Panjabi resources for Firefox
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-pa
Obsoletes:	mozilla-firefox-lang-pa
BuildArch:	noarch

%description lang-pa
Panjabi resources for Firefox.

%description lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Firefoksa.

%package lang-pl
Summary:	Polish resources for Firefox
Summary(pl.UTF-8):	Polskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.firefox.pl/
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-pl
Obsoletes:	mozilla-firefox-lang-pl
BuildArch:	noarch

%description lang-pl
Polish resources for Firefox.

%description lang-pl -l pl.UTF-8
Polskie pliki językowe dla Firefoksa.

%package lang-pt_BR
Summary:	Portuguese (Brazil) resources for Firefox
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-pt_BR
Obsoletes:	mozilla-firefox-lang-pt_BR
BuildArch:	noarch

%description lang-pt_BR
Portuguese (Brazil) resources for Firefox.

%description lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Firefoksa.

%package lang-pt
Summary:	Portuguese (Portugal) resources for Firefox
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-pt
Obsoletes:	mozilla-firefox-lang-pt
BuildArch:	noarch

%description lang-pt
Portuguese (Portugal) resources for Firefox.

%description lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii).

%package lang-rm
Summary:	Romansh resources for Firefox
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-rm
Obsoletes:	mozilla-firefox-lang-rm
BuildArch:	noarch

%description lang-rm
Romansh resources for Firefox.

%description lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Firefoksa.

%package lang-ro
Summary:	Romanian resources for Firefox
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ro
Obsoletes:	mozilla-firefox-lang-ro
BuildArch:	noarch

%description lang-ro
Romanian resources for Firefox.

%description lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Firefoksa.

%package lang-ru
Summary:	Russian resources for Firefox
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ru
Obsoletes:	mozilla-firefox-lang-ru
BuildArch:	noarch

%description lang-ru
Russian resources for Firefox.

%description lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Firefoksa.

%package lang-si
Summary:	Sinhala resources for Firefox
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-si
Obsoletes:	mozilla-firefox-lang-si
BuildArch:	noarch

%description lang-si
Sinhala resources for Firefox.

%description lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Firefoksa.

%package lang-sk
Summary:	Slovak resources for Firefox
Summary(pl.UTF-8):	Słowackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-sk
Obsoletes:	mozilla-firefox-lang-sk
BuildArch:	noarch

%description lang-sk
Slovak resources for Firefox.

%description lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Firefoksa.

%package lang-sl
Summary:	Slovene resources for Firefox
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-sl
Obsoletes:	mozilla-firefox-lang-sl
BuildArch:	noarch

%description lang-sl
Slovene resources for Firefox.

%description lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Firefoksa.

%package lang-son
Summary:	Songhai resources for Firefox
Summary(pl.UTF-8):	Songhajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-son
Obsoletes:	mozilla-firefox-lang-son
BuildArch:	noarch

%description lang-son
Songhai resources for Firefox.

%description lang-son -l pl.UTF-8
Songhajskie pliki językowe dla Firefoksa.

%package lang-sq
Summary:	Albanian resources for Firefox
Summary(pl.UTF-8):	Albańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-sq
Obsoletes:	mozilla-firefox-lang-sq
BuildArch:	noarch

%description lang-sq
Albanian resources for Firefox.

%description lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Firefoksa.

%package lang-sr
Summary:	Serbian resources for Firefox
Summary(pl.UTF-8):	Serbskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-sr
Obsoletes:	mozilla-firefox-lang-sr
BuildArch:	noarch

%description lang-sr
Serbian resources for Firefox.

%description lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Firefoksa.

%package lang-sv
Summary:	Swedish resources for Firefox
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-sv
Obsoletes:	mozilla-firefox-lang-sv
BuildArch:	noarch

%description lang-sv
Swedish resources for Firefox.

%description lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Firefoksa.

%package lang-ta
Summary:	Tamil (India) resources for Firefox
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ta
Obsoletes:	mozilla-firefox-lang-ta
BuildArch:	noarch

%description lang-ta
Tamil (India) resources for Firefox.

%description lang-ta -l pl.UTF-8
Tamilskie pliki językowe dla Firefoksa (wersja dla Indii).

%package lang-te
Summary:	Telugu resources for Firefox
Summary(pl.UTF-8):	Pliki językowe telugu dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-te
Obsoletes:	mozilla-firefox-lang-te
BuildArch:	noarch

%description lang-te
Telugu resources for Firefox.

%description lang-te -l pl.UTF-8
Pliki językowe telugu dla Firefoksa.

%package lang-th
Summary:	Thai resources for Firefox
Summary(pl.UTF-8):	Tajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-th
Obsoletes:	mozilla-firefox-lang-th
BuildArch:	noarch

%description lang-th
Thai resources for Firefox.

%description lang-th -l pl.UTF-8
Tajskie pliki językowe dla Firefoksa.

%package lang-tr
Summary:	Turkish resources for Firefox
Summary(pl.UTF-8):	Tureckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-tr
Obsoletes:	mozilla-firefox-lang-tr
BuildArch:	noarch

%description lang-tr
Turkish resources for Firefox.

%description lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Firefoksa.

%package lang-uk
Summary:	Ukrainian resources for Firefox
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-uk
Obsoletes:	mozilla-firefox-lang-uk
BuildArch:	noarch

%description lang-uk
Ukrainian resources for Firefox.

%description lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Firefoksa.

%package lang-ur
Summary:	Urdu resources for Firefox
Summary(pl.UTF-8):	Pliki językowe urdu dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-ur
Urdu resources for Firefox.

%description lang-ur -l pl.UTF-8
Pliki językowe urdu dla Firefoksa.

%package lang-uz
Summary:	Uzbek resources for Firefox
Summary(pl.UTF-8):	Uzbeckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-uz
Obsoletes:	mozilla-firefox-lang-uz
BuildArch:	noarch

%description lang-uz
Uzbek resources for Firefox.

%description lang-uz -l pl.UTF-8
Uzbeckie pliki językowe dla Firefoksa.

%package lang-vi
Summary:	Vietmanese resources for Firefox
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-vi
Obsoletes:	mozilla-firefox-lang-vi
BuildArch:	noarch

%description lang-vi
Vietmanese resources for Firefox.

%description lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Firefoksa.

%package lang-xh
Summary:	Xhosa resources for Firefox
Summary(pl.UTF-8):	Pliki językowe xhosa dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-xh
Obsoletes:	mozilla-firefox-lang-xh
BuildArch:	noarch

%description lang-xh
Xhosa resources for Firefox.

%description lang-xh -l pl.UTF-8
Pliki językowe xhosa dla Firefoksa.

%package lang-zh_CN
Summary:	Simplified Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-zh_CN
Obsoletes:	mozilla-firefox-lang-zh_CN
BuildArch:	noarch

%description lang-zh_CN
Simplified Chinese resources for Firefox.

%description lang-zh_CN -l pl.UTF-8
Chińskie uproszczone pliki językowe dla Firefoksa.

%package lang-zh_TW
Summary:	Traditional Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-zh_TW
Obsoletes:	mozilla-firefox-lang-zh_TW
BuildArch:	noarch

%description lang-zh_TW
Traditional Chinese resources for Firefox.

%description lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Firefoksa.

%package lang-zu
Summary:	Zulu resources for Firefox
Summary(pl.UTF-8):	Zuluskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-zu
Obsoletes:	mozilla-firefox-lang-zu
BuildArch:	noarch

%description lang-zu
Zulu resources for Firefox.

%description lang-zu -l pl.UTF-8
Zuluskie pliki językowe dla Firefoksa.

%package geckodriver
Summary:	WebDriver for Firefox
Summary(pl.UTF-8):	WebDriver dla Firefoksa
Group:		Applications
Requires:	firefox >= %{version}

%description geckodriver
WebDriver is an open source tool for automated testing of webapps
across many browsers. It provides capabilities for navigating to web
pages, user input, JavaScript execution, and more.

%description geckodriver -l pl.UTF-8
WebDriver to mające otwarte źródła narzędzia do automatycznego
testowania aplikacji WWW w różnych przeglądarkach. Jego możliwości to
m.in. nawigowanie po stronach WWW, wejście od użytkownika, wykonywanie
JavaScriptu.

%prep
unpack() {
	local args="$1" file="$2"
	cp -p $file .
}
%define __unzip unpack
%setup -q %(seq -f '-a %g' 100 192 | xargs)

%patch4 -p1
%patch5 -p1
%patch6 -p2
%patch7 -p1
%patch8 -p2
%patch9 -p1
%{?with_system_cairo:%patch10 -p1}

%if %{with pgo}
%{__sed} -i -e 's@__BROWSER_PATH__@"../../dist/bin/firefox-bin"@' build/automation.py.in
%endif

%build
cp -p %{_datadir}/automake/config.* build/autoconf

cat << 'EOF' > .mozconfig
. $topsrcdir/browser/config/mozconfig

%if %{with clang}
export CC="clang"
export CXX="clang++"
export LLVM_PROFDATA="llvm-profdata"
export AR="llvm-ar"
export NM="llvm-nm"
export RANLIB="llvm-ranlib"
%else
export CC="%{__cc}"
export CXX="%{__cxx}"
%endif
%ifarch %{ix86}
export CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64 -g0"
export CXXFLAGS="%{rpmcxxflags} -D_FILE_OFFSET_BITS=64 -g0"
export MOZ_DEBUG_FLAGS=" "
export LLVM_USE_SPLIT_DWARF=1
export LLVM_PARALLEL_LINK_JOBS=1
export MOZ_LINK_FLAGS="-Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
export RUSTFLAGS="-Cdebuginfo=0"
%else
export CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="%{rpmcxxflags} -D_FILE_OFFSET_BITS=64"
%endif

mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/obj-%{_target_cpu}

# Options for 'configure' (same as command-line options).
ac_add_options --host=%{_target_platform}
ac_add_options --prefix=%{_prefix}
%if %{?debug:1}0
ac_add_options --disable-optimize
ac_add_options --enable-debug
ac_add_options --enable-debug-modules
ac_add_options --enable-debugger-info-modules
ac_add_options --enable-crash-on-assert
%else
ac_add_options --disable-debug
%endif
ac_add_options --disable-strip
ac_add_options --disable-install-strip
%if %{with tests}
ac_add_options --enable-tests
ac_add_options --enable-mochitest
%else
%if %{with pgo}
ac_add_options --enable-tests
%else
ac_add_options --disable-tests
%endif
%endif
ac_add_options --disable-crashreporter
ac_add_options --disable-gconf
ac_add_options --disable-necko-wifi
ac_add_options --disable-updater
ac_add_options --enable-alsa
ac_add_options --enable-chrome-format=omni
ac_add_options --enable-default-toolkit=cairo-gtk3
ac_add_options --enable-extensions=default
%{?with_geckodriver:ac_add_options --enable-geckodriver}
%{?with_gold:ac_add_options --enable-linker=gold}
ac_add_options --disable-elf-hack
%if %{with lto}
ac_add_options --enable-lto
%endif
%{?with_clang:ac_add_options --enable-linker=lld}
ac_add_options --enable-readline
%{?with_shared_js:ac_add_options --enable-shared-js}
ac_add_options --enable-startup-notification
%{?with_system_cairo:ac_add_options --enable-system-cairo}
ac_add_options --enable-system-ffi
ac_add_options --enable-system-sqlite
%{?with_official:ac_add_options --enable-official-branding}
ac_add_options --with-distribution-id=org.pld-linux
ac_add_options --with-system-bz2
ac_add_options --with%{!?with_system_icu:out}-system-icu
ac_add_options --with-system-jpeg
ac_add_options --with-system-libevent
ac_add_options --with%{!?with_system_libvpx:out}-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-pixman
ac_add_options --with-system-png
ac_add_options --with-system-webp
ac_add_options --with-system-zlib
# Workaround for mozbz#1341234
ac_add_options BINDGEN_CFLAGS="$(pkg-config nspr pixman-1 --cflags)"
%if %{with legacy_exts}
ac_add_options "MOZ_ALLOW_LEGACY_EXTENSIONS=1"
%endif
EOF

%{!?with_clang:export MOZ_MAKE_FLAGS="-j1"}
export MOZ_SERVICES_SYNC="1"
%if %{with pgo}
D=$(( RANDOM % (200 - 100 + 1 ) + 5 ))
/usr/bin/Xvfb :${D} &
XVFB_PID=$!
[ -n "$XVFB_PID" ] || exit 1
export DISPLAY=:${D}
MOZ_PGO=1 AUTOCONF=/usr/bin/autoconf2_13 ./mach build
kill $XVFB_PID
%else
AUTOCONF=/usr/bin/autoconf2_13 ./mach build
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_libdir}} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/browser \
	$RPM_BUILD_ROOT%{_libdir}/%{name}/browser/plugins \
	$RPM_BUILD_ROOT%{_includedir}/%{name} \
	$RPM_BUILD_ROOT%{_pkgconfigdir}

%browser_plugins_add_browser %{name} -p %{_libdir}/%{name}/browser/plugins

OBJDIR=obj-%{_target_cpu}
%{__make} -C ${OBJDIR}/browser/installer stage-package \
	DESTDIR=$RPM_BUILD_ROOT \
	installdir=%{_libdir}/%{name} \
	PKG_SKIP_STRIP=1

cp -aL ${OBJDIR}/dist/firefox/* $RPM_BUILD_ROOT%{_libdir}/%{name}/
%{?with_geckodriver:cp -aL ${OBJDIR}/dist/bin/geckodriver $RPM_BUILD_ROOT%{_bindir}/}

# move arch independant ones to datadir
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/browser/chrome $RPM_BUILD_ROOT%{_datadir}/%{name}/browser/chrome
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/browser/extensions
%{__mv} $RPM_BUILD_ROOT%{_libdir}/%{name}/defaults $RPM_BUILD_ROOT%{_datadir}/%{name}/browser/defaults
%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/browser/defaults/{pref,preferences}

ln -s ../../../share/%{name}/browser/chrome $RPM_BUILD_ROOT%{_libdir}/%{name}/browser/chrome
ln -s ../../../share/%{name}/browser/defaults $RPM_BUILD_ROOT%{_libdir}/%{name}/browser/defaults
ln -s ../../../share/%{name}/browser/extensions $RPM_BUILD_ROOT%{_libdir}/%{name}/browser/extensions

sed 's,@LIBDIR@,%{_libdir},' %{SOURCE4} > $RPM_BUILD_ROOT%{_bindir}/firefox
chmod 755 $RPM_BUILD_ROOT%{_bindir}/firefox

# install icons and desktop file
for i in 16 32 48 %{?with_official:22 24 256}; do
	install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/${i}x${i}/apps
	cp -a browser/branding/%{!?with_official:un}official/default${i}.png \
		$RPM_BUILD_ROOT%{_iconsdir}/hicolor/${i}x${i}/apps/firefox.png
done

cp -a %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

# install our settings
%if "%{pld_release}" == "ac"
cp -a %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/%{name}/browser/defaults/preferences/vendor.js
%else
cp -a %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/%{name}/browser/defaults/preferences/vendor.js
%endif

# GeckoMediaPlugin API headers
install -d $RPM_BUILD_ROOT%{_includedir}
cp -pr dom/media/gmp/gmp-api $RPM_BUILD_ROOT%{_includedir}

for a in *.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{_datadir}/%{name}/browser/extensions/langpack-$basename@firefox.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_browser_plugins
%update_icon_cache hicolor
%update_desktop_database

%postun
if [ "$1" = 0 ]; then
	%update_browser_plugins
	%update_icon_cache hicolor
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}

%{_desktopdir}/firefox.desktop
%{_iconsdir}/hicolor/*/apps/firefox.png

# browser plugins v2
%{_browserpluginsconfdir}/browsers.d/%{name}.*
%config(noreplace) %verify(not md5 mtime size) %{_browserpluginsconfdir}/blacklist.d/%{name}.*.blacklist

%dir %{_libdir}/%{name}/browser
%dir %{_libdir}/%{name}/browser/plugins
%dir %{_libdir}/%{name}/browser/features

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/browser
%dir %{_datadir}/%{name}/browser/extensions
%{_datadir}/%{name}/browser/chrome
%{_datadir}/%{name}/browser/defaults

# symlinks
%{_libdir}/%{name}/browser/extensions
%{_libdir}/%{name}/browser/chrome
%{_libdir}/%{name}/browser/defaults

%attr(755,root,root) %{_libdir}/%{name}/firefox
%attr(755,root,root) %{_libdir}/%{name}/firefox-bin
%attr(755,root,root) %{_libdir}/%{name}/pingsender
%{_libdir}/%{name}/application.ini
%{_libdir}/%{name}/chrome.manifest
%{_libdir}/%{name}/browser/blocklist.xml
%{_libdir}/%{name}/browser/chrome.manifest
%{_libdir}/%{name}/browser/omni.ja

%{_libdir}/%{name}/browser/features/formautofill@mozilla.org.xpi
%{_libdir}/%{name}/browser/features/screenshots@mozilla.org.xpi
%{_libdir}/%{name}/browser/features/webcompat@mozilla.org.xpi
%{_libdir}/%{name}/browser/features/webcompat-reporter@mozilla.org.xpi

%attr(755,root,root) %{_libdir}/%{name}/plugin-container

%dir %{_libdir}/%{name}/fonts
%{_libdir}/%{name}/fonts/TwemojiMozilla.ttf

%dir %{_libdir}/%{name}/gmp-clearkey
%dir %{_libdir}/%{name}/gmp-clearkey/0.1
%{_libdir}/%{name}/gmp-clearkey/0.1/manifest.json
%attr(755,root,root) %{_libdir}/%{name}/gmp-clearkey/0.1/libclearkey.so
%{!?with_system_icu:%{_libdir}/%{name}/icudt58l.dat}

%dir %{_libdir}/%{name}
%{_libdir}/%{name}/platform.ini
%{?with_shared_js:%attr(755,root,root) %{_libdir}/%{name}/libmozjs.so}
%attr(755,root,root) %{_libdir}/%{name}/liblgpllibs.so
%attr(755,root,root) %{_libdir}/%{name}/libxul.so
%attr(755,root,root) %{_libdir}/%{name}/libmozavcodec.so
%attr(755,root,root) %{_libdir}/%{name}/libmozavutil.so
%attr(755,root,root) %{_libdir}/%{name}/libmozsandbox.so
%attr(755,root,root) %{_libdir}/%{name}/libmozwayland.so
%{_libdir}/%{name}/dependentlibs.list
%{_libdir}/%{name}/omni.ja
%dir %{_libdir}/%{name}/gtk2
%attr(755,root,root) %{_libdir}/%{name}/gtk2/libmozgtk.so
%attr(755,root,root) %{_libdir}/%{name}/libmozgtk.so

%files -n gmp-api
%defattr(644,root,root,755)
%{_includedir}/gmp-api

%files lang-ach
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ach@firefox.mozilla.org.xpi

%files lang-af
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-af@firefox.mozilla.org.xpi

%files lang-an
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-an@firefox.mozilla.org.xpi

%files lang-ar
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ar@firefox.mozilla.org.xpi

%files lang-ast
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ast@firefox.mozilla.org.xpi

%files lang-az
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-az@firefox.mozilla.org.xpi

%files lang-be
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-be@firefox.mozilla.org.xpi

%files lang-bg
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-bg@firefox.mozilla.org.xpi

%files lang-bn
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-bn@firefox.mozilla.org.xpi

%files lang-br
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-br@firefox.mozilla.org.xpi

%files lang-bs
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-bs@firefox.mozilla.org.xpi

%files lang-ca
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ca@firefox.mozilla.org.xpi

%files lang-cak
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-cak@firefox.mozilla.org.xpi

%files lang-cs
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-cs@firefox.mozilla.org.xpi

#%files lang-csb
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/browser/extensions/langpack-csb@firefox.mozilla.org.xpi

%files lang-cy
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-cy@firefox.mozilla.org.xpi

%files lang-da
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-da@firefox.mozilla.org.xpi

%files lang-de
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-de@firefox.mozilla.org.xpi

%files lang-dsb
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-dsb@firefox.mozilla.org.xpi

%files lang-el
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-el@firefox.mozilla.org.xpi

%files lang-en_CA
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-en-CA@firefox.mozilla.org.xpi

%files lang-en_GB
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-en-GB@firefox.mozilla.org.xpi

%files lang-en_US
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-en-US@firefox.mozilla.org.xpi

%files lang-eo
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-eo@firefox.mozilla.org.xpi

%files lang-es_AR
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-es-AR@firefox.mozilla.org.xpi

%files lang-es_CL
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-es-CL@firefox.mozilla.org.xpi

%files lang-es
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-es-ES@firefox.mozilla.org.xpi

%files lang-es_MX
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-es-MX@firefox.mozilla.org.xpi

%files lang-et
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-et@firefox.mozilla.org.xpi

%files lang-eu
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-eu@firefox.mozilla.org.xpi

%files lang-fa
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-fa@firefox.mozilla.org.xpi

%files lang-ff
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ff@firefox.mozilla.org.xpi

%files lang-fi
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-fi@firefox.mozilla.org.xpi

%files lang-fr
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-fr@firefox.mozilla.org.xpi

%files lang-fy
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-fy-NL@firefox.mozilla.org.xpi

%files lang-ga
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ga-IE@firefox.mozilla.org.xpi

%files lang-gd
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-gd@firefox.mozilla.org.xpi

%files lang-gl
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-gl@firefox.mozilla.org.xpi

%files lang-gn
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-gn@firefox.mozilla.org.xpi

%files lang-gu
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-gu-IN@firefox.mozilla.org.xpi

%files lang-he
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-he@firefox.mozilla.org.xpi

%files lang-hi
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-hi-IN@firefox.mozilla.org.xpi

%files lang-hr
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-hr@firefox.mozilla.org.xpi

%files lang-hsb
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-hsb@firefox.mozilla.org.xpi

%files lang-hu
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-hu@firefox.mozilla.org.xpi

%files lang-hy
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-hy-AM@firefox.mozilla.org.xpi

%files lang-ia
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ia@firefox.mozilla.org.xpi

%files lang-id
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-id@firefox.mozilla.org.xpi

%files lang-is
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-is@firefox.mozilla.org.xpi

%files lang-it
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-it@firefox.mozilla.org.xpi

%files lang-ja
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ja@firefox.mozilla.org.xpi

%files lang-ka
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ka@firefox.mozilla.org.xpi

%files lang-kab
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-kab@firefox.mozilla.org.xpi

%files lang-kk
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-kk@firefox.mozilla.org.xpi

%files lang-km
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-km@firefox.mozilla.org.xpi

%files lang-kn
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-kn@firefox.mozilla.org.xpi

%files lang-ko
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ko@firefox.mozilla.org.xpi

#%files lang-ku
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/browser/extensions/langpack-ku@firefox.mozilla.org.xpi

%files lang-lij
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-lij@firefox.mozilla.org.xpi

%files lang-lt
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-lt@firefox.mozilla.org.xpi

%files lang-lv
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-lv@firefox.mozilla.org.xpi

%files lang-mk
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-mk@firefox.mozilla.org.xpi

%files lang-mr
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-mr@firefox.mozilla.org.xpi

%files lang-ms
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ms@firefox.mozilla.org.xpi

%files lang-my
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-my@firefox.mozilla.org.xpi

%files lang-nb
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-nb-NO@firefox.mozilla.org.xpi

%files lang-ne
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ne-NP@firefox.mozilla.org.xpi

%files lang-nl
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-nl@firefox.mozilla.org.xpi

%files lang-nn
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-nn-NO@firefox.mozilla.org.xpi

%files lang-oc
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-oc@firefox.mozilla.org.xpi

%files lang-pa
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-pa-IN@firefox.mozilla.org.xpi

%files lang-pl
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-pl@firefox.mozilla.org.xpi

%files lang-pt_BR
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-pt-BR@firefox.mozilla.org.xpi

%files lang-pt
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-pt-PT@firefox.mozilla.org.xpi

%files lang-rm
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-rm@firefox.mozilla.org.xpi

%files lang-ro
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ro@firefox.mozilla.org.xpi

%files lang-ru
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ru@firefox.mozilla.org.xpi

%files lang-si
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-si@firefox.mozilla.org.xpi

%files lang-sk
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-sk@firefox.mozilla.org.xpi

%files lang-sl
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-sl@firefox.mozilla.org.xpi

%files lang-son
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-son@firefox.mozilla.org.xpi

%files lang-sq
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-sq@firefox.mozilla.org.xpi

%files lang-sr
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-sr@firefox.mozilla.org.xpi

%files lang-sv
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-sv-SE@firefox.mozilla.org.xpi

%files lang-ta
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ta@firefox.mozilla.org.xpi

%files lang-te
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-te@firefox.mozilla.org.xpi

%files lang-th
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-th@firefox.mozilla.org.xpi

%files lang-tr
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-tr@firefox.mozilla.org.xpi

%files lang-uk
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-uk@firefox.mozilla.org.xpi

%files lang-ur
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ur@firefox.mozilla.org.xpi

%files lang-uz
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-uz@firefox.mozilla.org.xpi

%files lang-vi
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-vi@firefox.mozilla.org.xpi

%files lang-xh
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-xh@firefox.mozilla.org.xpi

%files lang-zh_CN
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-zh-CN@firefox.mozilla.org.xpi

%files lang-zh_TW
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-zh-TW@firefox.mozilla.org.xpi

#%files lang-zu
#%defattr(644,root,root,755)
#%{_datadir}/%{name}/browser/extensions/langpack-zu@firefox.mozilla.org.xpi

%if %{with geckodriver}
%files geckodriver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/geckodriver
%endif
