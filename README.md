# Transforming Models in WebGME With Python and Templating

Taking steps toward learning how to build my own design studio with [WebGME](https://webgme.org) as part of CS 6388 Model Integrated Computing (an Advanced Graduate Course) at [Vanderbilt University](https://vanderbilt.edu). Homeworks assignments [5](hw5/README.md), [6](hw6/README.md), and [7](hw7/README.md) specifically focus on using [iCore](https://www.npmjs.com/package/webgme-icore), a visualizer for WebGME that enables editing and execution of code using the same APIs as a **plugin** directly in the WebGME GUI, where a [plugin](https://github.com/webgme/webgme/wiki/GME-Plugins) is a custom extension point to a webgme-deployment intended to be used for querying, interpreting, and building models.

## Context : Model Driven Engineering

Model-driven engineering is a software development methodology focusing on creating and exploiting domain models, i.e. conceptual models of all the topics related to a specific problem, such as railroad networks. With railroad networks, you have stations, you have switches (and different kinds of switches), you have tracks connecting stations and switches, etc.

With model-driven engineering, if you want to make sure that all railroad networks are created or implemented properly, you can first create a meta-model of a railroad network that wraps up all of the concepts within the domain and precisely and formally defines how those concepts can relate each other in real life.
We use the meta model to represent a set of precisely defined specifications, which define the full set of all possible conforming railroad network models. For example, one specification could be that any fork switch within a network always must have one entry point and two exit points.

When we have our specifications (i.e. requirements around the concepts and how they relate) for a domain, we can build our meta model; when we have our meta model, we can build models (instances of the metamodel) representing real objects (e.g. a model of a railroad network in the Eastern US) in that domain and we can answer the question, _does this model meet our defined specifications?_ If it doesn't, the meta model may need to be updated to more strictly enforce the specifications. If it does, we can use interpreters and model transformations within a design studio to translate our model into actual source code that makes its way into production systems. That source code then lives on a solid foundation of a formally verified model based on a specification-defining meta-model.

## Context : Model Transformations

Model transformations provide an automated way of modifying and creating models; some use cases include model simplification (grouping together components of a complex model for a simpler abstraction that is still meaningful), code generation (that is, generating code from a model based on parameterized code templates; we're moving in that direction with homework 5, 6, and 7)), and even reachability testing (e.g. taking a state machine model and transforming it to a FORMULA program (see my other [FORMULA repository for CS 6388](https://github.com/austinjhunt/6388-formula))) that answers questions like "is every state reachable from the initial state?". The aim of using a model transformation is to save effort and reduce errors by automating the building and modification of models where possible.

## Links

- [WebGME - Web-based Generic Modeling Environment](https://webgme.org)
- [WebGME Vanderbilt](https://mic.isis.vanderbilt.edu/)
- [WebGME Vanderbilt API](https://mic.isis.vanderbilt.edu/api)
- [WebGME ICore Interpreter docs](https://editor.webgme.org/docs/source/Core.html)
