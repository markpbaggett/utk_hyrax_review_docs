VII. Goodbye MODS, Hello RDF!
-----------------------------

=====
About
=====

One of the biggest changes in our move to a next generation digital repository system will be saying goodbye to MODS
and XML for descriptive metadata.

Instead, our descriptive metadata will be serialized as `RDF <https://www.w3.org/RDF/>`_.

This is an incredibly important certainty as it will:

1. Determine how interoperability works between objects in the system and external services
2. Dictate how we will describe new objects
3. Influence how we go about migration
4. Force us to make decisions about future description and if we drop anything that we currently describe

In this section, I will talk about:

1. An explanation of Hyrax’s default MAP
2. How some of our sample MODS records would map to Hyrax out-of-the-box
3. What we would lose
4. Alternative mappings based on the Samvera Working Group Document (Simple and Complex)

======================================
Hyrax 2.0 Metadata Application Profile
======================================

Hyrax ships with a default Metadata Application Profile. The MAP is divided into two sections: Core Metadata and Basic
Metadata. Core metadata cannot be changed and is required for Hyrax to function properly.  Basic Metadata is customizable.

It's important to note that while the Hyrax MAP is influenced by the
`Final Recommendation of the Samvera MODS to RDF Description Subgroup Report <https://wiki.duraspace.org/download/attachments/87460857/MODS-RDF-Mapping-Recommendations_SMIG_v1_2019-01.pdf?api=v2>`_,
it does not follow it for simple or complex minting. Because of this, we would likely need to:

1. Selectively lose metadata
2. Define our own mapping

----------
Namespaces
----------

+------------------+----------------------------+----------------------------------------+
| Predicate Prefix | Rdf-vocab Predicate Prefix | Namespace                              |
+==================+============================+========================================+
| dce:             | DC11:                      | http://purl.org/dc/elements/1.1/       |
+------------------+----------------------------+----------------------------------------+
| dct:             | DC:                        | http://purl.org/dc/terms/              |
+------------------+----------------------------+----------------------------------------+
| edm:             | EDM:                       | http://www.europeana.eu/schemas/edm/   |
+------------------+----------------------------+----------------------------------------+
| foaf:            | FOAF:                      | http://xmlns.com/foaf/0.1/             |
+------------------+----------------------------+----------------------------------------+
| rdfs:            | RDFS:                      | http://www.w3.org/2000/01/rdf-schema#  |
+------------------+----------------------------+----------------------------------------+
| xsd:             |                            | http://www.w3.org/2001/XMLSchema#      |
+------------------+----------------------------+----------------------------------------+
| mrel:            |                            | http://id.loc.gov/vocabulary/relators/ |
+------------------+----------------------------+----------------------------------------+

Local controlled vocabularies can be pulled in from
`here <https://github.com/samvera/hyrax/blob/4fd8d9ad3c32db7deffc3b5246af5d1459a4b046/lib/generators/hyrax/config_generator.rb>`_.

-------------
Core Metadata
-------------

Core metadata should never be removed and can be found in `core_metadata.rb <https://github.com/samvera/hyrax/blob/2.0-stable/app/models/concerns/hyrax/core_metadata.rb>`_.

