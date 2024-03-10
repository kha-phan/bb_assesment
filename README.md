## Installing
### Clone the project
```bash
git clone https://github.com/kha-phan/bb_assesment.git
```

### Create supper user
```bash
python manage.py createsuperuser
```

### Apply migrations to create database tables
```bash
python manage.py migrate
```

### Start Django app with start script
```bash
./start.sh
```


### Start Django app with docker
```bash
docker-compose up
```


## Notes
- Dummy data is prepared in migration
- Should login user `/admin` to auth before verifying all features
- Evidences (run on local) on is attached into `evidence.md` file