package br.ufrn.locationtracker.Api;
import org.json.JSONArray;

public interface OnJSONArrayResponseCallback {
    void onJSONArrayResponse(boolean success, JSONArray response);
}
