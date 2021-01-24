package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"math/rand"
	"net/http"
	"strconv"
	"time"

	"github.com/gorilla/mux"
)

const (
	distPath    = "../ui/dist"
	indexPath   = distPath + "/index.html"
	faviconPath = distPath + "/favicon.ico"
)

type Product = struct {
	ID    string `json:"id"`
	URL   string `json:"url"`
	Image string `json:"image"`
}

func allProducts() ([]Product, error) {
	var products []Product

	b, err := ioutil.ReadFile("../scraping/products.json")
	if err != nil {
		return products, err
	}

	err = json.Unmarshal(b, &products)
	return products, err

}

func randomSample(products []Product, n int) []Product {
	l := len(products)
	if n >= l {
		return products
	}

	sample := make([]Product, n)
	for si := range sample {
		pi := rand.Intn(l)
		sample[si] = products[pi]
	}

	return sample

}

func fileHandler(filePath string) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, filePath)
	}
}

func main() {
	products, err := allProducts()
	if err != nil {
		log.Fatal(err)
	}

	r := mux.NewRouter()

	r.HandleFunc("/products", func(w http.ResponseWriter, r *http.Request) {
		n, err := strconv.Atoi(r.URL.Query().Get("n"))
		if err != nil {
			w.WriteHeader(400)
			return
		}

		ps := randomSample(products, n)

		b, err := json.Marshal(ps)
		if err != nil {
			w.WriteHeader(500)
			return
		}

		w.WriteHeader(200)
		w.Write(b)
	})

	r.PathPrefix("/static").Handler(http.FileServer(http.Dir(distPath)))
	r.HandleFunc("/favicon.ico", fileHandler(faviconPath))
	r.PathPrefix("/").HandlerFunc(fileHandler(indexPath))

	server := http.Server{
		// Addr: ":https",
		Addr: ":8000",
		// TLSConfig: &tls.Config{
		// 	GetCertificate: certManager.GetCertificate,
		// },
		Handler:      r,
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 5 * time.Second,
		IdleTimeout:  120 * time.Second,
	}

	log.Fatal(server.ListenAndServe())
}
