FROM python:3.9

LABEL maintainer="Lyle Wang <lyle927@outlook.com>"

# RUN pip install meinheld gunicorn

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./gunicorn_conf.py /gunicorn_conf.py

COPY . /app/
WORKDIR /app/

ENV PYTHONPATH=/app

RUN pip install pipenv && pipenv install

EXPOSE 80

ENTRYPOINT ["/entrypoint.sh"]

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Meinheld
CMD ["/start.sh"]