+------------------+-------------------+-------------------------------------------------------------+-----------------+----------------------------+------------------------------------+----------+------------+
| Property (Field) | Predicate         | Rdf-vocab Predicate                                         | Recommendation  | Expected Value (Data Type) | Expected Value (Controlled Source) | Multiple | Obligation |
+==================+===================+=============================================================+=================+============================+====================================+==========+============+
| title            | dct:title         | ::RDF::Vocab::DC.title                                      | MUST (Required) | xsd:string (Literal)       | n/a                                | TRUE     | {1,n}      |
+------------------+-------------------+-------------------------------------------------------------+-----------------+----------------------------+------------------------------------+----------+------------+
| depositor        | mrel:dpt          | ::RDF::URI.new(‘http://id.loc.gov/vocabulary/relators/dpt’) | MUST (Required) | user                       | n/a                                | FALSE    | {1}        |
+------------------+-------------------+-------------------------------------------------------------+-----------------+----------------------------+------------------------------------+----------+------------+
| date_uploaded    | dct:dateSubmitted | ::RDF::Vocab::DC.dateSubmitted                              | MUST (Required) | Literal                    | n/a                                | FALSE    | {1}        |
+------------------+-------------------+-------------------------------------------------------------+-----------------+----------------------------+------------------------------------+----------+------------+
| date_modified    | dct:modified      | ::RDF::Vocab::DC.modified                                   | MUST (Required) | Literal                    | n/a                                | FALSE    | {1}        |
+------------------+-------------------+-------------------------------------------------------------+-----------------+----------------------------+------------------------------------+----------+------------+

--------------
Basic Metadata
--------------

Basic metadata properties are defined in `basic_metadata.rb <https://github.com/samvera/hyrax/blob/2.0-stable/app/models/concerns/hyrax/basic_metadata.rb>`_.

**MUSTs** are required for form validation.

+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| Property (Field) | Predicate       | Rdf-vocab Predicate            | Recommendation  | Expected Value (Data Type)                    | Expected Value (Controlled Source)  | Multiple | Obligation |
+==================+=================+================================+=================+===============================================+=====================================+==========+============+
| creator          | dce:creator     | ::RDF::Vocab::DC11.creator     | MUST (Required) | xsd:string (Literal)                          | n/a                                 | TRUE     | {1,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| keyword          | dce:relation    | ::RDF::Vocab::DC11.relation    | MUST (Required) | xsd:string (Literal)                          | n/a                                 | TRUE     | {1,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| rights_statement | edm:rights      | ::RDF::Vocab::EDM.rights       | MUST (Required) | xsd:anyUri                                    | Rights statements menu as YAML      | FALSE    | {1}        |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| contributor      | dce:contributor | ::RDF::Vocab::DC11.contributor | MAY             | xsd:string (Literal)                          | n/a                                 | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| description      | dce:description | ::RDF::Vocab::DC11.description | MAY             | xsd:string (Literal)                          | n/a                                 | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| license          | dct:rights      | ::RDF::Vocab::DC.rights        | MAY             | xsd:anyURI                                    | License menu as YAML                | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| publisher        | dce:publisher   | ::RDF::Vocab::DC11.publisher   | MAY             | xsd:string (Literal)                          | n/a                                 | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| date_created     | dct:created     | ::RDF::Vocab::DC.created       | MAY             | xsd:date or xsd:dateTime xsd:string (Literal) | n/a                                 | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| subject          | dce:subject     | ::RDF::Vocab::DC11.subject     | MAY             | xsd:string (Literal)                          | n/a (but existing vocab encouraged) | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| language         | dce:language    | ::RDF::Vocab::DC11.language    | MAY             | xsd:string (Literal)                          | n/a                                 | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| identifier       | dct:identifier  | ::RDF::Vocab::DC.identifier    | MAY             | xsd:string (Literal)                          | n/a                                 | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| based_near       | foaf:basedNear  | ::RDF::Vocab::FOAF.based_near  | MAY             | xsd:anyURI                                    | GeoNames web service                | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| related_url      | rdfs:seeAlso    | ::RDF::RDFS.seeAlso            | MAY             | xsd:string or xsd:anyURI                      | n/a                                 | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| source           | dct:source      | ::RDF::Vocab::DC.source        | MAY             | xsd:string (Literal)                          | n/a                                 | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+
| resource_type    | dct:type        | ::RDF::Vocab::DC.type          | MAY             | xsd:string (Literal)                          | Type menu as YAML                   | TRUE     | {0,n}      |
+------------------+-----------------+--------------------------------+-----------------+-----------------------------------------------+-------------------------------------+----------+------------+


====================================================
Mapping UTK Metadata to Out-of-the-Box Hyrax MAP 2.0
====================================================

Now that we've seen the default MAP, how might our data *map* to it.

---------------------------------
Example 1: Knoxville Garden Slide
---------------------------------

This is a sample MODS record from the object from Knoxville Garden Slides that we saw earlier.

.. code-block:: xml
    :linenos:
    :caption: knoxgardens:115.xml
    :name: knoxgardens:115.xml

    <?xml version="1.0" encoding="UTF-8"?>
    <mods xmlns="http://www.loc.gov/mods/v3"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          xmlns:xs="http://www.w3.org/2001/XMLSchema"
          xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">
       <identifier type="local">0012_000463_000214</identifier>
       <identifier type="pid">knoxgardens:115</identifier>
       <identifier type="slide number">Slide 1</identifier>
       <identifier type="film number">Film  96</identifier>
       <identifier type="spc">record_spc_4489</identifier>
       <titleInfo>
          <title>Tulip Tree</title>
       </titleInfo>
       <abstract>Photograph slide of the Tennessee state tree, the tulip tree</abstract>
       <originInfo>
          <dateCreated qualifier="inferred">1930-1939</dateCreated>
          <dateCreated encoding="edtf"
                       point="start"
                       qualifier="inferred"
                       keyDate="yes">1930</dateCreated>
          <dateCreated encoding="edtf" point="end" qualifier="inferred">1939</dateCreated>
       </originInfo>
       <physicalDescription>
          <form authority="aat" valueURI="http://vocab.getty.edu/aat/300134977">lantern slides</form>
          <extent>3 1/4 x 5 inches</extent>
          <internetMediaType>image/jp2</internetMediaType>
       </physicalDescription>
       <name>
          <namePart>Unknown</namePart>
          <role>
             <roleTerm authority="marcrelator"
                       valueURI="http://id.loc.gov/vocabulary/relators/pht">Photographer</roleTerm>
          </role>
       </name>
       <subject authority="lcsh"
                valueURI="http://id.loc.gov/authorities/subjects/sh85101348">
          <topic>Photography of gardens</topic>
       </subject>
       <subject authority="lcsh"
                valueURI="http://id.loc.gov/authorities/subjects/sh85053123">
          <topic>Gardens, American</topic>
       </subject>
       <subject authority="lcsh"
                valueURI="http://id.loc.gov/authorities/subjects/sh85077428">
          <topic>Liriodendron tulipifera</topic>
       </subject>
       <subject authority="lcsh"
                valueURI="http://id.loc.gov/authorities/subjects/sh85049328">
          <topic>Flowering trees</topic>
       </subject>
       <subject authority="naf"
                valueURI="http://id.loc.gov/authorities/names/n79109786">
          <geographic>Knoxville (Tenn.)</geographic>
          <cartographics>
             <coordinates>35.96064, -83.92074</coordinates>
          </cartographics>
       </subject>
       <note>Mrs. A. C. Bruner donated this collection to the University of Tennessee. Creation dates were inferred from the dates associated with the archival collection and the activity dates of the Jim Thompson Company.</note>
       <relatedItem displayLabel="Project" type="host">
          <titleInfo>
             <title>Knoxville Garden Slides</title>
          </titleInfo>
       </relatedItem>
       <typeOfResource>still image</typeOfResource>
       <relatedItem displayLabel="Collection" type="host">
          <titleInfo>
             <title>Knoxville Gardens Slides</title>
          </titleInfo>
          <identifier>MS.1324</identifier>
          <location>
             <url>https://n2t.net/ark:/87290/v88w3bgf</url>
          </location>
       </relatedItem>
       <location>
          <physicalLocation valueURI="http://id.loc.gov/authorities/names/no2014027633">University of Tennessee, Knoxville. Special Collections</physicalLocation>
       </location>
       <recordInfo>
          <recordContentSource valueURI="http://id.loc.gov/authorities/names/n87808088">University of Tennessee, Knoxville. Libraries</recordContentSource>
          <languageOfCataloging>
             <languageTerm type="text" authority="iso639-2b">English</languageTerm>
          </languageOfCataloging>
       </recordInfo>
       <accessCondition type="use and reproduction"
                        xlink:href="http://rightsstatements.org/vocab/CNE/1.0/">Copyright Not Evaluated</accessCondition>
    </mods>

Following the metadata application profile above, here's how that metadata record would look as TTL in Fedora and feed
the front end / Solr in Hyrax.

Notice how an identifier is now just a dcterms identifier.

.. code-block:: turtle
    :linenos:
    :caption: TTL representation of knoxgardens:115.xml mapping to Hyrax MAP 2.0 Out-of-the-Box
    :name: TTL representation of knoxgardens:115.xml mapping to Hyrax MAP 2.0 Out-of-the-Box


    @prefix fedoraObject: <http://[LocalFedoraRepository]/>.
    @prefix dct: <http://purl.org/dc/terms/> .
    @prefix dce: <http://purl.org/dc/elements/1.1/> .
    @prefix edm: <http://www.europeana.eu/schemas/edm/> .
    @prefix foaf: <http://xmlns.com/foaf/0.1/> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    @prefix mrel: <http://id.loc.gov/vocabulary/relators/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        dct:title "Tulip Tree" ;
        dct:identifier "0012_000463_000214", "knoxgardens:115", "Slide 1", "Film  96", "record_spc_4489" ;
        dce:description "Photograph slide of the Tennessee state tree, the tulip tree" ;
        dct:created "1930-1939", "1930", "1939" ;
        dce:creator "Unknown" ;
        dce:subject "Photography of gardens", "Gardens, American", "Liriodendron tulipifera", "Flowering trees", "Knoxville (Tenn.)" ;
        dct:type "still image" ;
        rdfs:seeAlso <https://n2t.net/ark:/87290/v88w3bgf> ;
        edm:rights <http://rightsstatements.org/vocab/CNE/1.0/> .

**Notice**: The highlighted metadata elements below are now gone!

.. code-block:: xml
    :emphasize-lines: 24-28, 31-34, 36-37, 40-41, 44-45, 48-49, 52-53, 55-57, 59 - 64, 66-71, 73 - 83
    :linenos:
    :caption: Illustrating lost data from knoxgardens:115.xml
    :name: Illustrating lost data from knoxgardens:115.xml

    <?xml version="1.0" encoding="UTF-8"?>
    <mods xmlns="http://www.loc.gov/mods/v3"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          xmlns:xs="http://www.w3.org/2001/XMLSchema"
          xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-5.xsd">
       <identifier type="local">0012_000463_000214</identifier>
       <identifier type="pid">knoxgardens:115</identifier>
       <identifier type="slide number">Slide 1</identifier>
       <identifier type="film number">Film  96</identifier>
       <identifier type="spc">record_spc_4489</identifier>
       <titleInfo>
          <title>Tulip Tree</title>
       </titleInfo>
       <abstract>Photograph slide of the Tennessee state tree, the tulip tree</abstract>
       <originInfo>
          <dateCreated qualifier="inferred">1930-1939</dateCreated>
          <dateCreated encoding="edtf"
                       point="start"
                       qualifier="inferred"
                       keyDate="yes">1930</dateCreated>
          <dateCreated encoding="edtf" point="end" qualifier="inferred">1939</dateCreated>
       </originInfo>
       <physicalDescription>
          <form authority="aat" valueURI="http://vocab.getty.edu/aat/300134977">lantern slides</form>
          <extent>3 1/4 x 5 inches</extent>
          <internetMediaType>image/jp2</internetMediaType>
       </physicalDescription>
       <name>
          <namePart>Unknown</namePart>
          <role>
             <roleTerm authority="marcrelator"
                       valueURI="http://id.loc.gov/vocabulary/relators/pht">Photographer</roleTerm>
          </role>
       </name>
       <subject authority="lcsh"
                valueURI="http://id.loc.gov/authorities/subjects/sh85101348">
          <topic>Photography of gardens</topic>
       </subject>
       <subject authority="lcsh"
                valueURI="http://id.loc.gov/authorities/subjects/sh85053123">
          <topic>Gardens, American</topic>
       </subject>
       <subject authority="lcsh"
                valueURI="http://id.loc.gov/authorities/subjects/sh85077428">
          <topic>Liriodendron tulipifera</topic>
       </subject>
       <subject authority="lcsh"
                valueURI="http://id.loc.gov/authorities/subjects/sh85049328">
          <topic>Flowering trees</topic>
       </subject>
       <subject authority="naf"
                valueURI="http://id.loc.gov/authorities/names/n79109786">
          <geographic>Knoxville (Tenn.)</geographic>
          <cartographics>
             <coordinates>35.96064, -83.92074</coordinates>
          </cartographics>
       </subject>
       <note>Mrs. A. C. Bruner donated this collection to the University of Tennessee. Creation dates were inferred from the dates associated with the archival collection and the activity dates of the Jim Thompson Company.</note>
       <relatedItem displayLabel="Project" type="host">
          <titleInfo>
             <title>Knoxville Garden Slides</title>
          </titleInfo>
       </relatedItem>
       <typeOfResource>still image</typeOfResource>
       <relatedItem displayLabel="Collection" type="host">
          <titleInfo>
             <title>Knoxville Gardens Slides</title>
          </titleInfo>
          <identifier>MS.1324</identifier>
          <location>
             <url>https://n2t.net/ark:/87290/v88w3bgf</url>
          </location>
       </relatedItem>
       <location>
          <physicalLocation valueURI="http://id.loc.gov/authorities/names/no2014027633">University of Tennessee, Knoxville. Special Collections</physicalLocation>
       </location>
       <recordInfo>
          <recordContentSource valueURI="http://id.loc.gov/authorities/names/n87808088">University of Tennessee, Knoxville. Libraries</recordContentSource>
          <languageOfCataloging>
             <languageTerm type="text" authority="iso639-2b">English</languageTerm>
          </languageOfCataloging>
       </recordInfo>
       <accessCondition type="use and reproduction"
                        xlink:href="http://rightsstatements.org/vocab/CNE/1.0/">Copyright Not Evaluated</accessCondition>
    </mods>

====================
Alternative Mappings
====================

As I mentioned earlier, Hyrax Map 2.0 is influenced by, but does not follow, the
`Final Recommendation of the Samvera MODS to RDF Description Subgroup Report <https://wiki.duraspace.org/download/attachments/87460857/MODS-RDF-Mapping-Recommendations_SMIG_v1_2019-01.pdf?api=v2>`_.

This document provides two mappings for MODS to RDF:

1. Direct Mappings (Simple Option)

    This option provides mappings from MODS XML elements to RDF statements
    (subject, predicate, object) and do not require creating or maintaining local objects for concepts such as
    subjects, people, events, or places. All statements either end in a URI sourced from an external
    vocabulary (LCSH, for example) or in a literal value (text string). These RDF statements can be stored,
    maintained, and updated directly with the digital object being described. However, as the examples
    provided below demonstrate, while this is a simpler method for mapping, there are cases where
    granularity and detail from MODS records is lost because not every data point is directly mappable to
    an RDF property.

2. Minted Objects Mappings (Complex Option)

    This option creates a local concept object (which must be maintained
    by the local repository system) for that MODS element (a title object, a name object, etc.). These
    objects substitute for the use of blank nodes, which are problematic to manage in many data stores.
    The local object then has single-level RDF statements (subject, predicate, object) that provide either a
    URI sourced from an external vocabulary, URI for a local object, or a literal value (text string). The RDF
    statements stored with the digital object being described are pointers to these local concept objects.

    These local objects can be re-used for describing multiple digital objects (the same name concept
    object or subject concept object can be used to describe many objects in a repository). Any updates to
    that single concept object update the descriptive information for all digital objects described using that
    concept object. This option also allows for all details from MODS records to be serialized as RDF for
    complicated MODS elements such as names and subjects.

    Minted Objects increase the complexity of the data model, but descriptive bibliographic metadata is
    inherently complex. Many RDF predicates used in bibliographic or cultural heritage ontologies have a
    defined ​ range ​ (the class of acceptable values) of a URI or other RDF object type that is not a string
    literal. The mappings in this document strive to adhere to the defined ranges in all examples, which
    necessitates the need for creating local objects for concepts, titles, persons, places, collections, or
    organizations that are not represented by an existing URI.

----------------------
Direct Mappings Option
----------------------

Here is an example mapping from MODS to the Direct Mappings Option.

.. code-block:: turtle
    :linenos:
    :caption: TTL representation of knoxgardens:115.xml mapping to the Samvera MODS to RDF Description Subgroup's Direct Mapping
    :name: TTL representation of knoxgardens:115.xml mapping to the Samvera MODS to RDF Description Subgroup's Direct Mapping

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix identifiers: <http://id.loc.gov/vocabulary/identifiers> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
    @prefix edm: <http://www.europeana.eu/schemas/edm/> .
    @prefix rdau: <http://rdaregistry.info/Elements/u/#> .
    @prefix dce: <http://purl.org/dc/elements/1.1/> .
    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix bf: <http://id.loc.gov/ontologies/bibframe/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        identifiers:local "0012_000463_000214", "record_spc_4489", "Slide 1", "Film 96" ;
        dcterms:identifier "knoxgardens:115" ;
        dcterms:title "Tulip Tree" ;
        dcterms:abstract "Photograph slide of the Tennessee state tree, the tulip tree" ;
        dcterms:created "1930-1939", "1930", "1939" ;
        skos:note "Date: Inferred" ;
        edm:hastype <http://vocab.getty.edu/aat/300134977> ;
        rdau:extent "3 1/4 x 5 inches" ;
        dce:format "image/jp2" ;
        relators:pht "Unknown" ;
        dce:subject <http://id.loc.gov/authorities/subjects/sh85101348>, <http://id.loc.gov/authorities/subjects/sh85053123>, <http://id.loc.gov/authorities/subjects/sh85077428>, <http://id.loc.gov/authorities/subjects/sh85049328>;
        dce:coverage <http://id.loc.gov/authorities/names/n79109786>, "35.96064, -83.92074" ;
        skos:note "Mrs. A. C. Bruner donated this collection to the University of Tennessee. Creation dates were inferred from the dates associated with the archival collection and the activity dates of the Jim Thompson Company." ;
        relators:rps <http://id.loc.gov/authorities/names/no2014027633> ;
        bf:physicalLocation "University of Tennessee, Knoxville. Special Collections" ;
        edm:rights <http://rightsstatements.org/vocab/CNE/1.0/> .

**Note**: I haven't gotten around to modelling or have things to look at related to these things:

    dce:coverage (cartographics), dcterms:created (inferred dates), dce:subjects. relatedItem project, skipped all
    relatedItems for now, skipped record info

-----------------------
Complex Mappings Option
-----------------------

.. code-block:: turtle
    :linenos:
    :caption: TTL representation of knoxgardens:115.xml mapping to the Samvera MODS to RDF Description Subgroup's Minted Object Mapping with associated Objects
    :name: TTL representation of knoxgardens:115.xml mapping to the Samvera MODS to RDF Description Subgroup's Minted Object Mapping with associated Objects

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix utkevents: <http://[address-to-triplestore]/events/> .
    @prefix utktitles: <http://[address-to-triplestore]/titles/> .
    @prefix utksubjects: <http://[address-to-triplestore]/subjects/> .
    @prefix utkspatial: <http://[address-to-triplestore]/spatial/> .
    @prefix utknotes: <http://[address-to-triplestore]/notes/> .
    @prefix utkphysicalcollections: <http://[address-to-triplestore]/physicalcollections/> .
    @prefix rdfs: <https://www.w3.org/TR/rdf-schema/> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
    @prefix dcterms: <http://purl.org/dc/terms/> .
    @prefix bf: <http://id.loc.gov/ontologies/bibframe/> .
    @prefix relators: <http://id.loc.gov/vocabulary/relators> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
    @prefix geojson: <https://purl.org/geojson/vocab#> .
    @prefix pcdm: <http://pcdm.org/models#> .
    @prefix dbo: <http://dbpedia.org/ontology/> .
    @prefix identifiers: <http://id.loc.gov/vocabulary/identifiers> .
    @prefix edm: <http://www.europeana.eu/schemas/edm/> .
    @prefix rdau: <http://rdaregistry.info/Elements/u/#> .
    @prefix foaf: <http://xmlns.com/foaf/0.1/> .
    @prefix dcmitype: <http://purl.org/dc/dcmitype/> .
    @prefix owl: <https://www.w3.org/2002/07/owl#> .
    @prefix dce: <http://purl.org/dc/elements/1.1/> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        dce:title <utktitles:1> ;
        identifiers:local "0012_000463_000214", "record_spc_4489", "Slide 1", "Film 96" ;
        dcterms:identifier "knoxgardens:115" ;
        dcterms:abstract "Photograph slide of the Tennessee state tree, the tulip tree" ;
        bf:provisionActivity <utkevents:1>, <utkevents:2>, <utkevents:3> ;
        edm:hastype <http://vocab.getty.edu/aat/300134977> ;
        rdau:extent "3 1/4 x 5 inches" ;
        dce:format "image/jp2" ;
        relators:pht <utknames:1> ;
        dcterms:subject <utksubjects:1>, <utksubjects:2>, <utksubjects:3>, <utksubjects:4> ;
        dcterms:spatial <utkspatial:1> ;
        bf:Note <utknotes:1> ;
        pcdm:memberOf <fedoraObject:jk/88/99/adklasd908ads> ;
        relators:rps <http://id.loc.gov/authorities/names/no2014027633> ;
        bf:physicalLocation "University of Tennessee, Knoxville. Special Collections" ;
        edm:rights <http://rightsstatements.org/vocab/CNE/1.0/> .

    <utktitles:1>
        a bf:title ;
        rdfs:label "Tulip Tree" .

    <utkevents:1>
        a bf:provisionActivity ;
        dcterms:created "1930" ;
        skos:note "Date: Inferred" .

    <utkevents:2>
        a bf:provisionActivity ;
        dcterms:created "1939" ;
        skos:note "Date: Inferred" .

    <utkevents:3>
        a bf:provisionActivity ;
        dcterms:created "1930-1939" ;
        skos:note "Date: Inferred" .

    <utknames:1>
        a foaf:person ;
        foaf:name "Unknown" .

    <utksubjects:1>
        a skos:Concept ;
        rdfs:label "Photography of gardens";
        skos:exactMatch <http://id.loc.gov/authorities/subjects/sh85101348.html> .

    <utksubjects:2>
        a skos:Concept ;
        rdfs:label "Gardens, American";
        skos:exactMatch <http://id.loc.gov/authorities/subjects/sh85101348.html> .

    <utksubjects:3>
        a skos:Concept ;
        rdfs:label "Liriodendron tulipifera";
        skos:exactMatch <http://id.loc.gov/authorities/subjects/sh85077428.html> .

    <utksubjects:4>
        a skos:Concept ;
        rdfs:label "Flowering trees";
        skos:exactMatch <http://id.loc.gov/authorities/subjects/sh85049328.tml> .

    <utkspatial:1>
        a edm:Place ;
        rdfs:label "Knoxville (Tenn.)" ;
        owl:sameAs <http://id.loc.gov/authorities/names/n79109786> ;
        geojson:coordinates "35.96064, -83.92074" .

    <utknotes:1>
        a bf:Note ;
        rdfs:label "Mrs. A. C. Bruner donated this collection to the University of Tennessee. Creation dates were inferred from the dates associated with the archival collection and the activity dates of the Jim Thompson Company." .

    <fedoraObject:jk/88/99/adklasd908ads>
        a pcdm:Collection ;
        rdfs:label "Knoxville Gardens Slides" .

    <utkphysicalcollections:1>
        a dcmitype:Collection ;
        rdfs:label "Knoxville Gardens Slides" ;
        owl:sameAs <https://n2t.net/ark:/87290/v88w3bgf> .




**Note**: I never got around to or need to think about these things:

    `@TODO` or talkabout: provision activities, name modeling, project, physicalcollections:1 owl:sameAs, skipped recordInfo.
