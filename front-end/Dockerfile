FROM node:16.10

RUN npm install -g http-server
WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install --non-interactive --cache-folder ./ycache; rm -rf ./ycache

COPY . .
RUN yarn run build

EXPOSE 8080
CMD [ "http-server", "dist" ]
