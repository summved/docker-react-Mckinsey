FROM node:alpine as builder
WORKDIR '/app'
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

#/app/build

FROM nginx
EXPOSE 80														#Expose the 3000 port of docker app to port 80 of the server
COPY --from=builder /app/build /usr/share/nginx/html