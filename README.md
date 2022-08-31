# chinook-editor

Web app to visually edit the Chinook database


## Local development

### Declare local domain

Before running the app, the local domain chinook.local has to be referenced in our local domaine name resolver (`/etc/hosts`):

```bash
sudo echo '127.0.0.1 chinook.local' >> /etc/hosts
```

### Generate SSL certificate

The `mkcert` command is required to generate self-signed SSL certificates:

```bash
cd docker/files/ssl
CAROOT=$(pwd) mkcert -install
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain "$(pwd)/rootCA.pem"
CAROOT=$(pwd) mkcert "chinook.local"
cd -
```

### Run docker compose

The `docker` command has to be installed:

```bash
docker compose up -d --build -f ./docker/docker-compose.yml
```
