

/*
    vector<double> mz;

    for(int j=1;j<=nt-1;j++){
      if (xp[j-1]*xp[j+1]<0.0){
          mz.push_back(abs(x[j]));
      }
    }

    bool test = true;
    for( int i = int(mz.size()/2); i < mz.size(); i++ ){
        if(abs(mz[i]-mz[i-1])>0.005){
          test = false;
          break;
        }
    }

    if(test){
      file<< j<<endl;
    }
*/

double mu[] = {0.0 , 0.5};



#include<iostream>
#include<cmath>
#include<fstream>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_matrix.h>
#include <time.h>       /* time */
#include<gsl/gsl_odeiv2.h>
#include <vector>
using namespace std;


double flogistyczna(double t){

        return 4.0/(1.0+exp(-t+250.0));

}


int func (double t, const double y[], double f[], void *params){
  (void)(t); /* avoid unused parameter warning */
  double mu = *(double *)params;
  f[0] = y[1];
  f[1] = -0.2*(y[1]*(y[0]*y[0]-1.0)+ mu*y[0] - cos(t))- y[0];
  return GSL_SUCCESS;
}

int funcrad (double t, const double y[], double f[], void *params){
  (void)(t); /* avoid unused parameter warning */
  double mu;

  f[0] = y[1];
  f[1] = -1.0*( (flogistyczna(t)*y[1]+(y[0]*y[0]*y[0])-y[0] - cos(t))/5.0) - y[0];
  return GSL_SUCCESS;
}




int main (void){
  srand (time(NULL));
  int nt = 50000;
  //double mu[] = {0.0 , 0.5, 1.0, 1.5, 2.0};

  ofstream file( "zablokowane.txt");

  for (double j = 0;j<0.01;j+=0.01){

    double x[nt] = {0.};
    double xp[nt] = {0.};

    gsl_odeiv2_system sys = {funcrad, NULL, 2, &j};

    gsl_odeiv2_driver *d = gsl_odeiv2_driver_alloc_y_new (&sys, gsl_odeiv2_step_rk8pd, 1e-6, 1e-6, 0.0);


    double t = 0.0, t1 = 500.0;
    double y[2] = { 5.0, 5.0 };

    //double y[2] = { ((double)rand()/RAND_MAX-0.5)*4.0, ((double)rand()/RAND_MAX-0.5)*4.0 };




    for (int i = 1; i <= nt; i++){

        double ti = i * t1 / nt;
        int status = gsl_odeiv2_driver_apply (d, &t, ti, y);

        if (status != GSL_SUCCESS){
            printf ("error, return value=%d\n", status);
            break;
        }

        xp[i] =y[1];
        x[i] = y[0];

        file << t<<' '<<x[i]<<endl;
    }
/*
    vector<double> mz;

    for(int j=1;j<=nt-1;j++){
      if (xp[j-1]*xp[j+1]<0.0){
          mz.push_back(abs(x[j]));
      }
    }

    bool test = true;
    for( int i = int(mz.size()/2); i < mz.size(); i++ ){
        if(abs(mz[i]-mz[i-1])>0.005){
          test = false;
          break;
        }
    }

    if(test){
      file<< j<<endl;
    }
*/

    gsl_odeiv2_driver_free (d);
  }
  file.close();
  return 0;
}
