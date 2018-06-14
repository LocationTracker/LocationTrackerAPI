package br.ufrn.locationtracker.Activities;

import android.Manifest;
import android.annotation.SuppressLint;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.design.widget.TabLayout;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v4.view.ViewPager;
import android.telephony.TelephonyManager;
import android.view.View;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;

import org.json.JSONObject;

import java.util.ArrayList;

import br.ufrn.locationtracker.Api.LocationApi;
import br.ufrn.locationtracker.Api.OnJSONObjectResponseCallback;
import br.ufrn.locationtracker.Fragment.TabPagerAdapter;
import br.ufrn.locationtracker.R;
import br.ufrn.locationtracker.Utl.Utl;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    boolean todasPermissoes = true;
    public static final int MULTIPLY_PERMISSIONS = 4;
    TabPagerAdapter pagerAdapter;
    ViewPager viewPager;
    TabLayout tabLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();

        //setUpFacebook();
        //setupPublicidade();





        setupPermissions();
        while (!todasPermissoes){
            setupPermissions();
        }


        //getToken();
        configureTabLayout();

    }

    private void setupPermissions(){
        int fineLocationAccess = ActivityCompat.checkSelfPermission(getBaseContext(), Manifest.permission.ACCESS_FINE_LOCATION);
        int permissionIMEI = ContextCompat.checkSelfPermission(getBaseContext(), Manifest.permission.READ_PHONE_STATE);

        ArrayList<String> listaPermissoes = new ArrayList<>();

        if(permissionIMEI != PackageManager.PERMISSION_GRANTED){
            listaPermissoes.add(Manifest.permission.READ_PHONE_STATE);
            todasPermissoes = false;
        }
        else {
            TelephonyManager tm = (TelephonyManager)getSystemService(TELEPHONY_SERVICE);
            @SuppressLint("MissingPermission") String imei = tm.getDeviceId();
            Utl.setDevice(getBaseContext(), imei);
        }

        if(fineLocationAccess != PackageManager.PERMISSION_GRANTED){
            listaPermissoes.add(Manifest.permission.ACCESS_FINE_LOCATION);
            todasPermissoes = false;
        }

        if(listaPermissoes.size()>0){
            ActivityCompat.requestPermissions(this, listaPermissoes.toArray(new String[listaPermissoes.size()]),
                    MULTIPLY_PERMISSIONS);
        } else {
            todasPermissoes = true;
        }
    }

    private void configureTabLayout() {
        // Get the ViewPager and set it's PagerAdapter so that it can display items
        viewPager = findViewById(R.id.viewpager);
        viewPager.setOffscreenPageLimit(2);
        pagerAdapter = new TabPagerAdapter(getSupportFragmentManager(), MainActivity.this, viewPager);

        viewPager.setAdapter(pagerAdapter);

        // Give the TabLayout the ViewPager
        tabLayout = findViewById(R.id.tab_layout);
        tabLayout.setupWithViewPager(viewPager);


        tabLayout.getTabAt(0).setIcon(R.drawable.ic_menu_mapa_selecionado);
        //tabLayout.getTabAt(1).setIcon(R.drawable.ic_menu_linha);
        //tabLayout.getTabAt(2).setIcon(R.drawable.ic_menu_meuonibus);


        tabLayout.addOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override
            public void onTabSelected(TabLayout.Tab tab) {
                setTitle(tab.getText());
                int position = tab.getPosition();
                switch (position){
                    case 0:
                        tab.setIcon(R.drawable.ic_menu_mapa_selecionado);
                        break;
                    /*case 1:
                        tab.setIcon(R.drawable.ic_menu_linha_selecionado);
                        break;
                    case 2:
                        tab.setIcon(R.drawable.ic_menu_meuonibus_selecionado);
                        break;*/
                    default:
                        break;
                }
            }

            @Override
            public void onTabUnselected(TabLayout.Tab tab) {
                int position = tab.getPosition();
                switch (position) {
                    case 0:
                        tab.setIcon(R.drawable.ic_menu_mapa);
                        break;
                    /*case 1:
                        tab.setIcon(R.drawable.ic_menu_linha);
                        break;

                    case 2:
                        tab.setIcon(R.drawable.ic_menu_meuonibus);
                        break;*/
                    default:
                        break;

                }
            }

            @Override
            public void onTabReselected(TabLayout.Tab tab) {
                int position = tab.getPosition();
                switch (position) {
                    case 0:
                        tab.setIcon(R.drawable.ic_menu_mapa_selecionado);
                        return;
                   /* case 1:
                        tab.setIcon(R.drawable.ic_menu_linha_selecionado);
                        return;
                    case 2:
                        tab.setIcon(R.drawable.ic_menu_meuonibus_selecionado);
                        return;*/
                    default:
                        return;
                }
            }
        });
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.enviarPosicao) {
            enviarLocalizacao(this);
        }

        return true;
    }
    LocationApi locationApi;

    private void enviarLocalizacao(final Activity activity){
        if(locationApi== null){
            locationApi = new LocationApi(getBaseContext());

            locationApi.postSendLocation(1, Utl.getLatitude(getBaseContext()),
                    Utl.getLongitude(getBaseContext()),
                    new OnJSONObjectResponseCallback() {
                @Override
                public void onJSONObjectResponse(boolean success, JSONObject response) {
                    if(success){
                        new AlertDialog.Builder(activity)
                                .setTitle("Sucesso")
                                .setMessage("Enviado com Sucesso!")
                                .setCancelable(false)
                                .setPositiveButton("ok", new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                        dialog.cancel();
                                    }
                                }).show();
                        locationApi = null;
                    }
                    else {
                        new AlertDialog.Builder(activity)
                                .setTitle("Ops")
                                .setMessage("Erro no envio`!")
                                .setCancelable(false)
                                .setPositiveButton("ok", new DialogInterface.OnClickListener() {
                                    @Override
                                    public void onClick(DialogInterface dialog, int which) {
                                        dialog.cancel();
                                    }
                                }).show();
                        locationApi = null;
                    }
                }
            });
        }

    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_camera) {
            // Handle the camera action
        } else if (id == R.id.nav_gallery) {

        } else if (id == R.id.nav_slideshow) {

        } else if (id == R.id.nav_manage) {

        } else if (id == R.id.nav_share) {

        } else if (id == R.id.nav_send) {

        }

        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
