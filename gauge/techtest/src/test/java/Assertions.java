import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.JsonNode;
import com.mashape.unirest.http.JsonNode;
import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;
import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.datastore.DataStore;
import com.thoughtworks.gauge.datastore.DataStoreFactory;
import org.junit.Assert;
import org.json.JSONObject;
import org.json.JSONArray;

public class Assertions {



    @Step("Assert that the http response code is <response_code>")
    public void assertOnHttpResponseCode(Integer response_code) {
        DataStore dataStore = DataStoreFactory.getScenarioDataStore();
        Integer httpResponseCode = (Integer) dataStore.get("httpResponseCode");

        Assert.assertEquals(response_code, httpResponseCode);

    }

    @Step("Assert that the http response status text is <expectedResponse>")
    public void assertOnHttpResponseStatusText(String expectedResponse) {
        DataStore dataStore = DataStoreFactory.getScenarioDataStore();
        String httpResponseStatusText = (String) dataStore.get("httpResponseStatusText");
        Assert.assertEquals(expectedResponse, httpResponseStatusText);
    }

    @Step("Assert that the POSTDATA value is <value>")
    public void assertPostDataValueIs(String value) {
    	DataStore dataStore = DataStoreFactory.getScenarioDataStore();
        HttpResponse<String> httpResponse = (HttpResponse<String>)dataStore.get("httpResponse");

        JSONObject response = new JSONObject(httpResponse.getBody());
        String outerEleName = response.keys().next();
        JSONArray responseData = response.getJSONArray(outerEleName);
        String bodyReceived = responseData.getJSONObject(1).get("bodyReceived").toString();
        Assert.assertEquals(bodyReceived, "{\"test\":\"" + value.replace("\"", "\\\"") + "\"}");
    }

    @Step("Assert that timestamp is different to the saved timestamp")
    public void assertTimestampDiffersFromSaved() {
    	DataStore dataStore = DataStoreFactory.getScenarioDataStore();
    	String savedTimeStamp = (String)dataStore.get("saved_last_updated");
    	Helper h = new Helper();
    	String currentTimeStamp = h.getPreviousTimeStamp();
    	if(savedTimeStamp.equals(currentTimeStamp)) {
    		Assert.fail();
    	}
    }

}
