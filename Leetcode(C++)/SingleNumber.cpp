#include <iostream>
#include <vector>
using namespace std;

void singleNumber(vector<int>& num, int n){
  int s = num[0];
  for(int i=1; i<n; i++){
    s = s^num[i];
  }
  cout << s << endl;
}

int main() {
  int n; // input array size
  cout << "Please input n:";
  cin >> n;
  //cout << n;
  int input;

  vector<int> num;
  for(int i=0; i<n; i++){
    cin >> input;
    num.push_back(input);
  }

  singleNumber(num, num.size());
  return 0;
}
