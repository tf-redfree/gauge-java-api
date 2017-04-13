Internal Server Error
=====================

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
Internal Server Error is returned when doing a POST to the /internal_server_error endpoint
----------------

* Make a POST request to "/internal_server_error"
* Assert that the http response status text is "Internal Server Error"
* Assert that the http response code is "500"

OK is returned when doing a GET to the /internal_server_error endpoint
----------------------------------------------------------------

* Make a GET request to "/internal_server_error"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"



Details of the last response is returned when doing a GET to /internal_server_error/last endpoint
-------------------------------------------------------------------------------------------

* Update the POSTDATA in "/internal_server_error" with the value "FeeFiFoFum"
* Make a GET request to "/internal_server_error/last"
* Assert that the POSTDATA value is "FeeFiFoFum"

The lastUpdated timestamp is updating when new data is POSTed to /internal_server_error
-----------------------------------------------------------------------------

* Make a POST request to "/internal_server_error"
* Make a GET request to "/internal_server_error/last"
* Save the current timestamp
* Pause execution for "1050"ms
* Make a POST request to "/internal_server_error"
* Make a GET request to "/internal_server_error/last"
* Assert that timestamp is different to the saved timestamp