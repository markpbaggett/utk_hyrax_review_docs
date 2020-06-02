5. A Quick Primer on Link Data and Linked Data Principles
=========================================================

Linked data attempts to provide a universal way to read and reuse data on the Web. To do this, linking to the files the
data comes in is not enough.  Instead, you want data that you link to and that data to link to related data.  This helps
foster reuse of data between websits.

The 5 Star Scoring System of Linked Data
----------------------------------------

There is a five scoring system for defining the quality of linked data.  It is:

|:star2:| Data is available on the Web, in whatever format (for example, a TIFF of a scanned image)

|:star2:| |:star2:| Data is available as machine-readable structured data (for example, a Microsoft Excel spreadsheet)

|:star2:| |:star2:| |:star2:| Data is available in a non-proprietary format (for example, a CSV, a TSV, or and XML file)

|:star2:| |:star2:| |:star2:| |:star2:| Data is published using open data standards from the World Wide Web Consortium.

|:star2:| |:star2:| |:star2:| |:star2:| |:star2:| All of the above apply, plus links to other people's data.

This 5-star system is cumulative; each succeeding star presumes that your data meets the criteria from all proceeding
stars.

The W3C often paraphrases the 5 star ( |:star2:| ) system as:

|:star2:| On the web

|:star2:| |:star2:| Machine-readable data

|:star2:| |:star2:| |:star2:| Non-proprietary format

|:star2:| |:star2:| |:star2:| |:star2:| RDF standards

|:star2:| |:star2:| |:star2:| |:star2:| |:star2:| Linked RDF

Resource description framework (RDF) is used for the best quality linked data.

The primary purpose of linked data is to allow data to be combined with other Linked Data to form new knowledge.

The 4 Principles of Linked Data
-------------------------------

Linked Data and RDF are not the same thing.  While Linked Data uses RDF, it is separate from RDF because of Tim
Berners-Lee's `4 Principles of Linked Data <https://en.wikipedia.org/wiki/Linked_data#Principles>`_:

1. Use URIs as names for things
2. Use HTTP URIs so that people can look up those names
3. When someone looks up a URI, provide useful information, using the standards (RDF*, SPARQL).
4. Include links to other URIS, so people can discover more things.

=========================================
Principle 1: Use URIs as names for things
=========================================

If you can't identify something, you can't talk about it.  The first principle states you should use a URI to identify
something. A thing can be virtually anyting (a file, a digital object, a person, a photographer, a dog, a subject), but
the thing should be described by a URI.

=================================================================
Principle 2: Use HTTP URIs so that people can look up those names
=================================================================

A URI doesn't have to be a web URI.  It could be a file URI like file:///home/mark/my_file or an ISBN like
isbn:0140437428.  The problem here is that if you do either of these, you can't look them up on the web.  This principle
ensures that you can resolve data by using HTTP.

=====================================================================
Principle 3:  When someone looks up a URI, provide useful information
=====================================================================

========================================
Principle 4: Include links to other URIs
========================================
