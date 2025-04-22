---
title: Code Samples
layout: unm-base
date: 2019-04-23
---

## Essay components

*This page provides all the kinds of code snippets you might need. The gray boxes should show you exactly what code you need to use; copy and paste it into your own site pages and adjust the attributes as you need to.*

**• In all of the below examples, make sure you take extreme care with your quotation marks and other coding symbols!**

**• DO NOT use double quotation marks `"` in your titles or captions. Single quotation marks `'` are fine.**

**• Remember to use the [Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for Markdown syntax issues. And you can always double check and experiment with [Dillinger](http://dillinger.io).**

---

## Essay Metadata
All essays MUST BEGIN with the following metadata at the top of the page, with the values customized to your own page. **Be sure you have the 3 hyphens `---` before and after your metadata on their own lines**. The top of your essay page should look like:

``` markdown
---
title: Mesa Vista Hall
author: Fred Gibbs
layout: unm-base
date: 2025-04-17
---
```

Obviously, change the title, author, and date for your own essay, but keep the layout set to `unm-base`.

---


## Headings

## Second-level heading
blah blah blah blah ...

### Third-level heading
blah blah blah blah ...

#### Fourth-level heading
blah blah blah blah ...

``` markdown
## Second-level heading

### Third-level heading

#### Fourth-level heading
```


---

## Images
There is one basic way we will embed images in our essay files. Note that it is totally different from how you learned to do them in Markdown itself. This is because if we want to maintain consistency between images, like how the captions appear, we have to make sure we display all images exactly the same way.

In the following sections, the general effect is shown followed by the code snippet that produces it. You can cut and paste from the gray boxes directly into your essays, and change the image filenames, width, etc.


### Standard Usage

{% include figure.html class="img-right" width="33%" caption="Mesa Vista Hall" src="images/centennial-hotel.jpg" %}

You can set the parameter to be whatever percent of the page width you want.

Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum.


To embed the image above, we use:
```
{%raw%}{% include figure.html
  class="img-right"
  width="33%"
  caption="Centennial Hotel"
  src="images/centennial-hotel.jpg"
%}{%endraw%}
```


### Half-width
{% include figure.html class="img-left" width="50%" src="images/centennial-hotel.jpg" caption="Obviously we need a 50% image somewhere with text wrapping around it."%}

Here's a half-page image just for fun. Use the `width` parameter to set whatever percent you want. Usually, keeping images aligned with standard widths like 25%, 33%, 50%, 66% is best. 

Sometimes you need something a little different, though, so you _can_ enter whatever number you want for the `width` parameter.

<p style="clear:both"></p>


```
{%raw%}{% include figure.html
class="img-left"
width="50%"
caption="Obviously we need a 50% image somewhere with text wrapping around it."
src="images/centennial-hotel.jpg"
%}{%endraw%}
```


### Side by side
To achieve two images side by side use, make sure the width for each is 48%. (It's less than 50% to make room for margins.)

{% include figure.html class="img-left" width="48%" src="images/centennial-hotel.jpg" caption="Here's an image on the left."%}

{% include figure.html class="img-left" width="48%" src="images/centennial-hotel.jpg" caption="Here's an image on the right."%}

<p style="clear:both"></p>


{%raw%}
```
{% include figure.html
class="img-left"
width="48%"
caption="Here's an image on the left."
src="images/centennial-hotel.jpg"
%}

{% include figure.html
class="img-left"
width="48%"
caption="Here's an image on the right."
src="images/centennial-hotel.jpg"
%}
```
{%endraw%}


### Full-width
Of course you can have the image take 100% of the page container, but make sure you're image is large enough to look nice. Unlike the below example.

{% include figure.html class="img-center" width="100%" caption="Make sure your image is large enough to be 100% width or it will look grainy. See above."  src="images/centennial-hotel.jpg" %}


{%raw%}
```
{% include figure.html
  class="img-center"
  width="100%"
  caption="Make sure your image is large enough to be 100% width or it will look grainy. See above."
  src="images/centennial-hotel.jpg" %}
```
{%endraw%}



### Jumbotron Images
You'll notice that even a "full-width" image is still bound by our page margins. But sometimes you just need to turn things up to 11. 

In that case, go jumbo! You can make an image be the whole width of the browser window, and control the height of the image for whatever effect you need. Set the `height` parameter to be the % of the browser height. (So, 100 will take up the browser winder, however big or small that is.)

{% include jumbotron.html
  height="50"
  image-url="images/centennial-hotel.jpg"
  title=""
%}

```
{%raw%}{% include jumbotron.html
  height="50"
  image-url="images/centennial-hotel.jpg"
  title=""
%}{%endraw%}
```


### Juxtapose
It's easy to set up a slider to compare historic and contemporary photos. If you find a historic image from a vantage point that you can replicate, please take a modern photo so we can better illustrate the changes in the surrounding space. Obviously the effect is more striking the closer the images line up.


{% include juxtapose.html
image1="images/kimo-1928.jpg"
image2="images/kimo-1938.jpg"
caption=""
%}

<script src="https://cdn.knightlab.com/libs/juxtapose/latest/js/juxtapose.min.js"></script>
<link rel="stylesheet" href="https://cdn.knightlab.com/libs/juxtapose/latest/css/juxtapose.css">


```
{%raw%}{% include juxtapose.html
image1="images/kimo-1928.jpg"
image2="images/kimo-1938.jpg"
caption="These sliders are way more effective the more closely you line up the before and after images."
%}{%endraw%}
```



### Carousel
Extra images that are cool but you don't know how to integrate in your essay? Use a slide carousel! There are two little bits of code to include, one to define your images, and another to actually display the carousel. 

{% assign images = 
"images/mvh-construction.jpg,
images/mvh-room-cost.jpg,
images/mvh-tv-room.jpg" | split: ','
%}

{% include carousel.html
images = images 
%}

The following code generates the slide deck above. Be sure to just copy and paste the entire chunck (both parts) and edit carefully.

```
{%raw%}{% assign images = 
images/mvh-construction.jpg,
images/mvh-room-cost.jpg,
images/mvh-tv-room.jpg" | split: ','
%}

{% include carousel.html
images = images 
%}{%endraw%}
```

## 3D Models
To display your digital models, get the embed code from Sketchfab and paste it into your essay wherever you want it. The code I used is pasted below, but it's exactly what I got from Sketchfab.

<div class="sketchfab-embed-wrapper"> <iframe title="fortune cookie" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/d08c927950c74067b8ff37a738abe228/embed"> </iframe> <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/fortune-cookie-d08c927950c74067b8ff37a738abe228?utm_medium=embed&utm_campaign=share-popup&utm_content=d08c927950c74067b8ff37a738abe228" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;"> fortune cookie </a> by <a href="https://sketchfab.com/fredgibbs?utm_medium=embed&utm_campaign=share-popup&utm_content=d08c927950c74067b8ff37a738abe228" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;"> Fred Gibbs </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=d08c927950c74067b8ff37a738abe228" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p></div>


```
{%raw%}
<div class="sketchfab-embed-wrapper"> <iframe title="fortune cookie" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share src="https://sketchfab.com/models/d08c927950c74067b8ff37a738abe228/embed"> </iframe> <p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;"> <a href="https://sketchfab.com/3d-models/fortune-cookie-d08c927950c74067b8ff37a738abe228?utm_medium=embed&utm_campaign=share-popup&utm_content=d08c927950c74067b8ff37a738abe228" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;"> fortune cookie </a> by <a href="https://sketchfab.com/fredgibbs?utm_medium=embed&utm_campaign=share-popup&utm_content=d08c927950c74067b8ff37a738abe228" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;"> Fred Gibbs </a> on <a href="https://sketchfab.com?utm_medium=embed&utm_campaign=share-popup&utm_content=d08c927950c74067b8ff37a738abe228" target="_blank" rel="nofollow" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a></p></div>
{%endraw%}
```

## Audio recordings

  <audio controls src="code-narration.mp3"></audio>
  

```
{%raw%}
  <audio controls src="code-narration.mp3"></audio>
{%endraw%}
```

## Footnotes
All good historical essays (as you're writing) show what their sources are, which helps readers know what actual research underlies the essay.

To get a footnote to show up, there are two steps:

1) put `[^SOMETEXT]` in your essay where you want the superscript number to appear, and change SOMETEXT to some unique signifier related to the content of the note. In your markdown file, your text will look like:

```
Here's a sample sentence with a footnote at the end.[^source] Here is yet another sentence.[^another-source]
```

2) put  `[^SOMETEXT]: Your footnote text` at the bottom of your essay.


```
[^source]: Your footnote text
[^another-source]: Text for another footnote.
```

Viewed as a webpage, the code above will render as:

Here's a sample sentence with a footnote at the end.[^source] Here is yet another sentence.[^another-source]  Note that the numbering happens automagically, so you don't need to think about that.

[^source]: Your footnote text
[^another-source]: Text for another footnote.

We don't need to footnote every statement, and because you paragraphs should be on the same topic, you can simply use a footnote reference for each paragraph if everything in it comes from the same source. But if you have a certain point you want to make from another source, please cite it directly. Cite as precisely as you can. For books, you need a page number or range, and archival sources should be indicated with collection title, box, folder, etc, as appropriate. Make sure someone else can find what you have cited!


### Footnotes on captions
A good place for image credits is in our "footnotes". To put your image credit in the citation popup, just use the footnote code at the end of your blockquote.

> Here is my quote from a historical source that people would find interesting.[^mysource]

[^mysource]: Some trustworthy reference


Add the code, for that is:
```
> Here is my quote from a historical source that people would find interesting.[^mysource]

[^mysource]: Some trustworthy reference
```

---

## Pull Quotes

As part of our effort to highlight our most important ideas---even in the context of relatively short essays---we can use pull quotes. As it sounds, the idea is to "pull" a quote outside the main flow of the text to highlight it. You can specify if you want it on the left or right side.

{% include aside.html class="left" text="
Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis diam. Pellentesque ut neque." %}

Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus.

To place a pull quote as above, we use:


```
{%raw%}{% include aside.html
  class="left"
  text="Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis diam. Pellentesque ut neque."
  %}{%endraw%}
```

---

### Block quotes
If you are quoting from a historical source, you might want to say more than can fit in a normal pull quote format. For those cases, you can use a markdown blockquote to highlight a particularly juicy quotation. Just start your quote with a greater-than sign as shown below:

Here is my regular text. 

> Here is my very interesting quote. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis diam. Pellentesque ut neque.

And back to the regular text.


```
> Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis diam. Pellentesque ut neque.
```
