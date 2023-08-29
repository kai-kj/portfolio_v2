Title: DOI Lookup
Icon: logo.jpg

# DOI Lookup

A simple [DOI](https://www.doi.org/the-identifier/what-is-a-doi/) lookup tool, available at [doi.kaikitagawajones.com](https://doi.kaikitagawajones.com).

![DOI overview](assets/projects_doi_overview.png)

The main focus of the tool is to show relationships (citations and references) between articles, as shown below. This information is provided by the [OpenCitations Indexes unifying REST API](https://opencitations.net/index/api/v1).

![DOI title](assets/projects_doi_title.png)

Basic information about the article is also shown using data provided by the [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/):

<img alt="DOI details" src="assets/projects_doi_details.png" style="width: 60%">

In addition, easy-to-copy citations are also provided in plaintext, BibTeX, and RIS. The citation text is taken directly from [doi.org](https://www.doi.org/). [This document](https://citation.crosscite.org/docs.html) provides a good explanation of how this process works.

<img alt="DOI cite" src="assets/projects_doi_cite.png" style="width: 60%">

The web app was implemented in vanilla JavaScript without the use of any frameworks.