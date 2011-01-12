#!/usr/bin/make

.PHONY: all
all: updateWS

.PHONY: updateWS
updateWS:
	bin/wsdl2py -b src/gites/walhebcalendar/booking.wsdl -o src/gites/walhebcalendar/zsi
