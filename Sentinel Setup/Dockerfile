# Use the official Redis image from the Docker Hub
FROM redis:latest

# Copy the Redis configuration file into the container
COPY redis-master.conf /usr/local/etc/redis/redis-master.conf
COPY redis-slave.conf /usr/local/etc/redis/redis-slave.conf
COPY sentinel.conf /usr/local/etc/redis/sentinel.conf

# Expose the default Redis port and Sentinel port
EXPOSE 6379 26379

# Start the Redis server with the appropriate configuration file
# CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]