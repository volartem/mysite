Simple Django application with Django channels 2.

Add  folder `storage/` near the root of application. Inside this folder put `mysite/postgres; mysite/redis; mysite/for_dump`
It's a volume folders for running docker containers. In root directory must be `logs` folder and your env file.

The application run with docker-compose.
For local development:
`docker-compose -f docker-compose.yml -f docker-compose-dev.yml up`
Then you must run all manage.py commands all you need inside container.

For production:
`docker-compose -f docker-compose.yml up -d`

In the project used pipenv - as a best dependency resolver and it truly easy to use.
And it very simple to debug with pycharm as a remote debug.