# TODO:
# - consider --enable-libproxy
# - do something with *.rdf file, there if file conflict with other lang packages
# - enable RLBox (requires "wasi sysroot" in essence wasm/wasi toolchain, ie packaged wasm-sdk
#   https://github.com/WebAssembly/wasi-sdk)
#
# Conditional build:
%bcond_with	tests		# enable tests (whatever they check)
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
%bcond_with	lowmem2		# even lower memory requirements at cost of build time
%bcond_with	rust_simd	# enable SIMD in Rust code

%if %{with lto}
%define		with_clang	1
%undefine	with_gold
%endif

%ifarch %{ix86} %{arm} aarch64
%define		with_lowmem	1
%endif

%ifarch %{arm} aarch64 riscv64
%define		with_v4l2	1
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
U=https://releases.mozilla.org/pub/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

%define		nspr_ver	4.32
%define		nss_ver		3.112

Summary:	Firefox web browser
Summary(hu.UTF-8):	Firefox web böngésző
Summary(pl.UTF-8):	Firefox - przeglądarka WWW
Name:		firefox
Version:	141.0
Release:	1
License:	MPL v2.0
Group:		X11/Applications/Networking
Source0:	https://releases.mozilla.org/pub/firefox/releases/%{version}/source/firefox-%{version}.source.tar.xz
# Source0-md5:	468ccc01fde417e6286e43ae17060aef
Source3:	%{name}.desktop
Source4:	%{name}.sh
Source5:	vendor.js
Source6:	vendor-ac.js
Source100:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source100-md5:	4681754a7784448f9996dbc41eb17293
Source101:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source101-md5:	45b8680ed168dcb56f6a391eb81a99a3
Source102:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source102-md5:	6a2f0e2e476de2540554fcddf221dc77
Source103:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source103-md5:	2632b32d67c942dce201b8824619a8dc
Source104:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source104-md5:	521260367349ad5e50732e4287497ad3
Source105:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source105-md5:	21bfa6d770ef4faadfd4eda099d2c611
Source106:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source106-md5:	9e8b0879f9e9dc0913657db93bbe9452
Source107:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source107-md5:	251e214069ee654231b61248a0caef23
Source108:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bn.xpi
# Source108-md5:	e1901daaf1fc4d27178693275b618c91
Source109:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source109-md5:	f364989ef6ac6056594830575a339c99
Source110:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source110-md5:	c9aa474e6d0314d950ed3a031ab2e0a2
Source111:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source111-md5:	a33bd55cffb67548d984988daee7de3a
Source112:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ca-valencia.xpi
# Source112-md5:	a076cf044e2bc63763edf1f5ec420e50
Source113:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cak.xpi
# Source113-md5:	7aa1e86d81b8ac591310e35c4a06487b
Source114:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source114-md5:	e23899e54c838849f281dbcf6172bddf
Source115:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source115-md5:	2652b593f2fe16503affb46d444e78ce
Source116:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source116-md5:	92dcb639fffb3904e125bb485251320c
Source117:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source117-md5:	ef49d4464bd080558f857c2b4e32dedd
Source118:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source118-md5:	b59ec60315dbf81954dab917a64c568a
Source119:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source119-md5:	99e55cf4211aaaa498db26997d4ed6a3
Source120:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-CA.xpi
# Source120-md5:	c39d993e86030eb115e3b27ba9ba8eb9
Source121:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source121-md5:	6762b5356ec91bdde916ceabc17aaecf
Source122:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source122-md5:	04083458a5915e14aa34e43de36904d1
Source123:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source123-md5:	bb3e98ebef0ef99c16540558a4214255
Source124:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source124-md5:	8cbef103f0a34f1d937a6e87fa33a80f
Source125:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source125-md5:	8f433399620bf7af9d48eed44484a207
Source126:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source126-md5:	5d54629a8200cacf0d4a026ee80a59b1
Source127:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source127-md5:	4b1f2ab0fb2396027cf03a2fb06175b2
Source128:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source128-md5:	cf3d19a22ce8afd5ce496d8fdc01016e
Source129:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source129-md5:	6789b2481a1eed6d32eaec88f94b7ac4
Source130:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source130-md5:	dc7007dfc7c10523a7adf0cf1e037503
Source131:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source131-md5:	07f0e9c8bf6059b1d0f1c40023bb4de3
Source132:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source132-md5:	7034bfd22c5bdec36127c3149b1f1c72
Source133:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source133-md5:	f6d15177967ca343de4292b36d16ef4b
Source134:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fur.xpi
# Source134-md5:	b8ec75d5a266e354bffc585b8b21360e
Source135:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source135-md5:	79b3b6aa16c9fbc3926153bd74bdd2ad
Source136:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source136-md5:	fbf5e68c3511fb232ecf34b0cf962d2e
Source137:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source137-md5:	a5931161d0c36d005ed8804ef341f5f6
Source138:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source138-md5:	c57ee2ea1d2f7b683d5505be61cb3d76
Source139:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gn.xpi
# Source139-md5:	4ec93b3d0d1b07964cbf8529fca80b1c
Source140:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source140-md5:	40040565dc6fb5270b73db5f8e6e402a
Source141:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source141-md5:	c726e4607b55dde04869eb4b73510b95
Source142:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source142-md5:	1ff1a216bb79659020b7043a40872853
Source143:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source143-md5:	b2ec9bbbbbff0fcf50df4856bc0336b8
Source144:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source144-md5:	a4c5c51b9e2af7d7c6e4e78b1dce0ba0
Source145:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source145-md5:	34e65b02de31cafca774fb5ad70d22d1
Source146:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source146-md5:	24eb1232d6c508980f8cb27de9a5aad9
Source147:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ia.xpi
# Source147-md5:	f62609c51c0b057e11f76a51c3236a0e
Source148:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source148-md5:	c50f9fa2f5a24b8a3a07b5c2990741e3
Source149:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source149-md5:	1d97fd267e1f39f2ab6baaf68e1bac77
Source150:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source150-md5:	928d7ff7d59f9745281380420350a62d
Source151:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source151-md5:	60767783f9c4a4b81c02fe63b444de64
Source152:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ka.xpi
# Source152-md5:	4758be4ed25aa45be42db9da498ca328
Source153:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/kab.xpi
# Source153-md5:	d8e919c78b8b85eac98ab28531c167ea
Source154:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source154-md5:	e24a63520615ee447f73b0e11e69c92c
Source155:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source155-md5:	63c62f2434c0ee2d6cb11c6cb494885d
Source156:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source156-md5:	55fef0724bd88dec21e7377c6a0557f5
Source157:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source157-md5:	a9247a6968f7e6ca86ed692a23e79715
Source158:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source158-md5:	98230d76d579cb8840e403898c1abd30
Source159:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source159-md5:	c1d883ed57afb51343411968dfe20ed0
Source160:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source160-md5:	28a3ef8243bc500f5fe87f6fb3020783
Source161:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source161-md5:	a07e0ea3f93ed2cedbbf6d52448a430e
Source162:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source162-md5:	4cca95f827ba06559f0e19356c5d3707
Source163:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source163-md5:	0d5a298772b23abf98fc02a6d75eb39e
Source164:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/my.xpi
# Source164-md5:	3a13a0c462eeb7d5c7fa1ec5e0503144
Source165:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source165-md5:	a25afb5179e9d840c196e2c405010f1a
Source166:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ne-NP.xpi
# Source166-md5:	bdbf6067bb9d2bdbd58795b75d9a3da5
Source167:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source167-md5:	3b819b1d5576fd352fa862a4b4dae3a0
Source168:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source168-md5:	f3920ac139f10ecfa7e6f5e1f7813c1c
Source169:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/oc.xpi
# Source169-md5:	3b12754acc4102bdcccb302a4a8a156d
Source170:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source170-md5:	6c1233967da1b352f10aa8adbf965c61
Source171:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source171-md5:	3d9d487e24434153a38cd429e76d6710
Source172:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source172-md5:	9637e7296137928a5fa8f0df62a38e55
Source173:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source173-md5:	1b4027b9d647f39ee3786a85af52a15b
Source174:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source174-md5:	70ad3fae2631a13ac74da1b2d92a3dcc
Source175:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source175-md5:	5f81320ccaef1dc17dcdad2ac46fb456
Source176:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source176-md5:	1adb7830452d88ff8bef0656526e51f3
Source177:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sat.xpi
# Source177-md5:	9c6d0ca9a9379d06820afa9ee7378d0b
Source178:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sc.xpi
# Source178-md5:	22642a24e83bb326c500831bbd817146
Source179:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sco.xpi
# Source179-md5:	47c31367ad88c0a9ab6a63e53c4788f0
Source180:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source180-md5:	6a820fd1223e80da57163c8545c9261d
Source181:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source181-md5:	fb909e1157a4d6f63232653292e288d0
Source182:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/skr.xpi
# Source182-md5:	63b62f6d13f4b625dbe6a850f1a69afc
Source183:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source183-md5:	6647dc21012bd981cf9a7f006dcfad13
Source184:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source184-md5:	bf242babeb6edcc47bd5f9faa781995d
Source185:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source185-md5:	d0609886fb48d7e2c409530cea1cb16a
Source186:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source186-md5:	b7e7986d2f06e1a510ffcfa3e7c342c6
Source187:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source187-md5:	5608598c9980a33e975c6d72895ad1d3
Source188:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/szl.xpi
# Source188-md5:	86e76849cd2c5a6e5f65362e236f27cd
Source189:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source189-md5:	3c13595b1cc9897eea6c376b9fe35556
Source190:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source190-md5:	e928bf561be6e685ecf54323bf10c747
Source191:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/tg.xpi
# Source191-md5:	80765e7bc71f7a647f89e818943ed553
Source192:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source192-md5:	7f90f6913b5f582e043f02fa4360ce25
Source193:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/tl.xpi
# Source193-md5:	8fff84fae5eed8e5a1ff0419ddb4a701
Source194:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source194-md5:	0196821a4f0b9e0ec5289885a150fb42
Source195:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/trs.xpi
# Source195-md5:	4f60afa3498fb9352e985a597f444e61
Source196:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source196-md5:	370bc6d2a903eb59a986f18a1ff319c2
Source197:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/ur.xpi
# Source197-md5:	cf04fdffef7159804a7ee6fe157a4081
Source198:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/uz.xpi
# Source198-md5:	9e115eb0b5923a674ab902a6f29b83a2
Source199:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source199-md5:	cc00ddaf2082999ce6c8153564fe6540
Source200:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source200-md5:	6cee7d2419e4879f0538de3d19e04377
Source201:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source201-md5:	de86dd431e0eaf84311ca817b751c070
Source202:	https://releases.mozilla.org/pub/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source202-md5:	f93a6ec8468ba151eb20ef26cabd73a5
Patch1:		system-av1-link.patch
Patch4:		%{name}-prefs.patch
Patch5:		%{name}-pld-bookmarks.patch
Patch7:		%{name}-middle_click_paste.patch
Patch9:		%{name}-Disable-Firefox-Health-Report.patch
Patch10:	system-cairo.patch
Patch11:	glibc-double.patch
URL:		https://www.mozilla.org/firefox/
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	OpenGL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	aom-devel >= 3.0.0
BuildRequires:	autoconf2_13
BuildRequires:	automake
%{?with_gold:BuildRequires:	binutils >= 3:2.20.51.0.7}
%{?with_system_cairo:BuildRequires:	cairo-devel >= 1.10.2-5}
BuildRequires:	cargo >= 1.32.0
%{?with_clang:BuildRequires:	clang >= 8.0}
BuildRequires:	clang-devel >= 8.0
BuildRequires:	dav1d-devel >= 1.2.1
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	fontconfig-devel >= 1:2.7.0
BuildRequires:	freetype-devel >= 1:2.2.1
%{!?with_clang:BuildRequires:	gcc-c++ >= 6:8.1.0}
BuildRequires:	glib2-devel >= 1:2.42
BuildRequires:	gtk+3-devel >= 3.14.0
%ifnarch %arch_with_atomics64
BuildRequires:	libatomic-devel
%endif
BuildRequires:	libdrm-devel
# DECnet (dnprogs.spec), not dummy net (libdnet.spec)
#BuildRequires:	libdnet-devel
BuildRequires:	libevent-devel >= 1.4.7
# standalone libffi 3.0.9 or gcc's from 4.5(?)+
BuildRequires:	libffi-devel >= 7:3.0.9
%{?with_system_icu:BuildRequires:	libicu-devel >= 76.1}
# requires libjpeg-turbo implementing at least libjpeg 6b API
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng(APNG)-devel >= 0.10
BuildRequires:	libpng-devel >= 2:1.6.45
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libxcb-devel
%{?with_system_libvpx:BuildRequires:	libvpx-devel >= 1.10.0}
BuildRequires:	libwebp-devel >= 1.0.2
%{?with_clang:BuildRequires:	lld}
BuildRequires:	llvm-devel >= 8.0
%ifarch %{ix86} %{x8664}
BuildRequires:	nasm >= 2.14
%endif
# or --disable-nodejs ?
BuildRequires:	nodejs >= 12.22.12
BuildRequires:	nspr-devel >= 1:%{nspr_ver}
BuildRequires:	nss-devel >= 1:%{nss_ver}
BuildRequires:	pango-devel >= 1:1.22.0
BuildRequires:	pixman-devel >= 0.36.0
%ifarch %{arm}
BuildRequires:	perl-modules >= 5.006
%endif
BuildRequires:	pipewire-devel >= 0.3
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	pkgconfig(libffi) >= 3.0.9
BuildRequires:	pulseaudio-devel
BuildRequires:	python3-devel-tools
BuildRequires:	python3-modules >= 1:3.9
%{?with_pgo:BuildRequires:	python3-modules-sqlite}
BuildRequires:	python3-setuptools
BuildRequires:	python3-simplejson
BuildRequires:	python3-virtualenv >= 20
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.025
BuildRequires:	rust >= 1.82.0
BuildRequires:	rust-cbindgen >= 0.27.0
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.4.0
BuildRequires:	xorg-lib-libXtst-devel
%{?with_pgo:BuildRequires:	xorg-xserver-Xvfb}
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.4.1
BuildRequires:	xz
%ifarch %{ix86} %{x8664}
BuildRequires:	yasm >= 1.2
%endif
BuildRequires:	unzip
BuildRequires:	zip
BuildRequires:	zlib-devel >= 1.2.3
BuildConflicts:	%{name}-devel < %{version}
BuildConflicts:	python3-psutil < 5.4.2
BuildConflicts:	python3-psutil > 5.8.0
Requires(post):	mktemp >= 1.5-18
Requires:	aom >= 3.0.0
Requires:	browser-plugins >= 2.0
%{?with_system_cairo:Requires:	cairo >= 1.10.2-5}
Requires:	dav1d >= 1.2.1
Requires:	dbus-libs >= 0.60
Requires:	desktop-file-utils
Requires:	fontconfig-libs >= 1:2.7.0
Requires:	freetype >= 1:2.2.1
Requires:	glib2 >= 1:2.42
Requires:	gtk+3 >= 3.14.0
Requires:	hicolor-icon-theme
Requires:	libjpeg-turbo
Requires:	libpng >= 2:1.6.45
Requires:	libpng(APNG) >= 0.10
%{?with_system_libvpx:Requires:	libvpx >= 1.10.0}
Requires:	libwebp >= 1.0.2
Requires:	myspell-common
%requires_ge_to	nspr nspr-devel
%requires_ge_to	nss nss-devel
Requires:	pango >= 1:1.22.0
Requires:	pixman >= 0.36.0
Requires:	xorg-lib-libXrandr >= 1.4.0
Requires:	xorg-lib-libxkbcommon >= 0.4.1
%ifarch %{ix86}
Requires:	cpuinfo(mmx)
%endif
Provides:	xulrunner-libs = 2:%{version}-%{release}
Provides:	wwwbrowser
Obsoletes:	firefox-devel < 53
Obsoletes:	firefox-lang-as < 68.0-1
Obsoletes:	firefox-lang-en_ZA < 68.0-1
Obsoletes:	firefox-lang-mai < 68.0-1
Obsoletes:	firefox-lang-ml < 68.0-1
Obsoletes:	firefox-lang-or < 68.0-1
Obsoletes:	firefox-libs < 53
Obsoletes:	iceweasel < 45
Obsoletes:	iceweasel-libs < 45
Obsoletes:	mozilla-firebird < 0.8
Obsoletes:	mozilla-firefox < 38
Obsoletes:	mozilla-firefox-lang-en < 2.0.0.8-3
Obsoletes:	mozilla-firefox-libs < 38
Obsoletes:	xulrunner < 2:42
Obsoletes:	xulrunner-gnome < 2:42
Obsoletes:	xulrunner-libs < 2:42
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
%define		_noautoreq	libgkcodecs.so liblgpllibs.so libmozavcodec.so libmozavutil.so libmozgtk.so libmozjs.so libmozsandbox.so libmozsqlite3.so libmozwayland.so libxul.so

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
Obsoletes:	iceweasel-lang-ach < 45
Obsoletes:	mozilla-firefox-lang-ach < 38
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
Obsoletes:	iceweasel-lang-af < 45
Obsoletes:	mozilla-firefox-lang-af < 38
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
Obsoletes:	iceweasel-lang-an < 45
Obsoletes:	mozilla-firefox-lang-an < 38
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
Obsoletes:	iceweasel-lang-ar < 45
Obsoletes:	mozilla-firefox-lang-ar < 38
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
Obsoletes:	iceweasel-lang-ast < 45
Obsoletes:	mozilla-firefox-lang-ast < 38
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
Obsoletes:	iceweasel-lang-az < 45
Obsoletes:	mozilla-firefox-lang-az < 38
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
Obsoletes:	iceweasel-lang-be < 45
Obsoletes:	mozilla-firefox-lang-be < 38
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
Obsoletes:	iceweasel-lang-bg < 45
Obsoletes:	mozilla-firefox-lang-bg < 38
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
Obsoletes:	firefox-lang-bn_IN < 68
Obsoletes:	iceweasel-lang-bn < 45
Obsoletes:	iceweasel-lang-bn_IN < 45
Obsoletes:	mozilla-firefox-lang-bn < 38
Obsoletes:	mozilla-firefox-lang-bn_IN < 38
BuildArch:	noarch

