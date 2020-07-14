V. OAI-PMH: Out of the Box
==========================

Most Hyrax institutions use the `blacklight oai provider <https://github.com/projectblacklight/blacklight_oai_provider>`_
gem for harvesting and sharing metadata over OAI-PMH. This is because blacklight is a core component of search, index,
and discovery in Hyrax.

While there is a default mapping for OAI-PMH, the model here assumes that you will be configuring your things to meet your
own requirements.



The metadata displayed in the xml serialization of each record is based off the `field_semantics` hash in the
`SolrDocument` model. To update/change these fields add something like the following to your model:

.. code-block:: ruby

    field_semantics.merge!(
        creator: "author_display",
        date: "pub_date",
        subject: "subject_topic_facet",
        title: "title_display",
        language: "language_facet",
        format: "format"
    )

Let's look at a default Solr doc for one of our items:

.. code-block:: json

    {
        "system_create_dtsi":"2020-07-06T20:29:12Z",
        "system_modified_dtsi":"2020-07-06T21:17:42Z",
        "has_model_ssim":["Image"],
        "id":"qv33rw64w",
        "accessControl_ssim":["0bd8fe30-129c-43e6-9ef5-14eefad4fbaa"],
        "hasRelatedMediaFragment_ssim":["sf268508b"],
        "hasRelatedImage_ssim":["sf268508b"],
        "depositor_ssim":["mbagget1@utk.edu"],
        "depositor_tesim":["mbagget1@utk.edu"],
        "title_tesim":["Druid: a humanities magazine, May 1969"],
        "date_uploaded_dtsi":"2020-07-06T20:29:12Z",
        "date_modified_dtsi":"2020-07-06T21:17:42Z",
        "isPartOf_ssim":["admin_set/default"],
        "resource_type_tesim":["Other"],
        "creator_tesim":["University of Tennessee"],
        "keyword_tesim":["magazines (periodicals)"],
        "publisher_tesim":["University of Tennessee"],
        "subject_tesim":["College student newspapers and periodicals",
          "Price, Reynolds, 1933-2011",
          "American fiction--20th century--Periodicals",
          "American poetry--20th century--Periodicals",
          "College students' writings"],
        "language_tesim":["English"],
        "description_tesim":["Independently published magazine featuring interviews with creators, poetry, prose, plays, music reviews, photography, illustrations, and other creative works by University of Tennessee, Knoxville students."],
        "rights_statement_tesim":["http://rightsstatements.org/vocab/InC/1.0/"],
        "date_created_tesim":["1969-05"],
        "identifier_tesim":["druid_1969may",
          "druid:123"],
        "thumbnail_path_ss":"/downloads/sf268508b?file=thumbnail",
        "suppressed_bsi":false,
        "actionable_workflow_roles_ssim":["admin_set/default-default-managing",
          "admin_set/default-default-approving",
          "admin_set/default-default-depositing"],
        "workflow_state_name_ssim":["deposited"],
        "member_ids_ssim":["2227mp645",
          "sf268508b",
          "pr76f340k",
          "9593tv123",
          "4q77fr32b",
          "8g84mm241",
          "g732d8963",
          "2f75r800t",
          "r207tp33p",
          "6d56zw601",
          "qf85nb285",
          "f1881k888",
          "1j92g7448",
          "t435gc96m",
          "v405s9361",
          "6m311p28w",
          "h415p952n",
          "pk02c9724",
          "1g05fb60f",
          "bg257f046",
          "pv63g024f",
          "zw12z528p",
          "8623hx72q",
          "x346d4165",
          "z890rt24s",
          "k3569432s",
          "4b29b596v",
          "st74cq441",
          "xk81jk36q",
          "kw52j804p",
          "37720c723",
          "r207tp32d",
          "cn69m4128",
          "c821gj76b",
          "9k41zd48h",
          "9019s2443"],
        "member_of_collections_ssim":["Druid"],
        "member_of_collection_ids_ssim":["t148fh12j"],
        "file_set_ids_ssim":["2227mp645",
          "sf268508b",
          "pr76f340k",
          "9593tv123",
          "4q77fr32b",
          "8g84mm241",
          "g732d8963",
          "2f75r800t",
          "r207tp33p",
          "6d56zw601",
          "qf85nb285",
          "f1881k888",
          "1j92g7448",
          "t435gc96m",
          "v405s9361",
          "6m311p28w",
          "h415p952n",
          "pk02c9724",
          "1g05fb60f",
          "bg257f046",
          "pv63g024f",
          "zw12z528p",
          "8623hx72q",
          "x346d4165",
          "z890rt24s",
          "k3569432s",
          "4b29b596v",
          "st74cq441",
          "xk81jk36q",
          "kw52j804p",
          "37720c723",
          "r207tp32d",
          "cn69m4128",
          "c821gj76b",
          "9k41zd48h",
          "9019s2443"],
        "visibility_ssi":"open",
        "admin_set_tesim":["Default Admin Set"],
        "human_readable_type_tesim":["Image"],
        "read_access_group_ssim":["public"],
        "edit_access_group_ssim":["admin"],
        "edit_access_person_ssim":["mbagget1@utk.edu"],
        "nesting_collection__ancestors_ssim":["t148fh12j"],
        "nesting_collection__parent_ids_ssim":["t148fh12j"],
        "nesting_collection__pathnames_ssim":["t148fh12j/qv33rw64w"],
        "nesting_collection__deepest_nested_depth_isi":2,
        "_version_":1671503820468781056,
        "timestamp":"2020-07-06T21:17:43.356Z",
        "score":5.959342}]
    }

If we wanted to add our title to the XML serialization, we'd modify the `SolrDocument` model like so:

.. code-block:: ruby

    field_semantics.merge!(
        creator: "author_display",
        date: "pub_date",
        subject: "subject_topic_facet",
        title: "title_tesim",
        language: "language_facet",
        format: "format"
    )

By default, there are a default number of files used by the DublinCore serialization.  They are:

.. code-block:: ruby

    [:contributor, :coverage, :creator, :date, :description, :format, :identifier, :language, :publisher, :relation, :rights, :source, :subject, :title, :type]

