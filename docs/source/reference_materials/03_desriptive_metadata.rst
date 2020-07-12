III. Migrating Our Linked Data Ready Metadata
=============================================

Introduction
------------

Since 2015, UT Libraries has worked diligently to make our metadata "linked data-ready." You can see this throughout our
MODS with the presence of URIS in `valueURI` and `xlink:href` URIs.

While we've worked to make our data "linked-data ready," this part of our migration will be complex because we have our
own practices that are different from other libraries.  This is because our needs are different and our metadata has been
influence from local requirements and the requirements of metadata sharing agreements with things like the Digital
Publice Library of America.

In this chapter I will focus on:

* An explanation and justification for what we must do prior to migration
* Demonstrate how we can leverage our "linked data-ready" elements during migration.

In the next chapter, I will describe in detail:

* Hyrax's default RDF metadata mapping
* What we lose if we use it out of the box
* Alternative mappings

Hyrax's Metadata Application Profile and Applying our MODS to RDF
-----------------------------------------------------------------

As you'll see in the next chapter, Hyrax's Default Metadata Mapping is extremely basic and to some extent bad.  To be
honest, it does not even adhere to Linked Data principles appropriately. Because of this we would need to do a few things
prior to moving to Hyrax:

1. Create our own MODS to RDF mapping based on our data and needs

    Over time, we have developed our own practices based on our needs.  To ensure our migration is not lossy, we must first
    develop a  MODS to RDF mapping and associated metadata application profile for RDF.

2. Determine if we need an external triple store

    Hyrax does not ship with an external triple store.  If we need one, we will need to select one and install it.

3. Modify the default metadata application profile to remove bad elements or one's that don't meet our needs

    As you'll see in the next chapter, Hyrax's MAP is bad.  We need to modify the bad elements to be good base on our MAP
    and removed the good but unneeded metadata elements.

4. Expand the models of our generated works to include other required elements

    Once we have determined what work types we need, we need to update their models to have our other elements.

5. If necessary, modify code so that Hyrax can "talk" to our external triple store

    More info can be found `here <https://wiki.lyrasis.org/display/samvera/Hydra+Triple+Store+Interest+Group>`_.


Leveraging our "Linked Data-Ready" Elements During Migration
------------------------------------------------------------

===================================
mods:subject/@valueURI/[mods:topic]
===================================

As you'll see in the next section, subjects are strings by default in Hyrax.  We'd need to modify this prior to migration
to migrate this data.

The `Final Recommendation of the Samvera MODS to RDF Description Subgroup Report <https://wiki.duraspace.org/download/attachments/87460857/MODS-RDF-Mapping-Recommendations_SMIG_v1_2019-01.pdf?api=v2>`_
describes multiple ways to do this. In reality, we need to develop our own MAP, but for the purposes of this document, I
will follow the recommendations blindly.

Let's say we had some XML that looked like this:

.. code-block:: xml

    <subject authority="lcsh"
        valueURI="http://id.loc.gov/authorities/subjects/sh85101348">
        <topic>
            Photography of gardens
        </topic>
    </subject>
    <subject authority="lcsh"
        valueURI="http://id.loc.gov/authorities/subjects/sh85053123">
        <topic>
            Gardens, American
        </topic>
    </subject>
    <subject authority="lcsh"
        valueURI="http://id.loc.gov/authorities/subjects/sh85077428">
        <topic>
            Liriodendron tulipifera
        </topic>
    </subject>
    <subject authority="lcsh"
        valueURI="http://id.loc.gov/authorities/subjects/sh85049328">
        <topic>
            Flowering trees
        </topic>
    </subject>

If we were to follow the direct mappings option, our RDF would look like this:

.. code-block:: turtle

    @prefix dce: <http://purl.org/dc/elements/1.1/> .

    <http://example.org/object/1>
        dce:subject <http://id.loc.gov/authorities/subjects/sh85101348>, <http://id.loc.gov/authorities/subjects/sh85053123>, <http://id.loc.gov/authorities/subjects/sh85077428>, <http://id.loc.gov/authorities/subjects/sh85049328> .

.. image:: ../images/subject_direct.png

If we were to follow the minted objects mapping option, our RDF would look like this:

.. code-block:: turtle

    @prefix fedoraObject: <http://[LocalFedoraRepository]/> .
    @prefix utksubjects: <http://[address-to-triplestore]/subjects/> .
    @prefix owl: <https://www.w3.org/2002/07/owl#> .
    @prefix rdfs: <https://www.w3.org/TR/rdf-schema/> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .

    <fedoraObject:tq/57/nr/06/tq57nr067>
        dcterms:subject <utksubjects:1>, <utksubjects:2>, <utksubjects:3>, <utksubjects:4> .

    <utksubjects:1>
        a skos:Concept ;
        rdfs:label "Photography of gardens";
        skos:exactMatch <http://id.loc.gov/authorities/subjects/sh85101348> .

    <utksubjects:2>
        a skos:Concept ;
        rdfs:label "Gardens, American";
        skos:exactMatch <http://id.loc.gov/authorities/subjects/sh85101348> .

    <utksubjects:3>
        a skos:Concept ;
        rdfs:label "Liriodendron tulipifera";
        skos:exactMatch <http://id.loc.gov/authorities/subjects/sh85077428> .

    <utksubjects:4>
        a skos:Concept ;
        rdfs:label "Flowering trees";
        skos:exactMatch <http://id.loc.gov/authorities/subjects/sh85049328> .

.. image:: ../images/subject_minted.png

================================
mods:accessCondition/@xlink:href
================================

=======================================
mods:name/mods:valueURI/[mods:namePart]
=======================================
