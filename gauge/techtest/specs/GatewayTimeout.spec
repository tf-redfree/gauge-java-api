GatewayTimeout
==============

tags: gateway_timeout

This spec file details the interaction with the gateway_timeout endpoint and the expected results
of those actions
     
Gateway_timeout is returned when doing a POST to the /gateway_timeout endpoint
------------------------------------------------------------------------------

* Make a POST request to "/gateway_timeout"
* Assert that the http response status text is "Gateway Timeout"
* Assert that the http response code is "504"

OK is returned when doing a GET to the /gateway_timeout endpoint
----------------------------------------------------------------

* Make a GET request to "/gateway_timeout"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"

OK is returned when doing a GET to the /gateway_timeout/last endpoint
----------------------------------------------------------------

* Make a GET request to "/gateway_timeout/last"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"

POSTed JSON can be retrieved on /gateway_timeout/last endpoint
-------------------------------------------------------------------------------------------

* Update the POSTDATA in "/gateway_timeout" with the json value "FeeFiFoFum"
* Make a GET request to "/gateway_timeout/last"
* Assert that the POSTDATA JSON value is "FeeFiFoFum"

POSTed Input Form can be retrieved on GET to /gateway_timeout/last endpoint
---------------------------------------------------------------------------------------

* Update the POSTDATA in "/gateway_timeout" with the input form value "input=test"
* Make a GET request to "/gateway_timeout/last"
* Assert that the POSTDATA value is "input=test"

The lastUpdated timestamp is updating when new data is POSTed to /gateway_timeout
-----------------------------------------------------------------------------

* Make a POST request to "/gateway_timeout"
* Make a GET request to "/gateway_timeout/last"
* Save the current timestamp
* Pause execution for "1050"ms
* Make a POST request to "/gateway_timeout"
* Make a GET request to "/gateway_timeout/last"
* Assert that timestamp is different to the saved timestamp