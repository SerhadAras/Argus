from node:16-alpine

# Labels
LABEL org.opencontainers.image.source https://github.com/WatcherWhale/SecProA

# Run as node user
USER node

# Set default environment variables
ENV PORT=3000
ENV LOGLEVEL=http

# Create folders
RUN mkdir $HOME/logger && \
    mkdir $HOME/redis && \
    mkdir $HOME/service && \
    mkdir $HOME/app

#################
# Build modules #
#################

# Logger
WORKDIR /home/node/logger
COPY --chown=node:node ./logger/package* ./
COPY --chown=node:node ./logger/lib/ ./lib
RUN npm ci --production

# Redis
WORKDIR /home/node/redis
COPY --chown=node:node ./redis/package* ./
COPY --chown=node:node ./redis/lib/ ./lib
RUN npm ci --production

# Service
WORKDIR /home/node/service
COPY --chown=node:node ./service/package* ./
COPY --chown=node:node ./service/lib/ ./lib
RUN npm ci --production

#############
# Build app #
#############

ARG service

WORKDIR /home/node/app

# Install modules
COPY --chown=node:node ./$service/package* ./
RUN npm ci --production

# Copy src files
COPY --chown=node:node ./$service/src/ ./

# Set entrypoint
CMD [ "node", "index.js" ]
