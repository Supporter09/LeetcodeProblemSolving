**Time Complexity**: O(n)
## [Explained Video](https://www.youtube.com/watch?v=V-sEwsca1ak)
## Note: use in [longestPalindrome](../../string/longestPalindrome.py)

For calculating $d_{1}[]$ , we get the following code. Things to note:

- *i* is the index of the center letter of the current palindrome.
- If *i* exceeds *r* , $d_{1}[i]$ is initialized to 0.
- If *i* does not exceed *r* , $d_{1}[i]$  is either initialized to the $d_{1}[i]$ , where *j* is the mirror position of *i* in $(l,r)$ , - or $d_{1}[i]$ is restricted to the *size* of the *"outer" palindrome*.
- The while loop denotes the trivial algorithm. We launch it irrespective of the value of *k*.
- If the size of palindrome centered at *i* is *x* , then $d_{1}[i]$ stores $\frac{x+1}{2}$ 
 
```
vector<int> manacher_odd(string s) {
    int n = s.size();
    s = "$" + s + "^";
    vector<int> p(n + 2);
    int l = 1, r = 1;
    for(int i = 1; i <= n; i++) {
        p[i] = max(0, min(r - i, p[l + (r - i)]));
        while(s[i - p[i]] == s[i + p[i]]) {
            p[i]++;
        }
        if(i + p[i] > r) {
            l = i - p[i], r = i + p[i];
        }
    }
    return vector<int>(begin(p) + 1, end(p) - 1);
}
```