package main

import (
	"context"
	// "encoding/json"
	"log"
	// "math/rand"
	"net/http"
	"time"

	// "go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

// Country struct to hold country data
type Country struct {
	Name       string `json:"name"`
	Capital    string `json:"capital"`
	Population int    `json:"population"`
}

func main() {
	// MongoDB connection URI
	uri := "mongodb://mongodb:27017"
	// Connect to MongoDB
	client, err := mongo.NewClient(options.Client().ApplyURI(uri))
	if err != nil {
		log.Fatal(err)
	}
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	err = client.Connect(ctx)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Disconnect(ctx)

	// Get collection from stajdb database
	// collection := client.Database("stajdb").Collection("ulkeler")

	// Create HTTP server and handle routes
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Merhaba Go!"))
	})
	http.HandleFunc("/staj", func(w http.ResponseWriter, r *http.Request) {
		// Get a random country from MongoDB collection
		// var result Country
		// count, err := collection.CountDocuments(context.Background(), bson.M{})
		// if err != nil {
		// 	log.Fatal(err)
		// }
		// err = collection.FindOne(context.Background(), bson.M{}).Skip(rand.Intn(int(count))).Decode(&result)
		// if err != nil {
		// 	log.Fatal(err)
		// }
		// // Write country data as JSON response
		// jsonData, err := json.Marshal(result)
		// if err != nil {
		// 	log.Fatal(err)
		// }
		// w.Header().Set("Content-Type", "application/json")
		// w.Write("jsonData")
		w.Write([]byte("Staj"))
	})


	http.HandleFunc("/goapp", func(w http.ResponseWriter, r *http.Request) {
		// Get a random country from MongoDB collection
		// var result Country
		// count, err := collection.CountDocuments(context.Background(), bson.M{})
		// if err != nil {
		// 	log.Fatal(err)
		// }
		// err = collection.FindOne(context.Background(), bson.M{}).Skip(rand.Intn(int(count))).Decode(&result)
		// if err != nil {
		// 	log.Fatal(err)
		// }
		// // Write country data as JSON response
		// jsonData, err := json.Marshal(result)
		// if err != nil {
		// 	log.Fatal(err)
		// }
		// w.Header().Set("Content-Type", "application/json")
		// w.Write("jsonData")
		w.Write([]byte("Staj Goapp"))
	})

	// Start HTTP server on port 5555
	log.Fatal(http.ListenAndServe(":5555", nil))
}
