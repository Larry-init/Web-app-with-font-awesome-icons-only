FROM node:16 AS builder

WORKDIR /app

COPY  . .

EXPOSE 80

CMD ["nginx","-g","deamon off"]
