# CS 6388 Model-Integrated Computing Homework 7

## Assignment Description

For this homework, you will be working WebGME. It is highly recommended that you reuse you homework6 solution. Alternatively, you can start your work from the Homework567 project. You will create ICore interpretation that is specific to the RN domain. If you are using your own project, then make sure to rebuild the exact same model that can be found in Homework6 project, so you can produce the same output! Finally, make sure that you review your work by executing it!

### Task: RN -> text

Building on the paths you already computed in homework 6, your task will be to enhance the result into complete English sentences and put it in a text file. Also, you will need the path (which stations are travelled along the way) and not just its length! Another change is that you should not mention pairs of stations that are not reachable (where the length was -1 in homework6).
Here is an example line that should be generated for the ‘valid’ pairs of stations!

“A path from StationA to StationB is 150 miles. On the path you will travel through StationC, StationD, and StationE.”

The text in italic is the model dependent portion and you need to make sure you have your text template right. Also, make sure to store the template in an attribute and read it from there. Save your result into a text file named after the name of the RN network (like mynetwork.txt).
