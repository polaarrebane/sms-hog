FROM node:18-alpine as build
RUN mkdir -p /app/node_modules
WORKDIR /app
COPY public/ /app/public
COPY src/ /app/src
COPY package.json /app/
RUN npm install
ENV REACT_APP_API_URL_GET_SMS="/api/messages/sms"
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]
