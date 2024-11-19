FROM python:3.13-bookworm
LABEL MAINTAINER="Ibrahim Luqman"
LABEL version="1.0"
LABEL description="Development image of beachwood"

# Set environment variables
ENV TERM=xterm-256color \
    LANG=C.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_PROGRESS_BAR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install Trivy for vulnerability scanning
RUN apt update && apt install -y wget gnupg --no-install-recommends && \
    wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | tee /usr/share/keyrings/trivy.gpg > /dev/null && \
    echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main" | tee -a /etc/apt/sources.list.d/trivy.list && \
    apt update && apt install -y trivy

# Optionally: Use Trivy to scan for vulnerabilities in the base image
# RUN trivy image --timeout 25m --severity HIGH,CRITICAL python:3.12-bookworm

# Combine system update, package installation, and cleanup in one layer
RUN apt update && apt full-upgrade -y && \
    apt install -y bash-completion make build-essential libpq-dev libmagic-dev \
    apt-transport-https gnupg libssl-dev libncurses-dev wget2 curl nano micro \
    net-tools netcat-openbsd git libgraphviz-dev gettext libreadline-dev \
    libsqlite3-dev xz-utils tk-dev libxml2-dev ccache tree plocate --no-install-recommends && \
    apt purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /beachwoodfinancial_development

# Install Python dependencies with caching
COPY . .
RUN --mount=type=cache,target=/root/.cache pip3 install -U setuptools wheel pip
RUN --mount=type=cache,target=/root/.cache pip3 install -r requirements/_all.txt

# Remove Node.js and pnpm setup (handled in the Node.js service now)
# Setup NodeJs
#WORKDIR ~
RUN curl -fsSL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh
RUN bash -x nodesource_setup.sh
RUN apt update
#RUN apt install -y nodejs
RUN sed -i 's/\r$//g' src/node_installer
RUN chmod +x src/node_installer
RUN bash src/node_installer nodejs
RUN node -v
RUN npm set progress true
RUN npm --version
#RUN npm install -g pnpm
RUN npm update -g npm
RUN npm install -g pnpm
RUN npm install -g yarn

# Copy and set up the start script
COPY ./docker/django/start /start
RUN chmod +x /start

# Remove the frontend working directory setup (handled in Node.js service)
WORKDIR /beachwoodfinancial_development/src/frontend
RUN --mount=type=cache,target=/root/.cache/pnpm pnpm install

# Set the working directory for the final app
WORKDIR /beachwoodfinancial_development/src

# Create log directories
RUN mkdir -p /beachwoodfinancial_development/logs && \
    touch /beachwoodfinancial_development/logs/gunicorn_access.log && \
    touch /beachwoodfinancial_development/logs/gunicorn_error.log
