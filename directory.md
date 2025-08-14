---
title: UNM Campus Histories
layout: unm-base
date: 2024-04-13
header-image: "/assets/images/1946 map to campus.jpg"
header-height: 40vh
background-position: "0px -70px"
---

<!-- close the container div for full viewer width display -->
{::nomarkdown}
</div>
<div style="margin-left:10%; margin-right:10%; margin-top:2%">
{:/nomarkdown}

# Directory of Essays

{% assign essays = site.pages | where_exp: "page", "page.path contains 'essays/'" 
%}

{% include card-grid.html 
cards = essays
%}

</div>