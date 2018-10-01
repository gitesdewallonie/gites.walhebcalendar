#!/usr/bin/make
#
# Makefile for Debian
#
VERSION=$(shell cat version.txt)

deb:
	gbp dch -a --ignore-branch -v
	dch -v $(VERSION).$(BUILD_NUMBER) release --no-auto-nmu
	dpkg-buildpackage -b -uc -us
	mv ../*.deb .

DEB=gites-walhebcalendar-website_$(VERSION).$(BUILD_NUMBER)_amd64.deb
publish-deb:
	curl -F file=@$(DEB) http://aptly-api.affinitic.be/api/files/$(DEB)
	curl -X POST http://aptly-api.affinitic.be/api/repos/stretch_production/file/$(DEB)
	curl -X POST -H 'Content-Type: application/json' --data '{"Distribution": "stretch", "SourceKind": "local", "Signing": {"Skip": true},"Sources": [{"Name": "stretch_production"}]}' http://aptly-api.affinitic.be/api/publish/repos

.PHONY: deb upgrade-db publish-deb
