import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.JsonNode;
import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;
import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.datastore.DataStore;
import com.thoughtworks.gauge.datastore.DataStoreFactory;

public class ApiClient {

    @Step("Make a GET request to <endpoint>")
    public void makeGetRequestToEndpoint(String endpoint) {
        DataStore dataStore = DataStoreFactory.getScenarioDataStore();
        HttpResponse<String> httpResponse;
        String url = "http://localhost:3000" + endpoint;
        Gauge.writeMessage(url);
        try {
            httpResponse = Unirest.get(url)
                    .header("Content-Type", "application/json")
                    .header("Accept", "*/*")
                    .asString();
            dataStore.put("httpResponse", httpResponse);
            Integer httpResponseCode = httpResponse.getStatus();
            dataStore.put("httpResponseCode", httpResponseCode);
            String httpResponseStatusText = httpResponse.getStatusText();
            dataStore.put("httpResponseStatusText", httpResponseStatusText);
            Gauge.writeMessage(httpResponse.getBody());
            Gauge.writeMessage(httpResponseStatusText);

        }
        catch (UnirestException e) {
            e.printStackTrace();
        }
    }

    @Step("Make a POST request to <endpoint>")
    public void makePostRequestToEndpoint(String endpoint) {
        this.updatePostDataForEndpoint(endpoint, "123");
    }

    @Step("Update the POSTDATA in <endpoint> with the value <value>")
    public void updatePostDataForEndpoint(String endpoint, String value) {
        DataStore dataStore = DataStoreFactory.getScenarioDataStore();
        HttpResponse<String> httpResponse;
        String url = "http://localhost:3000" + endpoint;
        Gauge.writeMessage(url);
        try {
            httpResponse = Unirest.post(url)
                    .header("Content-Type", "application/json")
                    .header("Accept", "*/*")
                    .body("{\"test\": \"" + value + "\"}")
                    .asString();
            dataStore.put("httpResponse", httpResponse);
            Integer httpResponseCode = httpResponse.getStatus();
            dataStore.put("httpResponseCode", httpResponseCode);
            String httpResponseStatusText = httpResponse.getStatusText();
            dataStore.put("httpResponseStatusText", httpResponseStatusText);

         //   Gauge.writeMessage(httpResponse.getBody());
            Gauge.writeMessage(httpResponseStatusText);

        }
        catch (UnirestException e) {
            e.printStackTrace();
        }
    }
}
