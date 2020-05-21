III. Hyrax Origins and Why I'm Looking at It and not something else
-------------------------------------------------------------------

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

If you're wondering why on earth we would be looking at Hyrax as opposed to a more out-of-the-box solution like Hyku, I
think that's a fair question.  The primary reasons I chose to focus on Hyrax were:

1. I'm brand new to Samvera and there is no way I could inverstigate all solutions in depth simultaneously in a six week period
2. Our diverse use cases (ETD submission, digital collections, audio, video, etc.)
3. Educate myself about what it would take to run a Hyrax solution locally
4. Determine questions that would need to be answered for thinking about SaaS solutions for Hyrax
