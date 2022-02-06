# Design

#### Robert McKenzie
#### Fall Semester 2021

Welcome to my CS50 Final Project!

I knew very early on that I wanted to build a flask web app for this project. I have some experience in Python, and wanted to work on making a web-app that was appealing to look at and easy to use. I also wanted to use machine learning; it's a personal interest of mine and I wanted to explore packages like scikit and tensorflow. I also thought it would be a good way to synthesize all the material from the course: Python, html, CSS, and potentially SQLlite and javascript. 

I had a difficult time picking the right project, and very much stumbled onto the idea of an ASL translator. Online or in app stores, you can find plenty of apps that translate inputted text into ASL signs, but I couldn't find any translators that go the other way, turning images of ASL signs into text, so I decided to make one. 

I built a model in Python, using Google Colab for my processing needs. A lack of sufficient CPU power was a big problem during this project. Even using Colab to run the models, my computer and the library computers had a hard time operating at all given the size of some of the ASL datasets out there. For this reason, I used a very small dataset, only 2500 files, from Kaggle, here: https://www.kaggle.com/ayuraj/asl-dataset. I suspect this has hampered the accuracy of my model, but was limited in my options to resolve this problem. I used the sklearn package, especially scikit-image, to build a support vector machine capable of classifying different images of ASL signs. There were other possible packages or algorithms to use, but for complex image data, I believe a SVM was the best option for accurate results, as support vector machines work well with high-dimensional data.

I rescaled every image to a common size, a 100 by 100 matrix of rgb values, and then flattened that matrix. I applied the Sobel filter to the data, with the hypothesis that it would increase the distincticive of the boundaries between fingers which improved my accuracy, though I left the parameters of my SVM untouched. I could've spent a great deal of time adjusting the parameters of the SVM, but my initial accuracy was good enough I decided not to make those changes. 

The actual operation of the app is pretty simple. A user uploads a file, which is then stored on the local disk of the person running the app. I thought about using a database to store this data, but image data in the format I was using, an array of rgb values that isn't related to any other data and is very large, makes no sense in a database, so I stored it on local disk. I experimented with using the cache to store the uploaded image, but it was simpler and faster to load from the disk. The file is then called when the user clicks translate, the model makes a prediction based on the uploaded file, and that prediction is outputted. When the user reloads the page or starts a new session the folder where uploaded images are stored is wiped. 

Implementing sessions took some time, but it was needed to allow the user to upload and save a file. As well, it allows for lots of future features by storing the actions the user takes. 

Whenever a user uploads a file, there is some security risk. I did my best to mitigate that by using the werkzeug package to ensure filenames are secure and only allowing users to upload jpegs or pngs. I'm sure there are other cybersecurity vulnerabilities here, but I think my approach covers the most common types of attacks. 

The only real problem I had building this app was that my external CSS stylesheet would not load in flask. I have no idea why this happened, but I would always get a 404 error. For this reason, I included my CSS after my closing body tag in my html file. I also used some inline CSS for one-off styling. There is also a small Javascript effect I included that briefly changes the color of some text when you upload a file, mostly just to include some Javascript in the app.

I also tried using multiple html files, but ultimately found it unnecessary. Everything I wanted to do with this app could be done in one html page. 

