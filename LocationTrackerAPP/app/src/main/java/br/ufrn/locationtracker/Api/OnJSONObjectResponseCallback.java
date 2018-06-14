package br.ufrn.locationtracker.Api;

import org.json.JSONObject;

public interface OnJSONObjectResponseCallback {
    void onJSONObjectResponse(boolean success, JSONObject response);
}
