import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.JsonNode;
import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;
import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.datastore.DataStore;
import com.thoughtworks.gauge.datastore.DataStoreFactory;

public class ApiTests {

    @Step("Make a GET request to <endpoint>")
    public void makeGetRequestToEndpoint(String endpoint) {
        ApiClient client = new ApiClient();
        client.makeGetRequestToEndpoint(endpoint);
    }

    @Step("Make a POST request to <endpoint>")
    public void makePostRequestToEndpoint(String endpoint) {
        ApiClient client = new ApiClient();
        client.updatePostDataForEndpoint(endpoint, "{\"test\": \"123\"}", "application/json");
    }

    @Step("Update the POSTDATA in <endpoint> with the json value <value>")
    public void updatePostDataForEndpointWithJSON(String endpoint, String value) {
        ApiClient client = new ApiClient();
        client.updatePostDataForEndpoint(endpoint, "{\"test\": \"" + value + "\"}", "application/json");
    }

    @Step("Update the POSTDATA in <endpoint> with the input form value <value>")
    public void updatePostDataForEndpointWithFormData(String endpoint, String value) {
        ApiClient client = new ApiClient();
        client.updatePostDataForEndpoint(endpoint, value, "application/x-www-form-urlencoded");
    }

}
