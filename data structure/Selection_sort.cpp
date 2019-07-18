//
//  Selection_sort.cpp
//
//  Created by Cheng Yuan Ｗang on 2019/7/18.
//  Copyright © 2019 Cheng Yuan Ｗang. All rights reserved.
//

#include <iostream>
#include <iomanip>
using namespace std;

void swap(int *a, int *b){ // Change a and b
    int tmp;
    tmp = *b;
    *b = *a;
    *a= tmp;
}

void selection_sort(int *arr, int arr_size){
    int min;
    for (int i=0; i<arr_size; i++){
        min = i;
        for (int j=i+1; j<arr_size; j++){
            if (arr[j] < arr[min]){
                min = j;
            }
        }
        swap(&arr[i], &arr[min]);
    }
}

int main(){
    int size;
    int *ptr;
    
    
    cout << "Input the array size:" << endl;
    cin >> size;
    
    ptr = new int[size];
    
    cout << "Input datas:";
    
    for (int i=0; i<size; i++){
        cin >> ptr[i];
    }
    
    cout << "Before sorting:";
    
    for (int i=0; i< size; i++){
        cout << ptr[i] << " ";
    }
    
    cout << endl;
    
    selection_sort(ptr, size);
    
    cout << "After sorting:";
    
    for (int i=0; i<size; i++){
        cout << ptr[i] << " ";
    }
    
    cout << endl;
}