%description lang-bn
Bengali (Bangladesh) resources for Firefox.

%description lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu).

%package lang-br
Summary:	Breton resources for Firefox
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-br < 45
Obsoletes:	mozilla-firefox-lang-br < 38
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
Obsoletes:	iceweasel-lang-bs < 45
Obsoletes:	mozilla-firefox-lang-bs < 38
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
Obsoletes:	iceweasel-lang-ca < 45
Obsoletes:	mozilla-firefox-lang-ca < 38
BuildArch:	noarch

%description lang-ca
Catalan resources for Firefox.

%description lang-ca -l ca.UTF-8
Recursos catalans per Firefox.

%description lang-ca -l es.UTF-8
Recursos catalanes para Firefox.

%description lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Firefoksa.

%package lang-ca-valencia
Summary:	Catalan (Valencia variant) resources for Firefox
Summary(pl.UTF-8):	Katalońskie pliki językowe (wariant dla Walencji) dla Firefoksa
Group:		I18n
URL:		http://www.softcatala.org/projectes/mozilla/
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-ca-valencia
Catalan (Valencia variant) resources for Firefox.

%description lang-ca-valencia -l pl.UTF-8
Katalońskie pliki językowe (wariant dla Walencji) dla Firefoksa.

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
Obsoletes:	iceweasel-lang-cs < 45
Obsoletes:	mozilla-firefox-lang-cs < 38
BuildArch:	noarch

