====================
docker-postfix-relay
====================

Simple SMTP relay container

Allows other containers to connect anonymously to send emails, and then relays them
through your mail provider to ensure deliverability.


Usage
=====

In ``postfix-relay/``:

1. Copy ``docker-compose.yml.default`` to ``docker-compose.yml`` and customise the
   environment variables.

2. From your other service's ``docker-compose``, connect to the ``postfix-relay``
   network and send mail via the ``postfix-relay`` host on port 25::

      services:
        myservice:
          ...
          networks:
            - postfix-relay
      networks:
        postfix-relay:
          external: true


Environment variables
---------------------

``MAIL_HOST``
  Name to use for this originating mailserver. Should be legitimate FQDN.

``RELAY_HOST``, ``RELAY_PORT``
  Host and port of the SMTP server to relay to

``RELAY_USERNAME``, ``RELAY_PASSWORD``
  Credentials for ``RELAY_HOST``


Running a manual test
---------------------

Run ``postfix-relay`` first, then in ``sample/``:

1. Copy ``docker-compose.yml.default`` to ``docker-compose.yml`` and customise the
   environment variables.

2. Run ``docker-compose up`` to send the test message
