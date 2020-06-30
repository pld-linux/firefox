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
%bcond_without	system_libvpx	# build with system libvpx
%bcond_without	clang		# build using Clang/LLVM
%bcond_with	lowmem		# lower memory requirements

%if %{with lto}
%define		with_clang	1
%undefine	with_gold
%endif

%ifarch %{ix86} %{arm} aarch64
%define		with_lowmem	1
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

%define		nspr_ver	4.25
%define		nss_ver		3.53.1

Summary:	Firefox web browser
Summary(hu.UTF-8):	Firefox web böngésző
Summary(pl.UTF-8):	Firefox - przeglądarka WWW
Name:		firefox
Version:	78.0
Release:	1
License:	MPL v2.0
Group:		X11/Applications/Networking
Source0:	http://releases.mozilla.org/pub/firefox/releases/%{version}/source/firefox-%{version}.source.tar.xz
# Source0-md5:	075a9b78766f5706df36f3838f74d91c
Source3:	%{name}.desktop
Source4:	%{name}.sh
Source5:	vendor.js
Source6:	vendor-ac.js
Source100:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source100-md5:	f84e027e4e4b2134887472c10360fc8f
Source101:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source101-md5:	7a34fa47776debf9b99f63722a7fdaff
Source102:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source102-md5:	c05654cdf7ab1c10a42f167a38f86e7c
Source103:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source103-md5:	6bbbcb706fa82971ad02ed35fe84521f
Source104:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source104-md5:	30e326122074338ed843c38f11649799
Source105:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source105-md5:	f5aeacaae023f62c0edb504197ff3769
Source106:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source106-md5:	3f231670c9f8512dbea43f0ea14f4123
Source107:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source107-md5:	9a7c49214c3787be03b7815c648b4eeb
Source108:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bn.xpi
# Source108-md5:	2e8621967ea4c998c3d15441fea524e1
Source109:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source109-md5:	4532e56bc2479ccbf48fb67a5cb20540
Source110:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source110-md5:	1fe147d2252ca9dde2046cf86dc80447
Source111:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source111-md5:	4b46337b31b3d47cbd696a07ccfa1fc0
Source112:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cak.xpi
# Source112-md5:	d681f7b30e8a656364bb19836a1e2bf6
Source113:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source113-md5:	2f13f71f09016caf81c23cdd2e64289e
Source114:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source114-md5:	b10eb7b6fb88a9bf57a1ee208f412e75
Source115:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source115-md5:	01f3d06fc46aff57861d35f34f6919b0
Source116:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source116-md5:	d2f0f1889b7fea158cf877605a3f4af0
Source117:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source117-md5:	c608f8750ad80bb0e994972d51fa6732
Source118:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source118-md5:	33221096b305d4dd02a22c5c848e69ee
Source119:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-CA.xpi
# Source119-md5:	a53b1f77a888a4ec456a3fa14f3cbb73
Source120:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source120-md5:	cab17a0d591a1893aa248909cb8c7fae
Source121:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source121-md5:	92f82f71691de383a31cc2b99ffd316e
Source122:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source122-md5:	343fe8f286d4152b30401fc1981b46e8
Source123:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source123-md5:	b4255971262b2335e567b37d4298a303
Source124:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source124-md5:	7a9eac668565862c34d5617004d09c1a
Source125:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source125-md5:	f9915700190dece739553f8d973acf78
Source126:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source126-md5:	e83a3656af71353d8ca4c02783ba1ff5
Source127:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source127-md5:	83b880bc084fa178b619540bb3de6c32
Source128:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source128-md5:	8ef5921f7e89b282b71a1afe3789d73a
Source129:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source129-md5:	5516111dd916d97890aafd618c74c9e0
Source130:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source130-md5:	d16e5c18a096df734495a07466d401e5
Source131:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source131-md5:	01298ba0d712bc7e7838bb09a1577094
Source132:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source132-md5:	65cbc78b78cf00fa93aec58f9ea1eff8
Source133:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source133-md5:	71d9427ef72f1f81fe94e1d339616cd2
Source134:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source134-md5:	c592c42c1c234432f4df444aa00cd2eb
Source135:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source135-md5:	d73e98268bdd9bb8cc585d6163fd2ef2
Source136:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source136-md5:	b6af63aab9dd021f21d7c5c5bf239ad4
Source137:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gn.xpi
# Source137-md5:	7663cbd97a0935bbd7b955ace548f4f5
Source138:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source138-md5:	31bf12416df52180b89233ec76a74842
Source139:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source139-md5:	5ca7a721f761b6bcae10b53b5d3cbc34
Source140:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source140-md5:	42a5e853a10bd0026feb1bc021394a5d
Source141:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source141-md5:	3efa81ce39fa2bbef4903cef5e817697
Source142:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source142-md5:	901943d398456ca6687d47102e1fe4cd
Source143:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source143-md5:	b4b67159f957907683429bb1c423a3ab
Source144:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source144-md5:	3d442114f204c0739c9ce00919bf3de7
Source145:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ia.xpi
# Source145-md5:	ab65864780e5ef77fd10d5f1575b8a44
Source146:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source146-md5:	b648cfab3e48923f7bf6ac9d2de5fc95
Source147:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source147-md5:	5c7a07bc46b619cf5bc952925cb9c192
Source148:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source148-md5:	61a224a6a8e8de1a456998bc458d70e3
Source149:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source149-md5:	27d4b391cf856f2dd9265f94139a9fa8
Source150:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ka.xpi
# Source150-md5:	78472f51fac4070c1ed556fc071f4c4f
Source151:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/kab.xpi
# Source151-md5:	3eaef85a76fa755f168d83bb358c3345
Source152:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source152-md5:	69fe9cc267f890ac1fabfd43b3ccce76
Source153:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source153-md5:	69673056a03d0cac7e9c8d5b37f2b928
Source154:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source154-md5:	575233e6aa4d09b57b96b05a6c5ede20
Source155:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source155-md5:	faefb29da347814f79e2eaae46a60852
Source156:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source156-md5:	dc200e7ca78227463da42affe1f183c9
Source157:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source157-md5:	4231ad8e41698fb572af912e8628a888
Source158:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source158-md5:	c1ee420c8f1bd9460ad055c6cc9f2793
Source159:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source159-md5:	8493947d52ef833d1ea843f59334dd72
Source160:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source160-md5:	ec16c394fbcd33321b1c71c5e5481e5a
Source161:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source161-md5:	b18662f0495ade7d03ecd79702bbee16
Source162:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/my.xpi
# Source162-md5:	f2f7ef1e2d8bc948958e187c02a64391
Source163:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source163-md5:	5cbaecf7ec3b636b63f5fd3a8e72686e
Source164:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ne-NP.xpi
# Source164-md5:	e6ad3280c06c5e69eb1c492e3f44512b
Source165:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source165-md5:	0c07a3823222905ad812cacd5f8a1a65
Source166:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source166-md5:	d9952af3a9a6786aabe0159ea53f53f0
Source167:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/oc.xpi
# Source167-md5:	6a55011e1189ee74a12f35d23c40106b
Source168:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source168-md5:	74bce03e4f95d0a0e1d7cd04a737a5e0
Source169:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source169-md5:	2e4ea6d4c9e711cbfd3af3a4cfa269c3
Source170:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source170-md5:	1264a15a2c91db2761e6c939124dab8c
Source171:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source171-md5:	a0256e55724cfb522d5553edf32474d9
Source172:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source172-md5:	53c16847b2ea9f5a93ff93638898cee6
Source173:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source173-md5:	45d0197445e8bf0edb5bf833f0eae8ce
Source174:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source174-md5:	c3e14f17b5cad3495d8f165e05d81821
Source175:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source175-md5:	3c7ec02f11bb3be36e578823f5e7eda1
Source176:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source176-md5:	869f00eb73bd6ce1c064e4dfba532687
Source177:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source177-md5:	81349c8e4dc65922ef23b2e86d594444
Source178:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source178-md5:	415b557d422cd8aa36a9e1832b2f9f16
Source179:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source179-md5:	20e6e91c1126612b912c3013a5ab6001
Source180:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source180-md5:	1aa7720e63d6cd31365561fa4af37db5
Source181:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source181-md5:	2ab6f6a198130b126305c35c8cfad9ea
Source182:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source182-md5:	0d6ad760f9a7e71f262e526dbaf2efdf
Source183:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source183-md5:	4cd85b7d75b2819c182aba146dc53c19
Source184:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source184-md5:	4f1081df3fa581a5c3f50bdc652a75fa
Source185:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source185-md5:	cf3111d4961e7cb75541bd0ab5f1c3db
Source186:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source186-md5:	789673ed6058c8392fd1de9d1a7cc33f
Source187:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ur.xpi
# Source187-md5:	d8dba8ccb9dea39222025b36bfe4f9f3
Source188:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/uz.xpi
# Source188-md5:	cc80ca8126c64b0a6d08b3f61d384ba3
Source189:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source189-md5:	70574866049639095e4b593543d90745
Source190:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source190-md5:	905e66696ff1b19c72a07244e192a9b2
Source191:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source191-md5:	aa12cc26847ac002dd0435e7dcd8f8b2
Source192:	http://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source192-md5:	3837f29330593e310a87a9daa36157d5

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
%{?with_system_icu:BuildRequires:	libicu-devel >= 67.1}
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
BuildRequires:	nodejs >= 10.19
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
BuildRequires:	python3-virtualenv >= 16
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	rust >= 1.32.0
BuildRequires:	rust-cbindgen >= 0.14.1
BuildRequires:	sed >= 4.0
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
%{?with_system_libvpx:Requires:	libvpx >= 1.8.0}
Requires:	libwebp >= 1.0.2
Requires:	myspell-common
Requires:	nspr >= 1:%{nspr_ver}
Requires:	nss >= 1:%{nss_ver}
Requires:	pango >= 1:1.22.0
Requires:	pixman >= 0.19.2
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
%define		_noautoreq	liblgpllibs.so libmozavcodec.so libmozavutil.so libmozgtk.so libmozjs.so libmozsandbox.so libmozsqlite3.so libmozwayland.so libxul.so

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
export CFLAGS="%{rpmcflags} %{!?with_system_libvpx:-mmmx} -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="%{rpmcxxflags} -mmmx -D_FILE_OFFSET_BITS=64"
%else
export CFLAGS="%{rpmcflags} -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="%{rpmcxxflags} -D_FILE_OFFSET_BITS=64"
%endif

