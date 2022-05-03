FROM node:16 as build

WORKDIR /build

COPY ./descriptions ./descriptions
COPY ./build.sh ./

RUN npm install -g marked
RUN ./build.sh


FROM nginx:1.21-alpine

COPY --from=build --chown=nginx /build/descriptions /var/www/static/descriptions
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80