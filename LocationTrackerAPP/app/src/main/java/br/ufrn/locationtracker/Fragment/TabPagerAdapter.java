package br.ufrn.locationtracker.Fragment;

import android.content.Context;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.support.v4.view.ViewPager;

public class TabPagerAdapter extends FragmentPagerAdapter {

    Context context;
    private ViewPager viewPager;
    private String tabTitles[];

    public TabPagerAdapter(FragmentManager fm, Context _context, ViewPager viewPager) {
        super(fm);
        context = _context;
        this.viewPager = viewPager;
        this.tabTitles = new String[] {
                "MAPA"};


    }

    Fragment objFragment_map = null;

    @Override
    public Fragment getItem(int position) {
        switch (position) {
            case 0:
                if(this.objFragment_map == null) {
                    return MapaFragment.newInstance(position + 1);
                }else{
                    return this.objFragment_map;
                }
        }
        return  null;
    }

    @Override
    public  CharSequence getPageTitle(int position) {
        return tabTitles[position];
    }



    @Override
    public int getCount() {
        return tabTitles.length ;
    }
}
