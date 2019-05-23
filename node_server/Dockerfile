FROM node:10

RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

WORKDIR /home/node/app/Users/lvieira/Documents/huginmunin/node_server/package.json

COPY package.json ./

RUN npm install

COPY . .

COPY --chown=node:node . .

USER node

EXPOSE 8000

CMD [ "node", "hello.js" ]