# include "iostream"
using namespace std;
int main(){
	string str;
	cin>>str;
	for(int i=0;i<(str.length()/2);i++){
		if(str[i]!=str[str.length()-i-1]){
			cout<<"不是回文数！";
			return 0;
		}
	cout<<"是回文数！";
	return 0;
	}
}

//	8分
//	字符串的应用 
//	8分