%description lang-cs
Czech resources for Firefox.

%description lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Firefoksa.

%package lang-cy
Summary:	Welsh resources for Firefox
Summary(pl.UTF-8):	Walijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-cy < 45
Obsoletes:	mozilla-firefox-lang-cy < 38
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
Obsoletes:	iceweasel-lang-da < 45
Obsoletes:	mozilla-firefox-lang-da < 38
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
Obsoletes:	iceweasel-lang-de < 45
Obsoletes:	mozilla-firefox-lang-de < 38
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
Obsoletes:	iceweasel-lang-dsb < 45
Obsoletes:	mozilla-firefox-lang-dsb < 38
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
Obsoletes:	iceweasel-lang-el < 45
Obsoletes:	mozilla-firefox-lang-el < 38
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
Obsoletes:	iceweasel-lang-en_GB < 45
Obsoletes:	mozilla-firefox-lang-en_GB < 38
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
Obsoletes:	iceweasel-lang-en_US < 45
Obsoletes:	mozilla-firefox-lang-en_US < 38
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
Obsoletes:	iceweasel-lang-eo < 45
Obsoletes:	mozilla-firefox-lang-eo < 38
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
Obsoletes:	iceweasel-lang-es_AR < 45
Obsoletes:	mozilla-firefox-lang-es_AR < 38
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
Obsoletes:	iceweasel-lang-es_CL < 45
Obsoletes:	mozilla-firefox-lang-es_CL < 38
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
Obsoletes:	iceweasel-lang-es < 45
Obsoletes:	mozilla-firefox-lang-es < 38
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
Obsoletes:	iceweasel-lang-es_MX < 45
Obsoletes:	mozilla-firefox-lang-es_MX < 38
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
Obsoletes:	iceweasel-lang-et < 45
Obsoletes:	mozilla-firefox-lang-et < 38
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
Obsoletes:	iceweasel-lang-eu < 45
Obsoletes:	mozilla-firefox-lang-eu < 38
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
Obsoletes:	iceweasel-lang-fa < 45
Obsoletes:	mozilla-firefox-lang-fa < 38
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
Obsoletes:	iceweasel-lang-ff < 45
Obsoletes:	mozilla-firefox-lang-ff < 38
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
Obsoletes:	iceweasel-lang-fi < 45
Obsoletes:	mozilla-firefox-lang-fi < 38
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
Obsoletes:	iceweasel-lang-fr < 45
Obsoletes:	mozilla-firefox-lang-fr < 38
BuildArch:	noarch

