package br.ufrn.locationtracker.Utl;


import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;

import com.facebook.login.LoginManager;

public class Utl {

    public static Boolean getLogado(Context context){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        return  preferences.getBoolean(Keys.KEY_LOGADO, false);
    }

    public static void setLogado(Context context, Boolean isLogged){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        SharedPreferences.Editor editor = preferences.edit();
        editor.putBoolean(Keys.KEY_LOGADO, isLogged);
        editor.commit();
    }




    public static void setLogoff(Context context){
        LoginManager.getInstance().logOut();
        setLogado(context, false);
    }

    public static void setDevice(Context context, String device){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        SharedPreferences.Editor editor = preferences.edit();
        editor.putString(Keys.KEY_DEVICE, device);
        editor.commit();
    }

    public static void setLatitude(Context context, String latitude){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        SharedPreferences.Editor editor = preferences.edit();
        editor.putString(Keys.KEY_LATITUDE, latitude);
        editor.commit();
    }

    public static String getLatitude(Context context){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        return  preferences.getString(Keys.KEY_LATITUDE, null);
    }

    public static void setLongitude(Context context, String longitude){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        SharedPreferences.Editor editor = preferences.edit();
        editor.putString(Keys.KEY_LONGITUDE, longitude);
        editor.commit();
    }

    public static String getLongitude(Context context){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        return  preferences.getString(Keys.KEY_LONGITUDE, null);
    }

    public static String getDevice(Context context){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        return  preferences.getString(Keys.KEY_DEVICE, null);
    }


    public static void setNome(Context context, String nome){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        SharedPreferences.Editor editor = preferences.edit();
        editor.putString(Keys.KEY_USUARIO, nome);
        editor.commit();
    }

    public static String getNome(Context context){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        return  preferences.getString(Keys.KEY_USUARIO, "");
    }

    public static void setEmail(Context context, String nome){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        SharedPreferences.Editor editor = preferences.edit();
        editor.putString(Keys.KEY_EMAIL, nome);
        editor.commit();
    }

    public static String getEmail(Context context){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        return  preferences.getString(Keys.KEY_EMAIL, "");
    }

    public  static void setFacebookId(Context context, String userId){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        SharedPreferences.Editor editor = preferences.edit();
        editor.putString(Keys.KEY_FACEBOOKID, userId);
        editor.commit();
    }

    public static String getFacebookId(Context context){
        SharedPreferences preferences = context.getSharedPreferences(Keys.KEY_PREFERENCIAS, 0);
        return  preferences.getString(Keys.KEY_FACEBOOKID, null);
    }

}
