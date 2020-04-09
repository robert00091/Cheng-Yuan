
//  main.cpp
//  quicksort
//
//  Created by Cheng Yuan Ｗang on 2020/4/9.
//  Copyright © 2020 Cheng Yuan Ｗang. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

void swap(int* a, int* b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int partition(int* num, int p, int r){ // Hoare Partition
    int x = num[p];
    int i = p-1;
    int j = r+1;
    
    while(true){
        do{
            j--;
            
        }while(num[j]>x);
        
        do{
            i++;
            
        }while(num[i]<x);
        
        if(i<j){
            swap(&num[i], &num[j]);
        }
        
        else{
            return j;
        }
    }
        
}

void quicksort(int* num, int p, int r){
    if(p<r){
        int q = partition(num, p, r);
        quicksort(num, p, q-1);
        quicksort(num, q+1, r);
    }
    
    
}

int main(int argc, const char * argv[]) {
    int num[] = {5, 3, 2, 6, 4, 1, 3, 7};
    int len = sizeof(num)/sizeof(num[0]);
    
    quicksort(num, 0, len-1);
    
    for(int i=0; i<len; i++){
       cout << num[i] << " ";
    }
    
    cout << endl;
    return 0;
}
