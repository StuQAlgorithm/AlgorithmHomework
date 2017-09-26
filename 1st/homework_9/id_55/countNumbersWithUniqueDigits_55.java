//n = 0  => 1
//n = 1  _ 1+9 => 10
//n = 2  __ 9*9 => 81+10 => 91
//n = 3  ___ 9*9*8
//..
//n = 10


class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        if(n == 0) return 1;
        if(n > 11) return 0;

        int ret = 10;
        int base = 9;
        for(int i = 1; i < 11 && i < n; i++){
            base = base*(9 - i + 1);
            ret += base;
        }

        return ret;
    }
}