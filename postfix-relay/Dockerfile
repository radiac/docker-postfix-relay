FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postfix \
    libsasl2-modules \
    && rm -rf /var/lib/apt/lists/*

COPY postfix.conf /etc/postfix/main.cf

COPY run.sh /root/run.sh
RUN chmod +x /root/run.sh

EXPOSE 25
CMD ["/root/run.sh"]
