Unauthorized
============

tags: unauthorised

This spec file details the interaction with the unauthorised endpoint and the expected results
of those actions
     
Unauthorized is returned when doing a POST to the /unauthorized endpoint
------------------------------------------------------------------------

* Make a POST request to "/unauthorized"
* Assert that the http response status text is "Unauthorized"
* Assert that the http response code is "401"

OK is returned when doing a GET to the /unauthorized endpoint
-------------------------------------------------------------

* Make a GET request to "/unauthorized"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"

OK is returned when doing a GET to /unauthorized/last endpoint
-------------------------------------------------------------

* Make a GET request to "/unauthorized/last"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"

POSTed JSON can be retrieved on /unauthorized/last endpoint
----------------------------------------------------------------------------------------

* Update the POSTDATA in "/unauthorized" with the json value "FeeFiFoFum"
* Make a GET request to "/unauthorized/last"
* Assert that the POSTDATA JSON value is "FeeFiFoFum"


POSTed Input Form can be retrieved on GET to /unauthorized/last endpoint
---------------------------------------------------------------------------------------

* Update the POSTDATA in "/unauthorized" with the input form value "input=test"
* Make a GET request to "/unauthorized/last"
* Assert that the POSTDATA value is "input=test"



The lastUpdated timestamp is updating when new data is POSTed to /unauthorized
-----------------------------------------------------------------------------

* Make a POST request to "/unauthorized"
* Make a GET request to "/unauthorized/last"
* Save the current timestamp
* Pause execution for "1050"ms
* Make a POST request to "/unauthorized"
* Make a GET request to "/unauthorized/last"
* Assert that timestamp is different to the saved timestamp