FROM php:8.2-cli
RUN mkdir /app
WORKDIR /app

# COMPOSER
COPY ./composer.json /app/composer.json
RUN apt-get update && \
     apt-get install -y \
         libzip-dev \
         && docker-php-ext-install zip
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer
RUN composer install

COPY ./src /app/src
COPY ./client.php /app/client.php

CMD ["php", "client.php"]