%if %{with lowmem}
export CFLAGS="$CFLAGS -g0"
export CXXFLAGS="$CXXFLAGS -g0"
export MOZ_DEBUG_FLAGS=" "
export LLVM_USE_SPLIT_DWARF=1
export LLVM_PARALLEL_LINK_JOBS=1
export MOZ_LINK_FLAGS="-Wl,--no-keep-memory -Wl,--reduce-memory-overheads"
export RUSTFLAGS="-Cdebuginfo=0"
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
ac_add_options --disable-necko-wifi
ac_add_options --disable-updater
ac_add_options --enable-alsa
ac_add_options --enable-chrome-format=omni
ac_add_options --enable-default-toolkit=cairo-gtk3
ac_add_options --enable-extensions=default
%{?with_geckodriver:ac_add_options --enable-geckodriver}
%{?with_gold:ac_add_options --enable-linker=gold}
%ifarch %{ix86} %{x8664} %{arm}
ac_add_options --disable-elf-hack
%endif
%if %{with lto}
ac_add_options --enable-lto
%endif
%{?with_clang:ac_add_options --enable-linker=lld}
%{?with_shared_js:ac_add_options --enable-shared-js}
%{?with_system_cairo:ac_add_options --enable-system-cairo}
ac_add_options --enable-system-ffi
%{?with_official:ac_add_options --enable-official-branding}
ac_add_options --with-distribution-id=org.pld-linux
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
EOF

