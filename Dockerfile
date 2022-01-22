FROM python:3.9.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /note_app
COPY requirements.txt /note_app/
ADD docker-entrypoint.sh /docker-entrypoint.sh
RUN pip install -r requirements.txt
COPY . /note_app/
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["sh", "/docker-entrypoint.sh"]
