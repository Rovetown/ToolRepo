package main

import (
    "fmt"
    "net/http"

    "github.com/diamondburned/gotk4/pkg/gtk/v4"
    "github.com/gomarkdown/markdown"
    "github.com/gomarkdown/markdown/html"
    "github.com/gomarkdown/markdown/parser"
)

func main() {
    http.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintln(w, "OK")
    })
    // TODO: add caching, Markdown fetch, WebKitGTK API, etc.
    http.ListenAndServe(":8080", nil)
}
