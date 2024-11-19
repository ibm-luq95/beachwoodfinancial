FROM node:lts-alpine
ENV TERM=xterm-256color
ENV COLOR_PROMPT=yes
WORKDIR /app

COPY ./src/frontend/* .

#RUN npm install -g pnpm
RUN --mount=type=cache,target=/root/.cache/npm npm install --global glob
RUN --mount=type=cache,target=/root/.cache/npm npm install glob
#RUN pnpm add glob --save-dev
#RUN --mount=type=cache,target=/root/.cache/pnpm pnpm install
RUN --mount=type=cache,target=/root/.cache/npm npm install

EXPOSE 9091

#CMD ["npm", "start"]

