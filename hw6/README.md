# CS 6388 Model Integrated Computing Homework 6

## Assignment Description

For this homework, you will be working **[WebGME](https://webgme.org/)**. You can reuse your RailroadNetwork project (that already has the homework5 solution) or look for the Homework567 that has one implemented. You will create ICore interpretation that is specific to the RN domain. If you are using your own project, then make sure to rebuild the exact same model that can be found in Homework6 project, so you can produce the same output! Finally, make sure that you review your work by executing it!

### Task: RN -> JSON

Open your project and go to the RailroadNetwork meta-node. Switch to the ICore visualizer (if for some reason it is not available in your project, go to the property editor’s META tab and click on the ‘…’ at the end of the validVisualizers line, here you can select it by putting the ICore into the chosen set). So, in the ICore visualization your task is to create an interpreter specifically for the RailroadNetwork meta element (so it will work on any arbitrary RN) that will generate the following JSON output (and store it as an artifact):

- Create an entry for every pairs of stations with the id of (station1->station2)
- Each entry should have the ‘length’ of a possible path from station1 to station2 or -1 if there is no path from station1 to station2
- Once the JSON collection is complete, save it into an artifact/file on the server (you can obviously log it out as well for easier debugging)
  Do not forget that every possible pair is required (each direction)! Also, we only interested in station to station (no embedded networks). You need to use the ‘length’ attribute of the Track to compute the length of the path. If you have no idea how to traverse the graph, I suggest you google it (breadth-first search).
  As usual, you do not need to try to order the elements of the JSON object (by standard it is impossible anyways). You can implement it using either JS or Python.
  One example (partial) result:
  {
  “Chicago->Boston”: 240,
  “Boston->Chicago”:120,
  “Boston->Philadelphia”:150,
  “Philadelphia->Boston”: -1
  }
