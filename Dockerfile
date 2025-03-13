FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install pylint flake8 black isort autopep8
RUN npm install -g eslint prettier
RUN go install golang.org/x/tools/cmd/goimports@latest
RUN cargo install rustfmt
RUN composer global require squizlabs/php_codesniffer
RUN apt update && apt install -y cppcheck shellcheck

ENTRYPOINT ["bash", "/app/entrypoint.sh"]
