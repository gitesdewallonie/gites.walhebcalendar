#!/usr/bin/make
#
# Makefile for Debian
#
VERSION=`cat version.txt`
deb:
	gbp dch -a --ignore-branch -v
	dch -v $(VERSION).$(BUILD_NUMBER) release --no-auto-nmu
	dpkg-buildpackage -b -uc -us

.PHONY: deb upgrade-db
