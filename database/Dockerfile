FROM postgres:15.1-alpine

ENV POSTGRES_USER=nathan
ENV POSTGRES_PASSWORD=123
ENV POSTGRES_DB=mudanza

COPY db.sql /docker-entrypoint-initdb.d/
