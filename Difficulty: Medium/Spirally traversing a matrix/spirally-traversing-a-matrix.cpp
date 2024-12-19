//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends


class Solution {
  public:
    vector<int> spirallyTraverse(vector<vector<int> > &mat) {
        vector<int>ans;
        int n = mat.size();
        int m = mat[0].size();
        int str = 0 , enr = n-1 , stc = 0 , enc = m-1;
        while(ans.size() < n*m){
            for(int j=stc;j<=enc;j++){
                if(ans.size() == n*m){
                    break;
                }
                ans.push_back(mat[str][j]);
            }
            str++;
            for(int i=str;i<=enr;i++){
                if(ans.size() == n*m){
                    break;
                }
                ans.push_back(mat[i][enc]);
            }
            enc--;
            for(int j=enc;j>=stc;j--){
                if(ans.size() == n*m){
                    break;
                }
                ans.push_back(mat[enr][j]);
            }
            enr--;
            for(int i=enr;i>=str;i--){
                if(ans.size() == n*m){
                    break;
                }
                ans.push_back(mat[i][stc]);
            }
            stc++;
        }        
        return ans;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;

    while (t--) {
        int r, c;
        cin >> r >> c;
        vector<vector<int>> matrix(r);

        for (int i = 0; i < r; i++) {
            matrix[i].assign(c, 0);
            for (int j = 0; j < c; j++) {
                cin >> matrix[i][j];
            }
        }

        Solution ob;
        vector<int> result = ob.spirallyTraverse(matrix);
        for (int i = 0; i < result.size(); ++i)
            cout << result[i] << " ";
        cout << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends