#!/bin/bash
wget http://localhost:15672/cli/rabbitmqadmin -O rabbitmqadmin
chmod +x rabbitmqadmin
./rabbitmqadmin -u admin -p walhebcalendar declare vhost name=/walhebcalendar
./rabbitmqadmin -u admin -p walhebcalendar --vhost=/walhebcalendar declare permission vhost=/walhebcalendar user=admin configure=.* write=.* read=.*
./rabbitmqadmin -u admin -p walhebcalendar --vhost=/walhebcalendar declare exchange name=booking.update type=direct durable=true
./rabbitmqadmin -u admin -p walhebcalendar --vhost=/walhebcalendar declare queue name=booking.update.fromwalhebcalendar durable=true
./rabbitmqadmin -u admin -p walhebcalendar --vhost=/walhebcalendar declare binding source=booking.update destination=booking.update.fromwalhebcalendar routing_key=gdw
