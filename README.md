# blog

Source code of my personal site https://kovalev.website.

It is powered with Django + uWSGI + nginx. However, if you don't want to face with nginx or other webserver, you can use Django's built-in webserver (see instruction in the end of README).

## How to run

0. Clone this repository and set your django secret key in `mysite/settings.py`.

1. Redirect data from port 80 to port 3000:
   ```
   iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 3000
   ```

2. Set up configuration files:

   * /etc/nginx/sites-enabled/django
     ```
     server {
        listen 3000;
        server_name kovalev.website;
        if ($scheme = http) {
           return 301 https://$server_name$request_uri;
        }
     }

     server {
        listen 443 ssl;
        ssl_certificate /path/to/kovalev.website.crt;
        ssl_certificate_key /path/to/kovalev.website.key;
        server_name kovalev.website; 

        if ($host ~* www\.(.*)) {
           set $host_without_www $1;
           rewrite ^(.*)$ https://$host_without_www$1 permanent;
        }

        location / {
            # django running in uWSGI
            uwsgi_pass unix:///run/uwsgi/app/django/socket;
            include uwsgi_params;
            uwsgi_read_timeout 300s;
            uwsgi_connect_timeout 300s;
            client_max_body_size 32m;
        }

        location /static/ {
           # static files
           alias /path/to/static/; # ending slash is required
        }

        location /media/ {
            # media files, uploaded by users
            alias /path/to/media/; # ending slash is required
        }
     }
     ```

   * /etc/uwsgi/apps-enabled/django.ini
     ```
     [uwsgi]
     chdir = /path/to/blog
     env = DJANGO_SETTINGS_MODULE=mysite.settings
     wsgi-file = mysite/wsgi.py
     workers = 1
     plugins = python3
     ```

3. Collect static files (assuming current directory is this repository root):
   ```
   python3 manage.py collectstatic
   ```

4. Restart services:
   ```
   service uwsgi restart
   service nginx restart
   ```

5. Bonus: SSL-cert adding guide: https://www.reg.ru/support/ssl-sertifikaty/ustanovka-ssl-sertifikata/ustanovka-ssl-sertifikata-na-nginx

## How to run (without nginx)

Note that this method is NOT recommended. Also, you can only use http (not https) without a real webserver. 
```
nohup python3 manage.py runserver kovalev.website:80 --insecure 1> out.log 2> err.log &
```

`--insecure` is needed to make Django serve static files while `Debug` is set to `False`.
