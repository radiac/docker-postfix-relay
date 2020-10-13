#!/bin/bash

# Reconfigure postfix using environment variables
postconf -e "myhostname = ${MAIL_HOST}"
postconf -e "relayhost = [${RELAY_HOST}]:${RELAY_PORT}"
postconf -e "smtp_sasl_password_maps = static:${RELAY_USERNAME}:${RELAY_PASSWORD}"

# Set up DNS for postfix
cp /etc/resolv.conf /var/spool/postfix/etc/resolv.conf

# Run postfix
/usr/sbin/postfix -c /etc/postfix start-fg
