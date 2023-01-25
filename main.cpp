
#include<iostream>
#include<cmath>
#include<fstream>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_matrix.h>
#include<gsl/gsl_odeiv2.h>
#include <vector>
using namespace std;


int func (double t, const double y[], double f[], void *params){
  (void)(t); /* avoid unused parameter warning */
  double* mu = (double *)params;
  f[0] = -mu[0] * y[0] + y[1];
  f[1] = (y[0]*y[0]) / (1 + (y[0]*y[0]))-mu[1];
  //cout<<"f="<<f[0]<<' '<<f[1]<<endl;
  return GSL_SUCCESS;
}


vector<vector<double>> mainLoop(void *paramsY, void *params,int nt = 50000){
    double* mu = (double *)params;
    double* y = (double *)paramsY;

    vector<vector<double>> vectorWynikow;
    vector<double> temp;

    gsl_odeiv2_system sys = {func, NULL, 2, &mu[2]};
    gsl_odeiv2_driver *d = gsl_odeiv2_driver_alloc_y_new (&sys, gsl_odeiv2_step_rk8pd, 1e-6, 1e-6, 0.0);

    double t = 0.0, t1 = 500.0;

    for (int i = 1; i <= nt; i++){

        double ti = i * t1 / nt;
        int status = gsl_odeiv2_driver_apply (d, &t, ti, y);

        if (status != GSL_SUCCESS){
            printf ("error, return value=%d\n", status);
            break;
        }

        temp.clear();
        temp.push_back(ti);
        temp.push_back(y[0]);
        temp.push_back(y[1]);

        vectorWynikow.push_back(temp);
        //cout<<ti<<' '<<mu[0]<<' '<<mu[1]<<' '<<y[0]<<' '<<y[1]<<endl;

    }

    gsl_odeiv2_driver_free (d);

   return vectorWynikow;

}

void vectorToFile(vector<vector<double>> vec, string fileName){

  ofstream file(fileName);

    for(int i=0; i<vec.size();i++){
        for(int j=0;j<vec[i].size();j++){
            file<<vec[i][j]<<' ';
        }
        file<<endl;
    }
  file.close();
}


int main (void){

    for(double a=0.0;a<10;a+=0.01){
        for(double b=0.0;b<10;b+=0.01){
            double t[] = {1.0 , 1.0};
            double p[]={a,b};
            vector<vector<double>> tak = mainLoop(t,p,500000);

            vectorToFile(tak,"wyniki_a="+to_string(a)+"_b="+to_string(b)+".txt");
        }
    }

  return 0;

}
