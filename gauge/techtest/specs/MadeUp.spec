MadeUp
======

tags: made_up

This spec file details the interaction with the made_up endpoint and the expected results
of those actions
     
Made up is returned when doing a POST to the /made_up endpoint
----------------------------------------------------------------------

* Make a POST request to "/madeup"
* Assert that the http response status text is "Not Found"
* Assert that the http response code is "404"

OK is returned when doing a GET to the /made_up endpoint
------------------------------------------------------------

* Make a GET request to "/madeup"
* Assert that the http response status text is "Not Found"
* Assert that the http response code is "404"


OK is returned when doing a GET to the /does/not/exist endpoint
------------------------------------------------------------

* Make a GET request to "/does/not/exist"
* Assert that the http response status text is "Not Found"
* Assert that the http response code is "404"

OK is returned when doing a GET to the /qwertyuiop endpoint
------------------------------------------------------------

* Make a GET request to "/qwertyuiop"
* Assert that the http response status text is "Not Found"
* Assert that the http response code is "404"