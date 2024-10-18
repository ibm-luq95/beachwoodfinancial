FROM python:3.12-bookworm
#FROM python:3.12-slim
LABEL MAINTAINER="Ibrahim Luqman"
#LABEL "com.example.vendor"="ACME Incorporated"
#LABEL com.example.label-with-value="foo"
LABEL version="1.0"
LABEL description="This is the development image of beachwood \
that label-values can span multiple lines."
ENV TERM=xterm-256color
ENV COLOR_PROMPT=yes
ENV LANG=C.UTF-8
#ENV PIP_NO_CACHE_DIR=off
ENV PIP_PROGRESS_BAR=on
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV COLUMNS=80
ENV NODE_ENV=development
#ENV BUILD_ENV=${BUILD_ENVIRONMENT}
#ENV VIRTUAL_ENV="/usr/src/app/venv"
# --no-install-recommends

#RUN echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb || true";};' | tee /etc/apt/apt.conf.d/clean
#RUN echo 'APT::Keep-Downloaded-Packages "false";' > /etc/apt/apt.conf.d/01disable-cache
#RUN echo 'Dpkg::Progress-Fancy "1";\nAPT::Color "1";' > /etc/apt/apt.conf.d/99progressbarcolor
# Update the system
RUN apt update
RUN apt list --upgradeable
RUN apt full-upgrade -y
# Update the system

# Install & Init Bash
RUN apt install -y bash-completion
#COPY ./docker/.bashrc /root/.bashrc
#RUN . /root/.bashrc

# Install build and developments packages
RUN echo "Install build and developments packages"
# Install build and developments packages
RUN apt install -y make build-essential libpq-dev libmagic-dev apt-transport-https gnupg --no-install-recommends
# Install essential packages
RUN apt install -y libssl-dev libncurses-dev ncurses-base ncurses-bin ncurses-term wget2 curl nano micro xclip --no-install-recommends
RUN apt install -y net-tools netcat-openbsd git libgraphviz-dev --no-install-recommends
RUN apt install -y libreadline-dev libsqlite3-dev xz-utils tk-dev libxml2-dev ccache tree plocate --no-install-recommends
# Install essential packages
# Translations dependencies
RUN apt install -y gettext
# Translations dependencies

# Enhancing Security With Image Scanning
# To further enhance the security of your Docker images, use image scanning tools like Trivy or Clair. These tools are designed to identify vulnerabilities in your image layers and dependencies. Use Trivy for the calculator app, to conduct vulnerability scanning. 
#RUN wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | tee /usr/share/keyrings/trivy.gpg > /dev/null
#RUN echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main" | tee -a /etc/apt/sources.list.d/trivy.list
#RUN apt update
#RUN apt install -y trivy

RUN echo "##################################################################"
# Install build and developments packages
# cleaning up unused files
RUN apt purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && rm -rf /var/lib/apt/lists/*

RUN echo "Check python version with pip"
RUN #pip3 install -U setuptools pip wheel
RUN which python3
RUN python3 --version && pip3 -V
RUN echo "##################################################################"

WORKDIR /beachwoodfinancial_development


COPY . .
RUN pwd

RUN --mount=type=cache,target=/root/.cache pip3 install -U --progress-bar=on setuptools wheel pip
RUN --mount=type=cache,target=/root/.cache pip3 install --progress-bar=on -r requirements/_all.txt

# Setup NodeJs
#WORKDIR ~
RUN curl -fsSL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
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

# Minimizing Layers for Efficiency
# Combine commands to reduce the number of layers
#RUN echo "Build process goes here" && \
#   /usr/src/app/venv/bin/python3 -m compileall . && \
#   rm -rf __pycache__

WORKDIR /beachwoodfinancial_development/src

COPY ./docker/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

RUN pwd
RUN ls -la
RUN mkdir -p /beachwoodfinancial_development/logs
RUN touch /beachwoodfinancial_development/logs/gunicorn_access.log
RUN touch /beachwoodfinancial_development/logs/gunicorn_error.log