%description lang-fr
French resources for Firefox.

%description lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Firefoksa.

%package lang-fur
Summary:	Friulian resources for Firefox
Summary(pl.UTF-8):	Friulskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-fur
Friulian resources for Firefox.

%description lang-fur -l pl.UTF-8
Friulskie pliki językowe dla Firefoksa.

%package lang-fy
Summary:	Frisian resources for Firefox
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-fy < 45
Obsoletes:	mozilla-firefox-lang-fy < 38
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
Obsoletes:	iceweasel-lang-ga < 45
Obsoletes:	mozilla-firefox-lang-ga < 38
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
Obsoletes:	iceweasel-lang-gd < 45
Obsoletes:	mozilla-firefox-lang-gd < 38
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
Obsoletes:	iceweasel-lang-gl < 45
Obsoletes:	mozilla-firefox-lang-gl < 38
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
Obsoletes:	iceweasel-lang-gn < 45
Obsoletes:	mozilla-firefox-lang-gn < 38
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
Obsoletes:	iceweasel-lang-gu < 45
Obsoletes:	mozilla-firefox-lang-gu < 38
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
Obsoletes:	iceweasel-lang-he < 45
Obsoletes:	mozilla-firefox-lang-he < 38
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
Obsoletes:	iceweasel-lang-hi < 45
Obsoletes:	mozilla-firefox-lang-hi < 38
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
Obsoletes:	iceweasel-lang-hr < 45
Obsoletes:	mozilla-firefox-lang-hr < 38
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
Obsoletes:	iceweasel-lang-hsb < 45
Obsoletes:	mozilla-firefox-lang-hsb < 38
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
Obsoletes:	iceweasel-lang-hu < 45
Obsoletes:	mozilla-firefox-lang-hu < 38
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
Obsoletes:	iceweasel-lang-hy < 45
Obsoletes:	mozilla-firefox-lang-hy < 38
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
Obsoletes:	iceweasel-lang-id < 45
Obsoletes:	mozilla-firefox-lang-id < 38
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
Obsoletes:	iceweasel-lang-is < 45
Obsoletes:	mozilla-firefox-lang-is < 38
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
Obsoletes:	iceweasel-lang-it < 45
Obsoletes:	mozilla-firefox-lang-it < 38
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
Obsoletes:	iceweasel-lang-ja < 45
Obsoletes:	mozilla-firefox-lang-ja < 38
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
Obsoletes:	iceweasel-lang-ka < 45
Obsoletes:	mozilla-firefox-lang-ka < 38
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
Obsoletes:	iceweasel-lang-kk < 45
Obsoletes:	mozilla-firefox-lang-kk < 38
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
Obsoletes:	iceweasel-lang-km < 45
Obsoletes:	mozilla-firefox-lang-km < 38
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
Obsoletes:	iceweasel-lang-kn < 45
Obsoletes:	mozilla-firefox-lang-kn < 38
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
Obsoletes:	iceweasel-lang-ko < 45
Obsoletes:	mozilla-firefox-lang-ko < 38
BuildArch:	noarch

