BadRequest
==========

tags: bad_request

This spec file details the interaction with the bad_request endpoint and the expected results
of those actions
     
Bad Request is returned when doing a POST to the /bad_request endpoint
----------------------------------------------------------------------

* Make a POST request to "/bad_request"
* Assert that the http response status text is "Bad Request"
* Assert that the http response code is "400"

OK is returned when doing a GET to the /bad_request endpoint
------------------------------------------------------------

* Make a GET request to "/bad_request"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"

OK is returned when doing a GET to the /bad_request/last endpoint
------------------------------------------------------------

* Make a GET request to "/bad_request/last"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"

Details of the last response is returned when doing a GET to /bad_request/last endpoint
---------------------------------------------------------------------------------------

* Update the POSTDATA in "/bad_request" with the value "FeeFiFoFum"
* Make a GET request to "/bad_request/last"
* Assert that the POSTDATA value is "FeeFiFoFum"

The lastUpdated timestamp is updating when new data is POSTed to /bad_request
-----------------------------------------------------------------------------

* Make a POST request to "/bad_request"
* Make a GET request to "/bad_request/last"
* Save the current timestamp
* Pause execution for "1050"ms
* Make a POST request to "/bad_request"
* Make a GET request to "/bad_request/last"
* Assert that timestamp is different to the saved timestamp