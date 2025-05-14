package main

import (
	"fmt"
	"net/http"
)

func main() {
	http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "OK")
	})
	// TODO: add caching, Markdown fetch, WebKitGTK API, etc.
	http.ListenAndServe(":8080", nil)
}
