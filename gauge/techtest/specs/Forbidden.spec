Forbidden
=========

tags: forbidden

This spec file details the interaction with the forbidden endpoint and the expected results
of those actions
     
Forbidden is returned when doing a POST to the /forbidden endpoint
------------------------------------------------------------------------------

* Make a POST request to "/forbidden"
* Assert that the http response status text is "Forbidden"
* Assert that the http response code is "403"

OK is returned when doing a GET to the /forbidden endpoint
----------------------------------------------------------------

* Make a GET request to "/forbidden"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"

OK is returned when doing a GET to the /forbidden/last endpoint
----------------------------------------------------------------

* Make a GET request to "/forbidden/last"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"

POSTed JSON can be retrieved on GET to /forbidden/last endpoint
-------------------------------------------------------------------------------------------

* Update the POSTDATA in "/forbidden" with the json value "TestForbidden"
* Make a GET request to "/forbidden/last"
* Assert that the POSTDATA JSON value is "TestForbidden"

POSTed Input Form can be retrieved on GET to /forbidden/last endpoint
---------------------------------------------------------------------------------------

* Update the POSTDATA in "/forbidden" with the input form value "input=test"
* Make a GET request to "/forbidden/last"
* Assert that the POSTDATA value is "input=test"

The lastUpdated timestamp is updating when new data is POSTed to /forbidden
-----------------------------------------------------------------------------

* Make a POST request to "/forbidden"
* Make a GET request to "/forbidden/last"
* Save the current timestamp
* Pause execution for "1050"ms
* Make a POST request to "/forbidden"
* Make a GET request to "/forbidden/last"
* Assert that timestamp is different to the saved timestamp