%description lang-ko
Korean resources for Firefox.

%description lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Firefoksa.

%package lang-lij
Summary:	Ligurian resources for Firefox
Summary(pl.UTF-8):	Liguryjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-lij < 45
Obsoletes:	mozilla-firefox-lang-lij < 38
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
Obsoletes:	iceweasel-lang-lt < 45
Obsoletes:	mozilla-firefox-lang-lt < 38
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
Obsoletes:	iceweasel-lang-lv < 45
Obsoletes:	mozilla-firefox-lang-lv < 38
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
Obsoletes:	iceweasel-lang-mk < 45
Obsoletes:	mozilla-firefox-lang-mk < 38
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
Obsoletes:	iceweasel-lang-mr < 45
Obsoletes:	mozilla-firefox-lang-mr < 38
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
Obsoletes:	iceweasel-lang-ms < 45
Obsoletes:	mozilla-firefox-lang-ms < 38
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
Obsoletes:	iceweasel-lang-nb < 45
Obsoletes:	mozilla-firefox-lang-nb < 38
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
Obsoletes:	iceweasel-lang-nl < 45
Obsoletes:	mozilla-firefox-lang-nl < 38
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
Obsoletes:	iceweasel-lang-nn < 45
Obsoletes:	mozilla-firefox-lang-nn < 38
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
Obsoletes:	iceweasel-lang-pa < 45
Obsoletes:	mozilla-firefox-lang-pa < 38
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
Obsoletes:	iceweasel-lang-pl < 45
Obsoletes:	mozilla-firefox-lang-pl < 38
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
Obsoletes:	iceweasel-lang-pt_BR < 45
Obsoletes:	mozilla-firefox-lang-pt_BR < 38
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
Obsoletes:	iceweasel-lang-pt < 45
Obsoletes:	mozilla-firefox-lang-pt < 38
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
Obsoletes:	iceweasel-lang-rm < 45
Obsoletes:	mozilla-firefox-lang-rm < 38
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
Obsoletes:	iceweasel-lang-ro < 45
Obsoletes:	mozilla-firefox-lang-ro < 38
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
Obsoletes:	iceweasel-lang-ru < 45
Obsoletes:	mozilla-firefox-lang-ru < 38
BuildArch:	noarch

