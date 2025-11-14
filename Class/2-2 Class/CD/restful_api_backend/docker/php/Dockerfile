# docker/php/Dockerfile

FROM php:8.2-fpm

# mysqli 확장 설치
RUN docker-php-ext-install mysqli
RUN mkdir -p /var/log/php \
 && touch /var/log/php/php-error.log \
 && chown -R www-data:www-data /var/log/php \
 && chmod 664 /var/log/php/php-error.log
