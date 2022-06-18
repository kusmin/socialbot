FROM postgres:14.1-alpine
ENV POSTGRES_PASSWORD=social
ENV POSTGRES_USER=social
ENV POSTGRES_DB=social
COPY scripts/* /docker-entrypoint-initdb.d/