%description lang-ru
Russian resources for Firefox.

%description lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Firefoksa.

%package lang-sat
Summary:	Santali resources for Firefox
Summary(pl.UTF-8):	Pliki językowe santali dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-sat
Santali resources for Firefox.

%description lang-sat -l pl.UTF-8
Pliki językowe santali dla Firefoksa.

%package lang-sc
Summary:	Sardinian resources for Firefox
Summary(pl.UTF-8):	Sardyńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-sc
Sardinian resources for Firefox.

%description lang-sc -l pl.UTF-8
Sardyńskie pliki językowe dla Firefoksa.

%package lang-sco
Summary:	Scots resources for Firefox
Summary(pl.UTF-8):	Pliki językowe scots dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-sco
Scots resources for Firefox.

%description lang-sco -l pl.UTF-8
Pliki językowe scots dla Firefoksa.

%package lang-si
Summary:	Sinhala resources for Firefox
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-si < 45
Obsoletes:	mozilla-firefox-lang-si < 38
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
Obsoletes:	iceweasel-lang-sk < 45
Obsoletes:	mozilla-firefox-lang-sk < 38
BuildArch:	noarch

%description lang-sk
Slovak resources for Firefox.

%description lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Firefoksa.

%package lang-skr
Summary:	Saraiki resources for Firefox
Summary(pl.UTF-8):	Pliki językowe saraiki dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-skr
Saraiki resources for Firefox.

%description lang-skr -l pl.UTF-8
Pliki językowe saraiki dla Firefoksa.

%package lang-sl
Summary:	Slovene resources for Firefox
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-sl < 45
Obsoletes:	mozilla-firefox-lang-sl < 38
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
Obsoletes:	iceweasel-lang-son < 45
Obsoletes:	mozilla-firefox-lang-son < 38
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
Obsoletes:	iceweasel-lang-sq < 45
Obsoletes:	mozilla-firefox-lang-sq < 38
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
Obsoletes:	iceweasel-lang-sr < 45
Obsoletes:	mozilla-firefox-lang-sr < 38
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
Obsoletes:	iceweasel-lang-sv < 45
Obsoletes:	mozilla-firefox-lang-sv < 38
BuildArch:	noarch

