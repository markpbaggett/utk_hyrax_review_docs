Content Modeling in Hyrax
=========================

Work Types aka "Curation Concerns"
----------------------------------

In Hyrax, types of digital repository objects are referred to as work types.  In Islandora 7, we referred to these as
content models with associated "solution packs."  It's also worth noting that these were previously referred to as
curation concerns, which is where the old front-end solution for Hydra go its name.

In Hyrax, all repositories have at least one work type that you establish with a rails generator tool after installation.

Here's an example:

.. code-block:: sh

    rails generate hyrax:work Work

You can have as many "work types" as you need, but there are few rules. The type must be camel-cased:

.. code-block:: sh

    rails generate hyrax:work MovingImage

You can namespace these if necessary by using a forward slash:

.. code-block:: sh

    rails generate hyrax:work Marks/MovingImage

Also, it's important to note that these work types often have pluralized forms that are used in routing.  Rather than
simply adding an "s", Rails attempts to guess what the route should be. If this route doesn't meet expectations you can
override it in the `config/initializers/inflections.rb` file:

.. code-block:: ruby

    ActiveSupport::Inflector.inflections(:en) do |inflect|
        inflect.irregular 'atlas', 'atlases'
    end

Work Types, Fedora, and Portland Common Data Model
--------------------------------------------------

Hyrax, like most modern Fedora stacks, uses the `Portland Common Data Model <https://github.com/duraspace/pcdm/wiki>`_.
From the PCDM wiki:

    The Portland Common Data Model (PCDM) is a flexible, extensible domain model that is intended to underlie a wide array of repository and DAMS applications. The primary objective of this model is to establish a framework that developers of tools (e.g., Samvera-based engines, such as Hyrax, Hyku, Sufia, and Avalon; Islandora; custom Fedora sites) can use for working with models in a general way, allowing adopters to easily use custom models with any tool. Given this interoperability goal, the initial work has been focused on structural metadata and access control, since these are the key actionable metadata.

    To encourage adoption, this model must support the most complex use cases, which include rich hierarchies of inter-related collections and works, but also elegantly support the simplest use cases, such as a single user-contributed file with a few fields of metadata. It must provide a compact interface that tool developers can easily implement, but also be extensible enough for adopters to customize to their local needs.

    As the community migrates to Fedora 4, much of our metadata is migrating to RDF. This model encourages linked data best practices, such as using URIs to identify all resources, using widely-used vocabularies where possible, and subclassing existing classes and properties when creating new terms.

Here is a description of the `Knoxville Garden Slides` Collection and `knoxgardens:115.xml` modeled as rdf using PCDM in a Hyrax system.

.. code-block:: turtle
    :linenos:
    :caption: knoxgardens:115 in Hyrax as ttl and using PCDM, highlight structural metadata, with only core descriptive metadata
    :name:  knoxgardens:115 in Hyrax as ttl and using PCDM with only core metadata

    @prefix pcdm:  <http://pcdm.org/models#> .
    @prefix dct: <http://purl.org/dc/terms/> .
    @prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix relators: <http://id.loc.gov/vocabulary/relators/> .
    @prefix pcdmuse:  <http://pcdm.org/use#> .
    @prefix hydra:  <http://projecthydra.org/works/models#> .
    @prefix fedora:  <http://fedora.info/definitions/v4/repository#> .
    @prefix iana:  <http://www.iana.org/assignments/relation/> .
    @prefix faccess:  <http://fedora.info/definitions/1/0/access/ObjState#> .
    @prefix fmodels:  <info:fedora/fedora-system:def/model#> .
    @prefix ebucore:  <http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#> .
    @prefix acl:  <http://www.w3.org/ns/auth/acl#> .
    @prefix ldp:  <http://www.w3.org/ns/ldp#> .

    <http://localhost:8984/rest/dev/pr/76/f3/40/pr76f340k>
        rdf:type pcdm:Object ;
        rdf:type hydra:Work ;
        rdf:type fedora:Container;
        rdf:type fedora:Resource;
        dct:title "Tulip Tree"^^<http://www.w3.org/2001/XMLSchema#string> ;
        relators:dpt "mbagget1@utk.edu"^^<http://www.w3.org/2001/XMLSchema#string> ;
        dct:dateSubmitted "2020-05-12T21:59:19.647826267+00:00"^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
        dct:modified "2020-05-12T21:59:19.65408406+00:00"^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
        pcdm:memberOf <http://localhost:8984/rest/dev/gm/80/hv/32/gm80hv32k> ;
        iana:last <http://localhost:8984/rest/dev/pr/76/f3/40/pr76f340k/list_source#g47218150558240> ;
        faccess:objState faccess:active ;
        fmodels:hasModel "Image"^^<http://www.w3.org/2001/XMLSchema#string> ;
        ebucore:hasRelatedMediaFragment <http://localhost:8984/rest/dev/9p/29/09/32/9p2909328> ;
        fedora:createdBy "bypassAdmin"^^<http://www.w3.org/2001/XMLSchema#string> ;
        fedora:created "2020-05-12T21:59:19.736Z"^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
        fedora:lastModified "2020-05-12T21:59:26.707Z"^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
        dct:isPartOf <http://localhost:8984/rest/dev/ad/mi/n_/se/admin_set/default> ;
        dct:modified "2020-05-12T21:59:19.65408406+00:00"^^<http://www.w3.org/2001/XMLSchema#dateTime> ;
        acl:accessControl <http://localhost:8984/rest/dev/97/60/cf/c7/9760cfc7-b141-451c-84a1-ff7cb2223180> ;
        ebucore:hasRelatedImage <http://localhost:8984/rest/dev/9p/29/09/32/9p2909328> ;
        iana:first <http://localhost:8984/rest/dev/pr/76/f3/40/pr76f340k/list_source#g47218150558240> ;
        rdf:type ldp:RDFSource ;
        rdf:type ldp:Container ;
        fedora:writable "true"^^<http://www.w3.org/2001/XMLSchema#boolean> ;
        fedora:hasParent <http://localhost:8984/rest/dev> ;
        ldp:contains <http://localhost:8984/rest/dev/pr/76/f3/40/pr76f340k/member_of_collections> ;
        ldp:contains <http://localhost:8984/rest/dev/pr/76/f3/40/pr76f340k/members> ;
        ldp:contains <http://localhost:8984/rest/dev/pr/76/f3/40/pr76f340k/list_source> ;
        pcdm:hasMember <http://localhost:8984/rest/dev/9p/29/09/32/9p2909328> .

Here is a representation of the "Knoxville Garden Slides" Collection object: