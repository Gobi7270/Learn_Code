#include <iostream>
using namespace std;

int main() {
    int n = 1001;
    int rev = 0;

    while(n != 0)
    {
        int di = n % 10;       // Get the last digit
        rev = rev * 10 + di;   // Append digit to reversed number
        n = n / 10;            // Remove last digit
    }

    cout << "Reversed number: " << rev << endl;

    return 0;
}
