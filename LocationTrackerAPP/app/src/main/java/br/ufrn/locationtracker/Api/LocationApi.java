package br.ufrn.locationtracker.Api;

import android.content.Context;
import android.content.Intent;

import com.loopj.android.http.JsonHttpResponseHandler;
import com.loopj.android.http.RequestParams;

import org.json.JSONArray;
import org.json.JSONObject;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.TimeZone;

import cz.msebera.android.httpclient.Header;

public class LocationApi {
    private Context context;

    public LocationApi(Context ctx){
        context = ctx;
    }


    public void postSendLocation(int id, String Lat, String Long, final  OnJSONObjectResponseCallback callback){
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss'Z'");
        format.setTimeZone(TimeZone.getTimeZone("GMT-3"));
        String datetimeCelular = format.format(new Date());
        Date dateCelular = null;
        Calendar cal = Calendar.getInstance();
        SimpleDateFormat hora = new SimpleDateFormat("HH");
        SimpleDateFormat minuto = new SimpleDateFormat("mm");

        try {
            dateCelular = format.parse(datetimeCelular);
            cal.setTime(dateCelular);
        } catch (ParseException e) {
            e.printStackTrace();
        }

        RequestParams params = new RequestParams();
        params.put("ano",Integer.toString( cal.get(Calendar.YEAR)));
        params.put("mes",Integer.toString( cal.get(Calendar.MONTH)+1));
        params.put("dia", Integer.toString( cal.get(Calendar.DAY_OF_MONTH)));
        params.put("hora",hora.format(dateCelular).toString());
        params.put("minutos",minuto.format(dateCelular).toString());
        params.put("lat",Lat);
        params.put("long",Long);
        String url = "router/usuarios/" + Integer.toString(id) + "/send_location/";

        WebClient.post(url, params, new JsonHttpResponseHandler(){
            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONObject response) {
                callback.onJSONObjectResponse(true, response);
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, Throwable throwable, JSONObject errorResponse) {
                callback.onJSONObjectResponse(false, null);
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, Throwable throwable, JSONArray errorResponse) {
                callback.onJSONObjectResponse(false, null);
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, String responseString, Throwable throwable) {
                callback.onJSONObjectResponse(false, null);
            }
        });

    }


}
