NoResponse
==========

tags: no_response

This spec file details the interaction with the no_response endpoint and the expected results
of those actions
     
No Response is returned when doing a POST to the /no_response endpoint
----------------------------------------------------------------------

* Make a POST request to "/no_response"
* Assert that the http response status text is "No Content"
* Assert that the http response code is "204"

OK is returned when doing a GET to the /no_response endpoint
------------------------------------------------------------

* Make a GET request to "/no_response"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"

OK is returned when doing a GET to the /no_response/last endpoint
------------------------------------------------------------

* Make a GET request to "/no_response/last"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"

POSTed JSON can be retrieved on /no_response/last endpoint
---------------------------------------------------------------------------------------

* Update the POSTDATA in "/no_response" with the json value "FeeFiFoFum"
* Make a GET request to "/no_response/last"
* Assert that the POSTDATA JSON value is "FeeFiFoFum"


POSTed Input Form can be retrieved on GET to /no_response/last endpoint
---------------------------------------------------------------------------------------

* Update the POSTDATA in "/no_response" with the input form value "input=test"
* Make a GET request to "/no_response/last"
* Assert that the POSTDATA value is "input=test"


The lastUpdated timestamp is updating when new data is POSTed to /no_response
-----------------------------------------------------------------------------

* Make a POST request to "/no_response"
* Make a GET request to "/no_response/last"
* Save the current timestamp
* Pause execution for "1050"ms
* Make a POST request to "/no_response"
* Make a GET request to "/no_response/last"
* Assert that timestamp is different to the saved timestamp