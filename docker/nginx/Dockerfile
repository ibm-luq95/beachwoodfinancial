FROM nginx:latest

# Remove the default Nginx configuration file to avoid conflicts
RUN rm -rf /etc/nginx/conf.d/default.conf

# Copy the custom Nginx configuration file into the container
COPY ./docker/nginx/nginx.conf /etc/nginx/conf.d/default.conf
