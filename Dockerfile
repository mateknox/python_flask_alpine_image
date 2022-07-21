FROM python:3.6-alpine

ADD app /opt/app

WORKDIR /opt/app

USER root
RUN echo 'https://dl-3.alpinelinux.org/alpine/v3.15/main' > /etc/apk/repositories  && \
    echo '@testing https://dl-3.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories && \
    echo '@community https://dl-3.alpinelinux.org/alpine/v3.15/community'

RUN apk update --no-cache

RUN python3 -m pip install --upgrade pip --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host=files.pythonhosted.org
RUN python3 -m pip install -r req.txt --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host=files.pythonhosted.org

RUN touch /var/log/logs.txt
RUN chown 1001 /var/log/logs.txt

RUN chown -R 1001 /opt/app
USER 1001

EXPOSE 5003

CMD ["python3", "main.py"]
