Preface: Feature List
=====================

This table includes a non-exhaustive list of Hyrax features and notes about each.

+-----------------------------------------------------+------------------------------------------------------------------------------+
| Feature                                             | Details                                                                      |
+=====================================================+==============================================================================+
| Multiple file upload                                | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Recursive folder upload                             | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Flexible user- and group-based access controls      | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Generation and validation of identifiers            | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Generation of derivatives                           | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Fixity checking (using Fedora's fixity service)     | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Version control                                     | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Characterization of uploaded files                  | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Forms for batch editing metadata                    | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Faceted search and browse                           | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Social media interaction                            | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| User profiles                                       | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| User dashboard for file management                  | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Highlighted files / works on user profile           | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Sharing w/ groups and users                         | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| User notifications                                  | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Activity streams                                    | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Single-use links                                    | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Google Scholar-specific metadata embedding          | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Schema.org microdata, Opengraph/Twitter cards       | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| User-managed collections for grouping files         | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Full-text indexing & searching                      | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Responsive, fluid, Bootstrap 3-based UI             | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Featured works and researchers on homepage          | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Proxy deposit and transfers of ownership            | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Questioning Authority                               | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| ResourceSync capability lists and resource lists    | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Contact form                                        | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Administrative dashboard, w/ feature flippers       | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Flexible object model                               | Automatically enabled: to allow zero-file works, enable in Hyrax initializer |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Transcoding of audio and video files                | off by default: enable in Hyrax initializer (requires ffmpeg)                |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Administrative sets (curated collections)           | Automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Customizable banner image                           | specify a banner image in Hyrax initializer                                  |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Capture usage statistics                            | requires Google Analytics ID to be specified in Hyrax initializer            |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Geonames integration for location-oriented metadata | requires configuration                                                       |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Virus detection for uploaded files                  | install clamav package and follow the management guide instructions          |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Display usage statistics in the UI                  | requires configuration                                                       |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Administrative users                                | requires configuration                                                       |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Citation formatting suggestions                     | requires configuration: enable config.citations in Hyrax initializer         |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Integration with Zotero                             | requires configuration                                                       |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Integration w/ cloud storage providers              | requires configuration                                                       |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| Background jobs                                     | requires configuration: though jobs will automatically run via the default   |
|                                                     | in-memory adapter, we recommend using an ActiveJob adapter like              |
|                                                     | Sidekiq in production environments                                           |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| IIIF manifests                                      | automatically enabled                                                        |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| IIIF image server                                   | follow the management guide instructions                                     |
+-----------------------------------------------------+------------------------------------------------------------------------------+
| UniversalViewer on work show page                   | automatically enabled for image-like assets when using IIIF image server     |
+-----------------------------------------------------+------------------------------------------------------------------------------+