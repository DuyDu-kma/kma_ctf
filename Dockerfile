FROM python:3.7
WORKDIR /opt/KMActf
RUN mkdir -p /opt/KMActf /var/log/KMActf /var/uploads

# RUN apt update && \
#     apt install libffi-dev \
#         gcc \
#         make \
#         musl-dev \
#         py-pip \
#         mysql-client \
#         git \
#         openssl-dev
RUN apt install -y build-essential
RUN apt install -y libpq-dev

COPY . /opt/KMActf

RUN pip install -r requirements.txt --no-cache-dir
RUN for d in KMActf/plugins/*; do \
        if [ -f "$d/requirements.txt" ]; then \
            pip install -r $d/requirements.txt --no-cache-dir; \
        fi; \
    done;

RUN chmod +x /opt/KMActf/docker-entrypoint.sh
RUN adduser -D -u 1001 -s /bin/sh KMActf
RUN chown -R 1001:1001 /opt/KMActf /var/log/KMActf /var/uploads

USER 1001
EXPOSE 8000
ENTRYPOINT ["/opt/KMActf/docker-entrypoint.sh"]