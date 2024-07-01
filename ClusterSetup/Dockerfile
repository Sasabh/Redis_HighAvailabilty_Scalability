# Use the official Redis image from Docker Hub
FROM redis:latest

# Copy custom configuration file
COPY redis.conf /usr/local/etc/redis/redis.conf

# Expose Redis port
# EXPOSE 6379

# Run Redis with the custom configuration
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]