%description lang-sv
Swedish resources for Firefox.

%description lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Firefoksa.

%package lang-szl
Summary:	Silesian resources for Firefox
Summary(pl.UTF-8):	Śląskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-szl
Silesian resources for Firefox.

%description lang-szl -l pl.UTF-8
Śląskie pliki językowe dla Firefoksa.

%package lang-ta
Summary:	Tamil (India) resources for Firefox
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-ta < 45
Obsoletes:	mozilla-firefox-lang-ta < 38
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
Obsoletes:	iceweasel-lang-te < 45
Obsoletes:	mozilla-firefox-lang-te < 38
BuildArch:	noarch

%description lang-te
Telugu resources for Firefox.

%description lang-te -l pl.UTF-8
Pliki językowe telugu dla Firefoksa.

%package lang-tg
Summary:	Tajik resources for Firefox
Summary(pl.UTF-8):	Tadżyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-tg
Tajik resources for Firefox.

%description lang-tg -l pl.UTF-8
Tadżyckie pliki językowe dla Firefoksa.

%package lang-th
Summary:	Thai resources for Firefox
Summary(pl.UTF-8):	Tajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-th < 45
Obsoletes:	mozilla-firefox-lang-th < 38
BuildArch:	noarch

%description lang-th
Thai resources for Firefox.

%description lang-th -l pl.UTF-8
Tajskie pliki językowe dla Firefoksa.

%package lang-tl
Summary:	Tagalog resources for Firefox
Summary(pl.UTF-8):	Tagalskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-tl
Tagalog resources for Firefox.

%description lang-tl -l pl.UTF-8
Tagalskie pliki językowe dla Firefoksa.

%package lang-tr
Summary:	Turkish resources for Firefox
Summary(pl.UTF-8):	Tureckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-tr < 45
Obsoletes:	mozilla-firefox-lang-tr < 38
BuildArch:	noarch

%description lang-tr
Turkish resources for Firefox.

%description lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Firefoksa.

%package lang-trs
Summary:	Triqui (Oaxaca) resources for Firefox
Summary(pl.UTF-8):	Pliki językowe trike czikauastlańskiego dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
BuildArch:	noarch

%description lang-trs
Triqui (Oaxaca) resources for Firefox.

%description lang-trs -l pl.UTF-8
Pliki językowe trike czikauastlańskiego dla Firefoksa.

%package lang-uk
Summary:	Ukrainian resources for Firefox
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	firefox >= %{version}
Provides:	firefox-lang-resources = %{version}
Obsoletes:	iceweasel-lang-uk < 45
Obsoletes:	mozilla-firefox-lang-uk < 38
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
Obsoletes:	iceweasel-lang-uz < 45
Obsoletes:	mozilla-firefox-lang-uz < 38
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
Obsoletes:	iceweasel-lang-vi < 45
Obsoletes:	mozilla-firefox-lang-vi < 38
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
Obsoletes:	iceweasel-lang-xh < 45
Obsoletes:	mozilla-firefox-lang-xh < 38
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
Obsoletes:	iceweasel-lang-zh_CN < 45
Obsoletes:	mozilla-firefox-lang-zh_CN < 38
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
Obsoletes:	iceweasel-lang-zh_TW < 45
Obsoletes:	mozilla-firefox-lang-zh_TW < 38
BuildArch:	noarch

%description lang-zh_TW
Traditional Chinese resources for Firefox.

%description lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Firefoksa.

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
%setup -q
for s in %sources; do
	case $s in
	*.xpi)
		cp -p $s .
		;;
	esac
done

%patch -P1 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P7 -p1
%patch -P9 -p1
%{?with_system_cairo:%patch -P10 -p1}
%patch -P11 -p1

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
#export CARGO_INCREMENTAL=0  # candidate for with_lowmem2
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
# candidate for with_lowmem2
#ac_add_options --disable-unified-build
ac_add_options --disable-updater
ac_add_options --enable-alsa
ac_add_options --enable-chrome-format=omni
ac_add_options --enable-default-toolkit=cairo-gtk3-wayland
%{?with_geckodriver:ac_add_options --enable-geckodriver}
%{?with_gold:ac_add_options --enable-linker=gold}
%ifarch %{ix86} %{x8664} %{arm}
ac_add_options --disable-elf-hack
%endif
%if %{with lto}
ac_add_options --enable-lto=cross
%endif
%{?with_clang:ac_add_options --enable-linker=lld}
%{?with_rust_simd:ac_add_options --enable-rust-simd}
%{?with_shared_js:ac_add_options --enable-shared-js}
%{?with_system_cairo:ac_add_options --enable-system-cairo}
ac_add_options --enable-system-ffi
%{?with_official:ac_add_options --enable-official-branding}
ac_add_options --with-distribution-id=org.pld-linux
ac_add_options --with-system-av1
ac_add_options --with-system-gbm
ac_add_options --with%{!?with_system_icu:out}-system-icu
ac_add_options --with-system-jpeg
ac_add_options --with-system-libdrm
ac_add_options --with-system-libevent
ac_add_options --with%{!?with_system_libvpx:out}-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-pipewire
ac_add_options --with-system-pixman
ac_add_options --with-system-png
ac_add_options --with-system-webp
ac_add_options --with-system-zlib
ac_add_options --without-wasm-sandboxed-libraries
EOF

