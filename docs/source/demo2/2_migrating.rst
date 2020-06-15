II. Migration Paths and Hurdles
===============================

A. Designing a Migration Path Grant and Findings
------------------------------------------------

In 2018, Fedora Commons Inc. (that's a thing?) and Duraspace received a `50,000 grant <https://www.imls.gov/grants/awarded/lg-72-18-0204-18>`_
to investigate barriers to upgrading unsupported versions of the Fedora repository platform to Fedora 4 or later.

The grant's description states that:

    DuraSpace will investigate barriers to upgrading unsupported versions of the Fedora repository platform used by approximately 240 libraries and archives in the United States. Use of unsupported versions puts the stability, security, and functionality of the content and services these institutions support at risk. This project will consult with an advisory board of stakeholders from the Islandora, Samvera, and Fedora communities; conduct an environmental scan of relevant community initiatives; and gather primary research data to inform recommendations for reducing barriers to upgrading. Project outputs will include user stories, an inventory of resources for upgrading, and recommendations for migration paths.

I want to talk about some of the findings from this grant and specifically how it relates specifically to our use case.

======================
Environmental Profiles
======================

The grant first looked at environmental profiles for universities who had not yet moved to Fedora 4 or later.

For Islandora, the grant found:

    Islandora is a Drupal-based framework that interacts with Fedora 3.x largely through the REST-API. Islandora takes a modular approach, with a single core application that can be customized by enabling and configuring Drupal modules. This approach makes migrations easier because the majority of the community is using a common core application with similar data models. Islandora uses a Solution Pack framework; each Solution Pack handles a particular type of content and describes specific data models which are shared across the community. The profiled institutions use a common and relatively small set of file formats, most of which are already supported in Islandora 8.  Migrations will also be made easier by using the Drupal Migrate ecosystem, which allows administrators to migrate from an Islandora 7 application to an Islandora 8 application based on Fedora 5.x.  Such a migration is necessary because Islandora 7 only supports Fedora 3.x, while Islandora 8 only supports Fedora 5.x and higher.

    Islandora 8 continues to follow the same model of providing a core application with configurable modules, which mitigates the need for adopters to rebuild all of their Islandora interfaces and workflow tools - many of these will be part of the standard Islandora 8 application stack. However, some institutions have customized their interfaces, and these customizations will need to be rearchitected in Islandora 8, which may be challenging for institutions with limited resources. Islandora 7 has also been around for many years and it has accumulated many modules and features which have not yet been built into Islandora 8. This will present a barrier to anyone using Islandora 7 features that don’t exist in Islandora 8 yet, but fortunately as community members build these features they will be available for everyone to use.

    Each of the profiled institutions with Islandora repositories have made some front-end customizations to their repositories, and these customizations are largely unavailable to the public and may or may not be documented. This presents a challenge for migrations since these local customizations are unlikely to be developed as part of the core Islandora 8 offering, thus requiring some resource investment on the part of the affected institutions in terms of updating the code to work with Islandora 8.

For Samvera, the grant found:

    The Samvera (formerly Hydra) community takes a different approach compared to Islandora, with an ecosystem of many different applications and tools used by different institutions. There is no single Samvera application stack, but most applications and tools are written in the Ruby programming language and Rails web framework. The most commonly used front-end application (Hyrax) has already been made compatible with Fedora 4.x and 5.x; in fact, the Samvera community was an early adopter of Fedora 4.x, and a previous version of Hyrax (Sufia) was the first application based on Fedora 4.x to be used in production. This has allowed some institutions to migrate to the new platform, though the diversity of community deployments and prevalence of local customizations makes migrations more challenging.

    Stanford is an example of a founding Samvera community member that uses a diversity of applications and tools in a complex repository ecosystem. Many of these tools are customized to work within the local environment in particular ways, which makes a repository migration a daunting prospect. The level of customization and interdependency means that Stanford would likely need to undertake a migration of their application framework in-house using local resources; no one else in the community has a similar enough system to work together on a migration.


===================
Migration Utilities
===================

The grant also reviewed migration tools that existed as of Spring 2019. At the time, these were the three most prominent utilities:

1. `migration-utils <https://github.com/fcrepo4-exts/migration-utils>`_
2. `fedora-migrate <https://github.com/samvera-labs/fedora-migrate>`_
3. `migrate_7x_claw <https://github.com/Islandora-Devops/migrate_7x_claw>`_

Below are assessments from the `grant webpage <https://wiki.lyrasis.org/display/FF/Designing+a+Migration+Path+-+Migration+Tool+Review>`_
of each tool with focus on current migration use cases.

---------------
migration-utils
---------------

From Duraspace:

    First developed in early 2015, migration-utils is a Java-based command-line utility that iterates over the FOXML resources in a Fedora 3.x repository (either within the native filesystem or as exported content) and transforms them into Fedora 4-compatible resources before ingesting them into a Fedora 4.x repository. A Spring XML configuration file is used to define the source and destination repositories, as well as the nature of the Fedora 3.x content.

    This utility uses a default set of property mappings that can be found in the README. These mappings are based on community best practices, and they can be changed by editing configuration files. XML content that can be easily mapped to RDF (e.g. Dublin Core metadata and the contents of the RELS-EXT datastream) are transformed into RDF properties before being imported into Fedora 4.x. Any managed datastreams are stored as binary resources in Fedora 4.x, and external content can optionally be fetched and stored in this manner.

    The primary advantage of migration-utils is its agnosticism toward front-end applications. It is designed to maintain the basic structure of Fedora 3.x data in Fedora 4.x with some XML to RDF transformations where appropriate. The application also has a number of configuration options and supports customization via plugins that could be written for specific use cases. The tool could potentially save institutions the effort of writing custom data migration scripts, particularly if they are using a custom front-end environment that would not be able to take advantage of either of the other two tools.

--------------
fedora-migrate
--------------

From Duraspace:

    FedoraMigrate was developed within the Samvera community to facilitate migrations between Fedora 3 and Fedora 4 repositories within the context of Sufia, a popular Samvera institutional repository application. FedoraMigrate “iterates over your existing Fedora3 application using the Rubydora gem. For each object it finds, it creates a new object with the same id in Fedora4 and proceeds to migrate each datastream, including versions if they are defined, and verifies the checksum of each. Permissions and relationships are migrated as well but using different procedures due to the changes in Fedora4.” The migration process takes place in two steps: first, the resources are migrated, and then the relationships are added.

    FedoraMigrate is capable of transforming XML-based metadata in Fedora 3 to RDF properties in Fedora 4; however, the mappings for each metadata element must be defined in the tool’s configuration, which could be time consuming. In general, the tool is configurable, but this configuration must be done in Ruby code, so a developer with Ruby on Rails experience will need to configure and run the migration. FedoraMigrate was written with Sufia in mind, so it would need to be customized to support other Samvera applications.

---------------
migrate_7x_claw
---------------

From Duraspace:

    FedoraMigrate was developed within the Samvera community to facilitate migrations between Fedora 3 and Fedora 4 repositories within the context of Sufia, a popular Samvera institutional repository application. FedoraMigrate “iterates over your existing Fedora3 application using the Rubydora gem. For each object it finds, it creates a new object with the same id in Fedora4 and proceeds to migrate each datastream, including versions if they are defined, and verifies the checksum of each. Permissions and relationships are migrated as well but using different procedures due to the changes in Fedora4.” The migration process takes place in two steps: first, the resources are migrated, and then the relationships are added.

    FedoraMigrate is capable of transforming XML-based metadata in Fedora 3 to RDF properties in Fedora 4; however, the mappings for each metadata element must be defined in the tool’s configuration, which could be time consuming. In general, the tool is configurable, but this configuration must be done in Ruby code, so a developer with Ruby on Rails experience will need to configure and run the migration. FedoraMigrate was written with Sufia in mind, so it would need to be customized to support other Samvera applications.

=============================
Comparing Tools with Profiles
=============================

Below are notes specifically thinking about Samvera:

-------
Samvera
-------

From the findings:

    The FedoraMigrate tool is specifically designed to work with the Sufia Samvera application, and therefore would only be useful to institutions making use of this application (which has since been superseded by the Hyrax application). While the migration tool could certainly be updated, it has not received any substantive code commits for over two years. Even if the tool were to be updated to work with Hyrax, which is similar to Sufia, it would not be useful to institutions like Stanford that have heavily customized both their Samvera applications and their data models. A migration to any new system would likely need to be done in a customized, in-house way at Stanford.

------
Custom
------

From the findings:

    Of the three available tools, migration-utils would be the most useful to the custom Fedora 3.x repositories (National Library of Medicine, University of Wisconsin-Madison, UNC Chapel Hill, Amherst College). While it won’t address any of their front-end applications, migration-utils could be helpful in simply getting the data from Fedora 3.x to Fedora 4.x. In each case this would require some configuration and likely customization via plug-ins, but it would save the effort required to write custom migration scripts. However, the tool has not had any releases since Fedora 4.6.x so it would need to be updated to support Fedora 5.x and higher.

=================================
Gaps and Analysis and Conclusions
=================================

From Gaps and Analysis:

    Of the currently available migration tools, migrate_7x_claw is the most robust and well-supported with greatest opportunity to impact a large number of institutions in the Fedora community. As more content types are supported, a greater number of Islandora repositories will be able to be migrated to Islandora 8. With over 260 installations around the world running on Fedora 3.x, this represents an enormous opportunity for the Fedora and Islandora communities.

    Migration-utils is a useful tool in principle, but it is hampered by a lack of updates and its support for generic migration use cases. However, this represents a potential opportunity for the Fedora community to improve the tool based on the migration needs of those with custom front-end implementations. While it wouldn’t be possible to develop a tool that will work out-of-the-box in every scenario, a focus on configurable property mappings and data transformations could make the tool much more useful to the community.

From Conclusions:

    While the Islandora community has taken longer to release a version of Islandora that supports Fedora 4.x and higher, their use of Drupal and a common application framework has given them a huge advantage in terms of developing migration tools that will support a majority of use cases in the Islandora community. The greatest gaps in support are therefore with custom Fedora 3.x repositories and those that are using Samvera tools but not a common application like Sufia or Hyrax. By taking migration-utils as a starting point and gathering requirements for improvements it would be possible to support a greater number of migration projects throughout the community.

B. Thinking about Designing a Migration Path and Moving our data to Hyrax from Islandora
----------------------------------------------------------------------------------------

The findings of this grant are interesting and thought-provoking particularly for our use case. In the environtmental
scanning and institutional profiling of the grant, the team doesn't review or cover institutions who would be jumping
from Islandora and Fedora 3 to Samvera and Fedora 4 or later.  Because of this, our use case would likely be closest to
the custom solution category.

This is because our Fedora 3 objects are tightly-bound with Islandora 7. Simply migrating these objects from Fedora 3 to
Fedora 4 would not make them interoperable with Hyrax because certain elements would be missing and our objects would be
quite different than what Hyrax would expect.
