#### Hypertext Information Retrieval System to Incorporate Multimedia Information (Hypermedia)

###### Proposal
Limiting the target of any retrieval system to text documents overlooks many opportunities. What about video, audio, imagery, etc? For my technology review I want to research and discuss some cutting-edge approaches being used to optimize a retrieval system that targets hypermedia. Examples of this being used can be found in smarthome devices like Google Home and Alexa, and considering how premature these technologies are I see a lot of opportunity for growth on the topic of hypermedia retrieval. 

#### Research
###### [Hypermedia & Free Text Retrieval](https://personal.cis.strath.ac.uk/mark.dunlop/research/publications/ipm/)

The goal is to create a retrieval mechanism that targets non-text-based data. (2)

Many times non-text-based items are identified as text-based by being given a form of ID number 

Old style is browser-based hypermedia, which allows user to browse through document base using a series of paths connecting documents together. These are restricted in scale due to the undirected approach 

User issues a query to locate the approximate area to browse, but with this approach non-textual documents must be accessed by textual nodes. If user wants to search for an image, they could retrieve a URL that relates to both the image and their query. If a user enters a query, they will get a result of textual nodes that link to the non-textual item, which the user would use to ultimately access the non-textual item. These textual nodes form a cluster; closely related to the non-text-based item. The cluster representative assigns the non=text-based item a combined descriptor based on the nodes of the cluster. This descriptor can be used to perform information retrieval operations like querying and feedback.

Simple Cluster Based Model of Retrieval
###### Level 1 Cut Offyout
Consider each document $L$ as an $N$-dimensional vector where each term is a dimension. $L_i$ is a weight of term $i$ in document $L$. Use cluster algorithm to calculate the centroid of the points to represent the document in the cluster.
$$W_{d, i} = \frac{L \in C_d}{\mathbf{|C_d|}}$$

where $W$ is the cluster based weight and $C_d$ is the cluster of documents linked to and from document $d$

This only takes into account the immediate neighbors of the node in a hypermedia network. To do update this model, add a peice that takes into account all of the nodes which can be reached from the node in question by following at most two links and vice-versa.
$$W_{d, i} = \frac{L \in C_d}{\mathbf{|C_d|}} +  \frac{L \in C'_d}{\mathbf{|C'_d|}}$$

where C_d is the cluster of documents linked to and from document $d$ and $C'_d$ is the cluster of documents linked to and from document $d$ by exactly two links. Another extension of this model is to add weights to links based on relation of link to node of interest.

###### Limitations
- Limited on the quality and quantity of the links
- Also, the links must be different enough from each other as too similar will return convoluded results.

Can also benefit via query expansion by use of clustering information. Beyond returning non-text-based items, you can also add more context to the nodes used in the clustering process.


[Academia.edu \| Log In](https://www.academia.edu/RegisterToDownload#Papers)

Hyper media can serve two purposes:
- Improve text-retrieval
- Retrieval of multimedia documents

One of the most important contributions was made by Dunlop et al. (1993) and further developed by Harmandas et al. (1997) who introduced the automatic creation of non-text media descriptors to allow efficient and effective multimedia retrieval.

Concepts:
- Node: Basic unit iitem which any kind of info is kept and managed and presented.
- Anchor: How link is represented in a node. In node each link is associated with an anchor that represents node's content area for lin following.
- Links: connection between two related information items or between an information item and a node.

Malcon et al (1991) there was made summary of the limitations of the current closed hypermedia systems and the development of open hypermedia systems:
- Open Hypermedia Systems it is possible to use any application on hypermedia functionality by using proper protocol. No markup info imposed on data, data and processes can be distributed, no distinction between authors and the users.

###### Microcosm
Microcosm is an open hypermedia system developed at the University of Southampton. This systems presents to ways to navigate through info:
- Navigate on the abstract level
	- Navigation made through the classification of the documents until the relevant document is reached.
	- Info about classification of nodes is kept in a seperate database managed by a Document Management System: logical index, document description, keywords, author names, etc. DIrectories are logical indexes and files are identified by text description.
- Hypermedia navigation on the document level

Different kinds of links in the Microcosm model:
- Specific Links: tight connection between two fixed anchors. Important to create the backbone link structure of an application at the document level that allows user to navigate through different items of information that may be related or not.
- Local Links: Link with a fixed destination anchor, but with a source anchor. Depends on rules like pattern matching occurrences like a text string. Important for the definition of words or names, give examples, or show related information valid within the node
- Generic Links: same as Local links, but valid for all the application.
- Dynamic Computed Links: link with a computed destination anchor and a selected source. Allows some information retrieval techniques and suggests starting points for navigation.

Lack of markup in document achieved by keeping all link information in link databases. The Microcosm also seperates the front end from the backend. 
- Front End: viewers and responsible for user interaction
- Backend consists of chain of filters and responsible for many operations requested by the user

Different Retrieval Models
- Boolean Retrieval Models: compare boolean query statement (terms connected by boolean operators) with term set used to identify the document content.
- Vector Space Model: Queries and documents by vecotrs or weighted terms and computes global similarities between queries and documents. Similarity is a function that determines a sort of distance between two representative term vectors.
- Cluster Document Environments classifies all documents under clusters of related information structured in a hierarchal way used to perform browsing or analytical retrieval. This model can get to relevant documents even when they are not related to queries.
- Probabilistic Retrieval Models

It is important to seperate documents on different topics. After splitting text info into structured paragraphs techniques were applied to find similarity  between all paragraphs in a certain node making it possible to create links between related information. This creates a significantly high number of links. By studying the distribution of links within a node it is possible to identify a distribution pattern of the links inside a node to find the theme and segment passages.

Sets of three similar paragraphs are joined in a centroid vector and all similar centroid vectors with three or more paragraphs merged to form a theme. With nodes decomposed into themes and segments it is possible to implement passage retrieval. This allows:
- Text Retrieval (retrieve the best passages in a certain topic)
- Text Summerization: summerize info in a node by retrieving the most relevant paragraphs in a passage and connecting them with the appropriate transition material.

*** Will Continue in Section 4