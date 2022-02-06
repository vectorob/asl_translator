# Documentation

#### Robert McKenzie
#### Fall Semester 2021

Welcome to my CS50 Final Project!

For my final project, I built a web-app that turns JPEG or PNG files of signs in American Sign Language and converts those signs into text! At this stage, it only works one letter at a time, but the project could be scaled to translate whole words, perhaps using video files. The app can also convert pictures of the ASL digits from 1-9 into Arabic numbers.

Video: https://youtube.com/shorts/p_fJ7B2ZD5s?feature=share

Before using the app, you must make one change to the source code. The app stores files on local disk, in an upload folder. I declare the path to this folder in a variable called *UPLOAD_FOLDER* right at the top of app.py, and you must change that path to the appropriate folder on your own machine when you download the app. Just right-click on the uploads folder, select copy path, and paste that path into the declaration of *UPLOAD_FOLDER*. You will also need to download the sklearn and sk-image packages to load and run the model. 

The app is simple to use: launch the session in your browser and select a file to translate using the select file button. Then, click confirm to upload that file. For your convenience, I've included a folder called *test_photos* that includes some sample photos you can try to translate (some from the training data set, some that I found online), though feel free to search the web yourself for photos of signs to translate. 

When your file is uploaded, you should see the image appear in the left box, and the name of the file will appear under the box. If you do not select a jpeg or png or your filename fails a security check, or if you don't select a file at all before hitting confirm or translate, you will get an alert prompting you to upload a new file. 

If your image has been successfully uploaded (appears in the box and is ready to translate), click the translate button and the model I built will attempt to turn your image into the English letter represented by the ASL sign in your image. If your image does not contain an ASL sign, the prediction will be pretty far off! The model is highly accurate at classifying data from the training set, but has a harder time with other images, especially cartoon images. A full report of model accuracy can be found in the *translation_model* notebook. 

Once you have translated a file, you will need to select and upload a new file before you can translate again. 