%if ! %{with clang}
# On x86_64 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
MOZ_PARALLEL_BUILD=1
%ifarch %{x8664}
jobs="%{__jobs}"
[ -n "$jobs" -a "$jobs" -gt 4 ] && MOZ_PARALLEL_BUILD=4 || MOZ_PARALLEL_BUILD="$jobs"
%endif
export MOZ_PARALLEL_BUILD
%else
%{?__jobs:export MOZ_PARALLEL_BUILD="%__jobs"}
%endif

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
%{_libdir}/%{name}/browser/omni.ja

%{_libdir}/%{name}/browser/features/doh-rollout@mozilla.org.xpi
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

%dir %{_libdir}/%{name}
%{_libdir}/%{name}/platform.ini
%{?with_shared_js:%attr(755,root,root) %{_libdir}/%{name}/libmozjs.so}
%attr(755,root,root) %{_libdir}/%{name}/liblgpllibs.so
%attr(755,root,root) %{_libdir}/%{name}/libxul.so
%attr(755,root,root) %{_libdir}/%{name}/libmozavcodec.so
%attr(755,root,root) %{_libdir}/%{name}/libmozavutil.so
%ifarch %{ix86} %{x8664}
%attr(755,root,root) %{_libdir}/%{name}/libmozsandbox.so
%endif
%attr(755,root,root) %{_libdir}/%{name}/libmozsqlite3.so
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
