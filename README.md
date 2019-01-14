Simple Django application with Django channels 2.

Add  folder `storage/` near the root of application. Inside this folder put `mysite/postgres; mysite/redis; mysite/for_dump`
It's a volume folders for running docker containers. In root directory must be `logs` folder and your env file.

The application run with docker-compose.
For local development:
`docker-compose -f dev.yml up`
Then you must run all manage.py commands all you need inside container.

For production:
`docker-compose -f prod.yml up -d`
As nginx is using as the docker container and the top of project infrastructure, you must have a working config(with ssl, ports and other values) on the host machine that is not representing here.
In the project used pipenv - as a best dependency resolver and it truly easy to use.
And it very simple to debug with pycharm with a remote debug.

Must have .env file with your values for development:

```css
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
RABBITMQ_DEFAULT_USER=
RABBITMQ_DEFAULT_PASS=
RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS=-rabbit log_file_level [{connection,debug}]
RABBITMQ_LOGS=/var/logs/rabbitmq/rabbit.log
RABBITMQ_DEFAULT_LOG_LEVEL=debug
```