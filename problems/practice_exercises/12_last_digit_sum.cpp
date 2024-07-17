#include <iostream>
using namespace std;

int fibonacci_last_digit_sum(int n) {
    if (n <= 1) {
        return n;
    }

    int previous = 0, current = 1;
    int last_digit_sum = current;

    for (int i = 2; i <= n; ++i) {
        int temp = current;
        current = (previous + current) % 10;
        previous = temp;
        last_digit_sum = (last_digit_sum + current) % 10;
    }

    return last_digit_sum;
}

int main() {
    int n;
    std::cin >> n;
    int c = fibonacci_last_digit_sum(n);
    std::cout << c << '\n';
}
