Sesuaikan .env atau environment variables agar dapat diakses pada `docker-compose.yml`

Access guide for local development

[+] postgresql (LOCAL) : `psql -d kalender_akademik -U postgres`

[+] postgresql (DOCKER) : `psql -h localhost -p 6000 -d kalender_akademik -U postgres --password`

Docker guide

[+] Pada directory lakukan `docker-compose up -d`

# Setelah service up / berjalan

[+] `docker exec -it service_jadwal_siak_web_1 /bin/sh`

# Pada directory service yang ada di dalam container service `service_jadwal_siak_web_1' jalankan

[+] `python manage.py makemigrations && python manage.py migrate`

[+] `python manage.py collectstatic --no-input --clear`
