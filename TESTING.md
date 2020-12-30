# Picturesque - Testing

*Developer: Anthony Guillermo*

## Tests and Fixes

[HTML Validator Results](/)

[CSS Validator Results](/)

**Desktop/Tablet/Mobile** 
Tested on Chrome Desktop/Tablet/Mobile simulator
hompage carousel

***Desktop/Tablet/Mobile Issue***
Carousel images not loading properly

***Desktop/Tablet/Mobile Fix***
Changed the classes in the carousel div
```
from
<div  class="container carousel-container carousel-image-1 ">
to
<div  class="carousel-item active carousel-image-1"  data-interval="8000">
```
**Desktop Issue**
The anchor tag for the categories text was using default colour

***Desktop Fix***
Insert and inline style class to override the default underline colour
```
<a  href=""  style="color: #efbbff;">
```
***Desktop/Tablet/Mobile Issue***
Category image not appearing in the div

***Desktop/Tablet/Mobile Fix***
Use id attribute instead of class to target the image
```
<div  id="artistic-image"  class="category-box category-image">
```

***Desktop Issue***
Four items not appearing in one row in the home page

***Desktop Fix***
Changed size of the category-box class from 300 to 275
```
.category-box {
height: 275px;
width: 275px;
}
```

***Desktop/Tablet/Mobile Issue***
Icon size in the footer was too small

***Desktop/Tablet/Mobile Fix***
Change footer icon size add font awesome class fa-2x
```
<a  href="/"><i  class="fab fa-facebook fa-2x"></i></a>
```
***Desktop/Tablet Issue***
Quantity size button too big in poster details page 

***Desktop/Tablet Fix***
Removed min width 260px from purple-btn css
```
.purple-btn {
background: #8a25b1;
color: white;
}
```
***Desktop/Tablet/Mobile Issue***
Info and warning toasts had purple background

***Desktop/Tablet/Mobile Fix***
Changed toast background purple to white
```
from
<div  class="toast-header bg-white text-dark">
to
<div  class="toast-body bg-white">
```

***Desktop/Tablet/Mobile Issue***
Error when logging in using super user. User does not exist when it was created at early stage ing the project

***Desktop/Tablet/Mobile Fix***
Created new super user

***Desktop/Tablet/Mobile Issue***
Titles in basket and check out were too close to the banner

***Desktop/Tablet/Mobile Fix***
Add mt-3 class to container div
```
<div  class="overlay"></div>
<div  class="container mb-2 mt-3">
<div  class="row">
<div  class="col">
<h2  class="title-text mb-3 text-uppercase">My Basket</h2>
<hr>
</div>
</div>
```
```
<div  class="container mt-3">
<div  class="row">
<div  class="col">
<h2  class="title-text mb-4 text-uppercase">Checkout</h2>
<hr>
</div>
</div>
```
***Desktop/Tablet/Mobile Issue***
The footer bg was in container class in checkout and my profile pages

***Desktop/Tablet/Mobile Fix***
In checkout page & my profile added another closing div before end block
```
</div>
{% endblock %}
```
***Desktop/Tablet/Mobile Issue***
Allauth buttons not matching rest of the site

***Desktop/Tablet/Mobile Fix***
Added purple-btn rounded-pill class to Allauth button styling and also changed colour in css

```
.allauth-form-inner-content  button,
.allauth-form-inner-content  input[type='submit'] {
/* btn */
display: inline-block;
font-weight: 400;
color: #fff;
text-align: center;
vertical-align: middle;
-webkit-user-select: none;
-moz-user-select: none;
-ms-user-select: none;
user-select: none;
background-color: #8a25b1!;
border: 1px  solid  #8a25b1!;
padding: .375rem  .75rem;
font-size: 1rem;
line-height: 1.5;
border-radius: 0;
```
 ```
.allauth-form-inner-content  button:hover,
.allauth-form-inner-content  input[type='submit']:hover {
color: #fff;
background-color: #efbbff;
border-color: #efbbff;
}
```

## Manual Testing

**Desktop/Tablet/Mobile** 
Tested on Chrome Desktop/Tablet/Mobile simulator

**Exploratory Testing**

***Page Links - Desktop***
The app was navigated through the different pages on both Desktop/Tablet & Mobile. In order to check if the user was able to navigate to and from each of the pages; Homepage, Allauth templates, Poster, Poster detail, Bag, Checkout, Checkout details and Profile. 

All the buttons were checked in various other pages to see if it lead to the the right pages.

The navigation was also checked to so that the user would  be able to navigate the site without having to use the back button. The sorting in the navbar, category links were all checked along with the sorting or posters in Poster details page.

***Page Links - Tablet/Mobile***
In the tablet and mobile views there is a burger bar menu. This was tested to see if the menu would slide from the left when clicked.

As similar with the Desktop test, all pages were navigated to and from each other to test the links. The button navigation was tested as well.

**Device View - Desktop/Tablet/Mobile**
The rows and columns were checked to different devices to make sure the they were applied to correct screen size.

Also the text and buttons designed to appear on specific views were also checked to ensure there was no repeat or overlap.

 ***Social Links - Desktop/Tablet/Mobile***
All social links were checked at the footer of each page to make sure Facebook, Pinterest, Twitter, Instagram and Youtube all opened in a new tab.

**Base.html - Desktop/Tablet/Mobile**
All pages were checked to ensure the basic structure from the site extended to all pages.

**SQlite3 /PostgreSQL- Desktop/Tablet/Mobile**
The app was checked to see if the SQlite3 /PostgreSQL database was loading correctly on the site. Also that all the posters were appearing in the Product page and the name and description could be searched in the home page

**Purchasing/Order History- Desktop/Tablet/Mobile**
Test transactions were carried out for user and non user to check the whole order process was complete until the customer received a confirmation email. Checked registered users info was saved from previous order and appearing in users order history.

**Unresolved Bugs**

- Quantity button not the correct length in mobile view on Product details page.
- In mobile view icons appear squashed in header due to names
- Some buttons in the site are not inheriting the rounded-pill class.