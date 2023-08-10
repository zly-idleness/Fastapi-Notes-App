FROM node:lts-alpine
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH 
RUN npm install @vue/cli@5.0.8 -g
COPY package.json . 
COPY package-lock.json .
COPY /src .
RUN npm install
RUN npm install md-editor-v3
RUN npm install sanitize-html

CMD ["npm", "run", "serve"]
