#include <iostream>
#include <bits/stdc++.h>
#include <sys/time.h>
using namespace std;

int main(){

    clock_t start, end;
    time(&start);
    // double start = clock();
    for(int i = 1; i < 1000000000; i++){
        cout << i << endl;
    }
    // double end = clock();
    time(&end);
    double time_taken = double(end - start) / double(CLOCKS_PER_SEC);
    cout << time_taken;
return 0;
}