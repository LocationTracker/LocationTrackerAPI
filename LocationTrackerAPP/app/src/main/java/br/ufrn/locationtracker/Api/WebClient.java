package br.ufrn.locationtracker.Api;

import android.os.Looper;
import android.util.Log;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.AsyncHttpResponseHandler;
import com.loopj.android.http.RequestParams;
import com.loopj.android.http.SyncHttpClient;

public class WebClient {

    private static final String BASE_URL = "http://192.168.43.195:8000/api/";
    //private static final String BASE_URL = "http://localhost:3137/api/";

    private static AsyncHttpClient client;
    private static AsyncHttpClient syncHttpClient = new SyncHttpClient();
    private static AsyncHttpClient asyncHttpClient = new AsyncHttpClient();

    private static String getAbsoluteUrl(String relativeUrl) {
        return BASE_URL + relativeUrl;
    }

    public static void get(String url, RequestParams params, AsyncHttpResponseHandler responseHandler){
        getClient().get(getAbsoluteUrl(url), params, responseHandler);
    }

    public static void post(String url, RequestParams params, AsyncHttpResponseHandler responseHandler){
        getClient().post(getAbsoluteUrl(url), params, responseHandler);
    }

    private static AsyncHttpClient getClient(){
       Log.d("API", "HTTP Assincrono");
       return asyncHttpClient;
    }
}
