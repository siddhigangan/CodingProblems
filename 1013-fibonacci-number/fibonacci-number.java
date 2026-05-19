class Solution {
    public int fib(int n) {
        // int arr[] = new int[n+1];
        // if (n==0){
        //      return 0;
        // }
        // else if (n==1) {
        //     return 1;
        // }else if(n>=2){
        //     arr[0]=0;
        //     arr[1]=1;
        //     for(int i = 2;i<=n;i++){
        //     arr[i] = arr[i-1]+arr[i-2];
        // }
        // }
        // return arr[n];

        if(n<=1){
            return n;
        }
        int prev1 = 0;
        int prev2 = 1;
        int current = 0;

        for(int i = 2; i <= n ; i++){
                current = prev1+ prev2;
                prev1 = prev2;
                prev2 = current;
        }
        return current;
    }
}