IX. Hyrax as an Institutional Repository Solution
=================================================

Sufia and Hyrax Origins
-----------------------

For many years, the Hydra / Samvera community had two major *variants*:

1. `CurationConcerns <https://github.com/samvera-deprecated/curation_concerns>`_
2. `Sufia <https://github.com/samvera-deprecated/sufia>`_

These solutions were built on the Hydra (Samvera) framework and geared at separate needs. CurationConcerns' main focus
was on digital collections.  Sufia on the other hand was built for institutional repositories and had functionality to
support features like self-deposit, proxy deposit, mediated deposit, and embargoing.

As both solutions matured, they got their own unique features to fit their specialties and continued to diverge on
separate courses.

In 2015, PCDM was realized and adopted by the Samvera community as a shared way to model content. This adoption steered
both platforms towards a common way of modeling objects.

At Hydra Connect 2016, a session was held based on a circulating white paper called
`"Should Sufia and CurationConcerns Merge?" <https://docs.google.com/document/d/1bkc2Cik1T3KXFQdS5UrU2XE3Kywd7di2IIjyo-T_Atc/edit>`_.
The results of the session and its discussion resulted in a decision to merge the Sufia and Curation Concerns code bases
into a single solution called `Hyrax <https://github.com/samvera/hyrax>`_.

Because of Hyrax's origins in Sufia, it works as an institutional repository out-of-the-box. In fact, as stated in
`Hyrax's Current Roadmap <https://wiki.lyrasis.org/display/samvera/Hyrax+Roadmap>`_, the Samvera Interest Group for
Advising the Hyrax Roadmap (SIGAHR) recognizes:

    the current implementation of Hyrax is more suited to institutional & data repository use cases than it is to digital
    collections management repository use cases.

Hyrax as an Institutional Repository
------------------------------------

In order to serve as a replacement for our current institutional repository, the following functionality must exist as
specified by the IR RFP Group:

1. Unmediated Uploads
2. Google Scholar Integration
3. Accept, Publish, and Other Workflows
4. Embargoing
5. Tombstoning

Hyrax supports all of these things out-of-the-box.  In this section, I'll describe these features in detail and point
to examples of Hyrax being used as an institutional repository.

Institutions Using Hyrax as an Institutional Repository
-------------------------------------------------------

This section lists some examples of Hyrax used as an institutional repository:

1. `University of North Carolina's Carolina Digital Repository <https://cdr.lib.unc.edu/>`_
2. `George Washington University's ScholarSpace <https://scholarspace.library.gwu.edu/>`_
3. `Emory's Emory Theses and Dissertations <https://etd.library.emory.edu/>`_

