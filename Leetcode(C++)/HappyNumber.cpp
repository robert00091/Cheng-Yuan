// Happy Number
// Input:19
// Output: True(if == 1)
// 1^2 + 9^2 = 82
// 8^2 + 2^2 = 68
// 6^2 + 8^2 = 100
// 1^2 + 0^2 + 0^2 = 1 ....

#include <iostream>
using namespace std;

// Seperate the number respectively & combine them
int next_num(int num){
  int sum=0;
  while(num != 0){
    int d = num%10;
    num /= 10;
    sum += d*d;
  }
    return sum;
  
}

bool happy_num(int num){
  int slow = num;
  int fast = num;
  do{
    slow = next_num(slow);
    fast = next_num(next_num(fast));
  }while(slow != fast);
  return slow == 1;
}

int main() {
  int num;
  cout << "Input:";
  cin >> num;
  bool result = happy_num(num);
  cout << result;
  return 0;
}