%if %{without clang}
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
export MOZBUILD_STATE_PATH="$(pwd)/.mozbuild"
export MACH_SYSTEM_ASSERTED_COMPATIBLE_WITH_BUILD_SITE=1
export MACH_SYSTEM_ASSERTED_COMPATIBLE_WITH_MACH_SITE=1
%if %{with pgo}
D=$(( RANDOM % (200 - 100 + 1 ) + 5 ))
/usr/bin/Xvfb :${D} &
XVFB_PID=$!
[ -n "$XVFB_PID" ] || exit 1
export DISPLAY=:${D}
MOZ_PGO=1 \
AUTOCONF=/usr/bin/autoconf2_13 \
MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=none \
./mach build
kill $XVFB_PID
%else
AUTOCONF=/usr/bin/autoconf2_13 \
MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=none \
./mach build %{?with_lowmem2:-j1}
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
%{?with_geckodriver:cp -aL ${OBJDIR}/dist/host/bin/geckodriver $RPM_BUILD_ROOT%{_bindir}/}

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
%attr(755,root,root) %{_libdir}/%{name}/glxtest
%attr(755,root,root) %{_libdir}/%{name}/pingsender
%{?with_v4l2:%attr(755,root,root) %{_libdir}/%{name}/v4l2test}
%attr(755,root,root) %{_libdir}/%{name}/vaapitest
%{_libdir}/%{name}/application.ini
%{_libdir}/%{name}/browser/omni.ja

%dir %{_libdir}/%{name}/fonts
%{_libdir}/%{name}/fonts/TwemojiMozilla.ttf

%dir %{_libdir}/%{name}/gmp-clearkey
%dir %{_libdir}/%{name}/gmp-clearkey/0.1
%{_libdir}/%{name}/gmp-clearkey/0.1/manifest.json
%attr(755,root,root) %{_libdir}/%{name}/gmp-clearkey/0.1/libclearkey.so

%dir %{_libdir}/%{name}
%{_libdir}/%{name}/platform.ini
%attr(755,root,root) %{_libdir}/%{name}/libgkcodecs.so
%{?with_shared_js:%attr(755,root,root) %{_libdir}/%{name}/libmozjs.so}
%attr(755,root,root) %{_libdir}/%{name}/liblgpllibs.so
%attr(755,root,root) %{_libdir}/%{name}/libxul.so
%attr(755,root,root) %{_libdir}/%{name}/libmozavcodec.so
%attr(755,root,root) %{_libdir}/%{name}/libmozavutil.so
%ifarch %{ix86} %{x8664} %{arm} aarch64
%attr(755,root,root) %{_libdir}/%{name}/libmozsandbox.so
%endif
%attr(755,root,root) %{_libdir}/%{name}/libmozsqlite3.so
%attr(755,root,root) %{_libdir}/%{name}/libmozwayland.so
%{_libdir}/%{name}/dependentlibs.list
%{_libdir}/%{name}/omni.ja
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

%files lang-ca-valencia
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ca-valencia@firefox.mozilla.org.xpi

%files lang-cak
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-cak@firefox.mozilla.org.xpi

%files lang-cs
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-cs@firefox.mozilla.org.xpi

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

%files lang-fur
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-fur@firefox.mozilla.org.xpi

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

%files lang-sat
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-sat@firefox.mozilla.org.xpi

%files lang-sc
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-sc@firefox.mozilla.org.xpi

%files lang-sco
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-sco@firefox.mozilla.org.xpi

%files lang-si
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-si@firefox.mozilla.org.xpi

%files lang-sk
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-sk@firefox.mozilla.org.xpi

%files lang-skr
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-skr@firefox.mozilla.org.xpi

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

%files lang-szl
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-szl@firefox.mozilla.org.xpi

%files lang-ta
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-ta@firefox.mozilla.org.xpi

%files lang-te
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-te@firefox.mozilla.org.xpi

%files lang-tg
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-tg@firefox.mozilla.org.xpi

%files lang-th
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-th@firefox.mozilla.org.xpi

%files lang-tl
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-tl@firefox.mozilla.org.xpi

%files lang-tr
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-tr@firefox.mozilla.org.xpi

%files lang-trs
%defattr(644,root,root,755)
%{_datadir}/%{name}/browser/extensions/langpack-trs@firefox.mozilla.org.xpi

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

%if %{with geckodriver}
%files geckodriver
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/geckodriver
%endif
