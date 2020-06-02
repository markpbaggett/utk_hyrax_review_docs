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

In addition to using HTTP, principle 3 states that your URI should often be resolvable if not all the time. To do this,
your URI should link to another existing web resource or you should create or **mint** a web resource if one does not
exist. In either case, your URI should resolve to useful and machine actionable descriptions of the thing you've named.

Let's say we **minted** a web resource to describe the Ruby programming language.  That web resource may look something
like this:

.. code-block:: turtle
    :linenos:
    :emphasize-lines: 7

    @prefix utksubect: <http://[address-to-triplestore]/subjects/> .
    @prefix rdf: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <utksubject:1>
        a skos:Concept ;
        rdf:label "Ruby (Computer program language)".

You can see our web resource `http://[address-to-triplestore]/subjects/1` has a label "Ruby (Computer program language)"
and is a `skos:Concept <https://www.w3.org/2009/08/skos-reference/skos.html#Concept>`_.


========================================
Principle 4: Include links to other URIs
========================================

Finally, the URIs you link to should link to other things.  This is what makes linked data "linked."  For example, let's
improve our **minted object**.

.. code-block:: turtle
    :linenos:
    :emphasize-lines: 9

    @prefix utksubect: <http://[address-to-triplestore]/subjects/> .
    @prefix rdf: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
    @prefix schema: <https://schema.org/> .

    <utksubject:1>
        a skos:Concept ;
        rdf:label "Ruby (Computer program language)" ;
        schema:sameAs <http://id.loc.gov/authorities/subjects/sh00000128> .

Notice, that our **minted object** links to another RDF resource. The relationship tells our application and other
applications linking to our application that `<utksubject:1>` is the same thing as `this <http://id.loc.gov/authorities/subjects/sh00000128>`_.
Also, the URI that is the sameAS our `<utksubject:1>` has actionable data and links to other actionable things:

.. code-block:: turtle
    :linenos:

    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
    @prefix ns0: <http://purl.org/vocab/changeset/schema#> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

    <http://id.loc.gov/authorities/subjects/sh00000128>
      a skos:Concept ;
      skos:prefLabel "Ruby (Computer program language)"@en ;
      skos:broader <http://id.loc.gov/authorities/subjects/sh2006006405> ;
      skos:closeMatch <http://data.bnf.fr/ark:/12148/cb144105976>, <http://www.wikidata.org/entity/Q161053>, <http://id.worldcat.org/fast/1101038> ;
      skos:inScheme <http://id.loc.gov/authorities/subjects> ;
      skos:changeNote [
        a <http://purl.org/vocab/changeset/schema#ChangeSet> ;
        ns0:subjectOfChange <http://id.loc.gov/authorities/subjects/sh00000128> ;
        ns0:creatorName <http://id.loc.gov/vocabulary/organizations/dlc> ;
        ns0:createdDate "2000-08-31T00:00:00"^^xsd:dateTime ;
        ns0:changeReason "new"^^xsd:string
      ], [
        a ns0:ChangeSet ;
        ns0:subjectOfChange <http://id.loc.gov/authorities/subjects/sh00000128> ;
        ns0:creatorName <http://id.loc.gov/vocabulary/organizations/abau> ;
        ns0:createdDate "2006-12-05T07:51:11"^^xsd:dateTime ;
        ns0:changeReason "revised"^^xsd:string
      ] .
