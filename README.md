# OrarioFacileScraper
This script is used to parse informations in webpages provided by [Orario Facile © 7](http://www.orariofacile.com/) to a JSON list that is written to the *stdout*.
## Syntax
This script is quite easy to use: just exec `python ofscraper.py <url> extended` where `url`is the URL to the webpage provided by Orario Facile © and `extended` is an optional switch used to show more informations.
## Format
The JSON produced by the software is an array, representing the week, of arrays, representing the days, in which is stored the timetable.
## Compatibility
This software was made to work with Orario Facile © 7 but compatibility isn't guaranteed at all. For example, it worked with:
* http://servizi.alberghetti.it/orario/itis/Classi/2ALS.html, Orario Facile © 7
* http://www.itisgalileiconegliano.gov.it/orario/Classi/3AT.html, Orario Facile © 8

And it didn't worked with:
* http://www.filolao.it/joomla/orariodefinitivo15_16/Classi/Classe9.html, Orario Facile © 7 (even if it should require some minor tweaks)

If you want to report a compatible instance of Orario Facile ©, please write an email to eugenio \<at> etcloud.ddns.net and if you want to report an incompatible instance, just open an issue
## Dependancies
* python
* lxml
