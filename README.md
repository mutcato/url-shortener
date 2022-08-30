# URL Shortener

url-shortener is a bit.ly like scalable url shortener application written in Python and Django

# Usage
### Run the following commands
 `git clone git@github.com:mutcato/url-shortener.git`

`docker-compose up`

To shorten an URL, send POST request the http://127.0.0.1:8000/urls endpoint with
a payload: {"long_url": "https://longurl.com"} 
![Django Rest url shortenin window](https://i.imgur.com/eD2XaQi.png)

#### To get data for single URL send GET request to the http://127.0.0.1:8000/urls/{key} endpoint
![Single URL](https://i.imgur.com/FTTlqQ4.png)

## Highlevel Architechture

There is 6 service are going to be up after running `docker-compose up` command. keygenerator, urlshortener, celery, celery-beat, db(Postgres), redis

**urlshortener**(binds at port: 8000) and **keygenerator**(binds at port:8001) services are two different Django projects. There is a Celery task (generate_keys) works in every minute and generates keys and then saves these keys in keys_key table. 

Keygenerator has a single endpoint https://localhost:8001/keys which takes GET request from urlshortener service. 

When a POST request comes to **urlshortener** service (http://127.0.0.1:8000/urls) urlshortener service gets a pregenerated key from keygenerator service (https://127.0.0.1:8001/keys)

### To run tests
change `.env` file with `dev.env` in settings.py files and run `python manage.test` command
