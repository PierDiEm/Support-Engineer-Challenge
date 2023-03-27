0 0 * * 0 tar -czf /home/user/backup.tar.gz /home/user/ && ssh user@192.168.1.100 "mkdir -p /remote/backup/location && cat > /remote/backup/location/backup.tar.gz" < /home/user/backup.tar.gz
