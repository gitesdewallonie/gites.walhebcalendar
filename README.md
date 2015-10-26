gites.walhebcalendar
====================

gites.walhebcalendar offre des webservices permettant de consulter et modifier les disponibilités d'un gîte de Wallonie.

Pour plus d'informations sur les webservices, voir http://doc.walhebcalendar.be/

Cependant, lorsqu'une disponibilité est mise à jour via ces webservices, la mise à jour ne se fait pas directement dans la base de données des gîtes de Wallonie. Un message sera envoyé à une queue RabbitMQ, celui ci sera consumé par un daemon qui vient du package gites.calendar. Les informations seront quand même enregistrées dans une DB postgresql walhebcalendar.


Déploiement localhost
---------------------

Vu la complexité du workflow, voici les étapes à suivre pour pouvoir tester tout le cheminement en local.

**RabbitMQ**

Assurez-vous que RabbitMQ soit installé et lancez le serveur sur votre machine:

rabbitmq-server

Vous pouvez maintenant accéder à l'interface de management via l'url http://localhost:15672 (il faudra éventuellement installer cette interface via la commande `rabbitmq-plugins enable rabbitmq_management`).

On utilise le port AMQP par défaut de RabbitMQ: 5672, il n'y a donc rien à changer à ce niveau là.

If faut par contre ajouter un utilisateur qui sera utilisé par le script de configuration. Ajoutez donc, via l'interface, un utilisateur admin:walhebcalendar qui possède le tag 'administrator'. Lors de la première connexion, vous pouvez vous connecter avec l'utilisateur guest:guest.

Lancez le script de configuration: ./setuprabbit.sh

Assurez-vous que l'utilisateur admin peut accéder aux virtual hosts '/, /walhebcalendar'.


**Webservice**

Installez le buildout comme d'habitude, mais en changeant la valeur de **AMQP_BROKER_HOST** par **localhost** dans le buildout.cfg. Le buildout utilise python 2.7.

Pour que l'instance démarre, il faut avoir un serveur PostgreSQL sur la machine et avoir créé la base de donnée `walhebcalendar`.

Lancer l'instance zope: bin/instance fg

Après avoir configuré les webservice grace au .wsdl disponible, vous pouvez essayer de les lancer via l'url http://localhost:6011/calendar

Si vous avez des problèmes de 'Not authorized', vous pouvez passer les permissions 'WalhebCalendar: Add Booking' et 'WalhebCalendar: View Bookings' dans la ZMI. Attention qu'il faut changer ces permissions à chaque lancement de l'instance.

TODO: trouver un meilleur moyen de ne pas avoir de 'Not authorized'

Pour la suite du workflow, voir la doc de https://github.com/gitesdewallonie/gites.calendar


Schéma
------

![Walhebcalendar workflow](https://www.lucidchart.com/publicSegments/view/55706155-0af0-4db6-9278-59a90a0050c0/image.png)
