FROM python:3.9

COPY ./ /app/

WORKDIR /app

COPY ./run.sh /run.sh
RUN chmod +x /run.sh

RUN pip install pipenv && pipenv install

CMD ["/run.sh"]