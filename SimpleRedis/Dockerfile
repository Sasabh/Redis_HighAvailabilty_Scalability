# Pulling latest redis image
FROM redis:latest

# Copying the redis.conf
COPY redis.conf /usr/local/etc/redis/redis.conf

# Exposing the host port
EXPOSE 6380

# Command that should be executed when a container is started from the Docker image
# Ideally should be in docker-compose, if you're running the setup from same.
# CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]