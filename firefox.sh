#!/bin/sh
# based on script by (c) vip at linux.pl, wolf at pld-linux.org

LIBDIR="@LIBDIR@/firefox"

# copy profile from Iceweasel if its available and if no Firefox
# profile exists
if [ ! -d $HOME/.mozilla/firefox ]; then
	if [ -d $HOME/.iceweasel ]; then
		echo "Copying profile from Iceweasel"
		cp -rf $HOME/.iceweasel $HOME/.mozilla/firefox
	fi
fi

# compreg.dat and/or chrome.rdf will screw things up if it's from an
# older version.  http://bugs.gentoo.org/show_bug.cgi?id=63999
for f in ~/.mozilla/firefox/*/{compreg.dat,chrome.rdf,XUL.mfasl}; do
	if [[ -f ${f} && ${f} -ot /usr/bin/firefox ]]; then
		echo "Removing ${f} leftover from older firefox"
		rm -f "${f}"
	fi
done

FIREFOX="$LIBDIR/firefox"
PWD=${PWD:-$(pwd)}

if [ -z "$1" ]; then
	exec $FIREFOX
elif [ $# -eq 1 -a "$1" = "${1#-}" ]; then
	if [ -f "$PWD/$1" ]; then
		URL="file://$PWD/$1"
	else
		URL="$1"
	fi
	if ! grep -q browser.tabs.opentabfor.middleclick.*false ~/.mozilla/firefox/*/prefs.js; then
		exec $FIREFOX -new-tab "$URL"
	else
		exec $FIREFOX -new-window "$URL"
	fi
else
	exec $FIREFOX "$@"
fi
