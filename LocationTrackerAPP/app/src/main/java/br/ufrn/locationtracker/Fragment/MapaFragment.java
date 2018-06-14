package br.ufrn.locationtracker.Fragment;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.drawable.BitmapDrawable;
import android.location.Location;
import android.net.Uri;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.LatLngBounds;
import com.google.android.gms.maps.model.MapStyleOptions;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.squareup.otto.Subscribe;

import org.json.JSONArray;

import java.util.ArrayList;

import br.ufrn.locationtracker.R;
import br.ufrn.locationtracker.Utl.Keys;
import br.ufrn.locationtracker.Utl.Utl;
import co.mobiwise.materialintro.shape.Focus;
import co.mobiwise.materialintro.shape.FocusGravity;
import co.mobiwise.materialintro.shape.ShapeType;
import co.mobiwise.materialintro.view.MaterialIntroView;

public class MapaFragment extends SupportMapFragment implements
        OnMapReadyCallback,
        com.google.android.gms.location.LocationListener,
        GoogleApiClient.ConnectionCallbacks,
        GoogleApiClient.OnConnectionFailedListener  {

    private final LatLng cidadeInicial = new LatLng( Double.valueOf(Keys.LATITUDE), Double.valueOf(Keys.LONGITUDE));

    public GoogleMap mMap;
    public Location mLastLocation;
    private Marker mCurrLocationMarker;
    private LocationRequest mLocationRequest;
    private GoogleApiClient mGoogleApiClient;
    public LatLngBounds mCurrentCameraBounds;
    boolean moverParaPosicao = false;

    public MapaFragment(){

    }


    public static MapaFragment newInstance(int page){
        Bundle args = new Bundle();
        args.putInt(Keys.KEY_ARG_PAGE, page);
        MapaFragment fragment = new MapaFragment();
        fragment.setArguments(args);
        return fragment;
    }

    View view;

    @Override
    public View onCreateView(LayoutInflater layoutInflater, ViewGroup viewGroup, Bundle bundle) {
        view = layoutInflater.inflate(R.layout.fragment_mapa, viewGroup, false);
        return super.onCreateView(layoutInflater, viewGroup, bundle);
    }

    @Override
    public void onAttach(Activity activity) {
        super.onAttach(activity);
        try {

        } catch (ClassCastException e) {
            throw new ClassCastException("Error in retrieving data. Please try again");
        }
    }

    @Override
    public void onResume() {
        super.onResume();

        Log.d("MyMap", "onResume");
        setUpMapIfNeeded();
    }

    private void setUpMapIfNeeded() {

        if (mMap == null) {

            Log.d("MyMap", "setUpMapIfNeeded");
            buildGoogleApiClient();
            getMapAsync(this);
        }
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        Log.d("MyMap", "onMapReady");
        mMap = googleMap;
        setUpMap();


        //imprimirParadasNoMapa();
        //paradas();


    }

    @SuppressLint("MissingPermission")
    private void setUpMap() {

        mMap.setMyLocationEnabled(false);
        mMap.setMapType(GoogleMap.MAP_TYPE_NORMAL);
        mMap.getUiSettings().setMapToolbarEnabled(false);
        mMap.setMapStyle(MapStyleOptions.loadRawResourceStyle(getContext(), R.raw.map_style_json));

        mMap.moveCamera(CameraUpdateFactory.newLatLngZoom(cidadeInicial, Keys.ZOOM_PADRAO));

        mMap.animateCamera(CameraUpdateFactory.zoomTo(Keys.ZOOM_PADRAO));

        mMap.setOnCameraIdleListener(new GoogleMap.OnCameraIdleListener() {
            @Override
            public void onCameraIdle() {
                mCurrentCameraBounds = mMap.getProjection().getVisibleRegion().latLngBounds;
                float zoom = mMap.getCameraPosition().zoom;
                if( zoom < 16) {
                    mMap.clear();

                }
                else {

                }


            }
        });


        mMap.setOnMarkerClickListener(new GoogleMap.OnMarkerClickListener() {
            @Override
            public boolean onMarkerClick(final Marker marker) {

                return true;
            }
        });
    }

    @Override
    public void onLocationChanged(Location location) {
        mLastLocation = location;
        if (mCurrLocationMarker != null) {
            mCurrLocationMarker.remove();
        }
        Utl.setLatitude(getContext(), Double.toString( location.getLatitude()));
        Utl.setLongitude(getContext(), Double.toString(location.getLongitude()));

        LatLng latLng = new LatLng(location.getLatitude(), location.getLongitude());
        MarkerOptions markerOptions = new MarkerOptions();
        markerOptions.position(latLng);
        markerOptions.title("Você está aqui");
        if(getContext() != null){
            /*if(Utl.getFacebookId(getContext()) == null){
                markerOptions.icon(BitmapDescriptorFactory.fromResource(R.drawable.personagem));
            }else {
                try{
                    ImageView MenuImagem =  ((MainActivity) getActivity()).UserImage;
                    Bitmap bitmap = ((BitmapDrawable) MenuImagem.getDrawable()).getBitmap();
                    Bitmap resizedBitmap = Bitmap.createScaledBitmap(bitmap, 70, 70, false);
                    markerOptions.icon((BitmapDescriptorFactory.fromBitmap(resizedBitmap)));
                }catch (Exception e){
                    markerOptions.icon(BitmapDescriptorFactory.fromResource(R.drawable.personagem));
                }
            }*/
        }


        mCurrLocationMarker = mMap.addMarker(markerOptions);
        mCurrLocationMarker.showInfoWindow();

        if(moverParaPosicao == false) {
            mMap.moveCamera(CameraUpdateFactory.newLatLng(latLng));
            mMap.animateCamera(CameraUpdateFactory.zoomTo(Keys.ZOOM_PADRAO));
            this.moverParaPosicao = true;

        }
    }



    protected synchronized void buildGoogleApiClient() {
        mGoogleApiClient = new GoogleApiClient.Builder(getActivity())
                .addConnectionCallbacks(this)
                .addOnConnectionFailedListener(this)
                .addApi(com.google.android.gms.location.LocationServices.API)
                .build();
        mGoogleApiClient.connect();

    }

    @SuppressLint("MissingPermission")
    @Override
    public void onConnected(@Nullable Bundle bundle) {
        mLocationRequest = new LocationRequest();
        mLocationRequest.setInterval(1000);
        mLocationRequest.setFastestInterval(1000);
        mLocationRequest.setPriority(LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY);
        if (mGoogleApiClient == null) {
            buildGoogleApiClient();
        }
        else if(mGoogleApiClient.isConnected()){
            LocationServices.FusedLocationApi.requestLocationUpdates(mGoogleApiClient, mLocationRequest, this);
        }

    }

    @Override
    public void onConnectionSuspended(int i) {

    }

    @Override
    public void onConnectionFailed(@NonNull ConnectionResult connectionResult) {

    }


    @Override
    public void setUserVisibleHint(boolean isVisibleToUser) {
        super.setUserVisibleHint(isVisibleToUser);
        if(isVisibleToUser){

        }
    }

    @Override
    public void onDestroy() {
       // MyBus.getInstance().unregister(this);
        super.onDestroy();
    }
}
