FROM golang:1.17-alpine AS builder
# FROM golang:1.16-alpine

LABEL Name=goapp Version=0.0.1

RUN apk update && apk add --no-cache git

WORKDIR /go/src/app

# COPY . .

# RUN go get -d -v ./...

RUN go build -o /go/bin/app

FROM alpine:3.14

COPY --from=builder /go/bin/app /app

EXPOSE 5555

CMD ["/app"]


# # syntax=docker/dockerfile:1
# RUN go mod init

# WORKDIR /app

# COPY go.mod ./
# COPY go.sum ./
# RUN go mod download

# COPY *.go ./

# RUN go build -o /app

# EXPOSE 8080

# CMD [ "/app" ]