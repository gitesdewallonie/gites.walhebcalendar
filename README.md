gites.walhebcalendar
====================

gites.walhebcalendar offre des webservice permettant de consuler et modifier les disponibilités d'un gite de Wallonie.

Pour plus d'informations sur les webservices, voir http://doc.walhebcalendar.be/

Cependant, lorsqu'une disponibilité est mise à jour via ces webservices, la mise à jour ne se fait pas directement dans la base de données des gites de Wallonie. Un message sera envoyé à une queue RabbitMQ, celui ci sera consumé par un daemon qui vient du package gites.calendar. Les informations seront quand meme enregistrées dans une DB postgresql walhebcalendar.


Déploiement localhost
---------------------

Vu la complexité du workflow, voici les étapes à suivre pour pouvoir tester tout le cheminement en local.

**RabbitMQ**

Assurez vous que RabbitMQ soit installé et lancer le serveur sur votre machine:

rabbitmq-server

Vous pouvez maintenant accéder à l'interface de management via l'url http://localhost:15672

On utilise le port AMQP par défaut de RabbitMQ: 5672, il n'y a donc rien à changer à ce niveau là.

If faut par contre ajouter un utilisateur qui sera utilisé par un script de configuration. Ajoutez donc, via l'interface, un utilisateur admin:walhebcalendar qui possède le tag 'administrator'.

Lancer le script de configuration: ./setuprabbit.sh

Assurez vous que l'utilisateur admin peut accéder aux virtual hosts '/, /walhebcalendar'.


**Webservice**

Installez le buildout comme d'habitude.

Lancer l'instance zope: bin/instance fg

Après avoir configuré les webservice grace au .wsdl disponible, vous pouvez essayer de les lancer via l'url http://localhost:6011/calendar

Si vous avez des problèmes de 'Not authorized', vous pouvez passer les permissions 'WalhebCalendar: Add Booking' et 'WalhebCalendar: View Bookings' dans la ZMI. Attention qu'il faut changer ces permissions à chaque lancement de l'instance.

TODO: trouver un meilleur moyen de ne pas avoir de 'Not authorized'

Pour la suite du workflow, voir la doc de gites.calendar
