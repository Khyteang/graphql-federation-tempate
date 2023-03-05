# graphql-federation-tempate

# Install pyenv
```bash
brew install pyenv

pyenv install 3.9.1

pyenv global 3.9.1

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

# Install Poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -

nano ~/.zshrc

echo 'export PATH="/Users/khyteanglim/.local/bin:$PATH"' >> ~/.zshrc

poetry --verison
```

# Install Apollo Router
Link: https://www.apollographql.com/docs/router/quickstart/
```bash
$ curl -sSL https://router.apollo.dev/download/nix/latest | sh
```

# Install Apollo CLI (rover)
Link: https://www.apollographql.com/docs/rover/getting-started/
```bash
$ curl -sSL https://rover.apollo.dev/nix/latest | sh
```

# Start up databases
```bash
# make sure you populate the .env
$ cp .sample.env .env

$ docker-compose build

# this command will spin up two databases and pgadmin 
# port 5432 for patient-service
# port 5433 for order-service
$ docker-compose up -d
```

# Start up all services
## Start up order service
```bash
$ cd order-service

# make sure you populate the .env
$ cp .sample.env .env

$ poetry install

$ poetry run migrate

$ poetry run start
```

## Start up patient service
```bash
$ cd patient-service

# make sure you populate the .env
$ cp .sample.env .env

$ poetry install

$ poetry run migrate

$ poetry run start
```

# Generate supergraph using rover
```bash
# this command will use all the specified subgraph from supergraph.yaml and generate a supergraph in supergraph-schema.graphql
$ rover supergraph compose --elv2-license=accept --config ./supergraph.yaml > supergraph-schema.graphql
```

# Start the router
```bash
# --dev flag will launch the router with a sandbox
# go to http://localhost:4000/
$ ./router --dev --supergraph supergraph-schema.graphql
```
