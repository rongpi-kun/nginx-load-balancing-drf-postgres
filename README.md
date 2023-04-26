# nginx-load-balancing-drf-postgres

This project was made while I was practicing how to use nginx as a proxy and load balancer.

Workflow:
  1. I created two upstream servers 
  2. Used postgresql as the sql server
  3. Each  of the server is connected the same postgresql
  4. Any changes made in any upstream server that nginx will route will be reflected in both the servers
  
 #Here django is the nginx config file. Save this file in /etc/nginx/sites-enabled/django
 
#Execution:
  1. Start nginx: sudo service nginx start
  2. Restart nginx: sudo systemctl restart nginx
  3. Start Gunicorn Server: gunicorn -c conf/gunicorn_config.py simple.wsgi
  4. Now it's done.
