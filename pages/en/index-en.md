---
ptitle: Mari Nagem
layout: home
permalink: /en/
redirect: "../"
---
{{ site.pages | where:"permalink","/" | first | map: "content" | first }}
