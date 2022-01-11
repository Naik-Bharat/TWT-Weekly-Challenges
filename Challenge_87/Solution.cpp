#include<iostream>
using namespace std;

// This function returns True if the number (in base) equivalent to 'num' (in decimal) is filled with 1's, it returns False if number (in base) is not filled with 1's
bool change_base(int base, int num){
	while (num > 0){
		int remainder = num % base;
		// if number in base has anything other than 1
		if (remainder != 1){
			return false;
		}
		num = num / base;
	}
	return true;
}

// This function will return the smallest base that will have the number (in base) equivalent to 'num' (in decimal) filled with just 1's
// The smallest base that will be filled with just 1's will have the maximum number of 1's
int One(int num){
	int output;
	// 'base' is the base that we are converting the decimal number into
	for (int base = 2; base < num; base++){
		// If 'base' is even, then 111... (in 'base') has to be odd, so it will not be equal to 'num'
		if (num % 2 == 0 and base % 2 ==0){
			continue;
		}
		bool correct_result = change_base(base, num);    // correct_result tells if this base is giving required result
		if (correct_result == true){
			output = base;
			break;
		}
	}
	return output;
}


int main(){
	int N;    // Number of test cases
	cin >> N;
	for (int _ = 0; _ < N; _++){
		int num;
		cin >> num;
		cout << One(num) << endl;
	}
}