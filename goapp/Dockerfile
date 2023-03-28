FROM golang:1.17-alpine AS builder
LABEL Name=goapp Version=0.0.1
RUN apk update && apk add --no-cache git

WORKDIR /app

COPY . .

RUN go get -d -v ./...

RUN go build -o /app

FROM alpine:3.14

COPY --from=builder app /app

# EXPOSE 5555

CMD ["/app"]
