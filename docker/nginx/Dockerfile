FROM nginx:latest
ENV TERM=xterm-256color
ENV COLOR_PROMPT=yes
ENV LANG=C.UTF-8
RUN apt update
RUN apt full-upgrade -y
RUN mkdir -p /home/static/
RUN mkdir -p /home/media/
RUN mkdir -p /home/media/media
RUN mkdir -p /home/static/staticfiles
RUN rm -rf /etc/nginx/conf.d/default.conf
COPY ./docker/nginx/nginx.conf /etc/nginx/conf.d/default.conf


