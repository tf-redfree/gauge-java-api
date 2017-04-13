import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.JsonNode;
import com.mashape.unirest.http.Unirest;
import com.mashape.unirest.http.exceptions.UnirestException;
import com.thoughtworks.gauge.Gauge;
import com.thoughtworks.gauge.Step;
import com.thoughtworks.gauge.datastore.DataStore;
import com.thoughtworks.gauge.datastore.DataStoreFactory;
import org.json.JSONObject;
import org.json.JSONArray;

public class Helper {

    @Step("Save the current timestamp")
    public void savePreviousTimestamp() {
        DataStore dataStore = DataStoreFactory.getScenarioDataStore();
        String lastUpdated = this.getPreviousTimeStamp();
        dataStore.put("saved_last_updated", lastUpdated);
    }

    @Step("Pause execution for <time>ms")
    public void pauseExecution(String time) {
    	try {
    		Thread.sleep(Long.parseLong(time));
    	} catch(Throwable e) {
    		e.printStackTrace();
    	}
    }

	public String getPreviousTimeStamp() {
		DataStore dataStore = DataStoreFactory.getScenarioDataStore();
		HttpResponse<String> httpResponse = (HttpResponse<String>)dataStore.get("httpResponse");

        JSONObject response = new JSONObject(httpResponse.getBody());
        String outerEleName = response.keys().next();
        JSONArray responseData = response.getJSONArray(outerEleName);
        String lastUpdated = responseData.getJSONObject(0).get("lastUpdated").toString();
        return lastUpdated;
	}

}
