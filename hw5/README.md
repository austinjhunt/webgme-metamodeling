# CS 6388 Homework 5

## Assignment Description

For this homework, you will be working **[WebGME](https://webgme.org/)**. You can reuse your RailroadNetwork project or look for the Homework567 that has one implemented. You will create ICore interpretation that is domain agnostic, so in theory you could use any other project as well. Finally, make sure that you review your work by executing it!

### Task: Project -> JSON

Open your project and go to the ROOT node. Switch to the **ICore visualizer** (if for some reason it is not available in your project, go to the property editor’s META tab and click on the ‘…’ at the end of the validVisualizers line, here you can select it by putting the ICore into the chosen set). So, in the ICore visualization your task is to create an interpreter that will print the following information for every node:
name, GUID, name of its meta type, values of all valid attributes. The data of each node should be collected into a single JSON object (or dictionary in Python) where the key to each node is its path. Finally, you will need to use the logger to print out the generated JSON object. Try to use some ‘beautification’ so that it is a legible printout.
There is no ordering of nodes. Print only the valid attribute values (so you are not printing the code itself for example)! Finally, remember that the name of the meta type of a meta node is itself!
One example printout:

```{
    “”: {
        “name”: “ROOT”,
        “GUID”: “03d36072-9e09-7866-cb4e-d0a36ff825f6”,
        “meta”: null,
        “attributes”: {
            “name”: “ROOT”
        }
    },
    “/1”: {
        “name”: “FCO”,
        “GUID”:” cd891e7b-e2ea-e929-f6cd-9faf4f1fc045”,
        “meta”: “FCO”,
        “attributes”: {
            “name”: “FCO”
        }
    },
    “/p/6”: {
        “name”: ”Transition”,
        “GUID”: ”cf69d692-43d8-fd64-f294-f33eade60e2e”,
        “meta”: “Transition”,
        “attributes”: {
        “name”: “Transition”,
            “event”: “”
        }
    }
}
```
