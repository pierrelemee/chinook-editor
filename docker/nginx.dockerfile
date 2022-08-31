FROM debian:bullseye

# Update & install core APT packages
RUN apt update
RUN apt-get install -y apt-utils git wget vim curl gnupg2 procps

# Tool to debug  connection
# ex SCRIPT_NAME=/api/grid/1 SCRIPT_FILENAME=/app/public/ REQUEST_METHOD=GET DOCUMENT_ROOT=/app/public cgi-fcgi -bind -connect api:6000
RUN apt install -y libfcgi0ldbl

# Nginx
RUN apt install -y nginx
RUN rm -f /etc/nginx/sites-available/default
RUN rm -f /etc/nginx/sites-enabled/default

RUN mkdir -p /usr/local/share/ssl/

# chinook.local website configuration
COPY ./files/nginx/chinook.local.conf /etc/nginx/sites-available/chinook.local.conf
COPY ./files/ssl/chinook.local.pem /usr/local/share/ssl/
COPY ./files/ssl/chinook.local-key.pem /usr/local/share/ssl/
COPY ./files/ssl/rootCA.pem /usr/local/share/ssl/
RUN ln -sf /etc/nginx/sites-available/chinook.local.conf /etc/nginx/sites-enabled

# Files
RUN echo "alias ll='ls -l'" > /root/.bashrc
RUN echo "alias la='ls -la'" >> /root/.bashrc
RUN echo "PS1='\[\033[01;35m\]\h \[\033[01;34m\]\w $\[\033[00m\] '" >> /root/.bashrc
RUN echo "export LANG='fr_FR.UTF8'" >> /root/.bashrc

WORKDIR /etc/nginx

CMD ["nginx", "-g", "daemon off;"]
