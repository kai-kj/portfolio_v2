Title: DOI Lookup
Description: A web app to look up research articles, and see the relationships between them.
Icon: logo.jpg
Preview: assets/projects_doi_overview.png
Tags: HTML CSS JavaScript
Pos: 01_03

<div class="right_align">
    <img class="icon" src="assets/icon_pointer.svg" alt="github"/>
    <a href="https://doi.kaikitagawajones.com/">try it</a>
    &emsp;
    <img class="icon" src="assets/icon_github.svg" alt="github"/>
    <a href="https://github.com/kal39/doi_lookup">code</a>
</div>

# DOI Lookup

A web app to look up research articles. In addition to providing basic information about articles, the main focus of the tool is to show the relationship between articles. Available at [doi.kaikitagawajones.com](https://doi.kaikitagawajones.com).

![DOI overview](assets/projects_doi_overview.png)

The main focus of the tool is to show relationships (citations and references) between articles, as shown below. This information is provided by the [OpenCitations Indexes unifying REST API](https://opencitations.net/index/api/v1).

Basic information about the article is shown using data provided by the [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/). Easy-to-copy citations are also provided in plaintext, BibTeX, and RIS. The citation text is taken directly from [doi.org](https://www.doi.org/). [This](https://citation.crosscite.org/docs.html) document provides a good explanation of how this process works.

The web app was implemented in vanilla JavaScript without the use of any frameworks.