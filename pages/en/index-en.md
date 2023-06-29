---
ptitle: Mari Nagem
template: home
permalink: /en/
redirect: "../"
---
{{ site.pages | where:"permalink","/" | first | map: "content" | first }}
