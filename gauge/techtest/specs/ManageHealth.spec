ManageHealth
==========

tags: manage_health

This spec file details the interaction with the /manage/health endpoint and the expected results
of those actions

OK is returned when doing a GET to the /manage/health endpoint
------------------------------------------------------------

* Make a GET request to "/manage/health"
* Assert that the http response status text is "OK"
* Assert that the http response code is "200"