int getSum(int a, int b) {
        while(b) {
            unsigned c = a&b;
            a ^= b;
            b = c << 1;
        }
        return a;
}