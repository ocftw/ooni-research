FROM python:3.12.9-alpine3.21

WORKDIR /app
ADD pyproject.toml \
    poetry.lock \
    structs.py \
    setting.py \
    pgdb.py \
    tor_onionoo.py \
    tor.py \
    ./

ENV PATH="/root/.local/bin:${PATH}"

RUN \
    apk update && apk upgrade && \
    apk add --no-cache ca-certificates && \
    apk add --no-cache --virtual .build-deps curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    poetry install --no-root --only main && \
    apk del .build-deps && \
    cd ~/.cache/ && \
    rm -rf /var/cache/apk/* /var/lib/apk/* /etc/apk/cache/*

RUN \
    echo "@reboot cd /app; poetry run python3 tor.py details" >> /etc/crontabs/root
RUN \
    echo "@reboot cd /app; poetry run python3 tor.py details --country=jp" >> /etc/crontabs/root
RUN \
    echo "@reboot cd /app; poetry run python3 tor.py details --country=kr" >> /etc/crontabs/root
RUN \
    echo "@reboot cd /app; poetry run python3 tor.py details --country=hk" >> /etc/crontabs/root

RUN \
    echo "5 * * * * cd /app; poetry run python3 tor.py details" >> /etc/crontabs/root
RUN \
    echo "5 * * * * cd /app; poetry run python3 tor.py details --country=jp" >> /etc/crontabs/root
RUN \
    echo "5 * * * * cd /app; poetry run python3 tor.py details --country=kr" >> /etc/crontabs/root
RUN \
    echo "5 * * * * cd /app; poetry run python3 tor.py details --country=hk" >> /etc/crontabs/root

ENTRYPOINT ["/bin/sh", "-c", "crond -f"]
